const { sharedConfig } = require('./wdio.shared.conf');
exports.config = {
  ...sharedConfig,
  capabilities: [{ platformName: 'iOS', 'appium:automationName': 'XCUITest' }],
};
