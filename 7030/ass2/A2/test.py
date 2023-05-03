from a2 import *
# from a2_support import *


#
# #
# class Card:
#
#     def get_damage_amount(self) -> int:
#         return 0
#
#     def get_block(self) -> int:
#         return 0
#
#     def get_energy_cost(self) -> int:
#         return 1
#
#     def get_status_modifiers(self) -> dict[str, int]:
#         return {}
#
#     def get_name(self) -> str:
#         return self.__class__.__name__
#
#     def get_description(self) -> str:
#         return "A card"
#
#     def requires_target(self) -> bool:
#         return True
#
#     def __str__(self) -> str:
#         return "{}: {}".format(self.get_name(), self.get_description())
#
#     def __repr__(self) -> str:
#         return "Card()"

# #
# card = Card()
# print(card.__repr__())
# print(card.get_damage_amount())
# # print(card.get_block())
# # print(str(card))
# #
# #
# # class Strike(Card):
# #     def __init__(self):
# #         super().__init__()
# #
# #     def get_damage_amount(self):
# #         return 6
# #
# #     def get_energy_cost(self):
# #         return 1
# #
# #     def get_name(self):
# #         return "Strike"
# #
# #     def get_description(self):
# #         return "Deal 6 damage."
# #
# #     def __repr__(self):
# #         return "Strike()"
# #
# #
# # strike = Strike()
# # print(strike.get_damage_amount(), strike.get_block(), strike.get_energy_cost())
# # print(strike.get_name())
# # print(strike)
# # print(strike.requires_target())
# #
# #
# # class Defend(Card):
# #     def __init__(self):
# #         super().__init__()
# #
# #     def get_block(self):
# #         return 5
# #
# #     def get_energy_cost(self):
# #         return 1
# #
# #     def get_name(self):
# #         return "Defend"
# #
# #     def get_description(self):
# #         return "Gain 5 block."
# #
# #     def requires_target(self):
# #         return False
# #
# #     def __repr__(self):
# #         return "Defend()"
# #
# #
# # defend = Defend()
# # print(defend.get_damage_amount(), defend.get_block(), defend.get_energy_cost())
# # print(defend.get_name())
# # print(defend.get_description())
# # print(defend.requires_target())
# # print(str(defend))
# #
# #
# # class Bash(Card):
# #     def __init__(self):
# #         super().__init__()
# #
# #     def get_damage_amount(self):
# #         return 7
# #
# #     def get_block(self):
# #         return 5
# #
# #     def get_energy_cost(self):
# #         return 2
# #
# #     # def get_name(self):
# #     #     return self.__class__.__name__
# #
# #     def get_description(self):
# #         return "Deal 7 damage. Gain 5 block."
# #
# #     def __repr__(self):
# #         return "Bash()"
# #
# #
# # # bash = Bash()
# # # print(bash.get_damage_amount(), bash.get_block(),
# # #       bash.get_energy_cost())
# # # print(bash.get_name())
# # # print(bash.get_description())
# # # print(bash.requires_target())
# # # print(str(bash))
# #
# #
# # class Neutralize(Card):
# #     def __init__(self):
# #         super().__init__()
# #
# #     def get_damage_amount(self):
# #         return 3
# #
# #     def get_energy_cost(self) -> int:
# #         return 0
# #
# #     def get_status_modifiers(self):
# #         return {"weak": 1, "vulnerable": 2}
# #
# #     def get_name(self):
# #         return "Neutralize"
# #
# #     def get_description(self):
# #         return "Deal 3 damage. Apply 1 weak. Apply 2 vulnerable."
# #
# #     def __repr__(self):
# #         return "Neutralize()"
# #
# #
# # # neutralize = Neutralize()
# # # print(neutralize.get_damage_amount(), neutralize.get_block(), neutralize.get_energy_cost())
# # # print(neutralize.get_status_modifiers())
# #
# #
# # class Survivor(Card):
# #     # def __init__(self):
# #     #     super().__init__()
# #
# #     def get_block(self):
# #         return 8
# #
# #     def get_status_modifiers(self):
# #         return {"strength": 1}
# #
# #     def get_name(self):
# #         return "Survivor"
# #
# #     def get_description(self):
# #         return "Gain 8 block and 1 strength."
# #
# #     def requires_target(self):
# #         return False
# #
# #     def __repr__(self):
# #         return "Survivor()"
# #
# #
# survivor = Survivor()
# i = (survivor.get_status_modifiers()).get("weak")
# if i is None:
#     i = 0
# print(i)

