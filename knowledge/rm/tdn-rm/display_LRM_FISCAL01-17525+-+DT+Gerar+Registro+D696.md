---
content_hash: 109f619e3e158223065f871835dd143aa6a22698bb042f27f53cde5bbdf48d7b
fetched_at: '2026-06-29T00:11:16.521381+00:00'
page_id: '673780028'
product: rm
source: tdn-rm
title: FISCAL01-17525 - DT Gerar Registro D696
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-17525+-+DT+Gerar+Registro+D696
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Fiscais - SPED Fiscal |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17525 |

## **02. SITUAÇÃO/REQUISITO**

Registros D696 deve ser gerados pelas Empresas que fazem a **emissão** de Documentos Fiscais de notas de serviço de comunicação (código 21) e de serviço de telecomunicação (código 22) em **Única Via** conforme **previsto no Convênio 115/03**. Logo, devem ser gerados nestes registros as notas que foram geradas no Convênio 115.

## **03. SOLUÇÃO**

* Implementada geração do registro D696 conforme requisitos descritos no épico.
  + Validação para geração do D696:
    - Lançamento de Saída
    - CodModDoc 21 **OU** 22
    - Natureza iniciar com 5 **OU** 6
    - DLAF.CODAUTENTDIGITALDOC **preenchido**

* **Alterada geração do D500.**
  + O mesmo era gerado com as seguintes condições:
    - lançamentos de entrada **OU** **(**lançamentos de saída **E** "perfil A"**)**

* **Agora o D500 é gerado com as seguintes condições:**
  + lançamentos de entrada **OU** **(**lançamentos de saída **E** "perfil A" **E** campo DLAF.CODAUTENTDIGITALDOC **vazio)**.

Disponível a partir da biblioteca 12.1.34
