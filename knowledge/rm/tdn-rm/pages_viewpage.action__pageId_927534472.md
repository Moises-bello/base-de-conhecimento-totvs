---
content_hash: 6a33fdbaa732c50e0ee592c9528c3c699e8bc99b5f90f35fa492f0c63f83ed4a
fetched_at: '2026-06-29T00:12:07.899407+00:00'
page_id: '927534472'
product: rm
source: tdn-rm
title: FISCAL01-25100 - PIS\COFINS Guia de Recolhimento diferentes Código de receita
  iguais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=927534472
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Período de Apuração, GuiaDARF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25100 |

## **02. SITUAÇÃO/REQUISITO**

No processo de geração automático da guia DARF no Período de apuração PIS COFINS configurado nos Parâmetros de Rotina como principal, para empresas cujo regime é PIS/COFINS cumulativo e não cumulativo, cada uma das guias estavam sendo preenchidas com o mesmo código de receita.

## **03. SOLUÇÃO**

Foi implementado a busca do código da receita com base na chave específica do regime (cumulativo/não cumulativo), cadastrada no anexo Obrigações Acessórias > Rotina Fiscal > Parâmetros da Rotina.

Documentação com informações mais detalhadas do processo:  
[Guias DARF - Linha RM - TDN](https://tdn.totvs.com/display/LRM/Guias+DARF)

Disponível à partir da biblioteca 12.1.2406
