async function retry(task, options = {}) {
  const attempts = options.attempts ?? 3;
  const delayMs = options.delayMs ?? 25;
  let lastError;
  for (let current = 1; current <= attempts; current += 1) {
    try {
      return await task(current);
    } catch (error) {
      lastError = error;
      if (current < attempts) {
        await new Promise((resolve) => setTimeout(resolve, delayMs));
      }
    }
  }
  throw lastError;
}

module.exports = { retry };
