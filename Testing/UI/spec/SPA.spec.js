describe("SPA", () => {
    beforeAll(() => {
        spyOn(GameModule, 'init');
    });

    beforeEach(() => {
        SPA.init($("<div id='spa'></div>"))
    });
    
    describe("init", () => {
        it ("GameModule.init should be called", () => {
            expect(GameModule.init).toHaveBeenCalled();
        });
    });
});