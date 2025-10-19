import os
import sys
sys.path.append('backend')
import riot_api
import insights
import aws_ai

if os.getenv('RIOT_API_KEY'):
    print('✅ Riot API key loaded successfully!')
else:
    print('❌ Riot API key NOT found!')
    sys.exit(1)
