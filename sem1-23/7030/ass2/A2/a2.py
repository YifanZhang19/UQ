from a2_support import *


# Implement your classes here
class Card:
    """Cards are used by the player during
        encounters to attack monsters, defend, or apply status modifiers.
    """

    def get_damage_amount(self) -> int:
        """Return the amount of damage this card does to its target

        Return:
            the amount of damage
        """

        return 0

    def get_block(self) -> int:
        """Return the amount of block this card adds to its user.

        Return:
            the amount of block
        """

        return 0

    def get_energy_cost(self) -> int:
        """Returns the amount of energy this card costs to play.

        Return:
            the amount of energy cost
        """

        return 1

    def get_status_modifiers(self) -> dict[str, int]:
        """Returns a dictionary describing each status modifiers
            applied when this card is played.

        Return:
            an empty dictionary in the abstract Card class
        """

        return {}

    def get_name(self) -> str:
        """Returns the name of the card.

        Return:
            the name of card
        """

        return self.__class__.__name__

    def get_description(self) -> str:
        """Returns a description of the card.

        Return:
            the description of card
        """

        return "A card."

    def requires_target(self) -> bool:
        """Returns True if playing this card requires a target,
            and False if it does not.

        Return:
            the need target or not
        """

        return True

    def __str__(self) -> str:
        """Returns the string representation for the card.

        Return:
            the representation for the card in format
        """

        return "{}: {}".format(self.get_name(), self.get_description())

    def __repr__(self) -> str:
        """Returns the text that would be required to
            create a new instance of this class identical to self.

        Return:
            the text can create a new instance of this class identical to self.
        """

        return "Card()"


class Strike(Card):
    """Strike is a type of Card that deals 6 damage to its target.
        It costs 1 energy point to play.

        This class inherits form Card.
    """

    def get_damage_amount(self):
        """Return the amount of damage this card does to its target

        Return:
            the amount of damage
        """

        return 6

    def get_description(self):
        """Returns a description of the card.

        Return:
            the description of card
        """

        return "Deal 6 damage."

    def __repr__(self):
        """Returns the text that would be required to
            create a new instance of this class identical to self.

        Return:
            the text can create a new instance of this class identical to self.
        """

        return "Strike()"


class Defend(Card):
    """Defend is a type of Card that adds 5 block to its user.
        Defend does not require a target. It costs 1 energy point to play.

        This class inherits form Card.
    """

    def get_block(self):
        """Return the amount of block this card adds to its user.

        Return:
            the amount of block
        """

        return 5

    def get_description(self):
        """Returns a description of the card.

        Return:
            the description of card
        """

        return "Gain 5 block."

    def requires_target(self):
        """Returns True if playing this card requires a target,
            and False if it does not.

        Return:
            the need target or not
        """

        return False

    def __repr__(self):
        """Returns the text that would be required to
            create a new instance of this class identical to self.

        Return:
            the text can create a new instance of this class identical to self.
        """

        return "Defend()"


class Bash(Card):
    """Bash is a type of Card that adds 5 block to its user
        and causes 7 damage to its target. It costs 2 energy points to play.

        This class inherits form Card.
    """

    def get_damage_amount(self):
        """Return the amount of damage this card does to its target

        Return:
            the amount of damage
        """

        return 7

    def get_block(self):
        """Return the amount of block this card adds to its user.

        Return:
            the amount of block
        """

        return 5

    def get_energy_cost(self):
        """Returns the amount of energy this card costs to play.

        Return:
            the amount of energy cost
        """

        return 2

    def get_description(self):
        """Returns a description of the card.

        Return:
            the description of card
        """

        return "Deal 7 damage. Gain 5 block."

    def __repr__(self):
        """Returns the text that would be required to
            create a new instance of this class identical to self.

        Return:
            the text can create a new instance of this class identical to self.
        """

        return "Bash()"


