---
article_id: 360015222851
category: Contabilidade Gerencial - Rateio
content_hash: ff230113641c608561f6322a4db91b23830aad97fd2e01c49ad8fef354f97f38
fetched_at: '2026-06-28T22:40:35.553660+00:00'
product: protheus
section_id: 1500001548962
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Rotina CTBA281
type: support-article
updated_at: '2022-05-23T20:30:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015222851-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Rotina-CTBA281
---

**Dúvida**Qual a funcionalidade da rotina Rateio por Combinações (CTBA281)?  
   
 **Ambiente**Protheus – Contabilidade – A partir da versão 11.80  
  
   
**Solução**A rotina de **Rateio por Combinações (CTBA281)**,calcula os rateios *off-lines* cadastrados na tabela CTQ, tomando por base a entidade do lançamento se estiver em branco no rateio.

Inicialmente a rotina filtra as entidades informadas no cadastro do rateio tabela CTQ **(CTBA270)**. Os parâmetros abaixo informados pelo usuário antes da execução da rotina são desconsiderados caso as entidades (Conta, Centro de Custo, Item, Classe Valor) estejam preenchidas na tabela CTQ.  Caso as entidades estejam em branco no rateio, o sistema considera a parametrização abaixo informada no início da execução da rotina:

mv\_par12 ||Conta Origem Inicial

mv\_par13 ||Conta Origem Final

mv\_par14 ||C.Custo Origem Inicial

mv\_par15 ||C.Custo Origem Final

mv\_par16 ||Item Origem Inicial

mv\_par17 ||Item Origem Final

mv\_par18 ||Cl.Valor Origem Inicial

mv\_par19 ||Cl.Valor Origem Final

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba281_rateio_off_line_combinacoes.htm>
