---
content_hash: d5d7422c56641790beee42ebca117a77f21a2825861a7f95a84225329f2f0bbe
fetched_at: '2026-06-29T00:10:37.029826+00:00'
page_id: '533751432'
product: rm
source: tdn-rm
title: 7872082 FISCAL01-12284 DT SPED com geração do arquivo TXT duplicado.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=533751432
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | 7872082 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12284 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o arquivo SPED Fiscal da competência 11/2019, onde o cliente tem obrigatoriedade do Bloco B, ocorre duplicidade nos valores contábeis (Campo 12) e campo 17 (VL\_BC\_ISS) do registro B020 e nos valores do tributo ISS do item Campo 02 (VL\_CONT\_P) e campo 3 (VL\_BC\_ISS\_P) do registro B025, assim duplicando os valores do tributo ISS.

## **03. SOLUÇÃO**

**Funcionalidade: Geração do SPED**  
**Cenário I: Bloco B com fatura**  
  
Dado um movimento de fatura escriturado,   
Ao gerar o bloco B do SPED,   
Então deve-se considerar somente os lançamentos financeiros de status de faturamento 0,   
1 ou Nulo para cálculo dos campos 12 e 17 do B020, 2 e 3 do B025