class Neutralize(Card):
    """Neutralize is a type of card that deals 3 damage to its target.
        It also applies status modifiers to its target; namely,
        it applies 1 weak and 2 vulnerable.
        Neutralize does not cost any energy points to play.

        This class inherits form Card.
    """

    def get_damage_amount(self):
        """Return the amount of damage this card does to its target

        Return:
            the amount of damage
        """

        return 3

    def get_energy_cost(self) -> int:
        """Returns the amount of energy this card costs to play.

        Return:
            the amount of energy cost
        """

        return 0

    def get_status_modifiers(self):
        """Returns a dictionary describing each status modifiers
            applied when this card is played.

        Return:
            the dictionary describing each status modifiers applied
        """

        return {"weak": 1, "vulnerable": 2}

    def get_description(self):
        """Returns a description of the card.

        Return:
            the description of card
        """

        return "Deal 3 damage. Apply 1 weak. Apply 2 vulnerable."

    def __repr__(self):
        """Returns the text that would be required to
            create a new instance of this class identical to self.

        Return:
            the text can create a new instance of this class identical to self.
        """

        return "Neutralize()"


class Survivor(Card):
    """Survivor is a type of card that adds 8 block and
        applies 1 strength to its user. Survivor does not require a target.

        This class inherits form Card.
    """

    def get_block(self):
        """Return the amount of block this card adds to its user.

        Return:
            the amount of block
        """

        return 8

    def get_status_modifiers(self):
        """Returns a dictionary describing each status modifiers
            applied when this card is played.

        Return:
            the dictionary describing each status modifiers applied
        """

        return {"strength": 1}

    def get_description(self):
        """Returns a description of the card.

        Return:
            the description of card
        """

        return "Gain 8 block and 1 strength."

    def requires_target(self):
        """Returns True if playing this card requires a target,
            and False if it does not.

        Return:
            the need target or not
        """

        return False

    def __repr__(self):
        """Returns the text that would be required to
            create a new instance of this class identical to self.

        Return:
            the text can create a new instance of this class identical to self.
        """

        return "Survivor()"


class Eruption(Card):
    """Eruption is a type of card which costs 2 energy points to play,
        and deals 9 damage to its target.

        This class inherits form Card.
    """

    def get_damage_amount(self):
        """Return the amount of damage this card does to its target

        Return:
            the amount of damage
        """

        return 9

    def get_energy_cost(self):
        """Returns the amount of energy this card costs to play.

        Return:
            the amount of energy cost
        """

        return 2

    def get_description(self):
        """Returns a description of the card.

        Return:
            the description of card
        """

        return "Deal 9 damage."

    def __repr__(self):
        """Returns the text that would be required to
            create a new instance of this class identical to self.

        Return:
            the text can create a new instance of this class identical to self.
        """

        return "Eruption()"


class Vigilance(Card):
    """Vigilance is a type of card which costs 2 energy points to play and
        adds 8 block and 1 strength to its user. It does not require a target.

        This class inherits form Card.
    """

    def get_block(self):
        """Return the amount of block this card adds to its user.

        Return:
            the amount of block
        """

        return 8

    def get_energy_cost(self):
        """Returns the amount of energy this card costs to play.

        Return:
            the amount of energy cost
        """

        return 2

    def get_status_modifiers(self):
        """Returns a dictionary describing each status modifiers
            applied when this card is played.

        Return:
            the dictionary describing each status modifiers applied
        """

        return {"strength": 1}

    def get_description(self):
        """Returns a description of the card.

        Return:
            the description of card
        """

        return "Gain 8 block and 1 strength."

    def requires_target(self):
        """Returns True if playing this card requires a target,
            and False if it does not.

        Return:
            the need target or not
        """

        return False

    def __repr__(self):
        """Returns the text that would be required to
            create a new instance of this class identical to self.

        Return:
            the text can create a new instance of this class identical to self.
        """

        return "Vigilance()"


