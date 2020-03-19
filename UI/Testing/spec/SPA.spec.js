describe("SPA", () => {
    //1. SPA.init callen
    //2. ResponseModule's getplayertoken mocken
    //3. spy-en op ResponseModule's joinGame
    let playerToken
    const onSuccess = jasmine.createSpy('onSuccess');
    const onFailure = jasmine.createSpy('onFailure');

    beforeEach(() => {
        jasmine.Ajax.install(); 

        SPA.init($("<div id='spa'></div>"))
    });

    afterEach(() => {
        jasmine.Ajax.uninstall();
    });

    it("getPlayerToken ShouldBeCalled", () => {
        const tokenResponse = {
            status: 200,
            responseText: '{"token": "playerToken"}'
        }

        let promiseGetPlayerToken = ResponseModule.getPlayerToken();
        let request = jasmine.Ajax.requests.mostRecent();
        request.respondWith(tokenResponse);
        
        promiseGetPlayerToken
            .then((result) => {
                expect(result.token).toContain("playerToken");
                return onSuccess();
            })
            .catch((error) => {
                return onFailure();
            })
            .finally(() => {
                expect(onSuccess).toHaveBeenCalled();
                expect(onFailure).not.toHaveBeenCalled();
            });
    });

});