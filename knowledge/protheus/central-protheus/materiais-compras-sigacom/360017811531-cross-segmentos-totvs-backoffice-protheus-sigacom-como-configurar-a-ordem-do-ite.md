---
article_id: 360017811531
category: Materiais - Compras (SIGACOM)
content_hash: 66cfa41bda147da4175ef47caf7487c3936bb8baef941d8185bbb75a4ea6d574
fetched_at: '2026-06-28T22:41:07.548685+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar a ordem
  do item apresentada no Documento de Entrada - MATA103
type: support-article
updated_at: '2024-09-09T14:30:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017811531-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-a-ordem-do-item-apresentada-no-Documento-de-Entrada-MATA103
---

**Dúvida**Como configurar a ordem do item apresentada no Documento de Entrada (mata103)  
  
**Ambiente**

Protheus – Compras – A partir da versão 12

**Solução**

Temos dois parâmetros que podem ser utilizados para definir a ordem dos itens no documento de entrada:

1. **MV\_CLASORD**: Determina se os itens na classificação do documento de entrada devem ser ordenados por ITEM+COD.PRODUTO.
2. **MV\_NFEORD**: Define se, na visualização do documento de entrada, os itens devem ser ordenados por ITEM+COD.PRODUTO.

Os parâmetros podem ser configurados com os seguintes valores:

* **1** para **Sim**
* **2** para **Não**

**Realize os seguintes passo :**

1. Acesse o sistema no ambiente SIGACFG.
2. Navegue até: Base de Dados > Dicionário > Base de Dados.
3. Selecione a empresa de teste e vá para: Parâmetros > Pesquisar. Digite o(s) parâmetro(s) desejado(s).
4. Selecione o(s) parâmetro(s) e clique em **Editar**.
5. Preencha os parâmetros com o conteúdo desejado e salve as alterações.

Abaixo estão os prints que mostram como a ordem dos itens será ajustada de acordo com o valor do parâmetro:

* **MV\_CLASORD = 1**

Abaixo seguem os prints de como fica a ordem dos itens de acordo com o conteúdo dos parâmetros:

*MV\_CLASORD = 1*

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/15935469231511)*

*MV\_CLASORD = 2*

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/15935463544471)*

*MV\_NFEORD = 1*

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/15935499726999)*

*MV\_NFEORD = 2*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15935437227159)

***OBSERVAÇÃO :***

Os parâmetros MV\_CLASORD e MV\_NFEORD serão acionados respectivas na classificação e visualização para alterar a forma como são apresentados os itens na rotina de documento de entrada (MATA103), não temos um parâmetro que seja acionado na inclusão do documento de entrada.

Logo por se tratar de uma devolução, as informações referente ao documento de origem (D1\_NFORI,D1\_SERIORI,D1\_ITEMORI) são preenchidas corretamente, com isso mantendo a integridade do processo.

***Saiba Mais :***

[MP - SIGACOM - Ordenação dos itens do Documento de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016676951)

[PCOM12017 - Parâmetros MV\_CLASORD e MV\_NFEORD](http://tdn.totvs.com/pages/releaseview.action?pageId=273310482)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
