# Writing Voice

Write and edit plain, natural prose while checking whether the argument has substance. The skill follows Orwell's writing principles with judgment: preserve meaning, use familiar words, remove filler, and choose a form that fits the piece. It discourages stock AI phrasing, faux-sassy hooks, decorative triads, and needless fragments.

Version 2.0 replaces forced 10% cuts and blanket word bans with contextual editing. It keeps meaningful uncertainty, useful technical terms, and already-effective prose.

Version 2.0 is available on `main`. The commands below install the current version.

## Install locally

```sh
git clone https://github.com/tompulsarlabs/writing-voice-skill.git
cd writing-voice-skill
python3 scripts/install.py --user
python3 scripts/install.py --user --check
```

The installer maintains one copy in `~/.agents/skills/writing-voice-custom/` and links the Codex compatibility path, Claude Code, and Cursor to it. It refuses conflicting independent installations instead of replacing them. Repeat the install after pulling an update. Start a new session if the host does not discover the new skill automatically.

Invoke `$writing-voice-custom` in Codex or `/writing-voice-custom` in Claude Code, or ask for a prose edit and let the host select it. Supported work: full edit, quick tighten, voice check, and writing from scratch.

## Cloud and other machines

A local installation does not itself upload the skill to an account or another machine.

- **Claude, Cowork, and Claude Code cloud:** Create or update the skill in [Customize > Skills](https://claude.ai/customize/skills), using the name and description from the frontmatter and the body of `writing-voice-custom/SKILL.md`. Alternatively upload a ZIP containing `writing-voice-custom/`. Enable it for the account. Claude's [cloud skill documentation](https://code.claude.com/docs/en/skills#skills-in-cowork-and-cloud-sessions) describes account sync and project discovery.
- **ChatGPT Work cloud:** Create or update it in the account's [Skills editor](https://chatgpt.com/skills), using the same name, description, and body. Save the skill and verify its enabled state. Availability depends on the account's supported surfaces; test selection in a new session.
- **Repository-based cloud sessions and fresh clones:** Run `python3 scripts/install.py --project /path/to/repo`, then commit the generated `.agents/skills/writing-voice-custom/` and the relative links under `.claude/skills/` and `.cursor/skills/`. Codex reads `.agents/skills`; Claude reads `.claude/skills`. The links stay within the repository and need no local home directory. A source repository on GitHub alone does not install the skill into every other repository.
- **Other Agent Skills hosts or raw API clients:** Install the folder in the host's supported location, or provide its contents as writing guidance in the request. An API client must explicitly load it; there is no universal cross-vendor sync.

Cloud editor copies need updating when the source changes. Keep `writing-voice-custom/` authoritative and compare the saved body when updating an account copy. This skill requires no scripts, network access, or connectors for ordinary writing; the evaluation reference is for maintenance only.

## Evaluation and maintenance

`writing-voice-custom/eval.md` contains the rubric and 17 cases. Save actual model inputs and outputs when running it, and score the observed results. Installer and frontmatter checks do not measure writing quality. Current deployment and verification evidence belongs in `HANDOFF.md`.

## License

MIT.
