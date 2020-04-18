/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1_3307
 Source Server Type    : MySQL
 Source Server Version : 50645
 Source Host           : localhost:3307
 Source Schema         : backstage

 Target Server Type    : MySQL
 Target Server Version : 50645
 File Encoding         : 65001

 Date: 18/04/2020 17:47:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for api_model
-- ----------------------------
DROP TABLE IF EXISTS `api_model`;
CREATE TABLE `api_model`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) NOT NULL,
  `path` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `desc` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of api_model
-- ----------------------------
INSERT INTO `api_model` VALUES (1, 101, 'users', '用户');
INSERT INTO `api_model` VALUES (2, 102, 'goods', '商品');
INSERT INTO `api_model` VALUES (3, 103, 'power', '权限');
INSERT INTO `api_model` VALUES (4, 104, 'orders', '订单');
INSERT INTO `api_model` VALUES (5, 105, 'data', '数据');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add api model', 7, 'add_apimodel');
INSERT INTO `auth_permission` VALUES (26, 'Can change api model', 7, 'change_apimodel');
INSERT INTO `auth_permission` VALUES (27, 'Can delete api model', 7, 'delete_apimodel');
INSERT INTO `auth_permission` VALUES (28, 'Can view api model', 7, 'view_apimodel');
INSERT INTO `auth_permission` VALUES (29, 'Can add label model', 8, 'add_labelmodel');
INSERT INTO `auth_permission` VALUES (30, 'Can change label model', 8, 'change_labelmodel');
INSERT INTO `auth_permission` VALUES (31, 'Can delete label model', 8, 'delete_labelmodel');
INSERT INTO `auth_permission` VALUES (32, 'Can view label model', 8, 'view_labelmodel');
INSERT INTO `auth_permission` VALUES (33, 'Can add user model', 9, 'add_usermodel');
INSERT INTO `auth_permission` VALUES (34, 'Can change user model', 9, 'change_usermodel');
INSERT INTO `auth_permission` VALUES (35, 'Can delete user model', 9, 'delete_usermodel');
INSERT INTO `auth_permission` VALUES (36, 'Can view user model', 9, 'view_usermodel');
INSERT INTO `auth_permission` VALUES (37, 'Can add user type model', 10, 'add_usertypemodel');
INSERT INTO `auth_permission` VALUES (38, 'Can change user type model', 10, 'change_usertypemodel');
INSERT INTO `auth_permission` VALUES (39, 'Can delete user type model', 10, 'delete_usertypemodel');
INSERT INTO `auth_permission` VALUES (40, 'Can view user type model', 10, 'view_usertypemodel');
INSERT INTO `auth_permission` VALUES (41, 'Can add user token', 11, 'add_usertoken');
INSERT INTO `auth_permission` VALUES (42, 'Can change user token', 11, 'change_usertoken');
INSERT INTO `auth_permission` VALUES (43, 'Can delete user token', 11, 'delete_usertoken');
INSERT INTO `auth_permission` VALUES (44, 'Can view user token', 11, 'view_usertoken');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_bin NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (7, 'Api', 'apimodel');
INSERT INTO `django_content_type` VALUES (8, 'Api', 'labelmodel');
INSERT INTO `django_content_type` VALUES (9, 'Api', 'usermodel');
INSERT INTO `django_content_type` VALUES (11, 'Api', 'usertoken');
INSERT INTO `django_content_type` VALUES (10, 'Api', 'usertypemodel');
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'Api', '0001_initial', '2020-04-11 03:04:16.687357');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0001_initial', '2020-04-11 03:04:16.767355');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2020-04-11 03:04:16.895351');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0001_initial', '2020-04-11 03:04:17.217592');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0002_logentry_remove_auto_add', '2020-04-11 03:04:17.297587');
INSERT INTO `django_migrations` VALUES (6, 'admin', '0003_logentry_add_action_flag_choices', '2020-04-11 03:04:17.309588');
INSERT INTO `django_migrations` VALUES (7, 'contenttypes', '0002_remove_content_type_name', '2020-04-11 03:04:17.390586');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0002_alter_permission_name_max_length', '2020-04-11 03:04:17.433588');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0003_alter_user_email_max_length', '2020-04-11 03:04:17.483588');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0004_alter_user_username_opts', '2020-04-11 03:04:17.499594');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0005_alter_user_last_login_null', '2020-04-11 03:04:17.532590');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0006_require_contenttypes_0002', '2020-04-11 03:04:17.537594');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0007_alter_validators_add_error_messages', '2020-04-11 03:04:17.555587');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0008_alter_user_username_max_length', '2020-04-11 03:04:17.597587');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0009_alter_user_last_name_max_length', '2020-04-11 03:04:17.647590');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0010_alter_group_name_max_length', '2020-04-11 03:04:17.702592');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0011_update_proxy_permissions', '2020-04-11 03:04:17.720624');
INSERT INTO `django_migrations` VALUES (18, 'sessions', '0001_initial', '2020-04-11 03:04:17.741624');
INSERT INTO `django_migrations` VALUES (19, 'Api', '0002_auto_20200411_1124', '2020-04-11 03:24:23.429952');
INSERT INTO `django_migrations` VALUES (20, 'Api', '0002_auto_20200411_1330', '2020-04-11 05:30:59.943391');
INSERT INTO `django_migrations` VALUES (21, 'Api', '0003_auto_20200411_1331', '2020-04-11 05:31:40.818823');
INSERT INTO `django_migrations` VALUES (22, 'Api', '0004_usermodel_is_active', '2020-04-12 12:48:05.037471');
INSERT INTO `django_migrations` VALUES (23, 'Api', '0005_auto_20200414_1139', '2020-04-14 03:39:59.239587');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for label
-- ----------------------------
DROP TABLE IF EXISTS `label`;
CREATE TABLE `label`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label_name` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `parent_id` int(11) NOT NULL,
  `label_level` int(11) NOT NULL,
  `icon_class` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `pid` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of label
-- ----------------------------
INSERT INTO `label` VALUES (1, '用户管理', 0, 0, 'el-icon-users', 101);
INSERT INTO `label` VALUES (2, '商品管理', 0, 0, 'el-icon-goods', 102);
INSERT INTO `label` VALUES (3, '权限管理', 0, 0, 'el-icon-permission', 103);
INSERT INTO `label` VALUES (4, '订单管理', 0, 0, 'el-icon-dingdan', 104);
INSERT INTO `label` VALUES (5, '数据统计', 0, 0, 'el-icon-data', 105);
INSERT INTO `label` VALUES (7, '角色列表', 3, 1, NULL, 103);
INSERT INTO `label` VALUES (8, '用户列表', 1, 1, NULL, 101);
INSERT INTO `label` VALUES (9, '分类参数', 2, 1, NULL, 102);
INSERT INTO `label` VALUES (10, '商品分类', 2, 1, NULL, 102);
INSERT INTO `label` VALUES (11, '商品列表', 2, 1, NULL, 102);
INSERT INTO `label` VALUES (12, '权限列表', 3, 1, NULL, 103);
INSERT INTO `label` VALUES (13, '数据展示', 5, 1, NULL, 105);
INSERT INTO `label` VALUES (14, '订单列表', 4, 1, NULL, 104);

-- ----------------------------
-- Table structure for user_model
-- ----------------------------
DROP TABLE IF EXISTS `user_model`;
CREATE TABLE `user_model`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(16) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `userphone` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `created_time` datetime(6) NULL DEFAULT NULL,
  `updated_time` datetime(6) NULL DEFAULT NULL,
  `user_type_id` int(11) NOT NULL,
  `user_email` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `user_model_userphone_4378952c_uniq`(`userphone`) USING BTREE,
  UNIQUE INDEX `email`(`user_email`) USING BTREE,
  INDEX `user_model_user_type_id_bb4a4a40_fk_user_type_id`(`user_type_id`) USING BTREE,
  CONSTRAINT `user_model_user_type_id_bb4a4a40_fk_user_type_id` FOREIGN KEY (`user_type_id`) REFERENCES `user_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_model
