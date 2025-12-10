from datetime import datetime
from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actors(self):
        return self.actor_repository.get_actors()

    def get_actors_name(self):
        actors = self.get_actors()
        actors_name = [actor.get('name') for actor in actors]
        return actors_name

    def create_actor(self, name: str, birthday: datetime, nationality: str):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        return self.actor_repository.create_actor(actor)