# # # print(survivor.get_damage_amount(), survivor.get_block(), survivor.get_energy_cost())
# # # print(survivor.get_status_modifiers())
# # # print(survivor.requires_target())
# #
# # class Entity:
# #     def __init__(self, max_hp: int) -> None:
# #         self._max_hp = max_hp
# #         self._hp = max_hp
# #         self._block = 0
# #         self._strength = 0
# #         self._weak = 0
# #         self._vulnerable = 0
# #
# #     def get_hp(self) -> int:
# #         return self._hp
# #
# #     def get_max_hp(self) -> int:
# #         return self._max_hp
# #
# #     def get_block(self) -> int:
# #         return self._block
# #
# #     def get_strength(self) -> int:
# #         return self._strength
# #
# #     def get_weak(self) -> int:
# #         return self._weak
# #
# #     def get_vulnerable(self) -> int:
# #         return self._vulnerable
# #
# #     def get_name(self) -> str:
# #         return self.__class__.__name__
# #
# #     def reduce_hp(self, amount: int) -> None:
# #         if self._block >= amount:
# #             self._block -= amount
# #         else:
# #             self._hp = self._hp - (amount - self._block)
# #             if self._hp > 0:
# #                 self._hp = self._hp
# #             else:
# #                 self._hp = 0
# #             self._block = 0
# #
# #     def is_defeated(self) -> bool:
# #         if self._hp <= 0:
# #             return True
# #         else:
# #             return False
# #
# #     def add_block(self, amount: int) -> None:
# #         self._block += amount
# #
# #     def add_strength(self, amount: int) -> None:
# #         self._strength += amount
# #
# #     def add_weak(self, amount: int) -> None:
# #         self._weak += amount
# #
# #     def add_vulnerable(self, amount: int) -> None:
# #         self._vulnerable += amount
# #
# #     def new_turn(self) -> None:
# #         self._block = 0
# #         if self._weak > 0:
# #             self._weak -= 1
# #         else:
# #             self._weak = 0
# #         if self._vulnerable > 0:
# #             self._vulnerable -= 1
# #         else:
# #             self._vulnerable = 0
# #
# #     def __str__(self) -> str:
# #         return "{}: {} / {}".format(self.get_name(), self._hp, self._max_hp)
# #
# #     def __repr__(self) -> str:
# #         return "{}({})".format(self.get_name(), self.get_max_hp())
# #
# #
# # entity = Entity(20)
# # print(entity.get_name())
# # print(entity.get_hp(), entity.get_max_hp(), entity.get_block())
# # print(entity.get_strength(), entity.get_weak(), entity.get_vulnerable())
# # print(entity.reduce_hp(2))
# # print(entity.get_hp())
# # print(entity.add_block(5))
# # print(entity.get_block())
# # print(entity.reduce_hp(10))
# # print(entity.get_hp())
# # print(entity.get_block())
# # print(entity.is_defeated())
# # print(entity.add_strength(2))
# # print(entity.add_weak(3))
# # print(entity.add_vulnerable(4))
# # print(entity.get_strength(), entity.get_weak(), entity.get_vulnerable())
# # print(entity.add_block(5))
# # print(entity.get_block())
# # print(entity.new_turn())
# # print(entity.get_strength(), entity.get_weak(), entity.get_vulnerable())
# # print(entity.get_block())
# # print(entity.get_hp())
# # print(entity.reduce_hp(15))
# # print(entity.get_hp())
# # print(entity.is_defeated())
# #
# #


# class Player(Entity):
#     def __init__(self, max_hp: int, cards: list[Card] | None = None) -> None:
#         super().__init__(max_hp)
#         self._cards = cards
#         self._energy = 3
#         self._deck = []
#         if self._deck is not None:
#             self._deck = cards
#         else:
#             self._deck = []
#         self._hand = []
#         self._discard_pile = []
#
#     def get_energy(self) -> int:
#         return self._energy
#
#     def get_hand(self) -> list[Card]:
#         return self._hand
#
#     def get_deck(self) -> list[Card]:
#         return self._deck
#
#     def get_discarded(self) -> list[Card]:
#         return self._discard_pile
#
#     def start_new_encounter(self) -> None:
#         if len(self.get_hand()) == 0:
#             self._deck.extend(self._discard_pile)
#             self._discard_pile.clear()
#
#     def end_turn(self) -> None:
#         self._discard_pile.extend(self._hand)
#         self._hand.clear()
#
#     def new_turn(self) -> None:
#         super().new_turn()
#         self._energy = 3
#         draw_cards(self._deck, self._hand, self._discard_pile)
#
#     def play_card(self, card_name: str) -> Card | None:
#         for i in self._hand:
#             if i.get_name() == card_name:
#                 if self._energy >= i.get_energy_cost():
#                     self._hand.remove(i)
#                     self._discard_pile.append(i)
#                     self._energy -= i.get_energy_cost()
#                     return i
#                 else:
#                     return None
#         return None


