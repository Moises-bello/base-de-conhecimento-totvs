---
article_id: 360035637173
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 93b60b197b84bca5223725cf70f398ae4ba3a4b6dccc2f03453738383f86fcda
fetched_at: '2026-06-28T22:37:24.087541+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Qual a finalidade da
  Revisão de Readequação nos contratos ?
type: support-article
updated_at: '2024-03-08T11:42:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035637173-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Qual-a-finalidade-da-Revis%C3%A3o-de-Readequa%C3%A7%C3%A3o-nos-contratos
---

**Dúvida**Qual a finalidade da Revisão de Readequação nos contratos ?

**Ambiente**Microsiga Protheus  – Gestão de Contratos – A partir da versão 12  
  
**Solução**

A revisão de readequação consiste na alteração das quantidades dos itens, sem que o montante da planilha se altere. Em uma revisão de readequação não é permitida a alteração do valor unitário dos itens, porém devido a alteração das quantidades o valor total do item é alterado. Apenas o valor total da planilha não deve ser alterado.

Verifique os cadastros a seguir:

1. Ao realizar revisão de readequação, alterar a quantidade do item a ser reajustado. Com a readequação, sendo alterada a quantidade, o valor total será alterado, mudando o valor do contrato. Para que o contrato volte a ficar com seu valor inicial, conforme determina o tipo de revisão, será preciso alterar a quantidade de outros itens, até que o valor fique conforme o original.
2. Para cadastrar o tipo da revisão para ser vinculada ao contrato acesse: *Atualizações>Tipos>Revisões(CNTA010)>Incluir.*

**Cadastro do tipo de Revisão**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046590333)

3. Na rotina Manutenção**(CNTA300)** clique em *outras ações>Revisão>Readequação*

 No campo Tipo de Revisão**(CN9\_TIPREV)** selecione o tipo da revisão cadastrada no passo 2

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045733174)

Será habilitado os campos de quantidade para readequar o contrato sem que haja alteração no valor.

**Exemplo**

Contrato antes da revisão

Quantidade do item 001 - **3**

Quantidade do item 002 - **9**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046591913)

Valor atual do contrato**(CN9\_VLATU)** , Valor total**(CNA\_VLTOT)** e saldo da planilha**(CNA\_SALDO)** e montante do cronograma = **21.000,00**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046592073)

*Contrato Revisado*

Foi Alterado a quantidade dos itens sem que alterasse o valor total da planilha e o montante do cronograma.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046593693)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045735994)

***Além das quantidades poderá ser readequado o valor das parcelas do cronograma.***

O campo Valor.Prev.Parc**(CNF\_VLPREV)** será habilitado para edição poderá ser alterado os valores das parcelas sem que altere o valor do montante de seu cronograma e o valor total da planilha do contrato.

Exemplo da revisão de readequação das parcelas para o contrato acima

*Valores do Cronograma antes da revisão*

Valor.Prev.Parc**(CNF\_VLPREV)** de todas as parcelas - **2.100,00**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045736774)

*Valores do Cronograma Após a Revisão*

Valor.Prev.Parc**(CNF\_VLPREV)** 5 parcelas ajustei com o valor de **2.000,00**e as outras 5 com o valor de **2.200,00**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046594573)

**Observação:**

Caso possua parcelas do cronograma financeiro que foram medidas com valores parciais dos informados no cronograma, ao atualizar o cronograma financeiro essas parcelas serão readequadas com os valores que foram medidos e o saldo restante será redistribuído entre as parcelas em aberto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21908140041367)

Após atualização do cronograma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21908147207575)

***Saiba Mais:***

[MP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334-MP-SIGAGCT-Tipos-de-Revis%C3%A3o) [- SIGAGCT - Quais são os tipos de Revisão disponíveis, para revisar contratos no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334-MP-SIGAGCT-Tipos-de-Revis%C3%A3o)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
