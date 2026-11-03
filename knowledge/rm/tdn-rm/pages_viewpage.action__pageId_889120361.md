---
content_hash: cb8888148d54e8a2cc346b67ac9e0db449e65acd10a08677372787f7366a0e34
fetched_at: '2026-06-29T00:12:01.240101+00:00'
page_id: '889120361'
product: rm
source: tdn-rm
title: DT - Dashboard Ponto -Indicadores de funcionários - Férias_Afastamento_Feriado_Descanso
  e Compensado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=889120361
version: 9
---

## **01. DADOS GERAIS**

| **Produto:** | **RM** |
| --- | --- |
| **Linha de Produto:** | **Linha RM** |
| **Segmento:** | **RH** |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Função:** | **Relatório Dashboard** |
| **País:** | **Brasil** |
| **Requisito/Story/Issue:** | **[DRHJORNRM-6953](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6953)** |

## **02. VERSÕES**

* A partir dos patches:

  + 12.1.2406.192
  + 12.1.2410.126

## **03. SITUAÇÃO/REQUISITO**

O sistema está apresentando funcionários que não vão trabalhar no dia selecionado como férias, afastamento, descanso e compensado no indicador de funcionários sem marcação.

## **04. SOLUÇÃO**

Para os dias compensado, descanso, feriado e extra Normal (Batida Nula), caso o colaborador não tenha efetuado batidas, o sistema irá considerar como Pontos completos.

Para os funcionários que estiverem de férias/afastamento não serão considerados nos indicadores.

## **05. EXEMPLO  :**

**No dia  09/11/2024 é um dia de compensado.**

**Ao consultar o Dashboard de Marcações, será demonstrado em pontos Completos.**

## **06. ASSUNTOS RELACIONADOS**

* [Dashboard Ponto](https://tdn.totvs.com/display/public/LRM/Dashboard)
* [Dashboard Ponto - Gera os indicadores de Funcionários e Marcações](https://tdn.totvs.com/pages/releaseview.action?pageId=862603660)