# player = Player(50, [Strike(), Strike(), Strike(), Defend(), Defend(),
# Defend(), Bash()])
# print(player.get_name())
# print(player.get_hp())
# print(player.get_energy())
# print(print(player.get_hand(), player.get_discarded()))
# print(player.get_deck())
# print(player.new_turn())
# print(player.get_hand())
# print(player.get_deck())
# print(player.get_discarded())
# print(player.play_card('Bash'))
# print(player.get_hand())
# print(player.get_deck())
# print(player.get_discarded())
# print(player.end_turn())
# print(player.get_hand())
# print(player.get_deck())
# print(player.get_discarded())
# print(player.reduce_hp(10))
# print(str(player))


# class IronClad(Player):
#     def __init__(self):
#         super().__init__(80)
#         self._deck = [Strike()] * 5 + ([Defend()] * 4) + [Bash()]
#
#
# iron_clad = IronClad()
# print(iron_clad.get_name())
# print(str(iron_clad))
# print(iron_clad.get_hp())
# print(iron_clad.get_hand())
# print(iron_clad.get_deck())
# print(iron_clad.new_turn())
# print(iron_clad.get_hand())
# print(iron_clad.get_deck())

# class Monster(Entity):
#     monster_id = 0
#
#     def __init__(self, max_hp: int) -> None:
#         super().__init__(max_hp)
#         self._id = Monster.monster_id
#         Monster.monster_id += 1
#
#     def get_id(self) -> int:
#         return self._id
#
# def action(self) -> dict[str, int]:
#     raise NotImplementedError
#
#
# monster = Monster(20)
# print(monster.get_id())
# another_monster = Monster(3)
# print(another_monster.get_id())
# print(monster.get_id())
# # print(monster.action())
# print(monster.get_name())
# monster.reduce_hp(10)
# print(str(monster))

# class Louse(Monster):
#     def __init__(self, max_hp: int) -> None:
#         super().__init__(max_hp)
#         self._damage = random_louse_amount()
#
#     def action(self) -> dict[str, int]:
#         return {"damage": self._damage}
#
#
# louse = Louse(20)
# print(str(louse))
# print(louse.get_id())
# print(louse.action())
# print(louse.action())
# print(louse.action())
# another_louse = Louse(30)
# print(another_louse.action())
# print(another_louse.get_id())


# class Cultist(Monster):
#     def __init__(self, max_hp: int) -> None:
#         super().__init__(max_hp)
#         self._num_calls = 0
#         self._weak_amount = 0
#
#     def action(self) -> dict[str, int]:
#         if self._num_calls == 0:
#             self._num_calls += 1
#             return {"damage": 0, "weak": 0}
#         else:
#             damage_amount = 6 + self._num_calls
#             self._num_calls += 1
#             self._weak_amount = 1 - self._weak_amount
#             return {"damage": damage_amount, "weak": self._weak_amount}
#
#
# cultist = Cultist(20)
# print(cultist.action())
# print(cultist.action())
# print(cultist.action())
# print(cultist.action())
# print(cultist.action())
# another_cultist = Cultist(30)
# print(another_cultist.action())


# class JawWorm(Monster):
#     def __init__(self, max_hp: int) -> None:
#         super().__init__(max_hp)
#         self._damage_amount = 0
#         self._block = 0
#
#     def action(self) -> dict[str, int]:
#         damage = self._max_hp - self._hp
#         block = round(damage / 2)
#         self._block += block
#         damage_amount = damage // 2
#         self._damage_amount += damage_amount
#         return {'damage': damage_amount}
#
#     def get_block(self) -> int:
#         return self._block
#
#
# jaw_worm = JawWorm(20)
# print(jaw_worm.get_block())
# print(jaw_worm.action())
# print(jaw_worm.get_block())
# print(jaw_worm.reduce_hp(11))
# print(jaw_worm.action())
# print(jaw_worm.get_block())
# print(jaw_worm.reduce_hp(5))
# print(jaw_worm.get_hp())
# print(jaw_worm.get_block())
# print(jaw_worm.reduce_hp(5))
# print(jaw_worm.get_hp())
# print(jaw_worm.action())
# print(jaw_worm.get_block())
# monsters = [1]
# if monsters:
#     print(True)
# else:
#     print(False)
#
# monster_dic = {
#     "Louse": Louse,
#     "Cultist": Cultist,
#     "JawWorm": JawWorm
# }
#
# monster_list = []
#
# for iName in monsters:
#     name = iName[0]
#     hp = iName[1]
#     monster = monster_dic[name]
#     monster_list.append(monster(hp))
# print(monster_list)