class Entity:
    """Abstract base class from which all entities inherit."""

    def __init__(self, max_hp: int) -> None:
        """Sets up a new entity with the given max_hp.
            An entity starts with the maximum amount of HP it can have.
            Block, strength, weak, and vulnerable all start at 0.

            Args:
                max_hp: the maximum hp for entity

            Return:
                None
        """

        self.max_hp = max_hp
        self.hp = max_hp
        self.block = 0
        self.strength = 0
        self.weak = 0
        self.vulnerable = 0

    def get_hp(self) -> int:
        """Returns the current HP for this entity.

            Return:
                current HP
        """

        return self.hp

    def get_max_hp(self) -> int:
        """Returns the maximum possible HP for this entity.

            Return:
                maximum HP
        """

        return self.max_hp

    def get_block(self) -> int:
        """Returns the amount of block for this entity.

            Return:
                amount of block
        """

        return self.block

    def get_strength(self) -> int:
        """Returns the amount of strength for this entity.

            Return:
                amount of strength
        """

        return self.strength

    def get_weak(self) -> int:
        """Returns the number of turns for which this entity is weak.

            Return:
                amount of weak
        """

        return self.weak

    def get_vulnerable(self) -> int:
        """Returns the number of turns for which this entity is vulnerable.

            Return:
                number of turns for which this entity is vulnerable
        """

        return self.vulnerable

    def get_name(self) -> str:
        """Returns the name of the entity.

            Return:
                the name of the entity
        """

        return self.__class__.__name__

    def reduce_hp(self, amount: int) -> None:
        """Attacks the entity with a damage of amount.

            Args:
                amount: the amount of damage

            Return:
                None
        """

        # if block greater than block, just reduce block, or reduce block
        # first then reduce hp
        if self.block >= amount:
            self.block -= amount
        else:
            self.hp = self.hp - (amount - self.block)
            # if hp greater than zero, it means not defeat
            if self.hp > 0:
                self.hp = self.hp
            else:
                self.hp = 0
            self.block = 0

    def is_defeated(self) -> bool:
        """Returns True if the entity is defeated, and False otherwise.
            An entity is defeated if it has no HP remaining.

            Return:
                the boolean to define the status
        """

        if self.hp == 0:
            return True
        else:
            return False

    def add_block(self, amount: int) -> None:
        """Adds the given amount to the amount of block this entity has.

            Args:
                amount: the amount of block

            Return:
                None
        """

        self.block += amount

    def add_strength(self, amount: int) -> None:
        """Adds the given amount to the amount of strength this entity has.

            Args:
                amount: the amount of strength

            Return:
                  None
        """

        self.strength += amount

    def add_weak(self, amount: int) -> None:
        """Adds the given amount to the amount of weak this entity has.

            Args:
                amount: the amount of weak

            Return:
                None
        """

        self.weak += amount

    def add_vulnerable(self, amount: int) -> None:
        """Adds the given amount to the amount of vulnerable this entity has.

            Args:
                amount: the amount of vulnerable

            Return:
                None
        """

        self.vulnerable += amount

    def new_turn(self) -> None:
        """Applies any status changes that occur when a new turn begins.

            Return:
                None
        """

        # for the base Entity class, this involves setting block back to 0
        self.block = 0
        # reducing weak and vulnerable each by 1 if they are greater than 0
        if self.weak > 0:
            self.weak -= 1
        else:
            self.weak = 0
        if self.vulnerable > 0:
            self.vulnerable -= 1
        else:
            self.vulnerable = 0

    def __str__(self) -> str:
        """Returns the string representation for the entity.

            Return:
                the string representation for the entity in the format
        """

        return "{}: {}/{} HP".format(self.get_name(), self.hp, self.max_hp)

    def __repr__(self) -> str:
        """Returns the text that would be required to
            create a new instance of this class identical to self.

            Return:
                text that would be required to
                    create a new instance of this class identical to self
        """

        return "{}({})".format(self.get_name(), self.get_max_hp())


