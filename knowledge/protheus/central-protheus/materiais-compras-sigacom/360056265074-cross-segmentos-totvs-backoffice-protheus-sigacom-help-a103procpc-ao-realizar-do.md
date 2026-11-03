---
article_id: 360056265074
category: Materiais - Compras (SIGACOM)
content_hash: 109ab00c549719190aa68f54d0d0d9e78050120107a1a4a36325d27c40c4747b
fetched_at: '2026-06-28T22:41:18.836784+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A103ProcPC ao
  realizar Documento de Entrada
type: support-article
updated_at: '2022-05-18T20:56:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056265074-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A103ProcPC-ao-realizar-Documento-de-Entrada
---

**Ocorrência**Help A103ProcPC ao realizar Documento de Entrada  
  
**Ambiente**  
Microsiga Protheus – Compras – A partir da versão 12  
  
**Causa**

* O sistema pode apresentar o alerta quando não identifica o produto da filial consultada;
* Também pode ocorrer quando há alteração de compartilhamento da tabela SB1 e não efetuado ajuste do campo **B1\_FILIAL** do cadastro de sua tabela SB1 TOP de acordo com o compartilhamento que foi alterado.

**Solução**  
1. Exemplo de compartilhamento da SB1 antes da alteração do compartilhamento.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097797313/mceclip0.png)

Exemplo do campo **B1\_FILIAL** com conteúdo **D MG** do cadastro de produto **AGULHA02** antes da alteração de compartilhamento

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095493714/mceclip1.png)

2. Foi realizado a mudança no compartilhamento da tabela SB1

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097800393/mceclip2.png)

Não foi realizado o ajuste dos registros antigos do campo **B1\_FILIAL** no exemplo do produto **AGULHA02** continuou com **D MG**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095493714/mceclip1.png)

Exemplo Pedido de Compra

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095495894/mceclip4.png)

Tentativa de Vincular o Pedido de Compra no Documento de Entrada.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097801053/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097801693/mceclip6.png)

Ao tentar vincular um Pedido de Compra na Pré-Nota**(MATA140)** ou Documento de Entrada**(MATA103)**de um Produto que não foi ajustado o campo **B1\_FILIAL** para o devido compartilhamento será apresentado o Help A103ProcPC

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097800733/mceclip3.png)**

3. Após ajustar o campo B1\_FILIAL de acordo com o compartilhamento que foi alterado, o Help não foi apresentado e o pedido foi vinculado ao Documento de entrada.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097801813/mceclip7.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097801053/mceclip5.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095496874/mceclip8.png)

**Observação:** Qualquer ajuste ou alteração na base ou compartilhamento deverá ser realizado por um especialista/consultor com conhecimento em base/apsdu e qualquer ajuste realize em ambiente de teste com backup.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
