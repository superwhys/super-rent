import {request} from "./requests";

export function getLogin(userName, pwd) {

    return request({
        url: '/user/login',
        method: 'post',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        data: {
            "username": userName,
            "password": pwd
        },
        transformRequest: [function (data) {
            let ret = ''
            for (let key in data) {
                ret += encodeURIComponent(key) + '=' + encodeURIComponent(data[key]) + '&'
            }
            return ret.slice(0, ret.length-1)
        }],
    })
}