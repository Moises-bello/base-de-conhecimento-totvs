---
article_id: 360024947511
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: b639fb9f7da235e145d286ee3210a975492c6841795f4da14632e2d9465f6216
fetched_at: '2026-06-28T22:37:21.416017+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Característica da Alçada
  por Entidades Contábeis em Contratos
type: support-article
updated_at: '2022-06-23T19:57:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024947511-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Caracter%C3%ADstica-da-Al%C3%A7ada-por-Entidades-Cont%C3%A1beis-em-Contratos
---

**Dúvida**Característica da Alçada por Entidades Contábeis em Contratos  
  
**Ambiente**Microsiga Protheus – Gestão de Contratos – A partir da versão 12.1.17  
  
  
**Solução**

Ao gerar um contrato com aprovação por entidade contábil, "Ent. Contabil" (CN1\_ALCCTR= 2), é gerado registro na tabela SCR e submetido a aprovação apenas revisões em que há alteração direta à entidade contábil (quantidade/valor). Porem alteração de fornecedor e cláusula, NÃO são submetidas a aprovação.   
Como realizar o bloqueio total do processo?

Este comportamento é o padrão utilizado pela rotina. A alçada somente será validada quando ocorrerem alterações de valores no contrato, caso negativo o processo continuará liberado.  
Como tratamento específico para este cenário, existe o ponto de entrada [MTALCPER](http://tdn.totvs.com/pages/viewpage.action?pageId=268571093).

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alçada Por Entidade Contábil na Mudança de Situação do Contrato e / ou Revisão do Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404552326039)

[MTALCPER - Ponto para customizar a Alçadas em documentos que não controlam alçadas por padrão](https://tdn.totvs.com/pages/viewpage.action?pageId=268571093)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
