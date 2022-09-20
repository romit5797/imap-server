CREATE DATABASE  IF NOT EXISTS `playverse`;
USE `playverse`;

/*------------EMAIL STORE-------------*/
DROP TABLE IF EXISTS `email_store`;
CREATE TABLE `email_store` (
  `uuid` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `site` varchar(255) NOT NULL,
  `sender` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `body` longtext NOT NULL,
  `bcc` varchar(12),
  `cc` varchar(255)
);

/*------------Last ID-------------*/
DROP TABLE IF EXISTS `last_id`;
CREATE TABLE `last_id` (
  `uuid` varchar(255) NOT NULL
);
