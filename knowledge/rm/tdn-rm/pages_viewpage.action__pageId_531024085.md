---
content_hash: 33f08148612ac778b55b7b457d344eaf85091d8110d4b81a4664fdb6e459703e
fetched_at: '2026-06-29T00:10:35.658770+00:00'
page_id: '531024085'
product: rm
source: tdn-rm
title: Elaboração de AIH (Autorização de Internação Hospitalar)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531024085
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Documentos faturados**
3. **Modificação**
4. **Lista de procedimentos**
5. **Mensagens de erro**

## **01. VISÃO GERAL**

Registra os documentos AIH que deverão ser encaminhados ao SUS para cobrança.  
Esses  documentos devem ser preparados a partir do registro de internação do paciente.

## **02. DOCUMENTOS FATURADOS**

 Os documentos com status "Faturado" não podem ser modificados.

Nota-se que se o status está como "Faturado", todos os campos estão desabilitados.

## **03. MODIFICAÇÃO**

Sempre que um documento for modificado seu status deve ser modificado para "Elaboração".

A elaboração da AIH é dividida em...

1. Identificação.
2. Complemento.
3. Diagnóstico.
4. Obstetrícia.
5. Mensagens de Erro.

## **04. LISTA DE PROCEDIMENTOS**

O usuário especifica a ordem em que os procedimentos digitados devem aparecer na lista de procedimentos executados.  
Ao informar o procedimento a tela é alterada de modo a apresentar apenas os dados exigidos pelo tipo de procedimento.  
**Observação:**

Se o parâmetro "Agrupa procedimentos repetidos" estiver marcado, até os exames serão agrupados. Se "Agrupa exames" estiver marcado, somente esses serão agrupados.

## **05. MENSAGENS DE ERRO**

Ao Valorizar ou Validar uma AIH, será efetuada uma série de validações.

Caso exista algum problema a ser resolvido, na própria elaboração da AIH, ou em algum cadastro, como de pacientes, prestadores, condição contratual... Será adicionada uma mensagem de erro a ser tratada para cada validação efetuada.

Após efetuar todos os tratamentos listados nos erros, basta valorizar a AIH novamente.

As mensagens de erro são exibidas dentro da elaboração da AIH, na aba "Mensagens de Erro".
