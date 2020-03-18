// describe("SPA", () => {

//     //  jasmine.createSpy is om een spy functie te maken, die aan wil roepen na een Promise.
//     //      Waardoor je kan controlleren of de promise succesvol is uitgevoerd.
//     // 
//     //  jasmine.spyOn gebruik je om een spy te maken voor een functie die je zelf hebt geschreven.
//     //      Waardoor je kan controlleren of het resultaat van een promise is uitgevoerd.
//     //      Waardoor je kan controlleren of de promise succesvol is uitgevoerd.
    
//     //  Met mocks kun je resultaten van requests na bootsen, zodat je de server niet hoeft aan te roepen.
//     //  Vervolgens kan je de spies gebruiken om te controlleren of op de mock request en responds goed gereageerd is.
//     //  Dus de tests voor de frontend van reversi gaat getest worden op basis van de volgende principes:
//     //      1. SPA is de combinatie ResponseModule en GameModule; de eventhandlers staan hier beschreven.
//     //      2. De eventshandlers in SPA voeren methoden in de ResponseModule uit. (wordt gemockt)
//     //      3. De Resultaten van de van de methoden uit ResponseModule voeren methoden uit in de GameModule (worden spies voor gemaakt)
//     //      4. De hierboven beschreven principes betekent dat ResponseModule en GameModule onafhankelijk getest moeten worden.
//     //      5. Hoe ik SPA.JS ga testen moet ik nog even bekijken.
/**
 * Mocking ResponseModule
 */
describe("ResponseModule", () => {
    const onSuccess = jasmine.createSpy('onSuccess');
    const onFailure = jasmine.createSpy('onFailure');
    const playerToken = "playerToken"

    beforeEach(function () {
        jasmine.Ajax.install();
    });

    afterEach(function () {
        jasmine.Ajax.uninstall();
    });

    it ('getPlayerToken', () => {
        const playerTokenResponse = {
            status: 200,
            responseText: '{"token": "playerToken"}'
        }

        
        let promiseGetPlayerToken = ResponseModule.getPlayerToken(); // te testen methode
            let request = jasmine.Ajax.requests.mostRecent();
            request.respondWith(playerTokenResponse);
            return promiseGetPlayerToken
                .then(result => {
                    expect(result.token).toContain("playerToken");
                    return onSuccess();
                })
                .catch((err) => {
                    return onFailure();
                })
                .finally(function() {
                    expect(onSuccess).toHaveBeenCalled();
                    expect(onFailure).not.toHaveBeenCalled();
                });
    });

    it ('joinGame', () => {
        const joinGameResponse = {
            status: 200,
            responseText: 
            `{ "gameGrid": 
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1,-1, 0, 0, 0],
                    [0, 0, 0,-1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]
                ]
            }`
        }
        

        let promiseJoinGame = ResponseModule.joinGame(playerToken); // te testen methode
        let request = jasmine.Ajax.requests.mostRecent();
        request.respondWith(joinGameResponse);
        return promiseJoinGame
            .then(result => {
                expect(result.gameGrid).toEqual(
                    [
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1,-1, 0, 0, 0],
                        [0, 0, 0,-1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0]
                    ]
                )
                return onSuccess();
            })
            .catch((err) => {
                return onFailure();
            })
            .finally(() => {
                expect(onSuccess).toHaveBeenCalled();
                expect(onFailure).not.toHaveBeenCalled();
            });
    });

    it ('move', () => {
        const moveResponse = {
            status: 200
        }

        let promiseMove = ResponseModule.move(1, 'f', 6, playerToken) // te testen methode
        let request = jasmine.Ajax.requests.mostRecent();
        request.respondWith(moveResponse);
        return promiseMove
            .then(result => {
                return onSuccess();
            })
            .catch(err => {
                return onFailure();
            })
            .finally(() => {
                expect(onSuccess).toHaveBeenCalled();
                expect(onFailure).not.toHaveBeenCalled();
            });
    });
});
