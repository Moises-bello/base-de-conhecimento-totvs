---
article_id: 360013215531
category: SIGAEST - SALDOS
content_hash: ddba7041c87ca47e83597e70c5b913d7a65e10ebf0503dad973aa95538e8e6ac
fetched_at: '2026-06-28T22:39:14.784173+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito e utilização
  do parâmetro MV_TPSALDO no Estoque
type: support-article
updated_at: '2026-01-19T18:29:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013215531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-TPSALDO-no-Estoque
---

O parâmetro MV\_TPSALDO no Protheus define como o sistema calcula o saldo disponível em estoque, influenciando rotinas de vendas e movimentações. Possui três opções: Q (saldo simplificado), S (função SaldoSB2, que considera reservas e empenhos) e C (função CalcEst, que projeta saldo baseado na data-base). Parâmetros como MV\_SLDEMPE e MV\_SLDRESE refinam esse cálculo, especialmente em faturamento.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37782926523927) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como o ***parâmetro MV\_TPSALDO*** define como o sistema deve calcular o saldo disponível dos produtos no estoque?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O parâmetro **MV\_TPSALDO** é fundamental para determinar como o Protheus calcula o saldo disponível em estoque dentro da função **SaldoMov**. Este cálculo impacta diversas rotinas do sistema, definindo a disponibilidade de itens para empenhos, vendas e movimentações.

### **Opções do Parâmetro MV\_TPSALDO**

O comportamento do sistema varia conforme a letra atribuída ao parâmetro:

| **Opção** | **Método de Cálculo** | **Descrição Resumida** |
| --- | --- | --- |
| **Q** | **Saldo Simplificado** | Considera apenas: Saldo Atual (`B2_QATU`) - Qtd. a Endereçar (`B2_QACLASS`) - Reservas de PV (`B2_RESERVA`). |
| **S** | **Função SaldoSB2** | Baseia-se no Saldo Atual (`B2_QATU`) menos empenhos e reservas, somando/subtraindo saldos de terceiros. |
| **C** | **Função CalcEst** | Semelhante à opção **S**, porém utiliza a função `CalcEst`, que projeta o saldo retroativo ou atual com base na **Data-Base** do sistema. |

### **Fórmulas Detalhadas**

#### **A. Função SaldoSB2 (Opção S)**

A disponibilidade é calculada da seguinte forma:

> Saldo SB2 = B2\_QATU - B2\_RESERVA - B2\_QEMP (SD4) - B2\_QACLASS - B2\_QEMPSA - B2\_QEMPPRJ - B2\_QTNP + B2\_QNPT - B2\_QEMPPRE
>
> \*O campo B2\_QEMPPRE só é subtraído se o parâmetro **MV\_QTDPREV** estiver ativo.

#### **B. Função CalcEst (Opção C)**

Utiliza a reconstrução de saldo na data-base:

> CalcEst = Retorno CalcEst - B2\_RESERVA - B2\_QEMP (SD4) - B2\_QACLASS - B2\_QEMPSA - B2\_QTNP - B2\_QEMPPRE
>
> \*O campo B2\_QEMPPRE só é subtraído se o parâmetro **MV\_QTDPREV** estiver ativo.

### **Parâmetros Relacionados (Condicionais)**

O comportamento das opções **S** e **C** pode ser refinado pelos parâmetros abaixo:

#### [**MV\_SLDEMPE**](https://tdn.totvs.com/pages/viewpage.action?pageId=312165062#:~:text=IENE-,MV_SLDEMPE,-Verifica%20se%20n%C3%A3o) (Com uso do `MV_TPSALDO = C`)

Define a consideração de empenhos de OP (campo `B2_QEMP`) especificamente na rotina de **Movimentos Internos (MATA241)**.

* **S:** Não subtrai o empenho do saldo disponível.
* **N:** Subtrai o empenho (comportamento padrão).

#### [**MV\_SLDRESE**](https://tdn.totvs.com/x/Tg8pM)

É importante conceitar que o uso do **MV\_TPSALDO** e **MV\_SLDRESE** tem um comportamento diferente para regras no FATURAMENTO, sendo elas conforme boletim a seguir:

[Parâmetro MV\_SLDRESE = N não ignora Reserva na Avaliação de Saldo](https://tdn.totvs.com/x/Tg8pM)

Dúvidas sobre a validação de saldos disponiveis para "Faturar pedido de venda", deve-se validar juntamente ao time Faturamento.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)

[*Consulta F4 dos Saldos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto-)
