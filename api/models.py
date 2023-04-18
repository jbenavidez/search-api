from django.db import models
from django.db.models import Q
from typing import List, Dict


class Provider(models.Model):
    provider_id = models.IntegerField()
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.CharField(max_length=200, blank=True, null=True)
    rating = models.FloatField()
    primary_skills = models.TextField(null=True)
    secondary_skill = models.TextField(null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    returned_count = models.IntegerField(default=0)
    active = models.BooleanField()
    country = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)

    @classmethod
    def create(cls, provider: Dict) -> None:
        provider_id = provider['id']
        try:
            # check if provider exists
            cls.get_by_id(provider_id)
            print(f"Provider already exists, {provider_id}")
        except Exception:
            # create new provider
            print(f"creating new provider {provider_id}")
            entry = cls(
                provider_id=provider_id,
                first_name=provider['first_name'],
                last_name=provider['last_name'],
                sex=provider['sex'],
                birth_date=provider['birth_date'],
                rating=provider['rating'],
                primary_skills=provider['primary_skills'],
                secondary_skill=provider['secondary_skill'],
                company=provider['company'],
                active=provider['active'],
                country=provider['country'],
                language=provider['language']
            )
            entry.save()

    @classmethod
    def update_returned_count(cls, provider_id: str) -> None:
        """Update returned count"""
        provider = cls.get_by_id(provider_id)
        provider.returned_count = provider.returned_count + 1
        provider.save()

    @classmethod
    def get_all(cls) -> List["Provider"]:
        """Get all providers"""
        res = cls.objects.all().order_by('-returned_count')
        return [cls.entity_to_provider(provider) for provider in res]

    @classmethod
    def search(
        cls,
        search: str,
        include: str,
        exclude: str,
        is_active: bool
    ) -> List["Provider"]:
        """Search providers by term"""
        search_conditions = cls.get_conditions(search)
        # Set active flags
        if is_active is not None:
            search_conditions.append(Q(active=is_active))
        res = cls.objects.filter(*search_conditions)\
            .order_by('-returned_count')
        # add exclude terms a.k.a extra filters
        if include is not None:
            include_conditions = cls.get_conditions(include)
            res = res.filter(*include_conditions)
        # exclude terms
        if exclude is not None:
            print("hello_from_exluce", exclude)
            exclude_conditions = cls.get_conditions(exclude)
            res = res.exclude(*exclude_conditions)
        return [cls.entity_to_provider(provider) for provider in res]

    @classmethod
    def get_conditions(cls, param_type) -> any:
        """Get provider conditions"""
        return [
                Q(first_name__icontains=param_type) |
                Q(last_name__icontains=param_type) |
                Q(sex__icontains=param_type) |
                Q(birth_date__icontains=param_type) |
                Q(rating__icontains=param_type) |
                Q(primary_skills__icontains=param_type) |
                Q(secondary_skill__icontains=param_type) |
                Q(company__icontains=param_type) |
                Q(country__icontains=param_type) |
                Q(company__icontains=param_type)
                ]

    @classmethod
    def get_by_id(cls, id: str) -> "Provider":
        """Get provider by id"""
        return cls.objects.get(provider_id=int(id))

    @classmethod
    def delete_all(cls) -> None:
        """Delete provider only for dev"""
        cls.objects.all().delete()
        print("Provider deleted")

    @classmethod
    def entity_to_provider(cls, provider) -> Dict:
        """Convert entity to provider"""
        provider_id = provider.provider_id
        # update returned count
        cls.update_returned_count(provider_id)
        return {
            'id': provider_id,
            'first_name': provider.first_name,
            'last_name': provider.last_name,
            'sex': provider.sex,
            'birth_date': provider.birth_date,
            'rating': provider.rating,
            'primary_skills': provider.primary_skills,
            'secondary_skill': provider.secondary_skill,
            'company': provider.company,
            'returned_count': provider.returned_count,
            'active': provider.active,
            'country': provider.country,
            'language': provider.language
        }
