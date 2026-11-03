---
article_id: 27421281374615
category: Financeiro - Novo Gestor Financeiro
content_hash: 38e06c56ff78789150027a2309ce13bb437e2a67f613ba681f13458252f20b28
fetched_at: '2026-06-28T22:37:41.583760+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA718 - Baixas via
  API não apresentam no Extrato bancário e Conciliação Bancária
type: support-article
updated_at: '2026-01-07T14:23:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27421281374615-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA718-Baixas-via-API-n%C3%A3o-apresentam-no-Extrato-banc%C3%A1rio-e-Concilia%C3%A7%C3%A3o-Banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27421281353879) Tempo aproximado para leitura: **00:10:00 min****Duvida**  
Ao realizar a baixa via API de Pagamentos (FINA718), por qual motivo não apresentam as movimentações no Extrato Bancário (FINR470) e Conciliação Bancária (CTBA940) ou (FINA380)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir do release 12.1.2310

**Solução**A baixa foi gerada com o campo**E5\_MOTBX = NOR e E5\_TIPODOC =** **BA**com isso não apresenta no Extrato Bancário e Conciliação, devido a configuração do Retorno em **Configuração de Contas >> Baixas titulos (Retorno)**, onde o motivo da baixa está igual a **NOR - NORMAL**  
  
Realize os seguintes passos para solucionar:  
1. Acesse a rotina **FINA710 - Novo Gestor Financeiro**   
2. Altere a Conta em **Configuração de Contas**  
3. Em Outras Ações >> **Baixa Títulos (Retorno)**, apague o conteúdo atual e coloque o motivo de baixa para **DEB - Debito CC**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27421281355159)  
  
**Saiba mais**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA080 - E5\_TIPODOC = BA na baixa pagar Normal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052125413-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA080-E5-TIPODOC-BA-na-baixa-pagar-Normal)  
[Contas a pagar (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=734394071)
