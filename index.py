import PUBG_API as api
import Sqlite as db
import json

conn = db.connect_db()
db.init_db(conn)

test_account = 'account.95fb96ab3915485c998f6d9bc5eb84b6'
data = api.pubg_api_get_player_data(test_account)

if "data" in data:
    match_data = data["data"]["relationships"]["matches"]["data"]
    for match in match_data:
        print(match["id"])
        match_id = match["id"]
        match_record = db.get_match_by_id(conn, match_id)
        if match_record:
            print("  kills: %i" % match_record["kills"])
            print("  winPlace: %i" % match_record["rank"])
        else:
            match_resp = api.pubg_api_match_data(match_id)
            if "included" in match_resp:
                for item in match_resp["included"]:
                    if item["type"] == "participant":
                        stats = item["attributes"]["stats"]
                        if stats["playerId"] == test_account:
                            print("  kills: %i" % stats["kills"])
                            print("  winPlace: %i" % stats["winPlace"])
                            db.create_match_record(conn, {
                                "matchId": match_id,
                                "kills": stats["kills"],
                                "winPlace": stats["winPlace"]
                            })
            else:
                print(json.dumps(match_resp))
else:
    print(json.dumps(data))
