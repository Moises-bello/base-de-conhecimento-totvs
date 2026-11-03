---
article_id: 37527514739735
category: Financeiro
content_hash: 2b9b1d80500574fe3629a58e762aca14c6f6811e1eba94fad0df43ae08f08384
fetched_at: '2026-06-28T22:38:01.161354+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - FINA430 – O retorno
  CNAB pode realizar a baixa de títulos sem gerar movimentação bancária?
type: support-article
updated_at: '2026-01-08T12:58:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37527514739735-Cross-Segmentos-Backoffice-Linha-Protheus-Financeiro-FINA430-O-retorno-CNAB-pode-realizar-a-baixa-de-t%C3%ADtulos-sem-gerar-movimenta%C3%A7%C3%A3o-banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37527514727703) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
FINA430 – O retorno CNAB pode realizar a baixa de títulos sem gerar movimentação bancária?

**Ambiente**  
Exemplo:  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Até o momento (01/2026), não existe um ponto de entrada específico no Protheus do módulo Financeiro para alterar o motivo de baixa dos títulos no retorno de CNAB.

Caso o motivo de baixa seja alterado via ponto de entrada que não foi desenvolvido para essa finalidade e essa configuração do motivo de baixa esteja configurada para não gerar a movimentação bancária (ex.: E5\_TIPODOC = BA).

Informamos que o retorno do CNAB ainda assim realizará a movimentação bancária, respeitando o conceito padrão do CNAB enviado pelo banco.

Pois se o título foi enviado através do CNAB e o retorno não teve rejeição e não seja entrada confirmada, obrigatoriamente o CNAB entende que houve uma movimentação bancária associada
