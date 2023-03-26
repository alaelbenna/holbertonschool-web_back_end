import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  let txt = '';
  return Promise.all([uploadPhoto(), createUser()]).then((param) => {
    txt += `${param[0].body} ${param[1].firstName} ${param[1].lastName}`;
    console.log(txt);
  }).catch(() => {
    console.log('Signup system offline');
  });
}
