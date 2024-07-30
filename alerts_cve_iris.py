import requests
import json

# URL de l'API
url = 'https://localhost/alerts/add'

# En-têtes de la requête
headers = {
    'Authorization': 'Bearer ',
    'Content-Type': 'application/json'
}

# Données de l'alerte
data = {
  "alert_title": "Low-reputation arbitrary code executed by signed executable",
  "alert_description": "This is a test alert, courtesy of MS",
  "alert_source": "Test Source",
  "alert_source_ref": "Test-123",
  "alert_source_link": "https://source_link.com",
  "alert_source_content": {
    "_id": "603f704aaf7417985bbf3b22",
    "contextId": "206e2965-6533-48a6-ba9e-794364a84bf9",
    "description": "Contoso user performed 11 suspicious activities MITRE Technique used Account Discovery (T1087) and subtechnique used Domain Account (T1087.002)",
    "entities": [
      {
        "entityRole": "Source",
        "entityType": 2,
        "id": "6204bdaf-ad46-4e99-a25d-374a0532c666",
        "inst": 0,
        "label": "user1",
        "pa": "user1@contoso.com",
        "saas": 11161,
        "type": "account"
      },
      {
        "entityRole": "Related",
        "id": "55017817-27af-49a7-93d6-8af6c5030fdb",
        "label": "DC3",
        "type": "device"
      },
      {
        "id": 20940,
        "label": "Active Directory",
        "type": "service"
      },
      {
        "entityRole": "Related",
        "id": "95c59b48-98c1-40ff-a444-d9040f1f68f2",
        "label": "DC4",
        "type": "device"
      },
      {
        "id": "5bfd18bfab73c36ba10d38ca",
        "label": "Honeytoken activity",
        "policyType": "ANOMALY_DETECTION",
        "type": "policyRule"
      },
      {
        "entityRole": "Source",
        "id": "34f3ecc9-6903-4df7-af79-14fe2d0d4553",
        "label": "Client1",
        "type": "device"
      },
      {
        "entityRole": "Related",
        "id": "d68772fe-1171-4124-9f73-0f410340bd54",
        "label": "DC1",
        "type": "device"
      },
      {
        "type": "groupTag",
        "id": "5f759b4d106abbe4a504ea5d",
        "label": "All Users"
      }
    ],
    "idValue": 15795464,
    "isSystemAlert": false,
    "resolutionStatusValue": 0,
    "severityValue": 5,
    "statusValue": 1,
    "stories": [
      0
    ],
    "threatScore": 34,
    "timestamp": 1621941916475,
    "title": "Honeytoken activity",
    "comment": "",
    "handledByUser": "administrator@contoso.com",
    "resolveTime": "2021-05-13T14:02:34.904Z",
    "URL": "https://contoso.portal.cloudappsecurity.com/#/alerts/603f704aaf7417985bbf3b22"
  },
  "alert_severity_id": 4,
  "alert_status_id": 3,
  "alert_context": {
    "context_key": "context_value"
  },
  "alert_source_event_time": "2023-03-26T03:00:30",
  "alert_note": "A note on",
  "alert_tags": "defender,anothertag",
  "alert_iocs": [
    {
      "ioc_value": "tarzan5",
      "ioc_description": "description of Tarzan",
      "ioc_tlp_id": 1,
      "ioc_type_id": 2,
      "ioc_tags": "tag1,tag2",
      "ioc_enrichment": {
        "provider_1": {
          "data": 2,
          "new_data": 3
        },
        "provider_3": {
          "enric": "true"
        }
      }
    },
    {
      "ioc_value": "tarzan2",
      "ioc_description": "description_hey",
      "ioc_tlp_id": 2,
      "ioc_type_id": 4,
      "ioc_tags": "tag1,tag2",
      "ioc_enrichment": {
        "provider_1": {
          "data": "a very long\nblablablabdjsjofiasofiasjdxaisjhfaiosxhd bla\nddijwedoijwedw\ndhasdhaifuhafiassfsakjfhaskljfhaslkfjhaslkfdjhdqwleiuhxioauwedhoqwiuhzndoqwuehxdnzoiuwehfoqwiufhxnwoquhoiwefhxnqwoiuhwqomifuhqzwofuhqwofeuzhqwofeiuqhwe fifuhqwiofuh qwofuqh fuq hwfoiqwhfoiquhfe quhfqiouwhf qoufhq hufou qufhqowiufhowufih qwfuhqwioufh wqoufh wifhufdhas",
          "new_data": 3
        },
        "provider_3": {
          "enric": "true"
        }
      }
    }
  ],
  "alert_assets": [
    {
      "asset_name": "My super asset",
      "asset_description": "Asset description",
      "asset_type_id": 1,
      "asset_ip": "1.1.1.1",
      "asset_domain": "",
      "asset_tags": "tag1,tag2",
      "asset_enrichment": {
        "enrich1": {
          "A key": "A value"
        }
      }
    }
  ],
  "alert_customer_id": 1,
  "alert_classification_id": 1
}

# Effectuer la requête POST
response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

# Afficher la réponse
print(f"Status Code: {response.status_code}")
print(response.json())
