---
content_hash: 0917262d75b09e27a479f1d32d7497990751e25efe23efd7a6e670762b2666a0
fetched_at: '2026-06-29T00:11:10.214185+00:00'
page_id: '642621753'
product: rm
source: tdn-rm
title: FISCAL01-16574 - DT DMA-BA - QUADROS 30/31 - Implementação dos Registros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642621753
version: 5
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DMA-BA |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16574 |

## **02. SITUAÇÃO/REQUISITO**

Implementação dos Registros/Quadros 30/31

## **03. SOLUÇÃO**

**Regras de Geração:**

Lançamentos Fiscais de Entrada/Saída para a Filial informada no Parâmetro onde  
o Estado do Código de Município de Serviço seja igual a BA.

Registros Gerados apenas para Contribuinte Inscrição Única.

Possibilidade de gerar o Registro consolidado por Filial com mesmo Inscrição Estadual, basta  
marcar Inscrição Única nos Parâmetros de Geração.

**Registro:**  
TipoReg                 Fixo 30/31  
Ano                       Ano de Referência  
Mes                       Mês de Referência  
Inscrição Estadual Inscrição Estadual  
StatusES                Tipo de Lançamento E/S   
CodigoMunicipio  Código do Município   
VlrBaseCalculo      BASEREDICMS  
VlrIsentas              IsentoICMS  
VlrOutras              OutrosICMS
