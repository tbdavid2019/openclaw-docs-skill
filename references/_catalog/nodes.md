# Nodes documentation catalog

Mobile, desktop, and headless node capabilities.

Open only the entries relevant to the current request. Start with at most three documents.

- [Active computer presence](../nodes/presence.md) — Detect the Mac you most recently used and route node alerts there. Read when: You want OpenClaw to identify the active Mac; You are debugging last-input activity or active-node selection; You want to understand node connection notification routing.
- [Audio and voice notes](../nodes/audio.md) — How inbound audio/voice notes are downloaded, transcribed, and injected into replies. Read when: Changing audio transcription or media handling.
- [Camera capture](../nodes/camera.md) — Camera capture on iOS, Android, macOS, and Linux nodes for photos and short video clips. Read when: Adding or modifying camera capture on node platforms; Extending agent-accessible MEDIA temp-file workflows.
- [Computer use](../nodes/computer-use.md) — Capability-based desktop control through the computer tool and computer.act node command. Read when: Letting the gateway agent see and control a paired desktop; Enablement, permissions, or safety for computer use; Extending the computer.act node command or its fulfillers.
- [Image and media support](../nodes/images.md) — Image and media handling rules for send, gateway, and agent replies. Read when: Modifying media pipeline or attachments.
- [Location command](../nodes/location-command.md) — Location command for nodes, platform permission modes, and Linux GeoClue setup. Read when: Adding location node support or permissions UI; Designing Android location permissions or foreground behavior.
- [Media playback](../nodes/media-playback.md) — Inline audio and video playback across the Control UI and native apps. Read when: Playing or troubleshooting audio and video attachments in chat; Comparing media format support across OpenClaw clients; Debugging playback metadata, transcoding, or codec availability.
- [Media understanding](../nodes/media-understanding.md) — Inbound image/audio/video understanding (optional) with provider + CLI fallbacks. Read when: Designing or refactoring media understanding; Tuning inbound audio/video/image preprocessing.
- [Node troubleshooting](../nodes/troubleshooting.md) — Troubleshoot node pairing, foreground requirements, permissions, and tool failures. Read when: Node is connected but camera/canvas/screen/exec tools fail; You need the node pairing versus approvals mental model.
- [Nodes](../nodes/index.md) — Nodes: pairing, capabilities, permissions, and CLI helpers for canvas/camera/screen/device/notifications/system. Read when: Pairing iOS/watchOS/Android nodes to a gateway; Using node canvas/camera for agent context; Adding new node commands or CLI helpers.
- [Talk mode](../nodes/talk.md) — Talk mode: continuous speech conversations across local STT/TTS and realtime voice. Read when: Implementing Talk mode on macOS/iOS/Android; Changing voice/TTS/interrupt behavior.
- [Voice wake](../nodes/voicewake.md) — Global voice wake words (Gateway-owned) and how they sync across nodes. Read when: Changing voice wake words behavior or defaults; Adding new node platforms that need wake word sync.
