import json

from dist.CONSTANTS import default_account, default_settings

with open('account_data/account.json', 'w') as account:
    json.dump(default_account, account)

with open('settings/settings.json', 'w') as settings:
    json.dump(default_settings, settings)