---
article_id: 28500805878039
category: Financeiro - Contas a Receber
content_hash: 7d7032daf4dae2d544f9660f12ad5ab66701ef1513fcba59eda6d7a57ba7eace
fetched_at: '2026-06-28T22:38:12.504758+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA040 - Diferença
  entre RA (Recebimento Antecipado) x NCC (Nota de Crédito do Cliente)
type: support-article
updated_at: '2024-12-13T13:34:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28500805878039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Diferen%C3%A7a-entre-RA-Recebimento-Antecipado-x-NCC-Nota-de-Cr%C3%A9dito-do-Cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28500834427159) Tempo aproximado para leitura: **00:08min** **Dúvida**Caso crie ou gere uma NCC no financeiro, será criada uma movimentação bancária correspondente?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA040 - Todas as versões  
  
**Solução**

Diferença entre **RA (Recebimento Antecipado)** x **NCC (Nota de Crédito do Cliente)**

Enquanto a **RA (Recebimento Antecipado)** gera movimentação bancária automaticamente no momento de sua criação, a **NCC (Nota de Crédito do Cliente)** possui um comportamento diferente.

Quando uma **NCC** é criada diretamente no financeiro ou gerada a partir de uma devolução de nota, o sistema **não gera movimentação bancária**, pois considera que esse valor já foi pago durante a baixa do título original.

Para tratar a **NCC**, existem as seguintes opções:

1. **Baixa da NCC com saída bancária**  
   Caso o título já tenha sido baixado e uma devolução tenha gerado a NCC, é possível realizar uma baixa da NCC. Essa ação irá gerar uma movimentação de saída no extrato bancário, simulando um pagamento.
2. **Compensação com outra nota do cliente**  
   A NCC pode ser compensada com outra nota em aberto do mesmo cliente, ajustando os valores pendentes sem a necessidade de movimentação bancária.
3. **Compensação com a nota em aberto**  
   Caso a nota original ainda esteja em aberto e haja a necessidade de devolução, é possível realizar a compensação da **NF** com a **NCC**, evitando que o movimento permaneça em aberto.

**Saiba mais**

[Compensação contas a receber- FINA330 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=505768648)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA070 - Gerar movimento bancário ao baixar NCC ou RA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025846812-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Gerar-movimento-banc%C3%A1rio-ao-baixar-NCC-ou-RA)
