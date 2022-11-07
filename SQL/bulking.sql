USE Marketing;
BULK INSERT Client
FROM 'C:\Python\python\Faker\csv\clients.csv'
WITH(
  FIELDTERMINATOR = ',',
  ROWTERMINATOR = '\n',
  FIRSTROW = 2
);
BULK INSERT Contract
FROM 'C:\Python\python\Faker\csv\contracts.csv'
WITH(
  FIELDTERMINATOR = ',',
  ROWTERMINATOR = '\n',
  FIRSTROW = 2
);
BULK INSERT Consultation
FROM 'C:\Python\python\Faker\csv\consultations.csv'
WITH(
  FIELDTERMINATOR = ',',
  ROWTERMINATOR = '\n',
  FIRSTROW = 2
);
BULK INSERT Contract_Employee
FROM 'C:\Python\python\Faker\csv\contract_employee.csv'
WITH(
  FIELDTERMINATOR = ',',
  ROWTERMINATOR = '\n',
  FIRSTROW = 2
);