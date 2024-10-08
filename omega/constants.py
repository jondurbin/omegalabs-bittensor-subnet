MIN_VIDEO_LENGTH = 5  # five seconds
MAX_VIDEO_LENGTH = 120  # two minutes
FIVE_MINUTES = 300  # 5 minutes in seconds
VALIDATOR_TIMEOUT = 90  # 1.5 minutes
VALIDATOR_TIMEOUT_MARGIN = 30  # 30 seconds

# Validator constants
CHECK_PROBABILITY = 0.1
DIFFERENCE_THRESHOLD = 0.1
SIMILARITY_THRESHOLD = 0.95
VIDEO_DOWNLOAD_TIMEOUT = 10
MIN_SCORE = 0.005
FAKE_VIDEO_PUNISHMENT = -5.0
QUERY_RELEVANCE_SCALING_FACTOR = 1.3
DESCRIPTION_RELEVANCE_SCALING_FACTOR = 0.7
VIDEO_RELEVANCE_WEIGHT = 0.65
FOCUS_MIN_SCORE = 0
MAX_FOCUS_SCORE = 1000
STUFFED_DESCRIPTION_PUNISHMENT = -5.0
FOCUS_REWARDS_PERCENT = 0.025
YOUTUBE_REWARDS_PERCENT = 1.0 - FOCUS_REWARDS_PERCENT

# Description length scaling values.
DESCRIPTION_LENGTH_WEIGHT = 0.35
MIN_LENGTH_BOOST_TOKEN_COUNT = 100
MAX_LENGTH_BOOST_TOKEN_COUNT = 300
