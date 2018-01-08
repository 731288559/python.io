/*
Navicat MySQL Data Transfer

Source Server         : 204
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : python

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-01-08 13:39:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `bilibili_funny_all`
-- ----------------------------
DROP TABLE IF EXISTS `bilibili_funny_all`;
CREATE TABLE `bilibili_funny_all` (
`id`  int(11) NOT NULL AUTO_INCREMENT ,
`title`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`href`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`play_num`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`dm_num`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`collect_num`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`v_author`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`v_date`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
AUTO_INCREMENT=24954

;

-- ----------------------------
-- Auto increment value for `bilibili_funny_all`
-- ----------------------------
ALTER TABLE `bilibili_funny_all` AUTO_INCREMENT=24954;
