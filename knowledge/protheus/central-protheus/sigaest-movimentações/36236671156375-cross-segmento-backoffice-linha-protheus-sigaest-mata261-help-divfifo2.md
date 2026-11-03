---
article_id: 36236671156375
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 678cf83dc929c7ed73c6221f2da8ff57e61b4c6d465240ea84137f8539ab5306
fetched_at: '2026-06-28T22:38:57.050532+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA261 HELP DIVFIFO2
type: support-article
updated_at: '2025-11-10T21:51:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36236671156375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-HELP-DIVFIFO2
---

A rotina MATA261 no TOTVS Protheus não esta realizando movimentações que gerem divergências no custo FIFO On-Line, apresentando o erro HELP DIVFIFO2 quando não há saldo suficiente na camada FIFO mais antiga. Para resolver, ajuste o saldo FIFO disponível, o conceito de uso é via parâmetro MV\_CUSFIFO e pode-ser usar a rotina movimento interno (MATA241) para acerto de saldos caso não esteja desbalanceado.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36236676346519) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Validação de Custo FIFO On-Line impedindo a movimentação na rotina MATA261 com a apresentação do HELP DIVFIFO2. A movimentação não será realizada pois irá gerar divergência de saldos no custo FIFO On-Line.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Ajuste o saldo FIFO disponivel, caso voce de fato utilize o conceito FIFO, através do parametro MV\_CUSFIFO, utilizando movimento interno (MATA241).

A rotina MATA261 é utilizada para realizar a transferência de produtos entre almoxarifados. Quando o sistema está configurado para utilizar o método de custeio [FIFO](https://tdn.totvs.com/x/b_DuOQ) (First In, First Out) On-Line (conforme a função `IsFifoOnLine()`), (MV\_CUSFIFO Ativo) ele executa uma validação para garantir que a movimentação não crie divergências negativas ou inconsistências nos saldos por camada FIFO.

### **O HELP DIVFIFO2 é apresentado quando esta validação falha.**

Ao tentar confirmar a movimentação na MATA261, o usuário se depara com a mensagem:

> **AJUDA:DIVFIFO2**
>
> **A movimentação não será realizada pois irá gerar divergência de saldos no custo FIFO On-Line.**

A causa principal é a indisponibilidade de saldo suficiente na camada FIFO correta (a camada mais antiga) para a quantidade solicitada.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Tratamento correto de desbalanceamento de tabelas de Lote e Endereço em todos os cenários*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402491211159)
