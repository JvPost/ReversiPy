describe("SPA", () => {
    describe("init", () => {
            const playerToken = "playerTestToken"
            const gameToken = "gameTestToken"

            beforeAll(() => {
                spyOn(SPA.ResponseModule, "getPlayerToken").and.callFake(() => {
                    let d = $.Deferred();
                    let data = {
                        playerToken: playerToken
                    }
                    d.resolve(data)
                    return d.promise();
                });

                spyOn(SPA.ResponseModule, "joinGame").and.callFake((token) => { 
                    let d = $.Deferred();
                    let data = {
                        'gameGrid': [
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1,-1, 0, 0, 0],
                            [0, 0, 0,-1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]
                        ],
                        'gameColumns': ['a','b','c','d','e','f','g','h'],
                        'gameToken': gameToken
                    };
                    d.resolve(data);
                    return d.promise();
                });

                spyOn(SPA.ResponseModule, "subscribe").and.callFake((playerToken, callBack) => {
                    return $.Deferred().promise();
                });

                SPA.init($("<div id='spa'></div>"));
            });
            
            afterAll(() => {
            });
            
            beforeEach(() => {
                jasmine.Ajax.install();
            });
            
            afterEach(() => {
                jasmine.Ajax.uninstall();
            });
            
            it("SPA.ResponseModule's getPlayerToken should be called", () => {
                expect(SPA.ResponseModule.getPlayerToken).toHaveBeenCalled();
            });
            
            it("SPA.ResponseModule's joinGame should be called", () => {
                expect(SPA.ResponseModule.joinGame).toHaveBeenCalledWith(playerToken);
            });
            
            it ("SPA.ResponseModule's should now be listening for push messages", () => {
                expect(SPA.ResponseModule.subscribe).toHaveBeenCalled();
            });

        });
});