-- Code adapted from 2016 FA INFO 290 TA project assignment


-- Create users
drop table if exists users;
create table users (
	user_id integer primary key,
	email text not null unique,
	first_name text null null,
	last_name text not null,
	insecure_password text not null,
	active boolean not null
);

drop table if exists careers;
create table careers (
	careers_id integer primary key,
	careers_name text,
	user_id integer,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);
