#!/usr/bin/env node

import { lstat, mkdir, mkdtemp, readFile, rename, rm, rmdir, stat, writeFile } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { parseArgs } from 'node:util';
import { getSupportedAgents, installSkills } from 'skills';

const skillName = 'openclaw-docs';
const repository = 'tbdavid2019/openclaw-docs-skill';
const marker = '.openclaw-docs-npm';
const sha = /^[a-f0-9]{40}$/;

async function existingRevision(target) {
  let entry;
  try {
    entry = await lstat(target);
  } catch (error) {
    if (error.code === 'ENOENT') return undefined;
    throw error;
  }

  if (entry.isDirectory()) {
    try {
      await lstat(join(target, '.git'));
    } catch (error) {
      if (error.code !== 'ENOENT') throw error;
      const revision = await readFile(join(target, marker), 'utf8').catch((error) => {
        if (error.code === 'ENOENT') return '';
        throw error;
      });
      if (sha.test(revision.trim())) return revision.trim();
    }
  }
  throw new Error(`Installation already exists at ${target}. Update it with its original installer or choose another scope.`);
}

async function validateSnapshot(directory, commit) {
  const requiredFiles = ['SKILL.md', 'agents/openai.yaml', 'references/SKILL_INDEX.md'];
  for (const name of requiredFiles) {
    const file = await stat(join(directory, name));
    if (!file.isFile() || file.size === 0) throw new Error(`Invalid snapshot file: ${name}`);
  }
  const catalog = await stat(join(directory, 'references/_catalog'));
  if (!catalog.isDirectory()) throw new Error('Invalid snapshot catalog');
  const { upstream_commit: upstreamCommit } = JSON.parse(
    await readFile(join(directory, 'references/SOURCE.json'), 'utf8'),
  );
  if (typeof commit !== 'string' || !sha.test(commit)) throw new Error('Missing skill repository commit');
  if (typeof upstreamCommit !== 'string' || !sha.test(upstreamCommit)) {
    throw new Error('Invalid upstream documentation commit');
  }
  return upstreamCommit;
}

async function install(target) {
  const previousRevision = await existingRevision(target);
  const parent = dirname(target);
  await mkdir(parent, { recursive: true });
  const staging = await mkdtemp(join(parent, '.openclaw-docs-'));
  let keepBackup = false;
  try {
    console.log('Fetching the latest OpenClaw documentation snapshot…');
    const result = await installSkills(repository, {
      cwd: staging,
      ref: 'main',
      skills: [skillName],
      agents: ['universal'],
      mode: 'copy',
      lockfile: false,
      symlinks: 'reject',
      telemetry: false,
    });
    const [installed] = result.installed;
    if (result.failed.length || !installed) {
      throw new Error(result.failed.map(({ message }) => message).join('\n') || 'No skill was installed');
    }
    const commit = result.source.commit;
    const upstreamCommit = await validateSnapshot(installed.path, commit);
    await writeFile(join(installed.path, marker), `${commit}\n`, { flag: 'wx' });

    const lock = join(parent, '.openclaw-docs-install.lock');
    try {
      await mkdir(lock);
    } catch (error) {
      if (error.code !== 'EEXIST') throw error;
      throw new Error(`Another installation is using ${target}. Try again after it finishes.`);
    }
    try {
      if (await existingRevision(target) !== previousRevision) {
        throw new Error(`Installation changed while fetching the snapshot. Run the command again to update ${target}.`);
      }
      const backup = join(staging, 'previous-installation');
      if (previousRevision) await rename(target, backup);
      try {
        await rename(installed.path, target);
      } catch (error) {
        if (previousRevision) {
          try {
            await rename(backup, target);
          } catch (restoreError) {
            keepBackup = true;
            throw new AggregateError([error, restoreError], `Previous installation is available at ${backup}`);
          }
        }
        throw error;
      }
    } finally {
      await rmdir(lock);
    }

    console.log(`Installation directory: ${target}`);
    console.log(`Skill repository commit: ${commit}`);
    console.log(`Upstream documentation commit: ${upstreamCommit}`);
  } finally {
    if (!keepBackup) await rm(staging, { recursive: true, force: true });
  }
}

async function main() {
  const { values } = parseArgs({
    options: {
      agent: { type: 'string', short: 'a', default: 'codex' },
      global: { type: 'boolean', short: 'g' },
      help: { type: 'boolean', short: 'h' },
    },
  });
  if (values.help) {
    console.log(`Usage: npx -y openclaw-docs-skill@latest [--agent <id>] [--global]

Install or refresh the latest documentation snapshot from GitHub.
  -a, --agent <id>   Target agent (default: codex)
  -g, --global       Install in the agent's user directory
  -h, --help         Show this help`);
    return;
  }

  const agent = getSupportedAgents().find(({ id }) => id === values.agent);
  if (!agent) throw new Error(`Unknown agent: ${values.agent}`);
  const skillsDirectory = values.global ? agent.globalSkillsDir : agent.projectSkillsDir;
  if (!skillsDirectory) throw new Error(`${agent.name} only supports project installation`);
  await install(resolve(skillsDirectory, skillName));
}

main().catch((error) => {
  console.error(`openclaw-docs-skill: ${error.message}`);
  process.exitCode = 1;
});