#
# name = []
# hp = []
# m_hp = 0
# monsters = [Monster(name) for name, max_hp in monsters]
# print(monsters)
# for i in monsters:
#     name.append(i[0])
#     hp.append(i[1])
# for j in hp:
#     m_hp = j
#
# str1 = ''.join(name)
# m_name = str1.capitalize()
# print(m_name)
#
# m_name = Monster(m_hp)
# print(m_name)


# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# player = encounter.get_player()
# player.get_hand() != []

# def player_apply_card(self, card_name: str, target_id: int | None = None) \
#         -> bool:
#     """This method attempts to apply the first card with the
#         given name from the player’s hand
#
#         Return:
#             boolean
#     """
#
#     if not self._player_turn:
#         return False
#
#     if target_id is None:
#         for card in self._player.get_hand():
#             if card.get_name() == card_name:
#                 if card.requires_target():
#                     return False
#
#     if target_id is not None:
#         for monster in self.monster_list:
#             if monster.get_id() != target_id:
#                 return False
#
#     block = 0
#     strength = 0
#     for card in self._player.get_hand():
#         block = card.get_block()
#         strength = (card.get_status_modifiers()).get("strength")
#         if strength is None:
#             strength = 0
#     self._player.add_block(block)
#     self._player.add_strength(strength)
#
#     if target_id is not None:
#         weak = 0
#         vulnerable = 0
#         for card in self._player.get_hand():
#             if card.get_name() == card_name:
#                 weak = (card.get_status_modifiers()).get("weak")
#                 vulnerable = (card.get_status_modifiers()).get("vulnerable")
#                 if weak is None:
#                     weak = 0
#                 if vulnerable is None:
#                     vulnerable = 0
#         for monster in self.monster_list:
#             if monster.get_id() == target_id:
#                 monster.add_weak(weak)
#                 monster.add_vulnerable(vulnerable)
#
#         base_damage = 0
#         for card in self._player.get_hand():
#             if card.get_name() == card_name:
#                 base_damage = card.get_damage_amount()
#         damage = base_damage + self._player.get_strength()
#         for monster in self.monster_list:
#             if monster.get_vulnerable() > 0:
#                 damage = int(damage * 1.5)
#             if monster.get_weak() > 0:
#                 damage = int(damage * 0.75)
#             monster.reduce_hp(damage)
#             if monster.is_defeated():
#                 self.monster_list.remove(monster)
#
#     return True

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
# random.seed("end_player_ture")
# print(encounter.start_new_turn())
# monster_id = encounter.get_monsters()[0].get_id()
# print(monster_id)
# encounter.player_apply_card('Neutralize', monster_id)
# encounter.end_player_turn()
# i = encounter.get_monsters()[0].get_weak()
# print(i)
# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
# random.seed("player_apply_card")
# print(encounter.end_player_turn())
# print(encounter.start_new_turn())
# i = encounter.player_apply_card('Neutralize')
# print(i)

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Add block to the player
# encounter.player_apply_card('Defend')
# encounter.player_apply_card('Defend')
#
# # Check that the block applied
# i = encounter.get_player().get_block()
# print(i)

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Apply a card with a specific target
# monster_id = encounter.get_monsters()[0].get_id()
# encounter.player_apply_card('Strike', monster_id)
#
# # Check that the block applied
# monster = encounter.get_monsters()[0]
# i = monster.get_hp()
# print(i)
#
# # Kill the monster
# encounter.player_apply_card('Strike', monster_id)
#
# # Check that the monster died
# j = encounter.get_monsters()w
# print(j)

# def enemy_turn(self) -> None:
#     """This method attempts to allow all remaining monsters
#         in the encounter to take an action.
#
#         Return:
#             None
#     """
#
#     if self._player_turn:
#         return
#     extra_damage = 0
#     for monster in self.monster_list:
#         actions = monster.action()
#         if 'weak' in actions:
#             self._player.add_weak(actions["weak"])
#         if 'vulnerable' in actions:
#             self._player.add_vulnerable(actions["vulnerable"])
#         if 'strength' in actions:
#             self._player.add_strength(actions["strength"])
#         if "strength" in actions:
#             extra_damage = actions["strength"]
#         base_damage = actions["damage"] + extra_damage
#         if self._player.get_vulnerable() > 0:
#             base_damage = int(base_damage * 1.5)
#         if self._player.get_weak() > 0:
#             base_damage = int(base_damage * 0.75)
#         self._player.reduce_hp(base_damage)
#
#     self._player.new_turn()


# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Ensure it is the monster's turn
# encounter.end_player_turn()
#
# # Attempt the turn
# encounter.enemy_turn()
#
# # Check the player took damage
# i = encounter.get_player().get_hp()
# print(i)
#
# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Attempt the turn while still in the player turn
# encounter.enemy_turn()
#
# # Check the player took no damage
# j = encounter.get_player().get_hp()
# print(j)

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# monsters = [('Cultist', 10), ('Cultist', 10)]
# encounter = Encounter(player, monsters)
#
# # Set up the cultist turns
# encounter.end_player_turn()
# encounter.enemy_turn()
# encounter.end_player_turn()
#
# # Attempt the turn
# encounter.enemy_turn()
#
# # Check the player is weak
# i = encounter.get_player().get_weak()
# print(i)

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Store a copy of cards in the original hand
# original_hand = encounter.get_player().get_hand().copy()
# print(original_hand)
#
# # Take the enemy's turn
# encounter.end_player_turn()
# encounter.enemy_turn()
#
# # Check that a new turn has occured by checking the players hand
# new_hand = encounter.get_player().get_hand()
# print(new_hand)
# # new_hand != original_hand

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Replace the default louse action
# strength_action = lambda self: {'damage': 3, 'strength': 2}
# original_action = Louse.action
# Louse.action = strength_action
#
# # Wrap the entire test in a try/finally to ensure we fix the Louse
# try:
#     # Create an encounter using the modified monster
#     monsters = [('Louse', 10)]
#     encounter = Encounter(player, monsters)
#
#     # Check the monster does increased damage
#     encounter.end_player_turn()
#     encounter.enemy_turn()
#     i = encounter.get_player().get_hp()
#     print(i)
# finally:
#     # Restore the louse's action
#     Louse.action = original_action
# def player_apply_card(self, card_name: str, target_id: int | None = None)\
#         -> bool:
#     """This method attempts to apply the first card with the
#         given name from the player’s hand
#
#         Return:
#             boolean
#     """
#
#     if not self._player_turn:
#         return False
#
#     if target_id is None:
#         for card in self._player.get_hand():
#             if card.get_name() == card_name:
#                 if card.requires_target():
#                     return False
#
#     if target_id is not None:
#         for monster in self.monster_list:
#             if monster.get_id() != target_id:
#                 return False
#
#     block = 0
#     strength = 0
#     for card in self._player.get_hand():
#         block = card.get_block()
#         strength = (card.get_status_modifiers()).get("strength")
#         if strength is None:
#             strength = 0
#     self._player.add_block(block)
#     self._player.add_strength(strength)
#
#     if target_id is not None:
#         weak = 0
#         vulnerable = 0
#         for card in self._player.get_hand():
#             if card.get_name() == card_name:
#                 weak = (card.get_status_modifiers()).get("weak")
#                 vulnerable = (card.get_status_modifiers()).get("vulnerable")
#                 if weak is None:
#                     weak = 0
#                 if vulnerable is None:
#                     vulnerable = 0
#         for monster in self.monster_list:
#             if monster.get_id() == target_id:
#                 monster.add_weak(weak)
#                 monster.add_vulnerable(vulnerable)
#
#         base_damage = 0
#         for card in self._player.get_hand():
#             if card.get_name() == card_name:
#                 base_damage = card.get_damage_amount()
#         damage = base_damage + self._player.get_strength()
#         for monster in self.monster_list:
#             if monster.get_vulnerable() > 0:
#                 damage = int(damage * 1.5)
#             if monster.get_weak() > 0:
#                 damage = int(damage * 0.75)
#             monster.reduce_hp(damage)
#             if monster.is_defeated():
#                 self.monster_list.remove(monster)
#
#     return True
# def player_apply_card(self, card_name: str, target_id: int | None = None)\
#         -> bool:
#     """This method attempts to apply the first card with the
#         given name from the player’s hand
#
#         Return:
#             boolean
#     """
#
#     if not self._player_turn:
#         return False
#
#     card_to_apply = None
#     for card in self._player.get_hand():
#         if card.get_name() == card_name:
#             card_to_apply = card
#             if card.requires_target() and target_id is None:
#                 continue
#             break
#
#     if card_to_apply is None:
#         return False
#
#     block = 0
#     strength = 0
#     for card in self._player.get_hand():
#         block += card.get_block()
#         strength += (card.get_status_modifiers()).get("strength", 0)
#
#     self._player.add_block(block)
#     self._player.add_strength(strength)
#
#     if target_id is not None:
#         weak = 0
#         vulnerable = 0
#         for card in self._player.get_hand():
#             if card.get_name() == card_name:
#                 weak = (card.get_status_modifiers()).get("weak", 0)
#                 vulnerable = (card.get_status_modifiers()).get("vulnerable", 0)
#
#         for monster in self.monster_list:
#             if monster.get_id() == target_id:
#                 monster.add_weak(weak)
#                 monster.add_vulnerable(vulnerable)
#
#                 base_damage = card_to_apply.get_damage_amount()
#                 damage = base_damage + self._player.get_strength()
#
#                 if monster.get_vulnerable() > 0:
#                     damage = int(damage * 1.5)
#                 if monster.get_weak() > 0:
#                     damage = int(damage * 0.75)
#
#                 damage = int(damage)
#                 monster.reduce_hp(damage)
#
#                 if monster.is_defeated():
#                     self.monster_list.remove(monster)
#                 break
#
#     return True

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Check card not in hand
# a = encounter.player_apply_card('Neutralize') #False
# print(a)
#
# # Check lack of energy
# monster_id = encounter.get_monsters()[0].get_id()
# print(monster_id)
# encounter.player_apply_card('Defend')
# encounter.player_apply_card('Defend')
# encounter.player_apply_card('Strike', monster_id)
# b = encounter.player_apply_card('Strike', monster_id) #False
# print(b)
#
# # Check invalid card name
# c = encounter.player_apply_card('SomeCard') #False
# print(c)

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
# print(encounter)
# # Specify a seed for testing
# random.seed("start_new_turn")
#
# encounter.start_new_turn()
# monster_id = encounter.get_monsters()[0].get_id()
# print(monster_id)
# i = encounter.player_apply_card('Strike', monster_id) #== True
# print(i)


# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Add block to the player
# encounter.player_apply_card('Defend')
# encounter.player_apply_card('Defend')
#
# # Check that the block applied
# i = encounter.get_player().get_block() #== 10
# print(i)

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Apply a card with a specific target
# monster_id = encounter.get_monsters()[0].get_id()
# encounter.player_apply_card('Strike', monster_id)
#
# # Check that the block applied
# monster = encounter.get_monsters()[0]
# i = monster.get_hp() #== 4
# print(i)
#
# # Kill the monster
# encounter.player_apply_card('Strike', monster_id)
#
# # Check that the monster died
# j = encounter.get_monsters() #== []
# print(j)

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Check that applying the card returns the right result
# i = encounter.player_apply_card('Defend') #== True
# print(i)

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("end_player_turn")
#
# # Get new cards and play a card against a monster
# encounter.start_new_turn()
# monster_id = encounter.get_monsters()[0].get_id()
# encounter.player_apply_card('Neutralize', monster_id)
#
# # Check that the monster has no weak
# encounter.end_player_turn()
# i = encounter.get_monsters()[0].get_weak() #== 0
# print(i)


# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Add block to the player
# # print(encounter.player.get_hand())
# encounter.player_apply_card('Defend')
# # print(encounter.player.get_hand())
# encounter.player_apply_card('Defend')
#
# # Check that the block applied
# i = encounter.get_player().get_block() #== 10
# print(i)


# if not self._player_turn:
#     return False
#
# for card in self._player.hand:
#     if card.requires_target():
#         if target_id is None:
#             return False
#
# if target_id is not None:
#     for monster in self.monster_list:
#         if monster.get_id() != target_id:
#             return False
# card = self._player.play_card(card_name)
# if card is None:
#     return False
# if card in self._player.hand:
#     self._player.hand.remove(card)
#     block = card.get_block()
#     self._player.add_block(block)
# strength = (card.get_status_modifiers()).get("strength")
# if strength is None:
#     strength = 0
# else:
#     self._player.add_strength(strength)
#
# base_damage = card.get_damage_amount()
# damage = 0
# if target_id is not None:
#     vulnerable = (card.get_status_modifiers()).get("vulnerable")
#     weak = (card.get_status_modifiers()).get("weak")
#     if weak is None:
#         weak = 0
#     if vulnerable is None:
#         vulnerable = 0
#     for monster in self.monster_list:
#         if monster.get_id() == target_id:
#             monster.add_weak(weak)
#             monster.add_vulnerable(vulnerable)
#             if monster.get_vulnerable() > 0:
#                 damage = int(base_damage * 1.5)
#             if monster.get_weak() > 0:
#                 damage = int(base_damage * 0.75)
#             monster.reduce_hp(damage)
#             if monster.is_defeated():
#                 self.monster_list.remove(monster)
# return True
#
# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Check card not in hand
# i = encounter.player_apply_card('Neutralize') #== False
# # Check lack of energy
# print(encounter.player.get_hand())
# monster_id = encounter.get_monsters()[0].get_id()
# encounter.player_apply_card('Defend')
# print(encounter.player.energy)
# print(encounter.player.get_hand())
#
# encounter.player_apply_card('Defend')
# print(encounter.player.energy)
# print(encounter.player.get_hand())
#
# encounter.player_apply_card('Strike', monster_id)
# print(encounter.player.energy)
# print(encounter.player.get_hand())
#
# j = encounter.player_apply_card('Strike', monster_id) #== False
# print(j)
# # Check invalid card name
# p = encounter.player_apply_card('SomeCard') #== False


# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Check that applying the card returns the right result
# i = encounter.player_apply_card('Defend') #== True
# print(i)

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Replace the default louse action
# strength_action = lambda self: {'damage': 3, 'strength': 2}
# original_action = Louse.action
# Louse.action = strength_action
#
# # Wrap the entire test in a try/finally to ensure we fix the Louse
# try:
#     # Create an encounter using the modified monster
#     monsters = [('Louse', 10)]
#     encounter = Encounter(player, monsters)
#
#     # Check the monster does increased damage
#     encounter.end_player_turn()
#     encounter.enemy_turn()
#     i = encounter.get_player().get_hp() #== 65
#     print(i)
# finally:
#     # Restore the louse's action
#     Louse.action = original_action
# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Attempt the turn while still in the player turn
# encounter.enemy_turn()
#
# # Check the player took no damage
# i = encounter.get_player().get_hp() #== 70
# print(i)

# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Check that applying the card returns the right result
# i = encounter.player_apply_card('Defend') #== True
# print(i)


# if not self.player_turn:
#     return False
#
# hand_cards = self.player.get_hand()
# for card in hand_cards:
#     if card.get_name() == card_name:
#         if card.requires_target():
#             if target_id is None:
#                 return False
#
# if not self.is_active():
#     return False
#
# monster_exist = False
# for monster in self.monster_list:
#     if monster.get_id() == target_id:
#         monster_exist = True
#         break
# if monster_exist == False:
#     return False
#
# new_card = self.player.play_card(card_name)
# if new_card is None:
#     return False
#
# self.player.add_block(new_card.get_block())
# strength = (new_card.get_status_modifiers()).get("strength")
# if strength is None:
#     strength = 0
# else:
#     self.player.add_strength(strength)
#
# if target_id is not None:
#     weak = (new_card.get_status_modifiers()).get("weak")
#     if weak is None:
#         weak = 0
#     vulnerable = (new_card.get_status_modifiers()).get("vulnerable")
#     if vulnerable is None:
#         vulnerable = 0
#     for monster in self.monster_list:
#         if monster.get_id() == target_id:
#             monster.add_weak(weak)
#             monster.add_vulnerable(vulnerable)
#             base_damage = new_card.get_damage_amount()
#             extra_damage = self.player.get_strength()
#             damage = base_damage + extra_damage
#             if monster.get_vulnerable() > 0:
#                 damage = int(damage * 1.5)
#             if monster.get_weak() > 0:
#                 damage = int(damage * 0.75)
#             monster.reduce_hp(damage)
#             if monster.is_defeated():
#                 self.monster_list.remove(monster)
# return True

#
# player = Silent()
# monsters = [('Louse', 10)]
# encounter = Encounter(player, monsters)
#
# # Specify a seed for testing
# random.seed("player_apply_card")
#
# # Ensure cards are reset
# encounter.end_player_turn()
# encounter.start_new_turn()
#
# # Apply a card with a specific target
# monster_id = encounter.get_monsters()[0].get_id()
# encounter.player_apply_card('Strike', monster_id)
#
# # Check that the block applied
# monster = encounter.get_monsters()[0]
# i = monster.get_hp() #== 4
# print(i)
# # Kill the monster
# encounter.player_apply_card('Strike', monster_id)
#
# # Check that the monster died
# j = encounter.get_monsters() #== []
# print(j)

