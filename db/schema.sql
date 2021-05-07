use todos;

CREATE TABLE tasks (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

INSERT INTO tasks (name) values ('task 1');
INSERT INTO tasks (name) values ('task 2');
INSERT INTO tasks (name) values ('task 3');
