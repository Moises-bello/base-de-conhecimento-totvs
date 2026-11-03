---
content_hash: 18addc9218d9ff8b91a11adf22c84d1450c1175e0e70d03b1f7ede2b550edaf7
fetched_at: '2026-06-29T00:11:06.821982+00:00'
page_id: '635355158'
product: rm
source: tdn-rm
title: Matmed de Terceiros
type: documentation
url: https://tdn.totvs.com/display/LRM/Matmed+de+Terceiros
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Utilização**
3. **Validações**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O lançamento de Matmed de terceiros tem a finalidade de possibilitar à instituição, de fazer a cobrança do OPME.

## **02. UTILIZAÇÃO**

Para se utilizar dessa funcionalidade é necessário parametrizar nas condições contratuais com cada convênio, o parâmetro abaixo.

Ao se marcar o parâmetro, o mesmo fará com que a aba de "Matmed Terceiros" seja exibida na funcionalidade de "Elaboração de Contas".

Os itens podem ser pesquisados de duas maneiras, para serem lançados na conta:

1. Tabelas vinculadas nas condições contratuais
   1. O funcionamento é o mesmo da aba de Matmed
2. Tabela própria de cada prestador com cada convênio
   1. No credenciamento do prestador com o convênio, deve-se informar a tabela de Matmed utilizada
   2. No meu Cadastros > Faturamento > Outros Cadastros > Itens Terceirizados, deve-se cadastrar todos os itens praticados pelos prestadores
   3. Na aba "Preços - Itens Terceirizados", deve-se informar o preço praticado para cada tabela

Ao realizar o lançamento, caso marque a opção "Item do estoque", o sistema pesquisará nas tabelas das condições contratuais. Caso esteja desmarcado, a pesquisa será feita na tabela de "Itens Terceirizados" e o preço será o praticado pelo prestador na tabela vinculada no credenciamento

## **03. VALIDACÕES**

O seguintes campos devem ser informados:

* Prestador
* Data
* Item
* O item deve possuir preço

Não se pode lançar itens do tipo kit, seja ele kit pré-montado ou kit produto composto.

## **04.****TABELAS UTILIZADAS**

* SZLANCMMTERCEIRO
* SZITEMTERC
* SZITEMTERCPRECO
