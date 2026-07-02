import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 20,
    duration: '1m',
};

export default function () {
    const res = http.get('http://51.21.219.64/');

    check(res, {
        'status is 200': (r) => r.status === 200,
    });

    sleep(1);
}