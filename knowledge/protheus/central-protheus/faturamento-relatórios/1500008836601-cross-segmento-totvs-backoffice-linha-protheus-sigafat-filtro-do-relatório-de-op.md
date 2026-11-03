---
article_id: 1500008836601
category: FATURAMENTO - RELATÓRIOS
content_hash: ed348bc55e05577b4494a0271cb449ec040bae7eca1e83d687aa725515c2951d
fetched_at: '2026-06-28T22:38:23.031800+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Filtro do Relatório
  de Oportunidade
type: support-article
updated_at: '2022-05-11T17:43:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008836601-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Filtro-do-Relat%C3%B3rio-de-Oportunidade
---

**Dúvida**

Nos parâmetros de relatórios temos a opção de GRUPO DE PRODUTO: DE / ATÉ, mas independente do informado neste parâmetro, o relatório apresenta todas as oportunidades, mesmo que nenhum dos produtos da oportunidade pertença a algum deste intervalo de código de grupo.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- Versão 12  
  
**Solução**

Este relatório relaciona os produtos da Oportunidade de Vendas, o produto que será impresso é do campo AD1\_CODPRO ( Principal produto da Oportunidade), Os produtos informados na Aba de Produtos não serão considerados;

Para impresso com o filtro seguir os procedimentos;

1. Cadastre um produto, nesse exemplo iremos escolher o tipo "GG"

![Produto_GG.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013507081/Produto_GG.png)

2. Em Oportunidade> Informações Internas, informe um produto, e preencha as informações da Oportunidade;

![PrincipalProduto.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013506601/PrincipalProduto.png)3. Em Atualizações > Vendas > Oportunidade> Outras Ações Parâmetros:

Produto "De? "Branco"  Produto até  "zzzzzzzzzzzzzzz", Tipo De? "GG" Tipo Até? "GG" cliquei em Ok, Imprimir;

![PAR_METROS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013171302/PAR_METROS.png)

4. Será impresso apenas as Oportunidades com o Produto do Tipo GG do Código 000000050;

![Impressao.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013507801/Impressao.png)

**Saiba mais**: <https://tdn.totvs.com/x/eEabEg>
