---
article_id: 35702975377687
category: Financeiro - Contas a Pagar - Comunicação Bancária Online
content_hash: f81c8312a3a0c8a3db3d82f44f312b226e13bd6e5c903c90bf7e891e8cde28e7
fetched_at: '2026-06-28T22:37:49.905795+00:00'
product: protheus
section_id: 26656222001687
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA717 - Erro na transmissão
  no monitor de pagamento
type: support-article
updated_at: '2025-10-17T19:24:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35702975377687-Cross-Segmento-Backoffice-Linha-Protheus-FINA717-Erro-na-transmiss%C3%A3o-no-monitor-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35702950571799) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Erro na transmissão no monitor de pagamentos.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
O erro ocorre porque o **JSON** apresenta a tag de transferência com informações vazias, sendo esta a causa da falha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35702975366679)

Para auxiliar na identificação do **JSON**, disponibilizamos a seguinte documentação:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Como buscar as informações do Json após executar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451382489495-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Como-buscar-as-informa%C3%A7%C3%B5es-do-Json-ap%C3%B3s-executar-o-schedule?source=search)

Neste caso, é necessário validar o **layout**, certificando-se de que o **campo de transferência** contenha corretamente os dados do banco e da conta no **Novo Gestor Financeiro**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35702975367191)

**Saiba mais**

[Financeiro - Contas a Pagar - Comunicação Bancária Online](https://centraldeatendimento.totvs.com/hc/pt-br/sections/26656222001687-Financeiro-Contas-a-Pagar-Comunica%C3%A7%C3%A3o-Banc%C3%A1ria-Online)
