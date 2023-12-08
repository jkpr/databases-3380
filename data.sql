INSERT INTO PHYSICIAN (Employee_id, Full_name)
VALUES
    -- ONLY ATTENDING FOR THE ASSIGNMENT
    ('000-213-012', 'John Smith'),
    ('000-879-234', 'Franklin Wong'),
    ('001-454-999', 'Alicia Zelaya'),
    --- ONLY RESIDENT FOR THE ASSIGNMENT
    ('000-776-393', 'Jennifer Wallace'),
    ('000-285-111', 'Ramesh Narayan'),
    ('001-444-503', 'Joyce English'),
    ('000-320-500', 'Ahmad Jabbar'),
    ('000-600-051', 'James Borg');

INSERT INTO EMPLOYMENT (Employee_id, Start_date, End_date, Trainee_status, PGY_n, Active)
VALUES
    ('000-213-012', '2012-07-01', '2017-06-30', 'resident', NULL, 'F'),
    ('000-213-012', '2017-07-01', NULL, 'attending',  NULL, 'T'),
    ('000-879-234', '2020-09-11', NULL, 'attending',  NULL, 'T'),
    ('001-454-999', '2023-05-20', NULL, 'attending',  NULL, 'T'),
    ('000-776-393', '2020-07-01', '2021-06-30', 'resident', 2, 'F'),
    ('000-776-393', '2021-07-01', '2022-06-30', 'resident', 3, 'F'),
    ('000-776-393', '2022-07-01', '2023-06-30', 'resident', 4, 'F'),
    ('000-776-393', '2023-07-01', NULL, 'resident', 5, 'T'),
    ('000-285-111', '2021-07-01', '2022-06-30', 'resident', 2, 'F'),
    ('000-285-111', '2022-07-01', '2023-06-30', 'resident', 3, 'F'),
    ('000-285-111', '2023-07-01', NULL, 'resident', 4, 'T'),
    ('001-444-503', '2022-07-01', '2023-06-30', 'resident', 2, 'F'),
    ('001-444-503', '2023-07-01', NULL, 'resident', 3, 'T'),
    ('000-320-500', '2022-07-01', '2023-06-30', 'resident', 2, 'F'),
    ('000-320-500', '2023-07-01', NULL, 'resident', 3, 'T'),
    ('000-600-051', '2023-07-01', NULL, 'resident', 2, 'T');

INSERT INTO TRAINEE_REQUIREMENT (Id, PGY_n, Body_part, Imaging_modality, Requirement_source, Quantity)
VALUES
    (1, 2, 'chest', 'mri', 'acgme', 50),
    (2, 3, 'chest', 'mri', 'acgme', 50),
    (3, 4, 'chest', 'mri', 'acgme', 50),
    (4, 5, 'chest', 'mri', 'acgme', 50),
    (5, 2, 'shoulder', 'ultrasound', 'acgme', 10),
    (6, 3, 'shoulder', 'ultrasound', 'acgme', 10),
    (7, 4, 'shoulder', 'ultrasound', 'acgme', 10),
    (8, 5, 'shoulder', 'ultrasound', 'acgme', 10),
    (9, 2, 'brain', 'ct', 'acgme', 5),
    (10, 3, 'brain', 'ct', 'acgme', 5),
    (11, 4, 'brain', 'ct', 'acgme', 5),
    (12, 5, 'brain', 'ct', 'acgme', 5),
    (13, 2, 'wrist', 'xray', 'acgme', 100),
    (14, 2, 'wrist', 'xray', 'acgme', 100),
    (15, 2, 'wrist', 'xray', 'acgme', 100),
    (16, 2, 'wrist', 'xray', 'acgme', 100);

INSERT INTO IS_ASSIGNED (Employee_id, Requirement_id)
VALUES
    -- ONLY ONE RESIDENT FOR THE ASSIGNMENT
    ('000-776-393', 4),
    ('000-776-393', 8),
    ('000-776-393', 12),
    ('000-776-393', 16);

