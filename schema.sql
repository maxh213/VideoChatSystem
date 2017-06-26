drop table if exists user;
create table user (
    id integer primary key autoincrement,
    username text UNIQUE not null,
    password text not null
);

drop table if exists call_history;
create table call_history (
    id integer primary key autoincrement,
	host_user_id integer not null,
	invited_user_id integer not null,
	timestamp datetime DEFAULT CURRENT_TIMESTAMP,
  	FOREIGN KEY(host_user_id) REFERENCES user(id),
  	FOREIGN KEY(invited_user_id) REFERENCES user(id)
);