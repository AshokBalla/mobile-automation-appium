# appium-tests

Mobile automation framework built around reusable page objects, environment-driven capabilities, and CI-ready reporting.

## Highlights

- Appium 2
- WebdriverIO
- Mocha-ready structure
- Parallel Android and iOS capability profiles

## Getting Started

```bash
npm install
npm test
npm run test:e2e:android
```

## Project Structure

- `tests/`
- `pages/`
- `utils/`
- `config/`
- `reports/`
- `test-data/`
- `scripts/`

## Reporting

- HTML, JSON, and screenshot/video friendly output paths are pre-created.
- CI examples publish artifacts and preserve failure diagnostics.

## Contribution Guide

1. Create a branch from `develop`.
2. Keep helpers reusable and environment-driven.
3. Add or update validation tests with every framework change.
4. Document any new test data, report artifacts, and CI behavior.

## Notes

- This repository keeps browser and device endpoints in `.env.sample` only.
- Unit validations run without requiring a device farm.
- - 2023: created focused repository split for Mobile automation framework with Android and iOS execution profiles.

## Career Evolution & Historical Tests
The `original-tests` directory contains historical test suites and experiments from earlier stages of this project's lifecycle (2023-2025). This folder is preserved to demonstrate the evolution from initial test scripts to the modern, scalable framework architecture seen in the current `tests/` and `src/` directories.
