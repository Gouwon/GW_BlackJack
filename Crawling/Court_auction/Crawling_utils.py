def query2jquery(param_sources):
    ps = param_sources.split('&')
    result = {}
    for p in ps:
        pp = p.split('=')
        result[pp[0]] = pp[1]
    return result


if __name__ == '__main__':
    