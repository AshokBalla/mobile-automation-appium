const { sharedConfig } = require('./wdio.shared.conf');
exports.config = {
  ...sharedConfig,
  capabilities: [{ platformName: 'Android', 'appium:automationName': 'UiAutomator2' }],
};
