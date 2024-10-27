from pydantic import BaseModel, ConfigDict, Field, field_validator


class BuildHeroDetailsCategoryAbility(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    ability_id: int
    annotation: str | None

    @field_validator("annotation")
    @classmethod
    def validate_annotation(cls, v, values):
        if len(v) == 0:
            return None
        return v


class BuildHeroDetailsCategory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    mods: list[BuildHeroDetailsCategoryAbility]
    name: str
    description: str
    width: float
    height: float


class BuildHeroDetailsAbilityOrderCurrencyChange(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    ability_id: int
    currency_type: int
    delta: int
    annotation: str | None

    @field_validator("annotation")
    @classmethod
    def validate_annotation(cls, v, values):
        if len(v) == 0:
            return None
        return v


class BuildHeroDetailsAbilityOrder(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    currency_changes: list[BuildHeroDetailsAbilityOrderCurrencyChange]


class BuildHeroDetails(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    mod_categories: list[BuildHeroDetailsCategory]
    ability_order: BuildHeroDetailsAbilityOrder | None = Field(None)


class BuildHero(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    hero_id: int
    hero_build_id: int
    author_account_id: int
    last_updated_timestamp: int
    name: str
    description: str
    language: int
    version: int
    origin_build_id: int
    details: BuildHeroDetails


class BuildPreference(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    favorited: bool
    ignored: bool
    reported: bool


class Build(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    hero_build: BuildHero
    num_favorites: int
    num_ignores: int
    num_reports: int
    preference: BuildPreference | None = Field(None)

    @classmethod
    def parse(cls, json_str: str):
        try:
            return cls.model_validate_json(json_str)
        except Exception as e:
            print(f"Error parsing build: {e}")
            return None