class Player(Entity):
    """A Player is a type of entity that the user controls.

        This class inherits form Entity.
    """

    def __init__(self, max_hp: int, cards: list[Card] | None = None) -> None:
        """In addition to executing the initializer for the Entity superclass,
            this method must initialize the player’s energy which starts at 3,
            as well as three lists of cards (deck, hand, and discard pile).

            Args:
                max_hp: the maximum hp for player
                cards: the list of cards for player

            Return:
                None
        """

        super().__init__(max_hp)
        self.cards = cards
        self.energy = 3
        self.deck = []
        if self.deck is not None:
            self.deck = cards
        else:
            self.deck = []
        self.hand = []
        self.discard_pile = []

    def get_energy(self) -> int:
        """Returns the amount of energy the user has remaining.

            Return:
                the amount of energy
        """

        return self.energy

    def get_hand(self) -> list[Card]:
        """Returns the players current hand.

            Return:
                the list of hand cards
        """

        return self.hand

    def get_deck(self) -> list[Card]:
        """Returns the players current deck.

            Return:
                the list of deck cards
        """

        return self.deck

    def get_discarded(self) -> list[Card]:
        """Returns the players current discard pile.

            Return:
                the list of current discard pile cards
        """

        return self.discard_pile

    def start_new_encounter(self) -> None:
        """This method adds all cards from the player’s discard pile to
            the end of their deck,and sets the discard pile to be an empty list.
            A pre-condition to this method is that
            the player’s hand should be empty when it is called.

            Return:
                None
        """

        self.hand.clear()  # clear the hand cards
        for card in self.discard_pile:
            self.deck.append(card)  # add discard to deck
        self.discard_pile.clear()  # clear discard pile

    def end_turn(self) -> None:
        """This method adds all remaining cards from the player’s hand to
            the end of their discard pile, and sets their hand back to an
            empty list.

            Return:
                None
        """
        
        for card in self.hand:
            self.discard_pile.append(card)
        self.hand = []

    def new_turn(self) -> None:
        """This method sets the player up for a new turn.

            Return:
                None
        """

        super().new_turn()  # invoke Entity new_turn()
        self.energy = 3
        # use draw_cards function to draw cards.
        draw_cards(self.deck, self.hand, self.discard_pile)

    def play_card(self, card_name: str) -> Card | None:
        """Attempts to play a card from the player’s hand.

            Args:
                card_name: the name of which card to play

            Return:
                None
        """

        # use for loop find the card whether in hand
        for card in self.hand:  # card is an instance object of Card
            if card.get_name() == card_name:
                if self.energy >= card.get_energy_cost():
                    self.hand.remove(card)
                    self.discard_pile.append(card)
                    self.energy -= card.get_energy_cost()
                    return card
                else:
                    return None
        return None

    def __repr__(self) -> str:
        """Returns the text that would be required to
            create a new instance of this class identical to self.

            Return:
                text that would be required to
                    create a new instance of this class identical to self
        """

        return "Player({}, {})".format(self.get_max_hp(), self.cards)


class IronClad(Player):
    """IronClad is a type of player that starts with 80 HP.

        This class inherits form Player.
    """

    def __init__(self):
        """IronClad’s deck contains 5 Strike cards, 4 Defend cards,
            and 1 Bash card.
        """

        super().__init__(80)
        self.deck = [Strike()] * 5 + [Defend()] * 4 + [Bash()]

    def __repr__(self):
        """Returns the text that would be required to
            create a new instance of this class identical to self.

            Return:
                text that would be required to
                    create a new instance of this class identical to self
        """

        return "IronClad()"


