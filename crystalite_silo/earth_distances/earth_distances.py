    from math import radians, cos, sin, asin, sqrt
    R = 6371

    def haversine_distance(lat1, lng1, lat2, lng2):
        lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))
        lat = lat2 - lat1
        lng = lng2 - lng1
        d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
        h = 2 * R * asin(sqrt(d))
        return h

    def distance(first, second):
        first = first.replace('°', ',').replace('′', ',').replace('″', ',').replace('u', '').replace('"', ',').replace(', ', ',').replace(' ', ',').split(',')
        second = second.replace('°', ',').replace('′', ',').replace('″', ',').replace('u', '').replace('"', ',').replace(', ', ',').replace(' ', ',').split(',')
        first_latitude = int(first[0]) + int(first[1]) / 60 + int(first[2]) / 3600
        first_longitude = int(first[4]) + int(first[5]) / 60 + int(first[6]) / 3600
        second_latitude = int(second[0]) + int(second[1]) / 60 + int(second[2]) / 3600
        second_longitude = int(second[4]) + int(second[5]) / 60 + int(second[6]) / 3600
        if first[3] == "S":
            first_latitude *= -1
        if first[7] == "W":
            first_longitude *= -1
        if second[3] == "S":
            second_latitude *= -1
        if second[7] == "W":
            second_longitude *= -1
        return haversine_distance(first_latitude, first_longitude, second_latitude, second_longitude)


    if __name__ == '__main__':
        # These "asserts" using only for self-checking and not necessary for auto-testing
        def almost_equal(checked, correct, significant_digits=1):
            precision = 0.1 ** significant_digits
            return correct - precision < checked < correct + precision

        assert almost_equal(
            distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
        assert almost_equal(
            distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
        assert almost_equal(
            distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"

        print("All done? Earn rewards by using the 'Check' button!")
