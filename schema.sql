CREATE TABLE STUDY (
  Accession_number VARCHAR(128) NOT NULL PRIMARY KEY,
  Imaging_modality VARCHAR(64) NOT NULL,
  Body_part VARCHAR(64) NOT NULL,
  Priority INT NOT NULL,
  Patient_id VARCHAR(64) NOT NULL,
  Exam_date TIMESTAMP NOT NULL
);

CREATE TABLE CPT_CODE (
  Code VARCHAR(64) NOT NULL PRIMARY KEY,
  Billable_amount NUMERIC(9, 2),
  CDM_description VARCHAR(256) NOT NULL,
  wRVU NUMERIC(7, 3) NOT NULL
);

CREATE TABLE CODED_WITH (
  Accession_number VARCHAR(128) NOT NULL REFERENCES STUDY(Accession_number),
  CPT_code VARCHAR(64) NOT NULL REFERENCES CPT_CODE(Code),
  PRIMARY KEY (Accession_number, CPT_code)
);

CREATE TABLE PHYSICIAN (
  Employee_id VARCHAR(64) NOT NULL PRIMARY KEY,
  Full_name VARCHAR(128) NOT NULL
);

CREATE TABLE REPORT_REVISION (
  Accession_number VARCHAR(128) NOT NULL REFERENCES STUDY(Accession_number),
  Version_number INT NOT NULL,
  Author VARCHAR(64) NOT NULL REFERENCES PHYSICIAN(Employee_id),
  Prelim_or_final VARCHAR(32) NOT NULL,
  Report_text VARCHAR(4098) NOT NULL,
  Date_time_saved TIMESTAMP NOT NULL,
  PRIMARY KEY (Accession_number, Version_number)
);

CREATE TABLE EMPLOYMENT (
  Employee_id VARCHAR(64) NOT NULL REFERENCES PHYSICIAN(Employee_id),
  Start_date DATE NOT NULL,
  End_date DATE,
  Trainee_status VARCHAR(64) NOT NULL,
  PGY_n INT,
  Active BOOL,
  PRIMARY KEY (Employee_id, Start_date)
);

CREATE TABLE TRAINEE_REQUIREMENT (
  Id INT NOT NULL PRIMARY KEY,
  PGY_n INT NOT NULL,
  Body_part VARCHAR(64) NOT NULL,
  Imaging_modality VARCHAR(64) NOT NULL,
  Requirement_source VARCHAR(64) NOT NULL,
  Quantity INT NOT NULL
);

CREATE TABLE IS_ASSIGNED (
  Employee_id VARCHAR(64) NOT NULL,
  Requirement_id INT NOT NULL,
  PRIMARY KEY (Employee_id, Requirement_id)
);
