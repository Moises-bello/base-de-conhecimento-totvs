---
content_hash: e1f48eb770aefe54fcb61428fe3bf238901ce7777a6b9f79d5a4f1db925b5a95
fetched_at: '2026-06-29T00:11:21.446062+00:00'
page_id: '696096047'
product: rm
source: tdn-rm
title: FISCAL01-18190 - DT - Cadastro de Informações Fiscais Adicionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=696096047
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Informações Fiscais Adicionais |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18190 |

## **02. SITUAÇÃO/REQUISITO**

Criar o cadastro de **Informações Fiscais Adicionais.**

Estes cadastro será base para a geração dos Registros **0450: TABELA DE INFORMAÇÃO COMPLEMENTAR DO  DOCUMENTO FISCAL** e **0460: TABELA DE OBSERVAÇÕES DO LANÇAMENTO FISCAL** da EFD ICMS IPI.

O cadastro será composto basicamente de Código e Descrição e deve obedecer os tamanhos definidos no layout

* Código 6 dígitos
* Descrição 255 dígitos

## **03. SOLUÇÃO**

Foi criado uma tela de cadastro de Informações Fiscais Adicionais.

Menu: Cadastro | Global | Mais | Informações Fiscais Adicionais.

Nela é possível salvar os campos de Registro, Código, Descrição para realizar a integração com os campos livres da NFE para geração do SPED.

OBS: Caso haja uma alteração no Registro, Código ou Descrição, será emitido uma tela de aviso.

Disponível a partir da versão 12.1.33.  
Patches:  12.1.33.280 | 12.1.34.183 | 12.1.2205.122
