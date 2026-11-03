---
content_hash: 2235e89f1faf12b17fa4acbf0fb5fc17ac904656c78030a5dad15307efea5e89
fetched_at: '2026-06-29T00:09:45.852383+00:00'
page_id: '435096549'
product: rm
source: tdn-rm
title: Processo de Associação de Códigos de Ajuste SPED Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435096549
version: 12
---

O intuito deste processo é facilitar a associação de Códigos de Ajuste do SPED Fiscal no registro das Naturezas de Operação. Para que o processo seja executado obrigatoriamente deve ser criado um filtro para selecionar os Códigos de Ajuste a serem associados.

**Regras**

* Podem ser associados um ou mais códigos em uma mesma execução.
* As regras aplicadas à [Associação Manual](http://tdn.totvs.com.br/pages/viewpage.action?pageId=435096669#RegrasAssociacaoManual) são as mesmas aplicadas a este processo.
* Ao executar o processo se não for selecionado nenhum registro de Natureza de Operação a execução selecionará todos os registros da visão, inclusive os sintéticos. Neste caso o processo será executado normalmente e apresentará no seu log a informação de quais Natureza não tiveram Códigos de Ajuste associados por serem sintéticas e algum Código que por ventura não pôde ser associado.

***Atenção!***Este processo possui a opção **"Desassociar"**. Ao escolher esta opção o filtro de Códigos de Ajuste é ocultado da tela do processo. Ao final da execução **TODOS**os códigos associados às Naturezas selecionadas terão sido excluídos.
