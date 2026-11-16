def predict_traffic():
    # Demo forecast. Replace with a trained model and real historical data.
    return [{"time":"09:00","vehicles":400},{"time":"10:00","vehicles":450},{"time":"11:00","vehicles":510},{"time":"12:00","vehicles":620},{"time":"13:00","vehicles":570},{"time":"14:00","vehicles":680},{"time":"15:00","vehicles":630},{"time":"16:00","vehicles":720}]
def optimize_signals(junctions):
    # Illustrative calculation only, not a certified traffic signal algorithm.
    out=[]
    for j in junctions:
        v=int(j.get("vehicles",0)); seconds=max(15,min(60,round(15+v*.23)))
        out.append({"id":j["id"],"name":j["name"],"vehicles":v,"green_seconds":seconds,"density":j.get("density","Unknown"),"signal":j.get("signal","Red")})
    return out
