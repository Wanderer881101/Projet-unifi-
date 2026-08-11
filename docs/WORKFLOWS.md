# GitHub Actions Workflows Documentation

## 📋 Configured Workflows

### 1. Integration Workflow (`integration.yml`)
**Purpose**: Repository synchronization and structure validation

**Triggers**:
- Push to main/develop
- Pull requests to main/develop
- Daily schedule (2 AM UTC)

**Jobs**:
- `sync-repositories`: Uses git subtree to pull latest from source repos
- `validate-structure`: Verifies project structure integrity

**Status Badges**:
```markdown
[![Integration](https://github.com/Wanderer881101/Projet-unifi-/actions/workflows/integration.yml/badge.svg)](https://github.com/Wanderer881101/Projet-unifi-/actions/workflows/integration.yml)
```

---

### 2. Tests Workflow (`tests.yml`)
**Purpose**: Automated testing, linting, and code quality checks

**Triggers**:
- Push to any branch
- Pull requests to main/develop

**Jobs**:
- `test-core`: Unit tests on Python 3.11, 3.12, 3.13
- `test-module`: Module protocol validation
- `lint`: Code style (flake8, black, isort)
- `security`: Dependency and code security scans

**Coverage**:
- ✅ Unit tests with pytest
- ✅ Code coverage reporting to Codecov
- ✅ Linting (flake8)
- ✅ Code formatting (black)
- ✅ Import sorting (isort)

**Status Badges**:
```markdown
[![Tests](https://github.com/Wanderer881101/Projet-unifi-/actions/workflows/tests.yml/badge.svg)](https://github.com/Wanderer881101/Projet-unifi-/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/Wanderer881101/Projet-unifi-/branch/main/graph/badge.svg)](https://codecov.io/gh/Wanderer881101/Projet-unifi-)
```

---

### 3. Build Workflow (`build.yml`)
**Purpose**: Build packages and create releases

**Triggers**:
- Push to main branch
- Tagged releases (v*)
- Manual dispatch

**Jobs**:
- `build-package`: Builds on Ubuntu, Windows, macOS
- `create-release`: Creates GitHub release with artifacts
- `docker-build`: Builds Docker image (on main branch)

**Outputs**:
- Python wheel package
- PyInstaller executables
- Source distribution
- Docker image

**Status Badges**:
```markdown
[![Build](https://github.com/Wanderer881101/Projet-unifi-/actions/workflows/build.yml/badge.svg)](https://github.com/Wanderer881101/Projet-unifi-/actions/workflows/build.yml)
```

---

### 4. Security Workflow (`security.yml`)
**Purpose**: Comprehensive security scanning

**Triggers**:
- Push to main/develop
- Pull requests to main/develop
- Daily schedule (3 AM UTC)

**Jobs**:
- `dependency-check`: Checks for vulnerable dependencies
- `code-scanning`: Runs bandit and semgrep
- `codeql-analysis`: GitHub's advanced code analysis
- `secret-scanning`: Detects exposed secrets

**Integrations**:
- ✅ Codecov
- ✅ GitHub Security tab
- ✅ SARIF report generation

**Status Badges**:
```markdown
[![Security](https://github.com/Wanderer881101/Projet-unifi-/actions/workflows/security.yml/badge.svg)](https://github.com/Wanderer881101/Projet-unifi-/actions/workflows/security.yml)
```

---

## 🚀 Usage Examples

### Run All Workflows
```bash
# Automatically triggered on push
git push origin develop

# View workflow status
gh workflow list
gh workflow view integration.yml
```

### Trigger Manual Workflow
```bash
# Dispatch build workflow
gh workflow run build.yml

# View workflow runs
gh run list --workflow=build.yml

# View specific run details
gh run view <run-id>
```

### Access Workflow Results
- **Logs**: GitHub Actions tab → Workflow run → Job logs
- **Artifacts**: Artifacts section in workflow run
- **Reports**: Security tab for code scanning results
- **Coverage**: Link to Codecov dashboard

---

## 📊 Workflow Performance

| Workflow | Duration | Matrix |
|----------|----------|--------|
| Integration | ~2-3 min | Single (ubuntu-latest) |
| Tests | ~5-8 min | 3 Python versions |
| Build | ~10-15 min | 3 OS × 2 Python versions |
| Security | ~7-10 min | Single (ubuntu-latest) |

**Total CI/CD time per push**: ~15-20 minutes

---

## 🔐 Secrets Management

Required GitHub Secrets:
- `GITHUB_TOKEN` (auto-provided)
- `CODECOV_TOKEN` (optional, for codecov.io)

**Do NOT commit**:
- API keys
- Credentials
- Private tokens
- Database passwords

---

## ✅ Workflow Status Checks

All workflows required to pass before merging to `main`:
- ✅ Integration (structure validation)
- ✅ Tests (unit tests + linting)
- ✅ Build (successful build)
- ✅ Security (no vulnerabilities)

---

## 📈 Monitoring & Alerts

### GitHub Actions Dashboard
- View: https://github.com/Wanderer881101/Projet-unifi-/actions
- Status badge in README
- Email notifications on failure

### Status Page
- All workflows visible in Actions tab
- Individual run logs available
- Artifact downloads

---

## 🛠️ Troubleshooting

### Workflow Failure
1. Click on failed workflow run
2. View job logs
3. Check error messages
4. Fix issue locally
5. Push and retry

### Re-run Workflow
```bash
# Re-run failed jobs
gh run rerun <run-id> --failed

# Re-run entire workflow
gh run rerun <run-id>
```

### Skip Workflow
```bash
# Skip CI for a commit
git commit --allow-empty -m "chore: skip-ci" -m "[skip ci]"
```

---

## 📚 Resources

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Expressions](https://docs.github.com/en/actions/learn-github-actions/expressions)
- [Environment Variables](https://docs.github.com/en/actions/learn-github-actions/environment-variables)

---

**Owner**: Jonathan Therrien (Wanderer881101)  
**Last Updated**: 2026-08-11  
**Version**: 1.0
