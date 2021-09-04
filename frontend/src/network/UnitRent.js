import {request} from "./requests";

export function getUnitRent() {
    return request({
        url: '/get_unit_rent',
        headers: {
            // 先通过login请求获取 token， 然后在前面拼接"Bearer"
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJcdTY3NjhcdTZkNjlcdTY1ODciLCJhdXRoIjoib3duZXIiLCJjcmVhdGVfdGltZSI6IjIwMjEtMDktMDQgMjE6NTk6MjgiLCJleHAiOjE2MzA3NjU3Njh9.McrW3myNqbrhGtZLV-ywvTQHml2OfVuABrxcucdR61o',
            'Content-Type': 'application/json',
        }
    }).then(res => {
        console.log(res)
    })
}