class Silent(Player):
    """Silent is a type of player that starts with 70 HP.

        This class inherits form Player.
    """

    def __init__(self):
        """ Silent’s deck contains 5 Strike cards, 5 Defend cards,
            1 Neutralize card, and 1 Survivor card.
        """

        super().__init__(70)
        self.deck = [Strike()] * 5 + [Defend()] * 5 + \
                    [Neutralize()] + [Survivor()]

    def __repr__(self):
        """Returns the text that would be required to
            create a new instance of this class identical to self.

            Return:
                text that would be required to
                    create a new instance of this class identical to self
        """

        return "Silent()"


class Watcher(Player):
    """Watcher is a type of player which starts with 72 HP.

        This class inherits form Player.
    """

    def __init__(self):
        """ Watcher’s deck containing 4 Strike cards, 4 Defend cards,
            1 Eruption card, and 1 Vigilance card.
        """

        super().__init__(72)
        self.deck = [Strike()] * 4 + [Defend()] * 4 + \
                    [Eruption()] + [Vigilance()]

    def __repr__(self):
        """Returns the text that would be required to
            create a new instance of this class identical to self.

            Return:
                text that would be required to
                    create a new instance of this class identical to self
        """

        return "Watcher()"


class Monster(Entity):
    """ A Monster is a type of entity that the user battles during encounters.

        Attributes:
            monster id

        This class inherits form Entity.
    """
    monster_id = 0

    def __init__(self, max_hp: int) -> None:
        """Sets up a new monster with the given maximum HP
            and a unique id number.

            Args:
                max_hp: the maximum hp for monster

            Return:
                  None
        """

        super().__init__(max_hp)
        self.id = Monster.monster_id
        Monster.monster_id += 1

    def get_id(self) -> int:
        """Returns the unique id number of this monster.

            Return:
                  monster id
        """

        return self.id

    def action(self) -> dict[str, int]:
        """Performs the current action for this monster,
            and returns a dictionary describing the effects this
            monster’s action should cause to its target.

            Return:
                  a dictionary as action
        """

        raise NotImplementedError


class Louse(Monster):
    """ A type of monster.

        This class inherits form Monster.
    """

    def __init__(self, max_hp: int) -> None:
        """Sets up a louse monster with the given maximum HP
            and damage amount generate by random louse amount function.

            Args:
                max_hp: the maximum hp for louse monster

            Return:
                  None
        """

        super().__init__(max_hp)
        self.damage = random_louse_amount()

    def action(self) -> dict[str, int]:
        """Performs the current action for this monster,
            and returns a dictionary describing the effects this
            monster’s action should cause to its target.

            Return:
                  a dictionary as action
        """

        return {"damage": self.damage}


class Cultist(Monster):
    """ A type of monster.

        This class inherits form Monster.
    """

    def __init__(self, max_hp: int) -> None:
        """Sets up a cultist monster with the given maximum HP, num_calls is the
            number of times the action method has been called on this specific
            Cultist instance and the weak_amount alternates between 0 and 1 each
            time the action method is called on a specific Cultist instance,
            starting at 0 for the first call.

            Args:
                max_hp: the maximum hp for cultist monster

            Return:
                  None
        """

        super().__init__(max_hp)
        self.num_calls = 0
        self.weak_amount = 0

    def action(self) -> dict[str, int]:
        """Performs the current action for this monster,
            and returns a dictionary describing the effects this
            monster’s action should cause to its target.

            Return:
                  a dictionary as action
        """

        if self.num_calls == 0:
            self.num_calls += 1
            return {"damage": 0, "weak": 0}
        else:
            damage_amount = 6 + self.num_calls
            self.num_calls += 1
            self.weak_amount = 1 - self.weak_amount
            return {"damage": damage_amount, "weak": self.weak_amount}


