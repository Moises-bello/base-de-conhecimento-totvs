---
content_hash: 9bddfcaa32a4bc309de9da80236fb54ae1460aa479da701461f85672b8e1f53a
fetched_at: '2026-06-29T00:12:13.422228+00:00'
page_id: '955505130'
product: rm
source: tdn-rm
title: FISCAL01-25926 - EFD Contribuições - Alteração quantidade de campos D500 -
  Inclusão Campo 23 - Chave do Documento Fiscal Eletrônico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=955505130
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD Contribuições |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25926 |

## **02. SITUAÇÃO/REQUISITO**

Houve uma alteração na quantidade de campos do registro D500. Atualmente, o sistema gera o registro com 22 campos; no entanto, após a atualização, ele passa a conter 23 campos, conforme estabelecido na Nota Técnica 009, de 29 de outubro de 2024, que trata das alterações previstas no leiaute da EFD-Contribuições para o ano de 2025.

## **03. SOLUÇÃO**

Codificação:  
Ajuste para exibir o campo Chave Acesso no lançamento quando modelo de documento for 62:

Liberado novo Layout do Gerador de Saídas, contendo novo campo 23 referente a Chave do Documento Fiscal Eletrônico do registro D500 da EFD Contribuições.

Para o campo ser gerado, além das parametrizações para geração do D500, será necessário:

* DataLF a partir de 01/04/2025
* Modelo de documento 62 - NFCom
* Preencher o campo Chave Acesso no lançamento

Disponível à partir da biblioteca 12.1.2410
