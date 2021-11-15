import axios from 'axios'

// 封装网络请求模块
export function request(config) {
    const instance = axios.create({
        baseURL: 'http://127.0.0.1:8000/rent/v1',
        timeout: 5000,
        method: 'get'
    })

    instance.interceptors.request.use(config => {
        return config
    }, err => {
        console.log(err)
    })

    instance.interceptors.response.use(res => {

        return res.data
    }, err => {
        console.log(err);
        return err
    })

    return instance(config)
}

export function PostRequests(config, data) {
    const instance = axios.create({
        baseURL: 'http://127.0.0.1:8000/rent/v1',
        timeout: 5000,
        method: 'post'
    })

    instance.interceptors.request.use(config => {
        return config
    }, err => {
        console.log(err)
    })

    instance.interceptors.response.use(res => {

        return res.data
    }, err => {
        console.log(err);
        return err
    })

    return instance(config, data)
}