class JawWorm(Monster):
    """ A type of JawWorm monster.

        This class inherits form Monster.
    """

    def __init__(self, max_hp: int) -> None:
        """Sets up a cultist monster with the given maximum HP, damage amount
            and amount of block.

            Args:
                max_hp: the maximum hp for jaw worm monster

            Return:
                  None
        """

        super().__init__(max_hp)
        self.damage_amount = 0
        self.block = 0

    def action(self) -> dict[str, int]:
        """Performs the current action for this monster,
            and returns a dictionary describing the effects this
            monster’s action should cause to its target.

            Return:
                  a dictionary as action
        """

        # calculate the real damage amount
        damage = self.max_hp - self.hp
        # calculate the amount of block
        block = (damage + 1) // 2
        self.block += block
        # calculate the amount of damage
        damage_amount = damage // 2
        self.damage_amount += damage_amount
        return {'damage': damage_amount}

    def get_block(self) -> int:
        """Return the amount of block.

            Return:
                amount of block
        """

        return self.block


class Encounter:
    """Each encounter in the game is represented
        as an instance of the Encounter class.
    """

    def __init__(self, player: Player, monsters: list[tuple[str, int]]) -> None:
        """The initializer for an encounter takes the player instance,as well as
            a list of tuples describing the monsters in the encounter.

            Args:
                player: a player object
                monsters: a list with tuples for monster and monster maximum hp

            Return:
                None
        """

        self.player = player
        self.player.start_new_encounter()
        self.monsters = []
        # create a dictionary for monster objects
        monster_type = {
            "Louse": Louse,
            "Cultist": Cultist,
            "JawWorm": JawWorm
        }
        for m_detail in monsters:
            name = m_detail[0]
            hp = m_detail[1]
            monster = monster_type[name]
            self.monsters.append(monster(hp))
        self.start_new_turn()
        self.player_turn = True

    def start_new_turn(self) -> None:
        """This method sets it to be the player’s turn
            (i.e. the player is permitted to attempt to apply cards) and called
            new_turn on the player instance.

            Return:
                None
        """

        self.player_turn = True
        self.player.new_turn()

    def end_player_turn(self) -> None:
        """This method sets it to not be the player’s turn
            (i.e. the player is not permitted to attempt to apply cards),
            and ensures all cards remaining in the player’s hand move into
            their discard pile.

            Return:
                None
        """

        self.player_turn = False
        self.player.end_turn()
        for monster in self.monsters:
            monster.new_turn()

    def get_player(self) -> Player:
        """Returns the player in this encounter.

            Return:
                  Player
        """

        return self.player

    def get_monsters(self) -> list[Monster]:
        """Returns the monsters remaining in this encounter.

            Return:
                Monster
        """

        return self.monsters

    def is_active(self) -> bool:
        """Returns True if there are monsters remaining in
            this encounter, and False otherwise.

            Return:
                boolean
        """

        if self.get_monsters():
            return True
        else:
            return False

    def player_apply_card(self, card_name: str, target_id: int | None = None) \
            -> bool:
        """This method attempts to apply the first card with the
            given name from the player’s hand

            Args:
                card_name: card name for play
                target_id: the id for monster which in this turn

            Return:
                boolean
        """

        if not self.player_turn:
            return False

        for card in self.player.hand:
            if card.get_name() == card_name:
                if card.requires_target() and target_id is None:
                    return False

        # to check the target id whether have a monster
        if target_id is not None:
            monster_exist = False
            for monster in self.monsters:
                if monster.get_id() == target_id:
                    monster_exist = True
                    break
            if not monster_exist:
                return False
        # create a dictionary for card objects
        card_type = {
            "Strike": Strike,
            "Defend": Defend,
            "Bash": Bash,
            "Neutralize": Neutralize,
            "Survivor": Survivor,
            "Eruption": Eruption,
            "Vigilance": Vigilance
        }
        if self.player.play_card(card_name) is None:
            return False
        else:
            new_card = card_type[card_name]()  # to get the card ready to play
        self.player.add_block(new_card.get_block())
        strength = (new_card.get_status_modifiers()).get("strength")
        if strength is None:
            strength = 0
        else:
            self.player.add_strength(strength)

        if target_id is not None:
            weak = (new_card.get_status_modifiers()).get("weak")
            if weak is None:
                weak = 0
            vulnerable = (new_card.get_status_modifiers()).get("vulnerable")
            if vulnerable is None:
                vulnerable = 0
            # to find the monster which as a target and calculate the final
            # damage before to play.
            for monster in self.monsters:
                if monster.get_id() == target_id:
                    monster.add_weak(weak)
                    monster.add_vulnerable(vulnerable)
                    base_damage = new_card.get_damage_amount()
                    extra_damage = self.player.get_strength()
                    damage = base_damage + extra_damage
                    if monster.get_vulnerable() > 0:
                        damage = int(damage * 1.5)
                    if monster.get_weak() > 0:
                        damage = int(damage * 0.75)
                    monster.reduce_hp(damage)
                    if monster.is_defeated():
                        self.monsters.remove(monster)
        return True

    def enemy_turn(self) -> None:
        """This method attempts to allow all remaining monsters
            in the encounter to take an action.

            Return:
                None
        """

        if self.player_turn:
            return

        # to get the monster status and calculate the damage for player.
        for monster in self.monsters:
            actions = monster.action()
            if 'weak' in actions:
                self.player.add_weak(actions["weak"])
            if 'vulnerable' in actions:
                self.player.add_vulnerable(actions["vulnerable"])
            if 'strength' in actions:
                self.player.add_strength(actions["strength"])
            base_damage = actions["damage"]
            base_damage += self.player.get_strength()
            if self.player.get_vulnerable() > 0:
                base_damage = int(base_damage * 1.5)
            if self.player.get_weak() > 0:
                base_damage = int(base_damage * 0.75)
            self.player.reduce_hp(base_damage)
        self.player.new_turn()


