import pytest
from lib import Cult, Follower, BloodOath  # Import your actual classes from your module

# Define some sample data for testing
sample_cult_data = [
    {"name": "Cult1", "location": "City1", "founding_year": 2000, "slogan": "Slogan1"},
    {"name": "Cult2", "location": "City2", "founding_year": 2010, "slogan": "Slogan2"},
]

sample_follower_data = [
    {"name": "Follower1", "age": 25, "life_motto": "Motto1"},
    {"name": "Follower2", "age": 30, "life_motto": "Motto2"},
]

# Create actual Follower and Cult instances
follower1 = Follower(**sample_follower_data[0])
follower2 = Follower(**sample_follower_data[1])
cult1 = Cult(**sample_cult_data[0])
cult2 = Cult(**sample_cult_data[1])

sample_bloodoath_data = [
    {"initiation_date": "2023-01-01", "follower": follower1, "cult": cult1},
    {"initiation_date": "2023-02-15", "follower": follower2, "cult": cult2},
]

@pytest.fixture
def setup_cults_followers_bloodoaths():
    # Create Cult instances
    cults = [Cult(**data) for data in sample_cult_data]

    # Create Follower instances
    followers = [Follower(**data) for data in sample_follower_data]

    # Create BloodOath instances
    bloodoaths = [BloodOath(**data) for data in sample_bloodoath_data]

    return cults, followers, bloodoaths

def test_cult_attributes(setup_cults_followers_bloodoaths):
    cults, _, _ = setup_cults_followers_bloodoaths

    # Test Cult attributes
    for cult in cults:
        assert isinstance(cult.name, str)
        assert isinstance(cult.location, str)
        assert isinstance(cult.founding_year, int)
        assert isinstance(cult.slogan, str)

def test_cult_recruit_follower(setup_cults_followers_bloodoaths):
    cults, followers, _ = setup_cults_followers_bloodoaths

    # Test Cult recruit_follower method
    cult = cults[0]
    follower = followers[0]

    cult.recruit_follower(follower)
    assert follower in cult.all_members

def test_cult_all(setup_cults_followers_bloodoaths):
    cults, _, _ = setup_cults_followers_bloodoaths

    # Test Cult.all property
    all_cults = Cult.all
    assert {cult.name for cult in all_cults} == {cult.name for cult in cults}

def test_cult_find_by_name(setup_cults_followers_bloodoaths):
    cults, _, _ = setup_cults_followers_bloodoaths

    # Test Cult.find_by_name method
    cult_name = "Cult1"
    found_cult = Cult.find_by_name(cult_name)
    assert found_cult.name == cult_name

def test_follower_attributes(setup_cults_followers_bloodoaths):
    _, followers, _ = setup_cults_followers_bloodoaths

    # Test Follower attributes
    for follower in followers:
        assert isinstance(follower.name, str)
        assert isinstance(follower.age, int)
        assert isinstance(follower.life_motto, str)

def test_follower_join_cult(setup_cults_followers_bloodoaths):
    cults, followers, _ = setup_cults_followers_bloodoaths

    # Test Follower join_cult method
    follower = followers[0]
    cult = cults[0]

    follower.join_cult(cult)
    assert cult in follower.cults

def test_follower_of_a_certain_age(setup_cults_followers_bloodoaths):
    _, followers, _ = setup_cults_followers_bloodoaths

    # Test Follower.of_a_certain_age method
    age = 25
    filtered_followers = Follower.of_a_certain_age(age)
    assert all(f.age >= age for f in filtered_followers)

def test_bloodoath_initiation_date(setup_cults_followers_bloodoaths):
    _, _, bloodoaths = setup_cults_followers_bloodoaths

    # Test BloodOath initiation_date property
    for bloodoath in bloodoaths:
        assert isinstance(bloodoath.initiation_date, str)

def test_bloodoath_all(setup_cults_followers_bloodoaths):
    _, _, bloodoaths = setup_cults_followers_bloodoaths

    # Test BloodOath.all property
    all_bloodoaths = BloodOath.all
    assert {oath.initiation_date for oath in all_bloodoaths} == {oath.initiation_date for oath in bloodoaths}


if __name__ == '__main__':
    pytest.main()
