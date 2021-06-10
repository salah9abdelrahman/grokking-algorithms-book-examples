# o(n^2)
def best_stations():
    global states_needed
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            # covered is a set of uncovered stations that this station is covers
            # & for intersection
            covered = states_needed & states_for_station
            # check if this station covers more states than the current best_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        final_stations.add(best_station)
        # - for difference
        states_needed -= states_covered
    return final_stations


if __name__ == '__main__':
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    final_stations = set()

    print(best_stations())
