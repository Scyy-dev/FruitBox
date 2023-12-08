INSERT INTO team (teamID, prefix) VALUES
  ('team1', 'team1'),
  ('team2', 'tm2'),
  ('team3', 'TEAM3'),
  ('team4', 'team4'),
  ('team5', 'tm5'),
  ('team6', 'TEAM6'),
  ('team7', 'team7'),
  ('team8', 'tm8'),
  ('team9', 'TEAM9'),
  ('team10', 'team10'),
  ('team11', 'tm11'),
  ('team12', 'TEAM12');

INSERT INTO player (playerUUID, teamID, points) VALUES
  ('d99c665e0a8d4e39b97e6777cc613e62', 'team1', 78),
  ('6155f9f6a2dd43c9b753a1a65c419847', 'team1', 65),
  ('08cfd325a4644ef6b140500e9fd082fa', 'team2', 73),
  ('c2d4fc2c58dd40e2be0d03d449f6bb92', 'team2', 12),
  ('aff7965439f44cdea828a1d4f96de571', 'team3', 48),
  ('97074d5f5fb94c9aaf126ebb9fde1560', 'team3', 57),
  ('6c0ab2da1bdf4ee99d1c0bae1dcc711f', 'team4', 79),
  ('7db5e67d7420497a9bfc69c5f674a393', 'team4', 32),
  ('0d564cedd9be43fcba208154aa1e929b', 'team5', 53),
  ('cafb9b2bb57a427a99a5c5703d338b4a', 'team5', 40),
  ('7a675c488dee414798987f703833f94e', 'team6', 23),
  ('01d0010eb36f4c578bcafee1f9c58f00', 'team6', 56),
  ('fd18bf4bfbd2440a9da3ec1bc6a9f4e6', 'team7', 15),
  ('a9754982ab754c9bba2cbe02ff587816', 'team7', 60),
  ('30380c3e9e1a4726afd630691226f198', 'team8', 66),
  ('cf7d5d5ecd394375815200bd5666f907', 'team8', 84),
  ('1cacf13609d84bf39e4745a907079dbd', 'team9', 27),
  ('81a2acb1a1a647aaa932ae301e02f43a', 'team9', 38),
  ('59e7d6f162ca4e9c8781b7e40ea0557a', 'team10', 20),
  ('eb337020224c4465a60bdb15a5ea82c2', 'team10', 29),
  ('084c8708cb024270b2f73510da5b501a', 'team11', 58),
  ('1da1393be3f744239ee725198c5c2b8f', 'team11', 76),
  ('1638fb922a7f48829a89fb8515a547e5', 'team12', 70),
  ('e535a596d08d43c395abd647c3f253e2', 'team12', 75);

INSERT INTO boost (teamID, boost, boostEnd) VALUES
    ('team1', 1.5, 1701990550),
    ('team2', 5, 12345678),
    ('team3', 2, 1701990550);