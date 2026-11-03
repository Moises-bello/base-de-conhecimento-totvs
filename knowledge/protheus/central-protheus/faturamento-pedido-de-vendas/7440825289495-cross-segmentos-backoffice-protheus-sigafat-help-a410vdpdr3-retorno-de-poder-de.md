---
article_id: 7440825289495
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: bac616b3cca04a3d8ede99df157f5c4888640645ad5263eef9c353b5a7ab8100
fetched_at: '2026-06-28T22:38:39.827033+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help A410VDPDR3, retorno
  de Poder de Terceiros
type: support-article
updated_at: '2026-03-19T14:44:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7440825289495-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A410VDPDR3-retorno-de-Poder-de-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39153623373079) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao realizar o retorno de Poder de Terceiros pelo Pedido de Vendas é apresentado o **Help A410VDPDR3.**  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O **Help A410VDPDR3** é apresentado quando o valor unitário informado no Pedido de Venda (campo **C6\_PRCVEN**) está divergente do valor unitário registrado no documento de entrada de origem (campo **B6\_PRUNIT**).

Essa validação é realizada pelo sistema sempre que a TES utilizada estiver configurada como retorno de Poder de Terceiros, ou seja, quando o campo F4\_PODER3 estiver definido como “D” (Devolução).

Nessa situação, o sistema garante a consistência dos valores entre a operação de entrada e o retorno, não permitindo diferenças entre os valores unitários informados.

Para solucionar este incidente, você possui duas alternativas:

**1.** **Igualar os valores:**  
Realizar o ajuste do **valor unitário no Pedido de Venda (C6\_PRCVEN)** para que esteja **idêntico ao valor unitário do documento de entrada de origem (B6\_PRUNIT)**, garantindo a consistência exigida pelo sistema na validação.

**2.** **Permitir valor inferior por meio de parâmetros:**  
Caso a operação exija a **informação de um valor unitário inferior no Pedido de Venda** (por exemplo, em cenários de inclusão com **quantidade total da remessa e saldo financeiro reduzido**), será necessário **ajustar os parâmetros correspondentes no sistema**, de forma a permitir essa flexibilização na validação.

* **MV\_BLOQSB6**: Altere o conteúdo para **.F.** (Este parâmetro bloqueia a digitação de um valor diferente do campo de origem B6\_PRUNIT).
* **MV\_LIBESB6**: Altere o conteúdo para **.T.** (Este parâmetro permite a inclusão da nota com saldo financeiro a menor).

**Observação:** Mesmo com as alterações de parâmetros (MV\_BLOQSB6 = .F. e MV\_LIBESB6 = .T.), **não é possível** informar um valor unitário **maior** do que o registrado no documento de entrada original.  
  
**Saiba Mais:** [**Ajustes de Mensagens de Help do Pedido de Venda**](https://tdn.totvs.com/x/cgSJJw)
