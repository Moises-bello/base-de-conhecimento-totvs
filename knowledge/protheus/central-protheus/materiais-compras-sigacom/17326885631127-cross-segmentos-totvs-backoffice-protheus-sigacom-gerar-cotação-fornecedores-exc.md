---
article_id: 17326885631127
category: Materiais - Compras (SIGACOM)
content_hash: c62c698e75cb001ae4713e37ec170b55fcf40c2969eb0c2d66c53cc654e6b5ad
fetched_at: '2026-06-28T22:41:18.708892+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Gerar cotação / Fornecedores
  excluídos.
type: support-article
updated_at: '2023-09-06T19:08:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17326885631127-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Gerar-cota%C3%A7%C3%A3o-Fornecedores-exclu%C3%ADdos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17326897026839) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Qual a regra aplicada, quando parâmetro MV\_SELFOR estiver habilitado e for apresentada a tela para seleção dos fornecedores ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS -  VERSÃO 12  
  
**Solução**

 Ao acessar a opção **Gera Cotações**,é exibida a janela **Parâmetros**para que as informações sejam configuradas de acordo com os critérios desejados, após a confirmação a configuração dos parâmetros. É exibida uma tela dividida em: **Grupo → Produto → Fornecedores**

![tela.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17327904840215)

--

Quando parâmetro MV\_SELFOR estiver habilitado e for apresentada a tela para seleção dos fornecedores a regra aplicada é a seguinte:

**Grupo:**

* Para cada grupo pode-se ter 1 ou mais produtos.

**Produto:**

* Para cada produto pode-se ter 1 ou mais fornecedores.
* Para o produto em que estiver posicionado, sera refletido os fornecedores selecionados para a cotação.

**Fornecedores:**

* Fornecedores que podem e/ou serão utilizados:
  + Fornecedores que já possuem amarração junto ao produto (SA5)
  + Ultimo fornecedor
  + Incluir um novo participante
* Exclusão de fornecedor:
  + Ao excluir um fornecedor, ele sera deletado para o Produto que estiver posicionado, NÃO sera deletado para todos os produtos, se quiser deve ser deletado manualmente ou então utilizar a opção de "replicar p/todos" para que assim TODOS os Produtos tenham cotação com o mesmo fornecedor.

**SAIBA MAIS EM :**

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Totvs Backoffice Protheus - SIGACOM - Gera Cotação - Replica de Fornecedores.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17290088552215)**
