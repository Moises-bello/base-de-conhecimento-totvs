---
article_id: 34437716855063
category: SIGAEST - SALDOS
content_hash: 30eaebf29a1ab3900c443511c9a5e98085d5669b397256103193cfedcab5a404
fetched_at: '2026-06-28T22:39:14.955887+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST- Como funciona o Empenho
  de lote vencido ?
type: support-article
updated_at: '2025-08-26T13:20:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34437716855063-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-funciona-o-Empenho-de-lote-vencido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34437709842583) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como é gerado o empenho de lotes vencidos na SB8, campo B8\_EMPENHO?  
  
**Ambiente**  
Cross Segmento – TOTVS Backoffice (Linha Protheus) – Estoque/Custos – Todas as versões  
  
**Solução**  
O saldo empenhado de lote vencido, sera gerado em decorrencia do uso da função Proclote configurada, e demais parametros conforme boletim:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA275 - Lote vencido, como posso Movimentar ou Inventariar produto com Lote Vencido que está bloqueado?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025875571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA275-Lote-vencido-como-posso-Movimentar-ou-Inventariar-produto-com-Lote-Vencido-que-est%C3%A1-bloqueado)

É importante ressaltar que o lote não sera empenhado caso exista saldo a ser endereçado, ou seja, o produto possuir saldo a ser classificado no campo **B8\_QACLASS**, nesse caso é necessario distribuir o saldo a ser endereçado primeiro.

Caso seja feita a distribuição, e o pergunte da rotina **MATA265 > F12 > "Bloqueia a data de validade = Sim", Ao sair da rotina, sera processado a função Proclote na filial, e então o saldo que foi enderçado no lote vencido, sera automaticamente empenhado, seja o total ou parcial.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34438250990103)

**Atenção:** O parametro **MV\_DATALOT** por padrão é um parametro compartilhado, e esse parametro é alimentado com a data de acesso do usuario ao abrir o protheus e acessar qualquer rotina, assim sera gravado a data no parametro, e atualizado os lotes vencidos "**Na filial Logada**", dessa forma caso voce queira efetuar o controle para demais filiais, sugerimos o uso do parametro **MV\_DATALOT** cada um para sua respectiva Filial.

**IMPORTANTE:** A função **PROCLOTE** processa "na filial logada" e não em todas as filiais.

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações de Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
