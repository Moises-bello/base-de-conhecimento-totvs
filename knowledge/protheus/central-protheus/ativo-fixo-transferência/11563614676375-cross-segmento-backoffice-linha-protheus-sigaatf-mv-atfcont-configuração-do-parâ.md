---
article_id: 11563614676375
category: Ativo Fixo - Transferência
content_hash: 894a03dac7c093487ff52879a16190426d9f60dee6373bfc4dec4c8f9b0d3b87
fetched_at: '2026-06-28T22:41:52.203630+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - MV_ATFCONT – Configuração
  do parâmetro para cálculos do Ativo Online ou Offline
type: support-article
updated_at: '2023-11-22T12:42:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11563614676375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-MV-ATFCONT-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-para-c%C3%A1lculos-do-Ativo-Online-ou-Offline
---

**Dúvida**

Como configurar o parâmetro MV\_ATFCONT na Contabilização das movimentações de Cálculos do Ativo Fixo, quais rotinas são impactadas na habilitação do mesmo.  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**

Ao configurar o parâmetro MV\_ATFCONT é determinado se as rotinas referentes as movimentações irão ser contabilizadas online ou Offline, esta configuração se aplica as rotinas de Baixa e Calculo Mensal

Baixas (ATFA036)  
Ao configurar o parâmetro MV\_ATFCONT como N – Offline ou O - Online, as rotinas de baixa poderão ser executadas.

Cálculo Mensal (ATFA050)  
Ao configurar o parâmetro MV\_ATFCONT como N – Offline ou O - Online, a rotina de cálculo mensal poderá ser executada normalmente e todas as movimentações também são aplicadas a esta rotina.

Saiba mais:

* [Não processa o calculo de depreciação mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019761431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-N%C3%A3o-processa-o-calculo-de-deprecia%C3%A7%C3%A3o-mensal?source=search)
* [ATFA050 Valores duplicados na contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006600272-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Valores-duplicados-na-contabiliza%C3%A7%C3%A3o?source=search)
* [Porque o sistema não calcularia a depreciação de um bem?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018327952--Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Porque-o-sistema-n%C3%A3o-calcularia-a-deprecia%C3%A7%C3%A3o-de-um-bem-?source=search)
