---
content_hash: af5e3bc5f5cdf4236422c786770be52a933430db87f94fda51eb763c02f20c4b
fetched_at: '2026-06-29T00:10:30.213786+00:00'
page_id: '519702928'
product: rm
source: tdn-rm
title: FISCAL01-11157 DT EFD-REINF Processo de Geração dos Eventos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519702928
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Processo de Transmissão de Eventos da EFD-REINF |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11157 |

## **02. SITUAÇÃO/REQUISITO**

Implementar o processo para a transmissão do evento R-1000 da Reinf.

## **03. SOLUÇÃO**

Foi implementado o processo de Transmissão do Evento R-1000 para o TSS.

O processo EFD-Reinf - Transmitir Evento será exibido em RM -> Gestão Fiscal -> Obrigações Acessórias -> SPED -> REINF -> Eventos Cadastrais.

O processo irá montar o xml considerando a filial do contexto e integrar com o TSS conforme as regras e comportamentos definidos na especificação.

Especificação geral: 

Especificação do R-1000:
