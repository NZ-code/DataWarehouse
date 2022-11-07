CREATE TABLE Client(
  id int,
  name varchar(100),
  primary key(id)
);
CREATE TABLE Contract
(
  id int,
  price int,
  team_count int,
  client_id int,
  begin_at date,
  closed_at date,
  service_type varchar(100) CHECK( service_type in ('logo', 'poster','text','video','media care')),
  is_accepted bit,

  primary key(id),
  foreign key(client_id) references Client(id)
);
CREATE TABLE Consultation(
  id int,
  duration int,
  hourly_rate  int,
  employee_id int,
  contract_id int,
  date date,
  primary key(id),
  foreign key(contract_id) references Contract(id)
);

CREATE TABLE Contract_Employee
(
  contract_id int,
  employee_id int,
  primary key(employee_id, contract_id),
  foreign key(contract_id) references Contract(id)
);