---
article_id: 360038386133
category: Financeiro - Recálculos
content_hash: 5fc3b0dfd406ee02c9a05f5ba2fe83278a545aa631ad480404317ab14c01dc8f
fetched_at: '2026-06-28T22:38:20.145806+00:00'
product: protheus
section_id: 1500001550362
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Aglutinação dos títulos
  de Impostos
type: support-article
updated_at: '2025-11-27T17:10:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038386133-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Aglutina%C3%A7%C3%A3o-dos-t%C3%ADtulos-de-Impostos
---

**Dúvida**  
Como aglutinar imposto no Módulo Financeiro?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
As rotinas abaixo fazem a aglutinação de imposto:  
  
**FINA376** para aglutinar impostos de **IRRF**.  
**FINA378** para aglutinar impostos de **PCC**.  
**FINA381** para aglutinar todos os impostos. **IRRF, PIS, COFINS e CSLL**  
**FINA870** para aglutinação de Títulos **INSS**

**FINA382** para aglutinação de títulos de impostos gerados pelo configurador de tributos?   
  
No padrão, o PROTHEUS do módulo FINANCEIRO não disponibiliza uma rotina para aglutinação de imposto **ISS.**

**Saiba Mais**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA870 - Como gerar Aglutinação de títulos de INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016141732)  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA376 - Aglutinação de TXA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033261114)  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA378 - É possível aglutinar títulos dos impostos PIS/COFINS/CSLL pela data de vencimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022030252)

[Aglutinador de Impostos do Configurador de Tributos - FINA382](https://tdn.totvs.com/display/public/PROT/Aglutinador+de+Impostos+do+Configurador+de+Tributos+-+FINA382)

[**INSTRUÇÃO NORMATIVA SRF Nº 96, DE 27 DE NOVEMBRO DE 2001**](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=anotado&idAto=14554)

<http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=compilado&idAto=14554>
