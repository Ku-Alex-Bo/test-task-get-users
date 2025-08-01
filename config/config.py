from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix=False,
    environments=False,
    load_dotenv=True,
)