# game_details = [[('Louse', 25)], [('Louse', 30)]]
# monster_dic = {
#     "Louse": Louse,
#     "Cultist": Cultist,
#     "JawWorm": JawWorm
# }
# player_dic = {
#     "ironclad": IronClad,
#     "silent": Silent,
#     "watcher": Watcher
# }
# card_dic = {
#     "Strike": Strike,
#     "Defend": Defend,
#     "Bash": Bash,
#     "Neutralize": Neutralize,
#     "Survivor": Survivor,
#     "Eruption": Eruption,
#     "Vigilance": Vigilance
# }
# player = 'ironclad'
# player_class = player_dic[player]()
# for encounters in game_details:
#     encounter = Encounter(player_class, encounters)
#     for monsters in encounters:
#         name = monsters[0]
#         hp = monsters[1]
#         monster = monster_dic[name]
#         print("New encounter!")
#         display_encounter(encounter)
#         while encounter.is_active() and player_class.is_defeated() == False:
#             command = input("Enter a move: ")
#             if command == "inspect deck":
#                 print("\n{}\n".format(player_class.get_deck()))
#             elif command == "inspect discard":
#                 print("\n{}\n".format(player_class.get_discarded()))
#             elif "describe" in command:
#                 command = command.split(" ")
#                 name = command[1]
#                 print("\n{}\n".format(card_dic[name].get_description(Card)))
#             elif "play" in command:
#                 command = command.split(" ")
#                 if len(command) == 2:
#                     card = command[1]
#                     target = None
#                     if not encounter.player_apply_card(card, target):
#                         print(CARD_FAILURE_MESSAGE)
#                     else:
#                         display_encounter(encounter)
#                 elif len(command) == 3:
#                     card = command[1]
#                     target = int(command[2])
#                     if not encounter.player_apply_card(card, target):
#                         print(CARD_FAILURE_MESSAGE)
#                     else:
#                         display_encounter(encounter)
#             elif command == "end turn":
#                 encounter.end_player_turn()
#                 encounter.enemy_turn()
#                 if player_class.is_defeated():
#                     print(GAME_LOSE_MESSAGE)
#                     break
#                 else:
#                     display_encounter(encounter)
#         encounter.end_player_turn()
# if not player_class.is_defeated():
#     print(GAME_WIN_MESSAGE)
# else:
#     print(GAME_LOSE_MESSAGE)
# move = "describe Strike"
# card_name = move.split(' ')[1]
# print(card_name)

# def main():
# card_dic = {
#     "Strike": Strike,
#     "Defend": Defend,
#     "Bash": Bash,
#     "Neutralize": Neutralize,
#     "Survivor": Survivor,
#     "Eruption": Eruption,
#     "Vigilance": Vigilance
# }
# player_dic = {
#     "ironclad": IronClad,
#     "silent": Silent,
#     "watcher": Watcher
# }
#
# player = input("Enter a player type: ")
# player_type = player_dic[player]()
#
# file = input("Enter a game file: ")
# file_details = read_game_file(file)
#
# for encounters in file_details:
#     print("New encounter!\n")
#     encounter = Encounter(player_type, encounters)
#     display_encounter(encounter)
#     while encounter.is_active():
#         command = input("Enter a move: ")
#         if command == "end turn":
#             encounter.end_player_turn()
#             encounter.enemy_turn()
#             if not player_type.is_defeated():
#                 display_encounter(encounter)
#             else:
#                 return print(GAME_LOSE_MESSAGE)
#         elif "inspect" in command:
#             command = command.split(" ")[1]
#             if command == "deck":
#                 print("\n{}\n".format(player_type.get_deck()))
#             elif command == "discard":
#                 print("\n{}\n".format(player_type.get_discarded()))
#         elif "describe" in command:
#             name = command.split(" ")[1]
#             print("\n{}\n".format(card_dic[name].get_description(Card)))
#         elif "play" in command:
#             move = command.split(" ")
#             if len(move) == 2:
#                 card = move[1]
#                 target_id = None
#                 if not encounter.player_apply_card(card, target_id):
#                     display_encounter(encounter)
#             elif len(move) == 3:
#                 card = move[1]
#                 target_id = move[2]
#                 if not encounter.player_apply_card(card, target_id):
#                     display_encounter(encounter)
#     if not encounter.is_active():
#         print(ENCOUNTER_WIN_MESSAGE)
# if not player_type.is_defeated():
#     print(GAME_WIN_MESSAGE)
# if __name__ == "__main__":
#     main()
class Cultist(Monster):
    def __init__(self, max_hp: int) -> None:
        super().__init__(max_hp)
        self.name = "Cultist"
        self.damage_amount = 0
        self.weak_amount = 0
        self.num_calls = 0
    def action(self) -> dict[str, int]:
        if self.num_calls == 0:
            dic = {"damage": 0}
        else:
            dic = {"damage": 6 + self.num_calls}
        dic["weak"] = self.num_calls % 2
        self.num_calls += 1
        return dic


player = Silent()
monsters = [('Louse', 10)]
encounter = Encounter(player, monsters)

monsters = [('Cultist', 10), ('Cultist', 10)]
encounter = Encounter(player, monsters)

# Set up the cultist turns
encounter.end_player_turn()
encounter.enemy_turn()
encounter.end_player_turn()

# Attempt the turn
encounter.enemy_turn()

# Check the player is weak
i = encounter.get_player().get_weak() #== 1
print(i)
