---
article_id: 360061468714
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: fb0a5b71501fd629bcf1d6c72e3520399a4ddbe65971cd56e6b3a7f237df147d
fetched_at: '2026-06-28T22:38:38.681592+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - C6_NOTA
  não preenche ao eliminar resíduo
type: support-article
updated_at: '2026-05-15T16:30:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061468714-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-C6-NOTA-n%C3%A3o-preenche-ao-eliminar-res%C3%ADduo
---

**Dúvida**Ao eliminar resíduo de um pedido faturado parcial, o campo **C6\_NOTA** não é preenchido ao eliminar o resíduo.  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Solução**

No padrão do módulo Faturamento, quando há eliminação de resíduo no pedido de vendas (**MATA410**), o campo **C5\_NOTA** será marcado com **XXXXXX** e o campo **C6\_BLQ** será marcado como **"R"** ,porém, o campo **C6\_NOTA** não é marcado com **XXXXXX** permanecendo em branco, pois a indicação da linha de item que houve eliminação de resíduo é apenas o campo **C6\_BLQ** com a letra "**R" (Resíduo)**.

Exemplo:

Em um pedido parcialmente faturado e com eliminação de resíduo, o item faturado apresentará o número da nota e o item eliminado resíduo ficará em branco conforme a imagem abaixo:  
  
![elimina__o_de_res_suo_c6-nota.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003045921/elimina__o_de_res_suo_c6-nota.png)

​  
Perceba que o pedido 000047 teve seu Item 01 faturado, apresentando o número da nota 000149 série 1, já o item 02 como foi eliminado resíduo, apresenta o campo de nota no item em branco e o campo **C6\_BLQ** com **"R"**.

A marcação do X será efetuada apenas no campo **C5\_NOTA** do pedido 000047.

**Saiba mais:**

[**Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Como preencher os campos C5\_NOTA e C5\_SERIE**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018332432-MP-FAT-Como-preenche-os-campos-C5-NOTA-e-C5-SERIE?source=search)

[**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - (Outras Ações - Excluir - Resíduo), quando há reserva vinculada**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016173951-MP-FAT-Como-eliminar-Res%C3%ADduo-do-Pedido-de-Venda-mata410-selecionado-Outras-A%C3%A7%C3%B5es-Excluir-Res%C3%ADduo-quando-h%C3%A1-reserva-vinculada)

[**Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Qual o procedimento para reativar pedidos residuados**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015651047-MP-FAT-Qual-o-procedimento-para-reativar-pedidos-residuados)
