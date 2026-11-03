---
content_hash: d2f2212ee022cbeb4f15688e81c2f2de862427485c2cea97efecbbb3ddc3ced2
fetched_at: '2026-06-29T00:10:22.044622+00:00'
page_id: '496039932'
product: rm
source: tdn-rm
title: 5674403 FISCAL01-8996 DT SCANC Registro Tipo 40
type: documentation
url: https://tdn.totvs.com/display/LRM/5674403+FISCAL01-8996+DT+SCANC+Registro+Tipo+40
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração do Arquivo SCANC-MG |
| Ticket: | 5674403 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FIS000282 |

## **02. SITUAÇÃO/REQUISITO**

Adequar rotina SCANC CTB - MG ao Manual 3.0.7.6 (29/05/2017)

Foram identificados os ajustes abaixo:

         Registro Tipo 40 – Nota Fiscal - Campo 09: Número do Documento Fiscal, passou para tamanho 9 posições.

         Filtrar os lançamentos fiscais selecionados conforme Código Fiscal indicado da tabela 4.1

## **03. SOLUÇÃO**

Foi ajustado o tamanho do número de documentos para até 9 caracteres para o tipo de registro 40.

Os lançamentos fiscais serão filtrados conforme código fiscal do produto com Estado igual a MG.

Foi disponibilizado a documentação da rotina no TDN: <http://tdn.totvs.com/display/public/LRM/SCANC+-+CTB>
