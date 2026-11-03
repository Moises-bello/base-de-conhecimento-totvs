---
content_hash: fdb17065536cc2193c1e78ceccb7a44d51d369d5882fa7b7ae44ade5f46a8a43
fetched_at: '2026-06-29T00:11:06.274599+00:00'
page_id: '633056820'
product: rm
source: tdn-rm
title: AIH Rejeitada (Autorização de Internação Hospitalar)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=633056820
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Faturamento AIH**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

AIH Rejeitada (Autorização de Internação Hospitalar).

## **02. EXEMPLO DE UTILIZAÇÃO**

Uma vez selecionada a opção de AIH Rejeitada, o sistema fará a busca das contas de pacientes de acordo com os filtros informado.

Para a geração do faturamento para AIH Rejeitada, o sistema verifica as seguintes condições:

* Se existem contas selecionadas
* Se as contas selecionadas não ultrapassa 999 nessa remessa
* Se o percentual de cesáreas em relação aos partos normais, é menor ou igual ao parâmetro permitido (Parâmetros Sus | AIH | Gerais II | % Cesarianas)

## **03. FATURAMENTO AIH REJEITADA**

Para realizar o processo de faturamento de uma remessa é necessário que a mesma esteja em aberto, vide a imagem abaixo.

Devemos selecionar o tipo de faturamento AIH Rejeitada. É obrigatório o preenchimento do mês/ano de apresentação.

Nessa etapa devemos selecionar todas as contas que devem ser incluídas na remessa e serão faturadas.

Após executar o processo podemos notar que a remessa foi faturada, vale ressaltar que a fatura criada será do tipo AIH.

Um arquivo é gerado na pasta definida no parâmetro Diretório de Armazenamento do Arquivo.

## **04. TABELAS UTILIZADAS**

* SZSUSAIHPROD
* SZSUSRECEMNATO
* SZSUSAIHCID
* SZSUSPROCREALIZADOS
