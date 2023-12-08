CREATE TABLE team (
  teamID varchar(12),
  prefix varchar(55),

  CONSTRAINT teamID_pk PRIMARY KEY (teamID)
);

CREATE TABLE player (
  playerUUID char(32),
  teamID varchar(12),
  points BIGINT,

  CONSTRAINT playerUUID_pk PRIMARY KEY (playerUUID),
  CONSTRAINT player_teamID_fk FOREIGN KEY (teamID) REFERENCES team(teamID)
);

CREATE TABLE boost (
  boostID int NOT NULL AUTO_INCREMENT,
  teamID varchar(12),
  boost DOUBLE,
  boostEnd BIGINT,

  CONSTRAINT boostID_pk PRIMARY KEY (boostID),
  CONSTRAINT boost_teamID FOREIGN KEY (teamID) REFERENCES team(teamID)
);