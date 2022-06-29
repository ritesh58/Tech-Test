function parseIn(object, path) {
    if (path == undefined) throw new Error('Key not defined');
    const keysArray = path.split('/');
    var current = object;
    for (const key of keysArray) {
        current = current[key];
      }
    return current;
}
module.exports = parseIn;