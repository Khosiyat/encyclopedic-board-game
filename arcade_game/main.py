import arcade
import random
import time
from questions import QUESTIONS
from utils import load_sounds

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_COUNT = 128

class Player:
    def __init__(self, name, sprite_path, start_x, start_y):
        self.name = name
        self.position = 1
        self.sprite = arcade.Sprite(sprite_path, scale=0.5)
        self.sprite.center_x = start_x
        self.sprite.center_y = start_y
        self.score = 0

    def move_to_cell(self, cell):
        self.position = cell
        x, y = ArcadeGame.cell_to_coords(cell)
        self.sprite.center_x = x
        self.sprite.center_y = y

class ArcadeGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Encyclopedic Board Game")
        arcade.set_background_color(arcade.color.AMAZON)
        self.playerA = Player("Player A", "../assets/playerA_sprite.png", 50, 50)
        self.playerB = Player("Player B", "../assets/playerB_sprite.png", 50, 50)
        self.current_player = self.playerA
        self.other_player = self.playerB
        self.game_over = False
        self.dice_roll_sound, self.move_sound, self.win_sound = load_sounds("../assets/")
        self.question_index = 0
        self.font_size = 14
        self.cell_width = SCREEN_WIDTH // 8
        self.cell_height = SCREEN_HEIGHT // 16
        self.message = "Press SPACE to answer question"

    @staticmethod
    def cell_to_coords(cell_num):
        col = (cell_num - 1) % 8
        row = (cell_num - 1) // 8
        # Flip rows so 1 is bottom-left
        y = (15 - row) * (SCREEN_HEIGHT // 16) + (SCREEN_HEIGHT // 32)
        x = col * (SCREEN_WIDTH // 8) + (SCREEN_WIDTH // 16)
        return x, y

    def on_draw(self):
        arcade.start_render()
        self.draw_board()
        self.playerA.sprite.draw()
        self.playerB.sprite.draw()

        arcade.draw_text(f"{self.current_player.name}'s turn", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 18)
        arcade.draw_text(f"Score: {self.current_player.score}", 10, SCREEN_HEIGHT - 60, arcade.color.WHITE, 14)
        arcade.draw_text(self.message, 10, 10, arcade.color.WHITE, 14)

    def draw_board(self):
        for row in range(16):
            for col in range(8):
                x = col * self.cell_width
                y = row * self.cell_height
                arcade.draw_rectangle_outline(x + self.cell_width / 2, y + self.cell_height / 2,
                                              self.cell_width, self.cell_height, arcade.color.WHITE)
                cell_num = (15 - row) * 8 + col + 1
                arcade.draw_text(str(cell_num), x + 5, y + 5, arcade.color.LIGHT_GRAY, 12)

    def on_key_press(self, key, modifiers):
        if self.game_over:
            return

        if key == arcade.key.SPACE:
            self.ask_question()

    def ask_question(self):
        question, answer = QUESTIONS[self.question_index % len(QUESTIONS)]
        self.message = f"{self.current_player.name}, answer: {question}"
        self.question_index += 1

        # For demo, simulate correct answer after short delay
        arcade.schedule(lambda delta_time: self.process_answer(True), 2.0)

    def process_answer(self, correct):
        arcade.unschedule(self.process_answer)
        if correct:
            self.message = f"Correct! Roll dice!"
            self.dice_roll()
        else:
            self.message = f"Wrong answer. Turn passes."
            self.switch_turn()

    def dice_roll(self):
        roll = random.randint(1, 6)
        self.message = f"{self.current_player.name} rolled a {roll}!"
        self.dice_roll_sound.play()
        new_pos = self.current_player.position + roll
        if new_pos > CELL_COUNT:
            new_pos = CELL_COUNT

        # Animate movement (simplified here)
        self.current_player.move_to_cell(new_pos)
        self.move_sound.play()

        if new_pos == CELL_COUNT:
            self.message = f"{self.current_player.name} wins!"
            self.win_sound.play()
            self.game_over = True
        else:
            self.switch_turn()

    def switch_turn(self):
        self.current_player, self.other_player = self.other_player, self.current_player
        self.message = f"{self.current_player.name}, press SPACE to answer question"

def main():
    game = ArcadeGame()
    arcade.run()

if __name__ == "__main__":
    main()
