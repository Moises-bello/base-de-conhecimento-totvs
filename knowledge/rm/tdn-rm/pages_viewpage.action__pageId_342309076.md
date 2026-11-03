---
content_hash: e45a35a754f64776978723c2df8ecf1c45ec89ce9f84482edb2443cb26aaf380
fetched_at: '2026-06-29T00:08:53.069501+00:00'
page_id: '342309076'
product: rm
source: tdn-rm
title: O que é "Gatilho" e quando é gerado?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342309076
version: 1
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Folha de Pagamento |
| **Dúvida:** | O que é "Gatilho" e quando é gerado? |
| **Resposta:** | É um registro da fila de eventos do eSocial, ainda sem as informações do XML. Sua função é sinalizar a necessidade de envio de informações para o Governo.    Será gerado na carga inicial ("Gerar Gatilhos Eventos Iniciais") ou sempre que um fato gerador do eSocial acontece.  Exemplos:  Ao incluir um Funcionário, o sistema irá gerar um gatilho para o evento S-2200. Ao alterar um Funcionário, o sistema irá gerar um gatilho para o evento S-2205 ou S-2206. Ao excluir um período de gozo de férias, será gerado um gatilho para o Evento de Exclusão (S-3000).    Mais informações em <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.GerarGatilhosIniciais.aspx> |