def main():
    """The main function is run when your file is run,
        and manages overall gameplay.
    """
    # Implement this only once you've finished and tested ALL of the required
    # classes.
    card_type = {
        "Strike": Strike,
        "Defend": Defend,
        "Bash": Bash,
        "Neutralize": Neutralize,
        "Survivor": Survivor,
        "Eruption": Eruption,
        "Vigilance": Vigilance
    }
    player_type = {
        "ironclad": IronClad,
        "silent": Silent,
        "watcher": Watcher
    }

    player = input("Enter a player type: ")
    player_class = player_type[player]()
    file = input("Enter a game file: ")
    game_details = read_game_file(file)
    # iterate each encounters
    for encounters in game_details:
        encounter = Encounter(player_class, encounters)
        print("New encounter!\n")
        display_encounter(encounter)
        # while loop to control each encounter
        while encounter.is_active():
            command = input("Enter a move: ")
            # if-elif to judge which command is entered
            if command == "inspect deck":
                print("\n{}\n".format(player_class.get_deck()))
            elif command == "inspect discard":
                print("\n{}\n".format(player_class.get_discarded()))
            elif "describe" in command:
                command = command.split(" ")
                name = command[1]
                print("\n{}\n".format(card_type[name].get_description(Card)))
            elif "play" in command:
                # to judge the play command whether own a target id
                command = command.split(" ")
                if len(command) == 2:
                    card = command[1]
                    if not encounter.player_apply_card(card):
                        print(CARD_FAILURE_MESSAGE)
                    else:
                        display_encounter(encounter)
                elif len(command) == 3:
                    card = command[1]
                    target = int(command[2])
                    if not encounter.player_apply_card(card, target):
                        print(CARD_FAILURE_MESSAGE)
                    else:
                        display_encounter(encounter)
            elif command == "end turn":
                encounter.end_player_turn()
                encounter.enemy_turn()
                encounter.player_turn = True
                if not player_class.is_defeated():
                    display_encounter(encounter)
                else:
                    print(GAME_LOSE_MESSAGE)
                    break
        if not encounter.is_active():
            print(ENCOUNTER_WIN_MESSAGE)
    if not player_class.is_defeated():
        print(GAME_WIN_MESSAGE)


if __name__ == '__main__':
    main()

