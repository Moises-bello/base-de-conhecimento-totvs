---
article_id: 360025659713
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: a20134dc8de3f925e0421aaab74a25205a1372ccd026af42ebf422bc0be50f00
fetched_at: '2026-06-28T22:37:24.133328+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Revisão de Renovação
  de Contrato
type: support-article
updated_at: '2025-11-05T12:39:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025659713-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Revis%C3%A3o-de-Renova%C3%A7%C3%A3o-de-Contrato
---

**Dúvida**Revisão de Renovação para Adição de novos itens,Novas planilhas, preço unitário, prazo e condição de pagamento no contrato.

**Ambiente**Microsiga Protheus – Gestão de Contratos – A partir da versão 12

**Solução**

Nesse tipo de Revisão é permitido, atualizar a planilha existente do contrato,é permitido também adicionar novas planilhas, definir novas quantidades,preços, prazos, alteração da condição de pagamento ou um novo valor unitário negociado com o fornecedor ou cliente dos contratos vigentes.E reestruturar o cronograma financeiro após ajustes dos campos.

Obs: A revisão de Renovação não realinha medições já realizadas.

Passo a passo:

1. É necessário realizar a Inclusão do Tipo de Revisão **Acesse Atualizações > Cadastros > Tipos > Revisões(CNTA010)>Inclua a Revisão do Tipo C - Renovação** conforme print abaixo*:*

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040406733)

**Exemplo de Revisão**

**Dados inciais do contrato antes de Realizar a  Revisão de Renovação:**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039572454)

| Produto | Quantidade | Valor Unitário | Valor Total |
| --- | --- | --- | --- |
| GCT001 | 2 | 500 | 1000 |

* **Codição de Pagamento =** 001
* **Un.Vigência =** 2 - Meses

2. Na rotina Manutenção **CNTA300** selecione o contrato a ser revisado e clique em *Outras > Ações >Revisões>Renovação.*

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040405933)

3. Selecione no campo Tipo Revisão***(CN9\_TIPREV)*** cadastrado no passo 1.

Dessa forma será Habilitado para edição os campos do contrato:

-campo Quantidade**(*****CNB\_QUANT) -** Para que possa que possa alterar a quantidade da Planilha existente*

*-Valor unitário **(CNB\_VLUNIT)** -  Para que possa que possa alterar o campo preço da Planilha existente*

*-Un. Vigência**(CN9\_UNVIGE)** - Para que possa alterar a Vigência para meses dias ou anos.*

-Condição de pagamento***(CN9\_CONDPG)*** *Para que possa alterar a Condição de pagamento caso necessário*

**Continuação do Exemplo de Revisão**

No exemplo abaixo foi efetuado a  revisão de renovação da alteração e inclusão dos seguintes campos:

-Incluído o **novo Item** "GCT002" com **Quantidade** "1" e **Valor unitário** "1000"

-Foi alterado a **Condição de Pagamento** que antes estava preenchida "001" e ajustada para "30"

- Foi realizado a alteração de prazo ***Un. Vigência*** de "Meses" para "Anos".

- Foi realizado a alteração do campo Quantidade do Item "GCT001" que já estava existente no contrato de "2" para "4".

-Foi realizado a alteração do campo Preço do Item "GCT001" que já estava existente no contrato de "500" para "800".

Após relizar a Renovação o campo Quantidade**(*CNB\_QUANT*)** foi alterado para "04" e o campo Valor unitário **(*CNB\_VLUNIT*)** para "800" . Desta forma, o saldo total do item foi alterado para R$ 3200,00.

Nesse Tipo de Revisão também possível adicionar novos itens na planilha.No print abaixo demonstro como exemplo que foi incluso um novo "Produto GCT002" com Quantidade "1" e Valor unitário de "1000"

| Produto | Quantidade | Valor Unitário | Valor Total |
| --- | --- | --- | --- |
| GCT001 | 4 | 800 | 3200 |
| GCT002 | 1 | 1000 | 1000 |

Também  foi alterado o prazo no campo Un vigência(CN9\_UNVIGE)  para **Anos** e foi permitido alterar a **Condição de pagamento**no campo (CN9\_CONDPG) para 30.

* **Codição de Pagamento =** 30
* **Un.Vigência =** 3 - Anos

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040412633)

**Obs1:**Para que possa atualizar as informações do Cronograma financeiro automaticamente, após alterações realizadas ,segue procedimento abaixo:

Acesse a Aba **Parâmetros Revisão** >Marque as opções **Arrasto e Redist Val** ambas igual á "Sim".

Obs:Caso tenha Necessidade poderá também realizar o Acréscimo ou Decréscimo de parcelas no Campo destacado **Tipo conforme abaixo** é permitido que preencha com Acréscimo para adição de novas parcelas no cronograma já existe ou para ou descréscimo para exclusão de parcelas no cronograma.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36119434006423)

No **campo Quantidade** preencha com a Quantidade que deseja acrescentar ou excluir das parcelas do cronograma do contrato.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36119434009111)**

Após Adicionar ou Excluir parcelas é necessário clicar em **Outras Ações>Atualizar Cronograma Financeiro**, dessa forma o Cronograma existente será atualizado automaticamente com as alterações realizadas na Revisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36119411531799)

**Obs2:**Caso tenha necessidade também é permitido alterar o campo "Vigência" com a quantidade de dias , meses ou anos de acordo com o preechimento do campo *-Un. Vigência**(CN9\_UNVIGE)** - Para que possa alterar a Vigência para meses dias ou anos.*

**Obs3:**Caso ocorra o Help **CNTA300ND** ao Deletar Itens(Não medidos) do contrato , consulte o artigo a seguir - [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNTA300ND ao Deletar Itens(Não medidos) do contrato em Revisões?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28442693078807-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNTA300ND-ao-Deletar-Itens-N%C3%A3o-medidos-do-contrato-em-Revis%C3%B5es)

***Saiba Mais:***

[MP - SIGAGCT - Quais são os tipos de Revisão disponíveis, para revisar contratos no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNTA300ND ao Deletar Itens(Não medidos) do contrato em Revisões?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28442693078807-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNTA300ND-ao-Deletar-Itens-N%C3%A3o-medidos-do-contrato-em-Revis%C3%B5es)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
