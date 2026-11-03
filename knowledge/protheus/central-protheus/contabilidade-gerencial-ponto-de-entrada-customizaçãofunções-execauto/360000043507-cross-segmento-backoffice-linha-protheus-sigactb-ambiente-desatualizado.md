---
article_id: 360000043507
category: Contabilidade Gerencial - Ponto de entrada, Customização,Funções, Execauto
content_hash: 7d464e5cd56de052992144ee18e1395116990fd90afedf2c5251dfc506be01ae
fetched_at: '2026-06-28T22:41:00.649677+00:00'
product: protheus
section_id: 1500001548462
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Ambiente desatualizado
type: support-article
updated_at: '2024-04-22T18:15:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000043507-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Ambiente-desatualizado
---

**Ocorrência:**No módulo **Contabilidade Gerencial**, ao tentar realizar qualquer manutenção é apresentada as seguintes mensagens:

* Ambiente desatualizado. Atualize o ambiente
* Erro variable does not exist **CPLANOREF**
* Erro **Invalid MacroSource**
* Invalid class **CTBA020EVPCO**
* Invalid class **CTBA020EVGFE**
* Invalid class **CTBA080EVOK**
* **Invalid column name 'FB\_CONTA'**

**Ambiente:**  
Protheus – Contabilidade Gerencial.

Esse incidente ocorre, pois o sistema não conseguiu verificar a existência das novas validações do cadastro de plano de contas, visão gerencial e plano de contas referencial.  
  
**Solução:**  
Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Acessar o portal do cliente e realizar o download da última Atualização do Fontes do módulo Contabilidade:

* [EXPEDICAO\_CONTINUA\_CTB](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22922993051287)

**2.** Realizar aplicação do pacote e atualização dos dicionários conforme documentação:

[**https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024584251**](Framework%20-%20Linha%20Protheus%20-%20Upgrade%20de%20Release%20do%20Protheus%2012)

**3**. Será necessário verificar via configurador se o campo **CT1\_CTALP** esta com a seguinte validação: ***"Vazio() .Or. ValidaConta(FWFldGet('CT1\_CTALP')) .Or. (FWFldGet('CT1\_CTALP') = '\*')"***

Caso não esteja, proceder os passos 2 novamente.

**4**. Será necessário alterar via configurador a utilização do campo CTS\_NOME, onde somente a opção 'USADO' deve ser habilitada na aba USO. [![](https://totvssuporte.zendesk.com/attachments/token/Fe4JLwDahhQIuK1Rvc3DwuVZM/?name=inline-1798652086.png)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016121468-MP-SIGACTB-Plano-de-contas-Error-log-erro-no-par%C3%A2metroFWFormViewStruct-O-erro-no-m%C3%A9todo-SETPROPERTY-Campo-CTS-NOME-n%C3%A3o-encontrado)

**5**. Verifique dentro do campo WHEN do SX3 (Via configurador) se o campo CTS\_ORDEM (alias CTS) está com a expressão: **INCLUI .and. If(FunName()=="CTBA160",.T.,.F.)** .

Caso não esteja, proceder com o ajuste via configurador do campo conforme descrito abaixo:

INCLUI .and. If(FunName() $ "CTBA160|CTBA161",.T.,.F.)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22922993066135)

OBS: Após alteração, não esquecer de gravar as alterações no dicionário.

**IMPORTANTE: Após a atualização do ambiente, recomenda-se aplicar as correções também para os ambiente de schedule (caso tiver).**

**Veja também**

* Atualização de saldos em fila: [Clique aqui](http://tdn.totvs.com/display/PROT/CTB113_REPROCESSAMENTO_SALDOS_POR_FILA_P12)
