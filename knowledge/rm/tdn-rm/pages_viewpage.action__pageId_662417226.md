---
content_hash: 088675c86562362b79856c90a68dd239a85830864a108642cfe20ca95416e142
fetched_at: '2026-06-29T00:11:15.722565+00:00'
page_id: '662417226'
product: rm
source: tdn-rm
title: Endereçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=662417226
version: 11
---

Atenção

Recurso disponível na release 12.1.2205 ou superior.

## **01. VISÃO GERAL**

O cadastro de Endereçamento tem como objetivo o cadastro dos endereços internos de um Local de Estoque - permitindo assim cadastrar prateleiras, ruas, divisórias, etc.

## **02. EXEMPLO DE UTILIZAÇÃO**

Para realizar esse cadastro é necessário, em primeiro lugar, parametrizar a máscara do Endereçamento. Para isso acesse Parâmetros → Gestão de Estoque, Compras e Faturamento→ Parâmetros Gerais → Tabelas → Local de Estoque e preencha o campo Máscara do Endereçamento.

Após essa definição, basta acessar o cadastro de Local de Estoque e acessar o anexo Endereçamento e preencher as informações de cada Endereço do Estoque.

**Campos Obrigatórios:**Código.

* **Campo Código:**É o código do Endereço que deve seguir a Máscara definida no Parâmetro informado acima.
* **Descrição:** É a descrição do Endereço.
* **Código de Barras:** Código de Barras que identifica o local.
* **Inativo:** Define se o Local está ativo ou não.

Ao inativar um endereço, todos os vínculos de produtos associados a ele serão inativados também, conforme descrito na mensagem abaixo. Se o usuário clicar em não, a operação será cancelada e o Endereço e os seus vínculos permanecerão os mesmos.

Quando o usuário desejar reativar um endereço, será fornecida a opção de reativar **TODOS** os vínculos com os produtos associados também, ao clicar em sim o usuário confirma esta ação, ao clicar em não os vínculos permanecerão com o status de disponibilidade atual.

## **03. TABELAS UTILIZADAS**

* TLOCENDERECO - Tabela para endereçamento dentro dos Locais de Estoque

## **04. HOW TO**

**648432**

Processos Relacionados:

Anexo do Produto - 

Anexo do Endereçamento - [Produtos do endereçamento](https://tdn.totvs.com/pages/viewpage.action?pageId=706122009)