-- ----------------------------
INSERT INTO `user_model` VALUES (1, 'hwt', '123456', '16623456784', '2020-04-11 08:12:06.000000', '2020-04-15 06:17:49.829644', 2, 'hwt@123.com', 1);
INSERT INTO `user_model` VALUES (2, 'admin', '123456', '17711110001', '2020-04-11 06:05:02.000000', '2020-04-15 06:47:15.201155', 3, 'admin@163.com', 1);
INSERT INTO `user_model` VALUES (3, 'vector', '123456', '15412785431', '2020-04-11 03:26:23.293082', NULL, 2, 'vector@132.com', 0);
INSERT INTO `user_model` VALUES (4, 'Zhang', 'zhang123', '13514236543', '2020-04-11 03:44:48.040284', '2020-04-14 07:06:23.425664', 1, 'zhangsd@123.com', 1);
INSERT INTO `user_model` VALUES (6, 'XiaoMing', 'xiaoming123', '17821345432', '2020-04-11 03:54:08.364943', '2020-04-14 07:06:56.487342', 1, 'xiaomingcli12@gfd.io.cn', 0);
INSERT INTO `user_model` VALUES (7, 'Lufy', 'Lufy', '16753288910', '2020-04-11 08:02:26.392107', NULL, 1, 'Lufy123@sg.io', 0);
INSERT INTO `user_model` VALUES (8, 'ceshi1', '123456', '15612341234', '2020-04-13 07:01:48.299646', NULL, 1, 'ceshi1@test.com', 1);
INSERT INTO `user_model` VALUES (9, '张晓明', 'xiaoming123', '17654328901', '2020-04-13 07:04:02.974184', NULL, 2, 'xiaoming@163.com', 1);
INSERT INTO `user_model` VALUES (10, 'ceshi2', '123123', '19910231234', '2020-04-13 07:11:20.148083', NULL, 1, 'ceshi2@testing.cn', 1);
INSERT INTO `user_model` VALUES (12, 'test_vue1', '123456', '17534561342', '2020-04-13 07:19:20.350107', NULL, 1, 'vue@vue.cli.cn', 1);

-- ----------------------------
-- Table structure for user_token
-- ----------------------------
DROP TABLE IF EXISTS `user_token`;
CREATE TABLE `user_token`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id`) USING BTREE,
  CONSTRAINT `user_token_user_id_69e1f632_fk_user_model_id` FOREIGN KEY (`user_id`) REFERENCES `user_model` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_token
-- ----------------------------
INSERT INTO `user_token` VALUES (1, 'a3b2ed4eed8a456e9f7a36df245b67d2', 2);

-- ----------------------------
-- Table structure for user_type
-- ----------------------------
DROP TABLE IF EXISTS `user_type`;
CREATE TABLE `user_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_type
-- ----------------------------
INSERT INTO `user_type` VALUES (1, '普通用户');
INSERT INTO `user_type` VALUES (2, '管理用户');
INSERT INTO `user_type` VALUES (3, '超级用户');

SET FOREIGN_KEY_CHECKS = 1;