INSERT INTO CPT_CODE (Code, Billable_amount, CDM_description, wRVU)
VALUES
    ('71550', 2001.49, 'Chest MRI w/o contrast', 3.430),
    ('76881', 140.10, 'Ultrasound, complete joint (i.e., joint space and peri-articular soft-tissue structures), real-time with image documentation.', 1.010),
    ('70470', 3333.33, 'Ct head/brain w/o & w/dye', 4.053),
    ('73110', 105.05, 'X-ray upper extremity. Wrist, complete', 0.60);

INSERT INTO STUDY (Accession_number, Imaging_modality, Body_part, Priority, Patient_id, Exam_date)
VALUES
    ('U49845', 'mri', 'chest', 10, 'PATIENT-00001', '2023-12-07 10:23:54'),
    ('U49846', 'mri', 'chest', 10, 'PATIENT-00002', '2023-12-07 10:36:54'),
    ('U49847', 'mri', 'chest', 10, 'PATIENT-00003', '2023-12-07 10:40:01'),
    ('U49848', 'ultrasound', 'shoulder', 10, 'PATIENT-00004', '2023-12-05 10:23:54'),
    ('U49849', 'ultrasound', 'shoulder', 10, 'PATIENT-00005', '2023-12-06 10:36:54'),
    ('U49850', 'ct', 'brain', 10, 'PATIENT-00006', '2023-12-06 23:01:01'),
    ('U49851', 'xray', 'wrist', 10, 'PATIENT-00007', '2023-12-03 12:12:54'),
    ('U49852', 'xray', 'wrist', 10, 'PATIENT-00008', '2023-12-04 17:17:54'),
    ('U49853', 'xray', 'wrist', 10, 'PATIENT-00009', '2023-12-05 20:20:01');

INSERT INTO CODED_WITH (Accession_number, CPT_code)
VALUES
    ('U49845', '71550'),
    ('U49846', '71550'),
    ('U49847', '71550'),
    ('U49848', '76881'),
    ('U49849', '76881'),
    ('U49850', '70470'),
    ('U49851', '73110'),
    ('U49852', '73110'),
    ('U49853', '73110');

INSERT INTO REPORT_REVISION (Accession_number, Version_number, Author, Prelim_or_final, Report_text, Date_time_saved)
VALUES
    ('U49845', 1, '000-776-393', 'prelim', '<h1>Impressions</h1><p>Text of the report</p>', '2023-12-07 10:35:54'),
    ('U49845', 2, '000-213-012', 'final', '<h1>Impressions</h1><p>Text of the report.</p><p>Addended text here.</p>', '2023-12-07 10:46:54'),
    ('U49846', 1, '000-213-012', 'final', '<h1>Impressions</h1><p>Text of the report.</p>', '2023-12-07 10:49:53'),
    ('U49847', 1, '000-213-012', 'final', '<h1>Impressions</h1><p>Text of the report.</p>', '2023-12-07 10:52:52'),
    ('U49848', 1, '000-776-393', 'prelim', 'Impresions', '2023-12-05 10:50:54'),
    ('U49849', 1, '000-776-393', 'prelim', 'Impresions', '2023-12-06 10:59:54'),
    ('U49848', 2, '000-213-012', 'final', 'Impresions', '2023-12-05 11:03:54'),
    ('U49849', 2, '000-213-012', 'final', 'Impresions', '2023-12-06 11:06:54'),
    ('U49850', 1, '000-213-012', 'final', 'Impresions', '2023-12-06 23:31:01'),
    ('U49851', 1, '000-213-012', 'final', 'Impressions', '2023-12-03 12:18:54'),
    ('U49852', 1, '000-213-012', 'final', 'Impressions', '2023-12-04 17:23:54'),
    ('U49853', 1, '000-879-234', 'final', 'Impressions', '2023-12-05 23:20:01');
