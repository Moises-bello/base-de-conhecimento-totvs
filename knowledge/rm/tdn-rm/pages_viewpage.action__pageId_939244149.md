---
content_hash: e882288995ce503b89bbfd643ea92848fc2ee816c7d3208324d999ad3c1381e9
fetched_at: '2026-06-29T00:12:09.065442+00:00'
page_id: '939244149'
product: rm
source: tdn-rm
title: DT - Funcionário - Nacionalidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=939244149
version: 11
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Funcionário - Nacionalidade |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-13548](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13548 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2406.270
* 12.1.2410.222
* 12.1.2502.138 e superiores

## **03. SITUAÇÃO/REQUISITO**

Identificamos que a Tabela Dinâmica "INT08 - Nacionalidade" da Folha de Pagamento, bem como o cadastro de Nações localizado no menu eSocial, apresentam a nacionalidade **249 - China (Taiwan)** de forma unificada. No entanto, ao analisarmos a **Tabela 06 - Países** do leiaute do eSocial, versão S-1.3, constatamos que **China** e **Taiwan** são tratados como nacionalidades distintas.

## **04. SOLUÇÃO**

Adequamos o cadastro de nacionalidades no sistema, com a separação de **China** e **Taiwan** conforme previsto na T**abela 06 do eSocial**, a fim de garantir conformidade com o leiaute oficial e evitar inconsistências no envio dos eventos do eSocial.

Para que a correção seja aplicada, é necessário executar o **RM.Atualizador.exe** do sistema.  
Após a execução, a tabela **INT08 - Nacionalidade** será atualizada, passando a exibir a nacionalidade **Taiwan** de forma separada, conforme previsto na **Tabela 06 - Países** do leiaute do eSocial (versão S-1.3).
