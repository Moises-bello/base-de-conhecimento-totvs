---
content_hash: 29b98c1d019d07902c1465b5d2fac3c998342339aa67a08e5e3cfbd4bbd225c7
fetched_at: '2026-06-29T00:10:36.175309+00:00'
page_id: '531030598'
product: rm
source: tdn-rm
title: Tabela de MATMED Usadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Tabela+de+MATMED+Usadas
version: 5
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Atualização dos preços dos itens vinculados ao Brasíndice.**
3. ****Atualização dos preços dos itens vinculados ao Simpro.****
4. **Precificação do MATMED**

## **01. VISÃO GERAL**

As tabelas de MATMED usadas correspondem aos nomes das tabelas de materiais e medicamentos utilizadas pela entidade hospitalar. Cada tabela pode ser utilizada por um ou mais convênios, dependendo das particularidades de cada um.

## **02. ATUALIZAÇÃO DOS PREÇOS DOS ITENS VINCULADOS AO BRASÍNDICE**

Pode-se definir que os preços dos itens da tabela serão atualizados no momento da importação do Brasíndice. Pode-se definir também que os itens que já foram lançados tenham seus preços atualizados de acordo com a data de atualização do Brasíndice, ou seja, atualização com data retroativa. Para que o item seja atualizado, um fator deverá ser aplicado. Existem dois fatores que devem ser informados: O fator PMC (Preço Médio ao Consumidor) e o PFB (Preço de Fábrica). Exemplo: Para acrescer o valor em 30 %, informe 1,30 e para abater 30% informe 0,70.  
Pode-se definir que o código e a descrição sejam atualizados no momento da atualização dos itens. Para isto é necessário marcar o campo Atualizar o código ou Atualizar a descrição

## **03. ATUALIZAÇÃO DOS PREÇOS DOS ITENS VINCULADOS AO SIMPRO**

Pode-se definir que os preços dos itens da tabela serão atualizados no momento da importação do Simpro. Pode-se definir também que os itens que já foram lançados tenham seus preços atualizados de acordo com a data de atualização do Simpro, ou seja, atualização com data retroativa. Para que o item seja atualizado, um fator deverá ser aplicado. Existem dois fatores que devem ser informados: O fator PV (Preço de Venda) e o PFB (Preço de Fábrica). Exemplo: Para acrescer o valor em 30 %, informe 1,30 e para abater 30% informe 0,70.  
Pode-se definir que o código e a descrição sejam atualizados no momento da atualização dos itens. Para isto é necessário marcar o campo Atualizar o código ou Atualizar a descrição.  
Atualização dos preços dos itens não vinculados ao Brasíndice e Simpro. Se definido que os itens da tabela devem ser atualizados automaticamente, no momento da entrada da nota fiscal, o fator informado será aplicado ao item.  
   
Pode-se definir na tabela de MATMED usada que será utilizado codificação/descrição específica para o convênio, ou seja, apesar do item já possuir uma codificação e um nome, o mesmo poderá ser alterado de acordo com a tabela do convênio.  
Código ANS define o correlativo utilizado no processo de padronização TISS.

## **04. PRECIFICAÇÃO DO MATMED**

Para se obter o preço de uma MATMED, o sistema leva em consideração o histórico de preços, que pode ter validade e/ou vigências distintas.

Caso o campo de Data de validade não esteja preenchida, o sistema pegará a maior vigência válida para a data de lançamento. Se a data de validade estiver preenchida, o sistema procura pela revista em que a data de lançamento esteja compreendida entre os campos Data e Data de validade.

Atenção

Se na última revista estiver com data de validade, será necessário incluir as validades das revistas anteriores, para que o preço retornado não seja dessas revistas sem data de validade, ou incluir um novo registro com o preço atual.

Não encontrando nenhum preço no histórico, o sistema retorna o preço atual, que consta na tabela de preços, na aba Identificação.

Se estiver configurado como **preço fixo**, o sistema não verifica o histórico.
