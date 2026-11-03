---
content_hash: 3d16ad910bf35eae4a159b010a5410a0d696b385649761b7ea27cba3c48b0f8c
fetched_at: '2026-06-29T00:10:33.315501+00:00'
page_id: '528469234'
product: rm
source: tdn-rm
title: FISCAL01-11830 DT EFD-Contribuições 2020 - Registro C500
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=528469234
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração do Arquivo EFD Contribuições |
| Ticket: | FISCAL01-11830 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11830 |

## **02. SITUAÇÃO/REQUISITO**

**Alteração EFD-Contribuições 2020**

**NOVO Campo -** **Registro C500: Nota Fiscal/Conta de Energia Elétrica (Código 06),** **Nota Fiscal de Energia Elétrica Eletrônica – NF3e (Código 66)****, Nota Fiscal/Conta de fornecimento D’água Canalizada (Código 29), Nota Fiscal/Consumo Fornecimento de Gás (Código 28) e NF-e (Código 55) – Documentos de Entrada / Aquisição com Crédito**

Incluído o Modelo de Documento **Nota Fiscal de Energia Elétrica Eletrônica – NF3e (Código 66)**

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem da Informação |
| 1 | REG | Texto fixo contendo "C500” |  |
| 15 | CHV\_DOCe | Chave do Documento Fiscal Eletrônico | Gerado como Campo Chave de Acesso do Lançamento Fiscal |

## **03. SOLUÇÃO**

Foi implementado o campo 15 (CHV\_DOCe) no registro C500 da EFD Contribuições e o registro passara a gerar lançamentos fiscais com modelo de documento 66 referente a NF3e.  
Foi incluído a Versão do Layout 006 no Layout EFD Contribuições.
