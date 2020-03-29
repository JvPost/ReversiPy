this["Handlebars"] = this["Handlebars"] || {};
this["Handlebars"]["spa"] = this["Handlebars"]["spa"] || {};
this["Handlebars"]["spa"]["reversi_open"] = Handlebars.template({"compiler":[8,">= 4.3.0"],"main":function(container,depth0,helpers,partials,data) {
    var helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=container.hooks.helperMissing, alias3="function", alias4=container.escapeExpression, lookupProperty = container.lookupProperty || function(parent, propertyName) {
        if (Object.prototype.hasOwnProperty.call(parent, propertyName)) {
          return parent[propertyName];
        }
        return undefined
    };

  return "<button id=\"game-toggle-open\" value='"
    + alias4(((helper = (helper = lookupProperty(helpers,"btnvalue") || (depth0 != null ? lookupProperty(depth0,"btnvalue") : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"btnvalue","hash":{},"data":data,"loc":{"start":{"line":1,"column":37},"end":{"line":1,"column":49}}}) : helper)))
    + "' onclick='SPA.openReversiWindow()'> "
    + alias4(((helper = (helper = lookupProperty(helpers,"btntext") || (depth0 != null ? lookupProperty(depth0,"btntext") : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"btntext","hash":{},"data":data,"loc":{"start":{"line":1,"column":86},"end":{"line":1,"column":97}}}) : helper)))
    + " </button>";
},"useData":true});