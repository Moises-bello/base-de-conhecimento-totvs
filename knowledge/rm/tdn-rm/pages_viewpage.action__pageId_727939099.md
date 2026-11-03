---
content_hash: 2dab94250ab2e8b197011a6ba20262070d90a56a2503564c0bc5a4ae50923456
fetched_at: '2026-06-29T00:11:27.620715+00:00'
page_id: '727939099'
product: rm
source: tdn-rm
title: FISCAL01-18456 - DT - R-1050 - Transmissão e Consulta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=727939099
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17098/FISCAL01-18456 |

## **02. SITUAÇÃO/REQUISITO**

Alterar o texto da tela de parâmetros de Parâmetros Gerais Integração TSS para Parâmetros Gerais para Integração com a EFD Reinf.  
Alterar o tipo do campo usado para informar a versão do layout da Reinf, o campo é um combo box e deve ser alterado para um campo texto livre.

## **03. SOLUÇÃO**

Implementado a transmissão e consulta do evento R-1050 da Reinf  
As opções podem ser acessadas no menu de processos do evento R-1050, anexo ao evento cadastral R-1000.

Imagem

Para que o evento R-1050 seja exibido nos anexos do evento R-1000 é necessário definir uma versão superior ou igual a 2.01.01 nos parâmetros EFD Reinf da filial:

Imagem

Disponível a partir da biblioteca 12.1.2205
