var admin = require("firebase-admin");
var serviceAccount = require("./serviceAccount.json");
admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://shotottahon.firebaseio.com"
});

var db = admin.firestore();

var fireStoreService = require('firestore-export-import');

const jsonToFirestore = async () => {
    try {
        await fireStoreService.restore('./books.json');
    } catch (e) {
        console.log(e);
    }
}
jsonToFirestore();