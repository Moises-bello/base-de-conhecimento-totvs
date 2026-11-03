---
article_id: 9451094240151
category: ADVPL - Ponto de Entrada
content_hash: 395a8e13092b018b72fe2f68a7a033cab509faeaf9e8179378ccd54f21d76a01
fetched_at: '2026-06-28T22:40:12.982935+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAPCO - Ponto de entrada -
  PCOA5301 - Texto padrão
type: support-article
updated_at: '2023-01-12T14:56:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9451094240151-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAPCO-Ponto-de-entrada-PCOA5301-Texto-padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min****Dúvida**Ponto de Entrada para edição do texto padrão na tela de contingencia  - PCOA5301 - Texto padrão  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPCO - Todas as versões  
  
**Solução**Ponto de entrada: PCOA5301

O Ponto de entrada PCOA5301 serve para manipular o texto padrão do bloqueio orçamentário, quando o controle de saldos de contingência estiver ativo.

**PoC**

```
#include"protheus.ch"  
  
UserFunctionPCOA5301()  
  
    LocalcTxt:=ParamIXB[1]  
  
    LocalaDadosBlq:=ParamIXB[2]  
  
    cTxt+="teste do ponto de entrada PCOA5301() "  
  
Return(cTxt)
```

Exemplo:

Saiba mais:  
[PCOA5301 - Texto padrão](https://tdn.totvs.com/pages/releaseview.action?pageId=6073549)

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO - CheckList para utilização do modulo Planejamento de Custos Orçamentários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038998854-MP-SIGAPCO-CheckList-para-utiliza%C3%A7%C3%A3o-do-modulo-Planejamento-de-Custos-Or%C3%A7ament%C3%A1rios)

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO Utilização de Contingência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018523352-MP-SIGAPCO-Como-utilizar-a-conting%C3%AAncia-no-m%C3%B3dulo-PCO-)
