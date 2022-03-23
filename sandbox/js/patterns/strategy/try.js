const logger = (strategy, level, message, ...args) => {
  return strategy(level, message, ...args)
}

const logToConsoleStrategy = (level, message) =>      console[level](message)

const logToDOMStrategy = (level, message, node) => {
  node.innerHTML = `<div class='${level}'>${message}</div>`
  console[level](message)
  console[level](node)
}

logger(
  logToConsoleStrategy,
  'log',
  'log first message to console'
)

logger(
  logToDOMStrategy,
  'warn',
  'log second message to dom',
  document.querySelector('#log')
)
