---
article_id: 1500002943541
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: f2b94b746a3fd9525c5275e4ddea1fee00ef5e22dbf982d268688c3ab14e1c1e
fetched_at: '2026-06-28T22:39:09.542353+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - REGBLOQ
  - Cliente ou fornecedor bloqueado ao alterar um Cadastro de Produto
type: support-article
updated_at: '2025-03-12T12:26:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002943541-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-REGBLOQ-Cliente-ou-fornecedor-bloqueado-ao-alterar-um-Cadastro-de-Produto
---

**Ocorrência**Ao acessar à rotina MATA010 - Cadastro de Produtos e fazer alguma alteração, é apresentado o HELP REGBLOQ, indicando que Cliente ou Fornecedor está bloqueado na SA1/SA2.  
  
**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.17  
  
**Causa**

Este erro ocorre quando o Produto possui registro no campo Forn. Padrão (B1\_PROC) e este está bloqueado/inativado no seu cadastro, seja **Cadastro de Fornecedores (SA2) - MATA020** ou **Cadastro de Clientes - MATA030 (SA1)**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104147853/mceclip0.png)

**Solução**

Para resolver este produto, temos 2 alternativas:

**1° -** Desvincular o Fornecedor/Cliente do Cadastro do Produto, apagando o que estiver preenchido no campo Forn. Padrão (B1\_PROC);

**2° -** Identificar o Fornecedor/Cliente que está vinculado ao produto e, na rotina MATA020 (Fornecedores) ou MATA030 (Clientes) para reativá-lo.

**Caso seja Cliente**

Acessar à rotina MATA020, localizar o cliente e alterar o campo **Status** (**A1\_MSBLOQ**) para **2 - Ativo,**conforme imagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104147953/mceclip1.png)

**Caso seja Fornecedor**

Acessar à rotina MATA030, localizar o fornecedor e alterar o campo **Bloqueado?** (**A2\_MSBLOQ**) = **Nao**, conforme imagem abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003108702/mceclip2.png)

Após seguir a alternativa 1 ou 2 descritas no artigo, será possível fazer a alteração cadastral do produto normalmente.

**Saiba mais:**

*[MP - SIGAEST - MATA010 - HELP: UM.Industria (Unidade de Medida do WMS)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001932842)*

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
