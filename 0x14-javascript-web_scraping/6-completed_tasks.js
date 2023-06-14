#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId]++;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  } else {
    console.error('Failed to retrieve tasks. Status code:', response.statusCode);
  }
});
