function buildRuntimeConfig(env = process.env) {
  return {
    baseUrl: env.BASE_URL || 'http://127.0.0.1:4723',
    logLevel: env.LOG_LEVEL || 'info',
    platforms: {
      android: { parallel: true, retries: 1 },
      ios: { parallel: true, retries: 1 },
    },
  };
}

module.exports = { buildRuntimeConfig };
