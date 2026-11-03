---
article_id: 360060937474
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 8167980da7d339763372988d13a14accdc2529c7449371eae2697f3901d8e3f8
fetched_at: '2026-06-28T22:39:08.261463+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Help "Contr.Endere"
  na alteração do Cadastro de Produto (MATA010)
type: support-article
updated_at: '2025-12-19T15:14:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060937474-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-Contr-Endere-na-altera%C3%A7%C3%A3o-do-Cadastro-de-Produto-MATA010
---

No Protheus, não é possível usar o parâmetro MV\_LOCALIZ exclusivo por filial, pois os fontes usam a filial corrente. Para tabelas SB1 compartilhadas e controle de endereço por filial, deve-se habilitar o parâmetro MV\_ARQPROD com a tabela SBZ e usar a rotina Indicador de Produtos (MATA019). Assim, o sistema considera a indicação por filial, mesmo com "Contr.Endere" ativo. Recomenda-se incluir o alias da SBZ no parâmetro MV\_CADPROD.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18502985338775)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Tenho a tabela de Produtos (**SB1**) compartilhada e a tabela de Indicadores de Produtos (**SBZ**) exclusiva.

Na minha filial em que o parâmetro **MV\_LOCALIZ** é ativado e exclusivo, ao alterar o campo "Contr.Endere" (**B1\_LOCALIZ**) de um produto, o sistema apresenta o HELP "**Contr. Endere**". Como validar esta ocorrência?  
  
**Ambiente**  
Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - A partir da versão 12.1.17

**Solução**

Não é possível utilizar o parâmetro **MV\_LOCALIZ** exclusivo por filial, pois os fontes utilizam a filial corrente.

Para ambientes que utilizam a tabela de Cadastro de Produto (**SB1**) compartilhada e precisam que em determinada filial não utilize o controle de Endereço, deve-se habilitar o parâmetro [**MV\_ARQPROD**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418117626391) com a tabela **SBZ**, passando a utilizar a rotina [**Indicador de Produtos (MATA019)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021908151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA019-Indicador-de-Produtos), com a tabela **Indicadores de Produtos (SBZ)** exclusiva.

Desta forma, mesmo que o campo "Contr.Endere" (**B1\_LOCALIZ**) esteja com "**S**", o Protheus considera a indicação por filial na rotina **Indicador de Produtos (MATA019)**.

**Sugestão:** Incluir no parâmetro [**MV\_CADPROD**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068032-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utilidade-e-configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CADPROD)o alias da tabela SBZ.

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
