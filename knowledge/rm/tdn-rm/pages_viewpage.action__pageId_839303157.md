---
content_hash: 88d3ff467374f89350eaa5e9f1e4e5f2bf64b7e31693472430bcf1215ecf42e7
fetched_at: '2026-06-29T00:11:50.229481+00:00'
page_id: '839303157'
product: rm
source: tdn-rm
title: DT - Apuração do FGTS na Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=839303157
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculos da Folha - Rescisão |
| País: | Brasil |
| Épico: | [DRHCALCRM-6085](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6085) |

## **02. SITUAÇÃO/REQUISITO**

Para o eSocial, os valores referente ao aviso prévio não devem ser considerados para descontos de eventos que estornam na base de FGTS caso o funcionário possua alguma verba que estorna a base, mesmo sendo valor menor. O mesmo ocorre para a Base de FGTS 13º Salário, onde valores que estornam a base de FGTS de 13º não podem ser descontados dos proventos referente ao 13º indenizado.

## **03. SOLUÇÃO**

Alterações descritas na FAQ - [Apuração do FGTS na Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=839304283)

IMPORTANTE

Quando houver cálculo de rescisão complementar referente a rescisões processadas antes da liberação dessa implementação, os valores do FGTS não serão separados por não existirem Código de Cálculo 467 - FGTS AVISO PRÉVIO e Código de Cálculo 468 - FGTS 13º INDENIZADO na rescisão original.

## **04.** **ASSUNTOS RELACIONADOS**

* NOVOS CC’s CRIADOS:
  + [467 - FGTS AVISO PRÉVIO](https://tdn.totvs.com/pages/viewpage.action?pageId=839303477)
  + [468 - FGTS 13º INDENIZADO](https://tdn.totvs.com/pages/viewpage.action?pageId=839303545)
  + [469 - BASE DE FGTS DIFERENÇA AVISO INDENIZADO](https://tdn.totvs.com/pages/viewpage.action?pageId=839303603)
  + [470 - BASE DE FGTS DIFERENÇA 13º INDENIZADO](https://tdn.totvs.com/pages/viewpage.action?pageId=839303616)

* FÓRMULA
  + [BASECALCULO](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719241)
* FAQ
  + [Apuração do FGTS na Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=839304283)
