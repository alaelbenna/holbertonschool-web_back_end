import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';


export default function handleProfileSignup(firstName, lastName, fileName) {
    return Promise.allSettled([signUpUser(), uploadPhoto()]).then(() => {
        [
            {status: response.status, value: signUpUser(firstName, lastName).then((value) => value)},
            {status: response.status, value: uploadPhoto(fileName).then(() => Error())}
        ]
    })
}
