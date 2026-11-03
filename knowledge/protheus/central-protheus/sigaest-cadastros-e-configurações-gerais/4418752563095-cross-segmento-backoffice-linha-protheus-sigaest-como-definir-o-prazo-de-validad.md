---
article_id: 4418752563095
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 3a37e39ad0773507275135a9249927023926711d8fc5b983f83797d4e0eb148b
fetched_at: '2026-06-28T22:39:07.832388+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como definir o prazo
  de validade de lote de um Produto?
type: support-article
updated_at: '2026-06-09T21:47:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418752563095-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-definir-o-prazo-de-validade-de-lote-de-um-Produto
---

A validade dos lotes no TOTVS Protheus é definida automaticamente somando a data atual ao número de dias de validade do produto no campo B1\_PRVALID. Movimentações internas exibem a data de validade conforme cadastro. É importante evitar alterar a data-base do sistema para não comprometer a validação dos lotes. O sistema prioriza lotes próximos do vencimento e permite configurar alertas de antecedência para aviso de vencimento.

**Dúvida**  
Como posso definir o prazo de validade dos lotes de um Produto?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Para definir o prazo de validade sempre é preenchida automaticamente com a data atual (no caso do exemplo, estamos utilizando a data do dia 11/01/2022) mais o número de dias de **Validade do Produto** no campo **B1\_PRVALID,** conforme exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418752318359)

Ao fazer qualquer movimentação interna do estoque, irá apresentar a data de validade de acordo informado no cadastro de produto (neste caso, 20/02/2022 que dá 40 dias após a data-base do Sistema, que era de 11/01/2022):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418752553111)

**Essa funcionalidade não é valida para inclusão de Saldo Inicial** de estoque, ou seja sob uso da rotina MATA220, pois é um input de dados, diferente de uma movimentação.

**Observação:**

Para evitar empenho de lote antes de chegar ao vencimento, é importante validar se não está fazendo processo de avançar a data-base do sistema, pois o mesmo faz a validação do lote.

Com o controle de data do LOTE, sempre o lote proximo ao vencimeno sera o lote acionado para as movimentações por padrão.

É também possivel definir uma regra que avise com antecedencia do vencimento do lote dos produtos conforme documentação:

[Cadastro de regras de antecedência para aviso de vencimento (SIGAEST - ESTA010)](https://tdn.totvs.com/pages/releaseview.action?pageId=1002492090)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
