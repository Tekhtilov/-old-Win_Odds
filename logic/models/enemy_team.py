from logic.models.hero import Hero


class EnemyTeam(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.enemy_team_list = self.name.split(",")


enemy_team = EnemyTeam(name=input("Enter enemy team heroes: "))


