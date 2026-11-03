---
content_hash: 40f331674fd4d3e7c51e10bdf574651677e75cbbdc527c17c4fa5d8ff3f097fc
fetched_at: '2026-06-29T00:11:49.858654+00:00'
page_id: '839300061'
product: rm
source: tdn-rm
title: 7.2 EAI 2.0 - Contabilização por Regime de Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=839300061
version: 13
---

|  |  |
| --- | --- |
| **Descrição** | Reenvio da Contabilização por Regime de Competência - EAI 2.0 |
| **Observações** | Aplicável para SESI/SENAI. |

A partir dos patches 12.1.32.241, 12.1.33.177 e na versão 12.1.34 , o processo de Contabilização por Competência do Contrato do Aluno no TOTVS Educacional, ao término da integração para o BackOffice Protheus, a contabilização do RM será integrada automaticamente ao Lote Zero, quando os lançamentos contábeis forem integrados corretamente no Protheus.

Mas durante o processo de integração, em alguns casos, pode acontecer falha na integração entre RM e Protheus (por exemplo: Erro de timeout na comunicação com o servidor do Protheus, período fechado no Protheus, etc.). Quando uma dessas situações ocorrerem, a contabilização será registrada no RM, e o envio da integração para o Protheus ficará pendente, sendo possível posteriormente executar o processo de reenvio dessas contabilizações.

Ao clicar no menu Financeiro Contábil | Contabilização | “Lotes de Contabilizações por Competência para o Protheus”, o sistema irá apresentar todos os lotes com as contabilizações por competência do contrato pendentes de ser enviadas para o Protheus. Vale ressaltar que os lotes de contabilização e de estorno da contabilização são configurados no assistente de parametrização do TOTVS Educacional.

O usuário deverá selecionar o lote que tem contabilizações pendentes para serem integradas, e selecionar o processo "Executar Integração dos Lançamentos Contábeis - EAI 2.0" e será necessário confirmar a sua execução. O lote com contabilização pendente irá apresentar valor diferente de zero na coluna "Valor" na tela. O processo será executado sendo possível acompanhar a sua execução via tela de processo presente na parte inferior do sistema. Ao término da execução do processo, os lançamentos contábeis estarão integrados ao Lote Zero.

Para obter todo conteúdo referente a EAI 2.0 - Contabilização por Regime de Competência, acesse ao TDN:

* [Documentação completa](https://tdn.totvs.com/pages/releaseview.action?pageId=700993998)
