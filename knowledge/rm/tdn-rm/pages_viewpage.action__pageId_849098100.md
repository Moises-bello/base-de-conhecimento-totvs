---
content_hash: c14f7b4232fb1e3c113d4a244e81f358e5cc9a652b2c3b0e97aa3aa379690788
fetched_at: '2026-06-29T00:11:51.564057+00:00'
page_id: '849098100'
product: rm
source: tdn-rm
title: Codificação TISS Específica MatMed
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=849098100
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Cód. Tabela à Concatenar**
3. **Cód. Tab. MAT/MED**

itensVisão GeralAviso!

Os campos deste cadastro são opcionais. Se não forem preenchidos, o sistema usará os códigos definidos na tabela "Tabelas de MATMED Usadas".

## **01. VISÃO GERAL**

Nesse cadastro é possível configurar uma faixa de materiais ou medicamentos que precisam ter os seus códigos de tabelas alterados durante a geração do XML. É possível fazer um MIX de configurações, caso a configuração seja específica para apenas um item, no campo faixa inicial e final deverá ser utilizado o mesmo código do item

Cód. Tabela à Concatenar

## **02.** **CÓD. TABELA À CONCATENAR**

No primeiro campo podemos concatenar um código ao código da tabela de MatMed. Exemplo: Concatenar o código da tabela Brasíndice com a tabela TUSS de Materiais.

Cód. Tab. MAT/MED

## **03.** **CÓD. TAB. MAT/MED**

Indica qual código da tabela será trocado no momento da geração. Ex.: O cadastro tabela 17 está configurado para utilizar o padrão TUSS 19 para Materiais e a operadora deseja receber 00 - Tabela Própria da Operadora para o item "00.02.0569"

Cód. Grupo Gasto Correlativo

## **04.** **CÓD. GRUPO GASTO CORRELATIVO**

Aqui é possível realizar a troca do código padrão do item por um outro. Exemplo: No cadastro está configurado como Material e deverá ser enviado como Prótese.
