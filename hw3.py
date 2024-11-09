import data

#part 1
def population_total(county_list:list[data.CountyDemographics]) -> int:
    total_population = 0
    for county in county_list:
        total_population += county.population['2014 Population']
    return total_population
#part 2
def filter_by_state(county_list:list[data.CountyDemographics],state:str) -> list:
    return [county for county in county_list if county.state == state]


#part 3
def population_by_education(county_list:list,education:str) -> float:
    total_population = 0.0
    for county in county_list:
        if education in county.education:
            total_population += county.education[education]
    return total_population

def population_by_ethnicity(county_list:list,ethnicity:str) -> float:
    total_population = 0.0
    for county in county_list:
        if ethnicity in county.ethnicities:
            total_population += county.ethnicities[ethnicity]
    return total_population


def population_below_poverty_level(county_list:list,poverty:str) -> float:
    total_population = 0.0
    for county in county_list:
        if poverty in county.income:
            total_population += county.income[poverty]
        return total_population

#part 4

def percent_by_education(county_list:list[data.CountyDemographics],education:str) -> float:
    total_population = 0.0
    total_education_population = 0.0
    for county in county_list:
        if education in county.education:
            education_count = county.education[education]
        else:
            education = 0
        total_population += county.population.get("2014 Population",0)
        total_education_population += education_count * county.population.get('2014 Population', 0 )

    if total_population == 0:
        return 0.0
    percent = (total_education_population / total_population) * 100
    return percent

def percent_by_ethnicity(county_list:list[data.CountyDemographics],ethnicity:str) -> float:
    total_population = 0.0
    total_ethnicity_population = 0.0
    for county in county_list:
        if ethnicity in county.ethnicities:
            ethnicity_count = county.ethnicities[ethnicity]
        else:
            ethnicity_count = 0
        total_population += county.population.get("2014 Population",0)
        total_ethnicity_population += ethnicity_count * county.population.get('2014 Population', 0 )

    if total_population == 0:
        return 0.0
    percent = (total_ethnicity_population / total_population) * 100
    return percent

def percent_below_poverty_level(county_list:list[data.CountyDemographics],poverty:str) -> float:
    total_population = 0.0
    total_poverty_population = 0.0
    for county in county_list:
        if poverty in county.income:
            poverty_count = county.income[poverty]
        else:
            poverty_count = 0
        total_population += county.population.get("2014 Population",0)
        total_poverty_population += poverty_count * county.population.get('2014 Population', 0 )

    if total_population == 0:
        return 0.0
    percent = (total_poverty_population / total_population) * 100
    return percent

#part 5

def education_greater_than(counties: list[data.CountyDemographics],education:str,threshold:float)->list[data.CountyDemographics]:
    result = []
    for county in counties:
        if education in county.education:
            if county.education[education] > threshold:
                result.append(county)
    return result

def education_less_than(counties: list[data.CountyDemographics],education:str,threshold:float)->list[data.CountyDemographics]:
    result = []
    for county in counties:
        if education in county.education:
            if county.education[education] < threshold:
                result.append(county)
    return result


def ethnicity_greater_than(counties:list[data.CountyDemographics], ethnicity:str,threshold:float)->list[data.CountyDemographics]:
    result = []
    for county in counties:
        if ethnicity in county.ethnicities:
            if county.ethnicities[ethnicity] > threshold:
                result.append(county)
    return result

def ethnicity_less_than(counties:list[data.CountyDemographics], ethnicity:str,threshold:float)->list[data.CountyDemographics]:
    result = []
    for county in counties:
        if ethnicity in county.ethnicities:
            if county.ethnicities[ethnicity] < threshold:
                result.append(county)
    return result

def below_poverty_level_greater_than(counties:list[data.CountyDemographics], poverty:str, threshold:float) -> list[data.CountyDemographics]:
    result = []
    for county in counties:
        if poverty in county.income:
            if county.income[poverty] > threshold:
                result.append(county)
    return result

def below_poverty_level_less_than(counties:list[data.CountyDemographics], poverty:str, threshold:float) -> list[data.CountyDemographics]:
    result = []
    for county in counties:
        if poverty in county.income:
            if county.income[poverty] < threshold:
                result.append(county)
    return result






