---
article_id: 20714762958615
category: Financeiro - Viagens
content_hash: b7ffa001e86977c4c8826c31fa5a0a3b64bf34725dc3bbb8bafca646e53502c9
fetched_at: '2026-06-28T22:38:21.323608+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAFIN - FINA677 - AJUDA:OBRIGAT
  Falha na gravação automática do título
type: support-article
updated_at: '2024-01-22T19:26:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20714762958615-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA677-AJUDA-OBRIGAT-Falha-na-grava%C3%A7%C3%A3o-autom%C3%A1tica-do-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20714762935191) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a liberação do financeiro da prestação de contas em moeda diferente do real, ocorre a mensagem **AJUDA:OBRIGAT Falha na gravação automática do título.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20714702131991)**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a Pagar - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a data base utilizada para a liberação do financeiro não possui taxa da moeda (MATA090), cadastrada no dia.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina Moedas (**MATA090**) e cadastrar a taxa da moeda para o dia que está sendo realizado a Liberação para Financeiro.   
2. Feche a rotina **Prestação de Contas** (**FINA677**).  
3. Realize a Liberação para Financeiro, veja que o título será gerado fazendo a conversão da taxa.

**Saiba mais**  
**[Viagens - Financeiro - P12](https://tdn.totvs.com/display/PROT/Viagens+-+Financeiro+-+P12)**
