---
content_hash: 11ec94358ff80a2cb356757d50efbbed472334fe9a5bd625bd495f59ad154902
fetched_at: '2026-07-02T19:24:22.569372+00:00'
page_id: '270914772'
product: protheus
source: tdn-tec
title: dialog.advplToJs.connect
type: documentation
url: https://tdn.totvs.com/display/tec/dialog.advplToJs.connect
version: 1
---

dialog.advplToJs.connect

Essa função é reponsável pelo recebimento das mensagens vindas do ADVPL para o JavaScript, permitindo o tratamento para inserção de campos, páginas de estilo, trechos JavaScript, etc.

## Sintaxe

false, < codeContent > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| codeType | caractere | Código da mensagem recebida. | X |  |
| codeContent | caractere | Texto a ser tratado no recebimento, como páginas de estilo, trechos JavaScript, etc. | X |  |

## Observações

* Função disponível em builds superiores a 7.00.131227A.

## Exemplos

cppEclipsetruefalse"
oWebChannel:advplToJs("html", code)
// O trecho Javascript abaixo efetua a conexão WebSocket entre o SmartClient
// e o Navegador embedado, a função definida como callBack será disparada
// ao fim da carga inicial da pagina/componente
// Carrega mensageria exclusiva da pagina, neste caso a mensagem "html"
dialog.advplToJs.connect(function (codeType, codeContent, objectName) {
if (codeType == "html") {
var form = document.getElementById("mainForm");
form.innerHTML += codeContent;
}
});
]]>
