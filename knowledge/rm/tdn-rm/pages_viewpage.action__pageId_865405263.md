---
content_hash: eb14de194af423c4dcf6bd8d6be6aee60f5b8cb533a8ee6ee703ebd0c3df019b
fetched_at: '2026-06-29T00:11:56.361195+00:00'
page_id: '865405263'
product: rm
source: tdn-rm
title: DT - Fracionamento de JOBs - Cálculo do 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=865405263
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo do 13º Salário |
| País: | Brasil |
| Issue: | [DRHCALCRM-52](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-52) |

## **02. VERSÃO**

Este requisito estará disponível a partir dos patchs/Release abaixo:

* 12.1.2402.224
* 12.1.2406.151
* 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

Atualmente o produto não permite o fracionamento de JOBs para o Cálculo de 13º Salário.

## **04. SOLUÇÃO**

Implementado o recurso de Fracionamento de JOBs para o processo de Cálculo de 13º Salário no módulo TOTVS Folha de Pagamento.

Para Habilitar o recurso é necessário:

* O Host ou Service Host estar configurado com JobServer3Camandas = True
* Cadastrar a classe de processo FopLancamento13FracionadoProcess em Ambiente | Processos | Segurança de Jobs Fracionáveis, para o perfil que terá acesso

Com esta implementação podemos chegar em até 70% de ganho na performance do cálculo de 13º Salário.

## **05. DEMAIS INFORMAÇÕES**

Algumas evidências de ganho relacionadas ao processo:

Cenário: Lançamento da 2ª parcela de 13º Salário em base Oracle com 9812 funcionários. Foi utilizando 1 hot com 5 execuções simultâneas. O Fracionamento foi dividido em 4 Jobs e cada Job processou o cálculo para 2453 funcionários:

| Sem Fracionamento de Jobs | Com Fracionamento de Jobs | Ganho |
| --- | --- | --- |
| Início do Cálculo: 18:45:09  Fim do Cálculo: 19:56:03  Tempo total do Cálculo: 01:10:54 | Início do Cálculo: 21:12:39  Fim do Cálculo: 21:35:17  Tempo total do Cálculo: 00:22:38 | 68% |

Cenário: Lançamento da 2ª parcela de 13º Salário em base SQL com 2970 funcionários. Foi utilizando 1 hot com 5 execuções simultâneas. O Fracionamento foi dividido em 4 Jobs e cada 2 Job processou o cálculo para 742 funcionários e 2 Jobs processou o cálculo para 743 funcionários:

| Sem Fracionamento de Jobs | Com Fracionamento de Jobs | Ganho |
| --- | --- | --- |
| Início do Cálculo: 08:46:31  Fim do Cálculo: 08:57:48  Tempo total do Cálculo: 00:11:17 | Início do Cálculo: 08:35:10  Fim do Cálculo: 08:39:32  Tempo total do Cálculo: 00:04:22 | 64% |

Cenário: Lançamento da 1ª parcela de 13º Salário em base SQL com 2970 funcionários. Foi utilizando 1 hot com 5 execuções simultâneas. O Fracionamento foi dividido em 4 Jobs e cada 2 Job processou o cálculo para 742 funcionários e 2 Jobs processou o cálculo para 743 funcionários:

| Sem Fracionamento de Jobs | Com Fracionamento de Jobs | Ganho |
| --- | --- | --- |
| Início do Cálculo: 10:04:27  Fim do Cálculo: 10:16:12  Tempo total do Cálculo: 00:13:45 | Início do Cálculo: 10:40:39  Fim do Cálculo: 10:44:45  Tempo total do Cálculo: 00:04:06 | 70% |

**A configuração do ambiente, processos executando em paralelo, uso de fórmulas de cálculo, customizações, etc. podem interferir na performance do processo, não chegando a este ganho. Neste caso é necessário verificar estas e outras variáveis que podem comprometer o desempenho do cálculo do 13º Salário. IMPORTANTE!**

## **06. ASSUNTOS RELACIONADOS**

[TOTVS Folha de Pagamento - Fracionamento de Jobs](https://tdn.totvs.com.br/display/LRM/TOTVS+Folha+de+Pagamento+-+Fracionamento+de+Jobs)

[Lançamento de Decimo Terceiro Salário](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719506)
