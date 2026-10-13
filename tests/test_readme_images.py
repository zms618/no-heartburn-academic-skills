from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / 'skills/paper-reading/README.md').read_text(encoding='utf-8')
README_EN = (ROOT / 'skills/paper-reading/README.en.md').read_text(encoding='utf-8')

EXAMPLE_IMAGES = (
    'docs/images/plugin-creator-paper-reading-created.png',
    'docs/images/chatgpt-side-by-side-paper-figure.png',
    'docs/images/chatgpt-plugin-picker.png',
    'docs/images/chatgpt-paper-reading-analysis.png',
    'docs/images/chatgpt-paper-reading-stage1.png',
    'docs/images/self-attention-reading-example.png',
)


def test_readme_examples_are_preserved_and_exist():
    for relative_path in EXAMPLE_IMAGES:
        assert f'](../../{relative_path})' in README
        assert f'](../../{relative_path})' in README_EN
        assert (ROOT / relative_path).is_file()


def test_readme_documents_direct_plugin_zip_upload_and_creator_fallback():
    assert '## 在 ChatGPT 网页端上传 ZIP 并安装' in README
    assert '[下载论文带读 v0.7.0 插件 ZIP]' in README
    assert '添加' in README and '上传插件压缩包' in README
    assert '请根据以下 GitHub 仓库创建并安装一个名为「论文带读（paper-reading）」' in README


def test_root_readmes_are_collection_overviews():
    root_zh = (ROOT / 'README.md').read_text(encoding='utf-8')
    root_en = (ROOT / 'README.en.md').read_text(encoding='utf-8')
    assert root_zh.startswith('# 不烧心 academic-skills')
    assert '**简体中文** | [English](README.en.md)' in root_zh
    assert '[简体中文](README.md) | **English**' in root_en
    assert 'skills/paper-reading/README.md' in root_zh
    assert 'skills/paper-reading/README.en.md' in root_en
    assert '## 在 ChatGPT 网页端创建和安装' not in root_zh
    assert '## Create and install it on ChatGPT Web' not in root_en
    assert '不消耗 Codex 或 Claude 专用额度' in root_zh
    assert 'Codex-specific quota' in root_en
    assert 'ChatGPT Web Plugin' in root_en
    assert '### 🧩 ChatGPT Web Plugin 01 · [paper-reading]' in root_en
    assert 'ChatGPT 网页端插件' in root_zh
    assert '### 🧩 ChatGPT 网页端插件 01 · [论文带读 · paper-reading]' in root_zh
    assert 'ChatGPT 网页端插件 03 · [AI 导师 · AI Mentor]' in root_zh
    assert 'ChatGPT Web Plugin 03 · [AI Mentor]' in root_en
    assert '](docs/images/chatgpt-side-by-side-paper-figure.png)' in root_zh
    assert '](docs/images/chatgpt-side-by-side-paper-figure.png)' in root_en
    for rel in ('paper-reading-v0.7.0.zip','research-idea-discovery-v4.0.19.zip','ai-mentor-v1.4.0.zip'):
        assert (ROOT / 'downloads' / rel).is_file()


def test_plugin_documentation_is_bilingual_and_repository_maintained():
    plugin_readme = (ROOT / 'skills/paper-reading/README.md').read_text(encoding='utf-8')
    plugin_readme_en = (ROOT / 'skills/paper-reading/README.en.md').read_text(encoding='utf-8')
    assert '[English](README.en.md)' in plugin_readme
    assert '[简体中文](README.md)' in plugin_readme_en
    assert 'Upload the ZIP and install it on ChatGPT Web' in plugin_readme_en
    assert 'Plugin Creator' in plugin_readme_en  # documented only as a fallback
    assert 'skills/paper-reading/README.md' in (ROOT / 'AGENTS.md').read_text(encoding='utf-8')


def test_ready_to_upload_archives_are_valid_and_match_the_releases():
    import json
    from zipfile import ZipFile

    expected = {
        'paper-reading-v0.7.0.zip': ('paper-reading', '0.7.0', 'skills/paper-reading/SKILL.md'),
        'research-idea-discovery-v4.0.19.zip': (
            'research-idea-discovery', '4.0.19', 'skills/research-idea-discovery/SKILL.md'
        ),
        'ai-mentor-v1.4.0.zip': ('AI Mentor', '1.4.0', 'skills/personal-phd-advisor/SKILL.md'),
    }
    for filename, (name, version, primary_skill) in expected.items():
        with ZipFile(ROOT / 'downloads' / filename) as archive:
            assert archive.testzip() is None
            names = set(archive.namelist())
            manifest = json.loads(archive.read('plugin.json').decode('utf-8'))
            codex_manifest = json.loads(archive.read('.codex-plugin/plugin.json').decode('utf-8'))
            assert manifest['name'] == codex_manifest['name'] == name
            assert manifest['version'] == codex_manifest['version'] == version
            assert primary_skill in names
            assert not any('YOUR_GITHUB_USERNAME' in archive.read(n).decode('utf-8', 'ignore') for n in names if n.endswith('.json'))
            if name == 'AI Mentor':
                assert 'LICENSE' in names
                assert b'CC BY-NC-SA 4.0' in archive.read('LICENSE')
