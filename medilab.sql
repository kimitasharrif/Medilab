CREATE TABLE IF NOT EXISTS `members` (
	`member_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`surname` text NOT NULL,
	`others` text NOT NULL,
	`gender` text NOT NULL,
	`email` varchar(255) NOT NULL,
	`phone` varchar(255) NOT NULL,
	`d.o.b` date NOT NULL,
	`status` boolean NOT NULL,
	`password` varchar(255) NOT NULL,
	`location_id` int NOT NULL,
	`reg_date` timestamp NOT NULL,
	PRIMARY KEY (`member_id`)
);

CREATE TABLE IF NOT EXISTS `Location` (
	`location_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`location_name` int NOT NULL,
	PRIMARY KEY (`location_id`)
);

CREATE TABLE IF NOT EXISTS `dependants` (
	`dependant_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`surname` text NOT NULL,
	`others` text NOT NULL,
	`d.o.b` date NOT NULL,
	`reg_date` timestamp NOT NULL,
	`member_id` int NOT NULL,
	PRIMARY KEY (`dependant_id`)
);

CREATE TABLE IF NOT EXISTS `payements` (
	`payment_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`invoice_no` varchar(255) NOT NULL,
	`total_amount` int NOT NULL,
	`reg_date` timestamp NOT NULL,
	PRIMARY KEY (`payment_id`)
);

CREATE TABLE IF NOT EXISTS `Laboratories` (
	`lab_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`lab_name` text NOT NULL,
	`email` varchar(255) NOT NULL,
	`phone` varchar(255) NOT NULL,
	`permit_id` varchar(255),
	`password` varchar(255) NOT NULL,
	`reg_date` int NOT NULL,
	PRIMARY KEY (`lab_id`)
);

CREATE TABLE IF NOT EXISTS `Lab_tests` (
	`test_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`lab_id` int NOT NULL,
	`test_name` text NOT NULL,
	`test_description` int NOT NULL,
	`test_cost` int NOT NULL,
	`test_discount` int NOT NULL,
	`reg_date` timestamp NOT NULL,
	`new_field` int NOT NULL,
	PRIMARY KEY (`test_id`)
);

CREATE TABLE IF NOT EXISTS `nurses` (
	`nurse_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`surname` text NOT NULL,
	`others` text NOT NULL,
	`gender` text NOT NULL,
	`lab_id` int NOT NULL,
	`reg_date` int NOT NULL,
	PRIMARY KEY (`nurse_id`)
);

CREATE TABLE IF NOT EXISTS `admin` (
	`admin_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`email` varchar(255) NOT NULL,
	`username` varchar(255) NOT NULL,
	`status` boolean NOT NULL,
	`phone` varchar(255) NOT NULL,
	`password` varchar(255) NOT NULL,
	PRIMARY KEY (`admin_id`)
);

CREATE TABLE IF NOT EXISTS `booking` (
	`book_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`member_id` int NOT NULL,
	`booked_for` varchar(255) NOT NULL,
	`dependant_id` int,
	`test_id` int NOT NULL,
	`appointment_date` date NOT NULL,
	`appointment_time` int NOT NULL,
	`where_taken` text NOT NULL,
	`reg_date` timestamp NOT NULL,
	`latitude` varchar(255),
	`longitude` varchar(255),
	`status` text NOT NULL,
	`lab_id` int NOT NULL,
	`invoice_no` int NOT NULL,
	PRIMARY KEY (`book_id`)
);

CREATE TABLE IF NOT EXISTS `nurse_lab_allocations` (
	`allocation_id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`nurse_id` int NOT NULL,
	`invoice_no` int NOT NULL,
	PRIMARY KEY (`allocation_id`)
);

ALTER TABLE `members` ADD CONSTRAINT `members_fk9` FOREIGN KEY (`location_id`) REFERENCES `Location`(`location_id`);

ALTER TABLE `dependants` ADD CONSTRAINT `dependants_fk5` FOREIGN KEY (`member_id`) REFERENCES `members`(`member_id`);


ALTER TABLE `Lab_tests` ADD CONSTRAINT `Lab_tests_fk1` FOREIGN KEY (`lab_id`) REFERENCES `Laboratories`(`lab_id`);
ALTER TABLE `nurses` ADD CONSTRAINT `nurses_fk4` FOREIGN KEY (`lab_id`) REFERENCES `Laboratories`(`lab_id`);

ALTER TABLE `booking` ADD CONSTRAINT `booking_fk1` FOREIGN KEY (`member_id`) REFERENCES `members`(`member_id`);

ALTER TABLE `booking` ADD CONSTRAINT `booking_fk3` FOREIGN KEY (`dependant_id`) REFERENCES `dependants`(`dependant_id`);

ALTER TABLE `booking` ADD CONSTRAINT `booking_fk4` FOREIGN KEY (`test_id`) REFERENCES `Lab_tests`(`test_id`);

ALTER TABLE `booking` ADD CONSTRAINT `booking_fk12` FOREIGN KEY (`lab_id`) REFERENCES `Laboratories`(`lab_id`);

ALTER TABLE `booking` ADD CONSTRAINT `booking_fk13` FOREIGN KEY (`invoice_no`) REFERENCES `payements`(`invoice_no`);
ALTER TABLE `nurse_lab_allocations` ADD CONSTRAINT `nurse_lab_allocations_fk1` FOREIGN KEY (`nurse_id`) REFERENCES `nurses`(`nurse_id`);

ALTER TABLE `nurse_lab_allocations` ADD CONSTRAINT `nurse_lab_allocations_fk2` FOREIGN KEY (`invoice_no`) REFERENCES `booking`(`invoice_no`);