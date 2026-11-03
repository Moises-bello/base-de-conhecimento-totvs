---
content_hash: e0c7983afdbc8ff2420c8368b45a3893b529a35638840a475e289ad631e5d0fe
fetched_at: '2026-06-29T00:10:20.004991+00:00'
page_id: '484702005'
product: rm
source: tdn-rm
title: 5443538  FISCAL01-8822 DT Livro Eletrônico - 0150\CODPAIS Não Preenchido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=484702005
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Rotina Estadual Livro Eletrônico |
| Requisito/Story/Issue (informe o requisito relacionado) : | FIS000247 |

## **02. SITUAÇÃO/REQUISITO**

Erro ao validar arquivo txt do livro eletrônico:  
"Campo obrigatório de acordo com o layout Livro Eletrônico Registro: 0150 - Tabela de Cadastro do Participante. Campo: 4 - Código do pais do participante, conforme a tabela indicada no item 3.3.1"

O código do país do participante não é carregado porque o cliente cadastrou um Estado (UF) genérico, sem pais vinculado.

## **03. SOLUÇÃO**

No processamento do livro eletrônico ao carregar o participante de origem filial ou cliente\fornecedor e o Estado (UF) do mesmo não tem país vinculado, será verificado o código do país do cadastro da

filial ou cliente\fornecedor conforme classificação parametrizada na geração da rotina Livro Eletrônico.  Anteriormente o código do país era carregado via País vinculado no Estado, impossibilitando o

cadastramento de um Estado (UF) genérico. Ainda será considerado o país vinculado ao Estado, o tratamento ocorre para o Estado que for genérico ou seja, sem país cadastrado.
