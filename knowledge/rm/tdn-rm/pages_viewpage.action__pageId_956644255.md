---
content_hash: 7aa06078721f98c714956e79479243d7d5a6cf70524ec8f757f6703a2393a35b
fetched_at: '2026-06-29T00:12:13.445944+00:00'
page_id: '956644255'
product: rm
source: tdn-rm
title: Fracionamento de jobs inteligente (Geração de lançamentos em lote)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=956644255
version: 8
---

A partir das versões **12.1.2410.258,  12.1.2502.161, 12.1.2506.160**, foi disponibilizado o fracionamento de jobs inteligente para Geração de Lançamentos em Lote.

Com o parâmetro de "**Fracionamento de Jobs Inteligente**" ativo: O Fracionamento Inteligente é acionado durante a **Geração de Lançamentos em Lote**. É realizado um cálculo para obter o número de frações permitindo que os jobs sejam finalizados em menor tempo.

Importante

O fracionamento de jobs inteligente, está programado para funcionamento apenas em ambiente que tenha suporte a execução com mais de 20 jobs em paralelo.

Segue um exemplo do funcionamento (**Tal exemplo foi executado em um ambiente preparado para benchmark**):

Em um ambiente com suporte a 160 jobs em paralelo, configurado para geração de lançamentos com 30 jobs, foram enviadas requisições em paralelo de níveis de ensino e filiais diferentes dentro da mesma coligada. Todas requisições foram programadas para executar as 16:30, abaixo segue uma tabela com os dados das requisições e tempo do processo.

No total foram enviados 185 mil parcelas para geração de lançamento não contábil e sem baixa automática com o total de 150 frações, a soma dos tempos de execução foi de 1h16min, e o tempo de execução 36min conforme tabela abaixo:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Geração de lançamentos com concorrência | | | | | | | |
| Quantidade Lançamentos | Número de Jobs | Código Coligada | Classe do Processo | Status | Iniciado Em | Finalizado Em | Tempo de execução |
| 5.000 | 30 | 5 | EduGeraLancSliceableData | OK | 20/06/2025 16:30:01 | 20/06/2025 16:33:41 | 0:03 |
| 10.200 | 30 | 5 | EduGeraLancSliceableData | OK | 20/06/2025 16:30:02 | 20/06/2025 16:36:38 | 0:06 |
| 20.000 | 30 | 5 | EduGeraLancSliceableData | OK | 20/06/2025 16:30:01 | 20/06/2025 16:40:37 | 0:10 |
| 50.000 | 30 | 5 | EduGeraLancSliceableData | OK | 20/06/2025 16:30:02 | 20/06/2025 16:48:46 | 0:18 |
| 100.000 | 30 | 5 | EduGeraLancSliceableData | OK | 20/06/2025 16:30:01 | 20/06/2025 17:06:46 | 0:36 |

O mesmo processamento utilizando o fracionamento de jobs inteligente teve diferença de tempo.

O fracionamento inteligente fez o cálculo da melhor quantidade de frações por quantidade de lançamentos, a criação de menos frações na fila fez com que o processo fosse executado em menor tempo.

No exemplo não foram utilizados jobs acima do limite e ainda sim houve ganho na soma dos tempos e também no total do processamento.

A soma do tempo para os mesmos 185 mil lançamentos em paralelo, utilizando fracionamento inteligente, teve um total de 1h06min promovendo um ganho de 10min, já o tempo de execução foi de 21min usando 132 frações, conforme tabela abaixo:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Geração de lançamentos com concorrência | | | | | | | |
| Quantidade Lançamentos | Número de Jobs | Código Coligada | Classe do Processo | Status | Iniciado Em | Finalizado Em | Tempo de execução |
| 5.094 | 8 | 5 | EduGeraLancSliceableData | OK | 24/06/2025 17:40:04 | 24/06/2025 17:48:07 | 0:08 |
| 10.194 | 13 | 5 | EduGeraLancSliceableData | OK | 24/06/2025 17:40:03 | 24/06/2025 17:50:25 | 0:10 |
| 20.394 | 21 | 5 | EduGeraLancSliceableData | OK | 24/06/2025 17:40:02 | 24/06/2025 17:52:06 | 0:12 |
| 50.010 | 40 | 5 | EduGeraLancSliceableData | OK | 24/06/2025 17:40:04 | 24/06/2025 17:55:07 | 0:15 |
| 101.994 | 50 | 5 | EduGeraLancSliceableData | OK | 24/06/2025 17:40:03 | 24/06/2025 18:01:21 | 0:21 |

Concluímos que o fracionamento de jobs inteligente calcula a melhor proporção de "quantidade de lançamentos/frações" gerando menos itens na fila, o que diminui o tempo de execução do processo total.

Como visto nos exemplos, os processos foram executados em paralelo, no cenário 1 as execuções foram agendadas no dia 20/06/2025 as 16:30 e no cenário 2 os agendamentos foram no dia 24/06/2025 as 17:40.

No cenário 1 foram enviadas no total 150 frações sendo que as frações com maior quantidade demoraram mais tempo na fila.

Ao ajustar o número de frações de forma proporcional a quantidade de lançamentos, nos últimos testes, com valores calculados foi possível executar os 185 mil lançamentos em 21 minutos com menos frações esperando na fila.

## Configurando fracionamento de jobs inteligente:

1. *Configurações / Parâmetros / Integração / Financeiro / Fin – Geral 3/4*

Ao marcar o parâmetro de "Geração de lançamentos com fracionamento de jobs inteligente", um alerta informando os limites relacionados a quantidade mínima de geração de 20 lançamentos em paralelo é exibido:

Com o parâmetro marcado, ao executar o processo de "Geração de Lançamentos em Lote":

A quantidade de itens informada para fracionamento pode ser desconsiderada e o fracionamento calcular uma nova quantidade.

Ao clicar no botão executar, um alerta é exibido informando que a quantidade de jobs solicitada pode ser alterada:

(O Fracionamento de Jobs Inteligente será acionado apenas se já existirem outras solicitações de geração de lançamento sendo executadas)
