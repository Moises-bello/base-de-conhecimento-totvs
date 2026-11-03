---
content_hash: 112ed5674a185f036b4c95c9a1e38519beea8888c044d74ecdf8662f775ad727
fetched_at: '2026-06-29T00:11:45.033839+00:00'
page_id: '819051643'
product: rm
source: tdn-rm
title: DT - Fracionamento de Jobs - Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819051643
version: 21
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Geração de Lançamento Financeiros |
| País: | Brasil |
| Story : | [DRHCALCRM-3064](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3064) |

## **0. SITUAÇÃO/REQUISITO**

Atualmente o sistema não permite o fracionamento de JOBs no processo de Geração de Lançamentos Financeiros.

## **03. SOLUÇÃO**

Implementado o recurso de Fracionamento de JOBs para o processo de Geração de Lançamentos Financeiros no módulo TOTVS Folha de Pagamento.

Para habilitar o recurso é necessário:

* O host ou Service Host estar configurado com JobServer3Camadas = True
* Cadastrar a classe de processo FopRotinasLancFinanceiroProcess em Ambiente | Processos | Segurança de Jobs Fracionáveis, para o perfil que terá acesso

Com esta implementação tivemos mais de 60% de ganho na performance.

## **04. DEMAIS INFORMAÇÕES**

Algumas evidência de ganho relacionadas ao processo:

Cenário: Agrupados por Seção: todos os lançamentos (exceto o líquido de rescisão). Com o total de funcionário 23831. Total de lançamentos: 80 

| Sem Fracionamento de Jobs | Com Fracionamento de Jobs |
| --- | --- |
| Início do cálculo: 21/12/2023 21:46:35  Fim do cálculo: 21/12/2023 23:06:03  Tempo total do cálculo: 01:19:28 | Início do cálculo: 23/12/2023 10:50:05  Fim do cálculo: 23/12/2023 11:23:42  Tempo total do cálculo: 00:33:37 |

Cenário: Agrupados por Seção: todos os lançamentos (exceto o líquido de rescisão). Com o total de funcionário 84558.  Total de lançamentos: 75

| Sem Fracionamento de Jobs | Com Fracionamento de Jobs |
| --- | --- |
| Início do cálculo: 29/12/2023 13:10:59  Fim do cálculo: 29/12/2023 21:46:47  Tempo total do cálculo: 08:35:47 | Início do cálculo: 29/12/2023 22:01:29  Fim do cálculo: 30/12/2023 01:27:31  Tempo total do cálculo: 03:26:01 |

**O recurso de Fracionamento de Jobs não contempla os Lançamentos Financeiros quando os mesmos são Gerados individuais por funcionário e/ou dependentes.ATENÇÃO**
