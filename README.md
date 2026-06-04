# Writing Voice

A craft-first prose editing and writing skill for AI coding agents (Claude Code, Cursor, etc.).

It enforces clear, honest, muscular prose through three layers:

1. **On Writing fundamentals** — the mechanics (10% rule, active voice, no adverbs, kill qualifiers/hedges, simple words)
2. **Anti-Slop Protocol** — the immune system that strips AI tells (filler phrases, false-depth markers, hollow intensifiers, structural slop)
3. **Editorial Voice** — the spine (say the actual thing, no comfort language, earn every abstraction, no overclaiming, take a position)

## What it does

Use it to:
- Edit, tighten, or sharpen any draft
- Review AI-generated text before it ships
- Ghostwrite blog posts, newsletters, memos, or long-form content
- Run a quick voice check on something you wrote

## Install

The skill is a single `SKILL.md` inside a `writing-voice-custom/` folder. Drop that folder into your agent's skills directory.

**Claude Code**

```bash
git clone https://github.com/tompulsarlabs/writing-voice-skill.git
cp -r writing-voice-skill/writing-voice-custom ~/.claude/skills/
```

**Cursor**

```bash
git clone https://github.com/tompulsarlabs/writing-voice-skill.git
cp -r writing-voice-skill/writing-voice-custom ~/.cursor/skills/
```

(Or copy into a project-local `.claude/skills/` or `.cursor/skills/` directory if you only want it in one project.)

## Use

Invoke it by name or just ask for an edit:

```
/writing-voice-custom

clean this up: <paste draft>
```

Three editing modes:
- **Full edit** (default) — structural pass, line edit, anti-slop sweep, voice pass, 10% cut
- **Quick tighten** — mechanical rules + banned-word list + 10% cut
- **Voice check** — flags slop and comfort language without rewriting

## License

MIT. Use it, fork it, sharpen it.
