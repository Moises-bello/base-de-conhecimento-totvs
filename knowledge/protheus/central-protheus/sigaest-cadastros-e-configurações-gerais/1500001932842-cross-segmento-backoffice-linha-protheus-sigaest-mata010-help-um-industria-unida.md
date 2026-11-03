---
article_id: 1500001932842
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: f02c298bb929b16bcc427b9ed67b3d6d7d442c149ed425828e3e0590d31f5e17
fetched_at: '2026-06-28T22:39:09.503453+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - HELP UM
  Industria (Unidade de Medida do WMS)
type: support-article
updated_at: '2025-03-12T12:23:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001932842-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-HELP-UM-Industria-Unidade-de-Medida-do-WMS
---

**Dúvida**

Ao informar a unidade de medida do WMS no complemento do Produto (MATA010 - Cadastro de Produtos) o sistema exibe o HELP: UM.Industria - Valor Inválido (UM.Industria). O que fazer para resolver este problema?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102832353)

**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.17  
  
**Solução**Para solucionar este problema será necessário validar o campo B5\_UMIND. Ele precisará ficar com tamanho 1.

Para isso, via Configurador (SIGACFG) , acesse ao caminho: **Base de dados -> Dicionário -> Bases de Dados.**

Localize a tabela SB5 -> B5\_UMIND e altere o seu tamanho para **1**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001821161)

Após isso, salve as alterações;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001821221)

Posteriormente, basta acessar novamente ao Protheus e será possível informar a Unidade de Medida do WMS.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
