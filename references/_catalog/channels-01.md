# Channels documentation catalog

Messaging channel setup, routing, and troubleshooting.

Open only the entries relevant to the current request. Start with at most three documents.

- [Access groups](../channels/access-groups.md) — Reusable sender allowlists for message channels. Read when: Configuring the same allowlist across multiple message channels; Sharing DM and group sender access rules; Reviewing message-channel access control.
- [Ambient room events](../channels/ambient-room-events.md) — Let supported group rooms provide quiet context unless the agent sends with the message tool. Read when: Configuring always-on group or channel rooms; You want the agent to watch room chatter without posting final text automatically; Debugging typing and token usage with no visible room message.
- [Bot loop protection](../channels/bot-loop-protection.md) — Bot-to-bot loop protection defaults and channel overrides. Read when: Configuring bot-authored channel messages; Tuning bot-to-bot loop protection.
- [Broadcast groups](../channels/broadcast-groups.md) — Broadcast a WhatsApp message to multiple agents. Read when: Configuring broadcast groups; Debugging multi-agent replies in WhatsApp.
- [Buzz](../channels/buzz.md) — Connect OpenClaw agents to Buzz rooms. Read when: You want people to reach an OpenClaw agent from Buzz; You are setting up a Buzz bot identity and room access; You are troubleshooting a Buzz connection.
- [Channel location parsing](../channels/location.md) — Channel location parsing and portable outbound location payloads. Read when: Adding or modifying channel location parsing; Using location context fields in agent prompts or tools.
- [Channel routing](../channels/channel-routing.md) — Routing rules per channel (WhatsApp, Telegram, Discord, Slack) and shared context. Read when: Changing channel routing or inbox behavior.
- [Channel troubleshooting](../channels/troubleshooting.md) — Fast channel level troubleshooting with per channel failure signatures and fixes. Read when: Channel transport says connected but replies fail; You need channel specific checks before deep provider docs.
- [Chat channels](../channels/index.md) — Messaging platforms OpenClaw can connect to. Read when: You want to choose a chat channel for OpenClaw; You need a quick overview of supported messaging platforms.
- [ClickClack](../channels/clickclack.md) — ClickClack bot-token channel setup and target syntax. Read when: Connecting OpenClaw to a ClickClack workspace; Testing ClickClack bot identities.
- [Coming from BlueBubbles](../channels/imessage-from-bluebubbles.md) — Translate old BlueBubbles configs to the bundled iMessage plugin: key mapping, group allowlist gates, and cutover verification. Read when: Planning a move from BlueBubbles to the bundled iMessage plugin; Translating BlueBubbles config keys to iMessage equivalents; Verifying imsg before enabling the iMessage plugin.
- [Discord](../channels/discord.md) — Discord bot setup, config keys, components, voice, and troubleshooting. Read when: Working on Discord channel features.
- [Discord Activities](../channels/discord-activities.md) — Launch self-contained OpenClaw HTML widgets inside Discord Activities. Read when: Setting up or troubleshooting Discord Activity widgets.
- [Feishu](../channels/feishu.md) — Feishu bot overview, features, and configuration. Read when: You want to connect a Feishu/Lark bot; You are configuring the Feishu channel.
- [Google Chat](../channels/googlechat.md) — Google Chat app support status, capabilities, and configuration. Read when: Working on Google Chat channel features.
- [Groups](../channels/groups.md) — Group chat behavior across surfaces (Discord/iMessage/Matrix/Microsoft Teams/QQBot/Signal/Slack/Telegram/WhatsApp/Zalo). Read when: Changing group chat behavior or mention gating; Scoping mentionPatterns to specific group conversations.
- [iMessage](../channels/imessage.md) — Native iMessage support via imsg (JSON-RPC over stdio), with private API actions for replies, tapbacks, effects, polls, attachments, and group management. Preferred for new OpenClaw iMessage setups when host requirements fit. Read when: Setting up iMessage support; Debugging iMessage send/receive.
- [IRC](../channels/irc.md) — IRC plugin setup, access controls, and troubleshooting. Read when: You want to connect OpenClaw to IRC channels or DMs; You are configuring IRC allowlists, group policy, or mention gating.
- [LINE](../channels/line.md) — LINE Messaging API plugin setup, config, and usage. Read when: You want to connect OpenClaw to LINE; You need LINE webhook + credential setup; You want LINE-specific message options.
- [Matrix](../channels/matrix.md) — Matrix support status, setup, and configuration examples. Read when: Setting up Matrix in OpenClaw; Configuring Matrix E2EE and verification.
- [Matrix migration](../channels/matrix-migration.md) — How OpenClaw upgrades the previous Matrix plugin in place, including encrypted-state recovery limits and manual recovery steps. Read when: Upgrading an existing Matrix installation; Migrating encrypted Matrix history and device state.
- [Matrix presentation metadata](../channels/matrix-presentation.md) — Matrix MessagePresentation metadata for OpenClaw-aware clients. Read when: Building Matrix clients that render OpenClaw rich responses; Debugging com.openclaw.presentation event content.
- [Matrix push rules for quiet previews](../channels/matrix-push-rules.md) — Per-recipient Matrix push rules for quiet finalized preview edits. Read when: Setting up Matrix quiet streaming for self-hosted Synapse or Tuwunel; Users want notifications only on finished blocks, not on every preview edit.
- [Mattermost](../channels/mattermost.md) — Mattermost bot setup and OpenClaw config. Read when: Setting up Mattermost; Debugging Mattermost routing.
- [Microsoft Teams](../channels/msteams.md) — Microsoft Teams bot support status, capabilities, and configuration. Read when: Working on Microsoft Teams channel features.
- [Nextcloud Talk](../channels/nextcloud-talk.md) — Nextcloud Talk support status, capabilities, and configuration. Read when: Working on Nextcloud Talk channel features.
- [Nostr](../channels/nostr.md) — Nostr DM channel via NIP-04 encrypted messages. Read when: You want OpenClaw to receive DMs via Nostr; You're setting up decentralized messaging.
- [Pairing](../channels/pairing.md) — Pairing overview: approve who can DM you + which nodes can join. Read when: Setting up DM access control; Pairing a new iOS/Android node; Reviewing OpenClaw security posture.
- [QA channel](../channels/qa-channel.md) — Synthetic Slack-class channel plugin for deterministic OpenClaw QA scenarios. Read when: You are wiring the synthetic QA transport into a local or CI test run; You need the bundled qa-channel config surface; You are iterating on end-to-end QA automation.
- [QQ bot](../channels/qqbot.md) — QQ Bot setup, config, and usage. Read when: You want to connect OpenClaw to QQ; You need QQ Bot credential setup; You want QQ Bot group or private chat support.
