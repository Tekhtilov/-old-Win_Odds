from logic.models.hero import Hero


# class EnemyTeam:
#     def __init__(self, name):
#         self.name = name
#
#     def get_enemy_heroes(self):
#         enemy_team_list = [self.name]
#         for i in range(2, 6):
#             enemy_team_list.append(input(f"Enter enemy {i}: "))
#         return enemy_team_list

class EnemyTeam(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.enemy_team_list = self.name.split(",")


enemy_team = EnemyTeam(name=input("Enter enemy team heroes: "))


