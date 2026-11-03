---
content_hash: f7e422c576872771b920f11dcf785028d9412d9f4b314e22b228a6ac653c5eee
fetched_at: '2026-06-29T00:12:00.684629+00:00'
page_id: '883666460'
product: rm
source: tdn-rm
title: DT - AEJ Portaria 671/2021 - Adequação REPs utilizados - Registros 02 e 05
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=883666460
version: 12
---

## **01. DADOS GERAIS**

| **Produto:** | **RM** |
| --- | --- |
| **Linha de Produto:** | **Linha RM** |
| **Segmento:** | **RH** |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Função:** | **AEJ Portaria 671/2021** |
| **País:** | **Brasil** |
| **Requisito/Story/Issue:** | **[DRHJORNRM-6700](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6700)** |

## **02. VERSÕES**

* A partir dos patches:

  + 12.1.2402.242
  + 12.1.2406.180
  + 12.1.2410.116

## **03. SITUAÇÃO/REQUISITO**

Para o registro do tipo "02" não será apresentado os dados INPI e Para o registro "05" quando existir batidas inseridas manualmente não será demonstrado o identificador do Rep**.**

## **04. SOLUÇÃO**

Ajustado o relatório AEJ para os registros de tipos "02" e "05".

## **05. EXEMPLO**

**Exibição Registro do tipo "02"**

Caso exista apenas batidas manuais não serão listado nenhum rep, ou apenas rep vinculado a batidas coletadas.

**Exibição Registro do tipo "05", campo 04 .**

Para batidas inseridas manualmente , não será mais exibido o Identificador do REP ficando o campo vazio.

## **06. ASSUNTOS RELACIONADOS**

* [DT - AEJ Portaria 671/2021 - Adequação do número sequencial dos pares das batidas de acordo com a jornada realizada](https://tdn.totvs.com/pages/viewpage.action?pageId=845421464)
