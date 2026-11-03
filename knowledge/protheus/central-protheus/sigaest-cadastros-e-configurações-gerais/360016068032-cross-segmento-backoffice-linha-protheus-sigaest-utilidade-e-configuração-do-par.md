---
article_id: 360016068032
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 8952de55c84edcbefd11d30697769a2bf655931332d5e93e4c606795f7c7885a
fetched_at: '2026-06-28T22:39:07.967365+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Utilidade e configuração
  do parâmetro MV_CADPROD
type: support-article
updated_at: '2026-02-02T16:53:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068032-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utilidade-e-configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CADPROD
---

**Dúvida**  
Como utilizar e realizar a configuração do parâmetro MV\_CADPROD?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

O parâmetro **MV\_CADPROD**tem como objetivo informar quais cadastros complementares devem ser apresentados no cadastro de produtos.

**Configuração:**  
**Tipo:** Caractere  
**Valor Default:** "|SBZ|SB5|SGI|"

**Cadastros aceitos:**

|SA5|SBZ|SB5|DH5|SGI|F2Q|AGRO|ACV|D4X

* SA5 - Produto X Fornecedor
* SBZ - Indicadores
* SB5 - Complemento de Produto
* DH5 - Complemento de Produto DCL
* SGI - Produtos Alternativos
* F2Q - Complemento Fiscal de Produto
* AGRO - Complemento Produtos Agronegócio
* [ACV - Amarração Produto x Categoria](https://tdn.totvs.com/x/BSbwP)
* [D4X - Amarração Produto x Características](https://tdn.totvs.com/x/9AXePQ)

|  |
| --- |
| **Observações**   * Para que seja apresentado o formulário de Indicadores de Produtos (SBZ), a tabela de Cadastro Genérico de Produtos (SB1) deverá estar compartilhada por Filial (C); * Para que seja apresentado o formulário de Complemento de Produto DCL (DH5) o parâmetro MV\_DCLNEW tem que estar configurado; * Para que seja apresentado o Formulário de Produtos Agronegócio (NCR), o parâmetro MV\_SIGAAGR precisará estar ativo (conteúdo = .T.). O Formulário de Produtos Agronegócio está disponível à partir do Release 12.1.27 (Outubro/2020). |

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
