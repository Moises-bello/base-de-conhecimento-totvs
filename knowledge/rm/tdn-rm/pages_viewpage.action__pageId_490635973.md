---
content_hash: 2606ee631f8c01cedc5153ad376cf2b03d9f130488aea1de9c89348f237eae46
fetched_at: '2026-06-29T00:10:20.274958+00:00'
page_id: '490635973'
product: rm
source: tdn-rm
title: FISCAL01-7845 DT Cadastro de Filial - Novo campo Tipo Apuração CPRB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490635973
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro de Filial - Dados Fiscais |
| Requisito/Story/Issue (informe o requisito relacionado) : | FIS000036 |

## **02. SITUAÇÃO/REQUISITO**

Criar o Campo “**Apurar CPRB – Regime de Caixa**”.

Este campo será utilizado para identificar que o método de apuração da CPRB, se pelo regime de competência (DESMARCADO) ou pelo regime de caixa (MARCADO).

Se o Campo estiver habilitado a Apuração do Tributo deve ser feita com base na Data da Baixa dos Lançamentos Financeiros parametrizados.

Uma vez que a CPRB é apurada na Filial Matriz, este novo parâmetro só deve ser editado na Filial Matriz ou na Filial SCP.

## **03. SOLUÇÃO**

No anexo Dados Fiscais do Cadastro de Filial na aba Tributos foi implementado o campo Tipo Apuração - CPRB.

O campo deve ser preenchido com Regime de Caixa ou Competência somente na filial Matriz ou filial SCP.

Observação: O parâmetro de definição da filial matriz da coligada, fica em parâmetro fiscal → Apuração de Tributos → Filial Matriz.
