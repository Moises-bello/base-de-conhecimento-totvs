---
content_hash: c8dc6107a71f05564d0491c0a485abf2f36d8919b281d01f4458774f0565cd85
fetched_at: '2026-06-29T00:05:53.034969+00:00'
page_id: '1064140238'
product: rm
source: tdn-rm
title: Alterações Abril/2026 (NF-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1064140238
version: 6
---

# Conteúdo

1Conteúdononenone

# 1. Sobre

Esta atualização permiti emitir NF-e gerando os tributos da reforma tributária (IBS e CBS) com base de calculo = 0;

Também permite gerar o grupo de agropecuaria pelas informações da pasta "Agronegócio" do movimento.

# 2. Versões para atualização

Biblioteca RM:

* 12.1.2506.298
* 12.1.2510.223
* 12.1.2602.141

# 3. Principais Alterações

## Geração do grupo IBSCBS

O grupo deixa de validar o preenchimento da base de calculo dos tributos IBS e CBS e passa a validar se existe algum dos tributos (IBS e CBS) e se algum deles possuem o campo situação tributária (CST) ou Classif. Tributação preenchidos.

Detalhes:

## Geração do grupo ZF - Informações de Produtos da Agricultura, Pecuária e Produção Florestal

O grupo deixa de usar os campos complementares do movimento e será gerado pelas informações cadastradas na pasta "Agronegócio" do movimento.

Detalhes: [Grupo ZF - Informações de Produtos da Agricultura, Pecuária e Produção Florestal](https://tdn.totvs.com/pages/viewpage.action?pageId=1052744485)
