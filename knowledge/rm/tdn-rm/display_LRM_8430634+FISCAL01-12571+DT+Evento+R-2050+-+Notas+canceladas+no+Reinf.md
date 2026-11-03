---
content_hash: 3bc1d4e91e4a6951b7b86ade9aa006684200241bbf908a8d68eb68921d538938
fetched_at: '2026-06-29T00:10:37.848631+00:00'
page_id: '542151148'
product: rm
source: tdn-rm
title: 8430634 FISCAL01-12571 DT Evento R-2050 - Notas canceladas no Reinf
type: documentation
url: https://tdn.totvs.com/display/LRM/8430634+FISCAL01-12571+DT+Evento+R-2050+-+Notas+canceladas+no+Reinf
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Geração de Eventos da Reinf |
| Ticket: | 8430634 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12571 |

## **02. SITUAÇÃO/REQUISITO**

Na geração dos eventos periódicos Reinf, evento R-2050, o sistema está gerando no arquivo xml, valores das notas com status de Cancelado, porém no manual da Reinf não existe um evento/campo onde sejam encaminhadas as informações de notas canceladas.

## **03. SOLUÇÃO**

Funcionalidade: Gerar Evento R-2050  
Cenário I:   
  
Dado que estão cadastrados lançamentos com status normal, cancelado, estorno e extemporâneo  
E todas possuem o tributo FUNRURAL,  
Ao executar o processo de gerar eventos da Reinf,  
Então só devem ser gerados eventos R-2050 referentes aos lançamentos com status normal.
