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
    const onSuccess = jasmine.createSpy('onSuccess'); // Spy om te controlleren of de te testen methode goed is uitgevoerd.
    const onFailure = jasmine.createSpy('onFailure'); // Spy om te controlleren of de te testen methode goed is uitgevoerd.
    const playerToken = "playerToken"

    beforeEach(function () {
        jasmine.Ajax.install(); // Zorgt er voor dat de ajax calls niet uitgevoerd worden, maar de mock versie gebruikt wordt.
    });

    afterEach(function () {
        jasmine.Ajax.uninstall(); // Zorgt er voor de ajax calls weer gebruikt kunnen worden.
    });

    it ('mocking getPlayerToken', () => {
        const playerTokenResponse = { 
            status: 200,
            responseText: '{"token": "playerToken"}'
        }
        
        // Te testen methode, die een promise met ajax call returned. Door Ajax.install() wordt de ajax call niet uitgevoerd
        let promiseGetPlayerToken = ResponseModule.getPlayerToken();
        // Pakt het tegen gehouden request.
        let request = jasmine.Ajax.requests.mostRecent(); 
        // Mockt de response van het tegengehouden request
        request.respondWith(playerTokenResponse);
        // De volgende regels zijn de reactie op het gemockte request.
         promiseGetPlayerToken
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

   
    it ('mocking joinGame', () => {
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
            status: 200,
            responseText: "{}"
        }

        let promiseMove = ResponseModule.move(1, 'f', 6, playerToken) // te testen methode
        let request = jasmine.Ajax.requests.mostRecent();
        request.respondWith(moveResponse);
        return promiseMove
            .then((result) => {
                expect(true).toBe(true);
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
});

describe("Spying getPlayerToken", () => {
    let onSuccess, onFailure, request;

    beforeEach(() => {
        jasmine.Ajax.install();

        beforeEach(() => {
            onFailure = jasmine.createSpy('onFailure');
            onSuccess = jasmine.createSpy('onSuccess');

            // We spy-en hier op de getJSON methode van het jQuery object,
            // Maar misschien kunnen we dit ook doen Response-,SPA- en GameModules.
            spyOn($, 'getJSON').and.callFake(function(req){ 
                let d= $.Deferred();
                // resolve using our mock data
                let data = {x: 1, y:2};
                d.resolve(data); //resolve leidt tot een succesvolle response, reject leidt tot een error.
                return d.promise(); 
            });
        });

        afterEach(() => {
            jasmine.Ajax.uninstall();
        });

        describe("onSuccess", () => {
            it ("should not have called the spyOnSuccess before doing the request", () => {
                expect(onSuccess).not.toHaveBeenCalled();
            });

            it("after the request it should have called the spy onSuccess", () => {
                return ResponseModule.getPlayerToken()
                    .then((data) => {
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
        });
    });
});



