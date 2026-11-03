---
article_id: 360018809411
category: PCO - Integrações
content_hash: 38c5a2c7b2b962159c3def7c84a54cf9cb3675f3402401d70452a16ccbe55945
fetched_at: '2026-06-28T22:37:10.152660+00:00'
product: protheus
section_id: 1500001550902
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA030 Quais são as
  Rotinas que possuem integração com o Módulo PCO ?
type: support-article
updated_at: '2023-11-21T13:12:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018809411-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA030-Quais-s%C3%A3o-as-Rotinas-que-possuem-integra%C3%A7%C3%A3o-com-o-M%C3%B3dulo-PCO
---

**Dúvida**Quais são as Rotinas que possuem integração com o Módulo PCO?

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
   
**Solução**

Para que seja possível identificar as possíveis rotinas que possuem integração com o módulo 57-Planejamento e Controle Orçamentário (PCO), acesse a Rotina **PCOA030 - Lançamentos Por Processo**

Dentro dessa rotina, temos a coluna **FUNÇÃO** ao qual informa o código da Rotina que possui Integração com o módulo PCO.

**Exemplo*:***

**Código:** 000052

**Descrição:** Pedido de Compra

**Função**: MATA121

**Exibe Lanto :** Sim/Não

Neste exemplo a Rotina **MATA121** possui a chamada (internamente no Fonte) para o processo de integração com o Módulo PCO
