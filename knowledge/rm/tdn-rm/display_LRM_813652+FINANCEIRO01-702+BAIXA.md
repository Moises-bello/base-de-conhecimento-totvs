---
content_hash: 486c64ba5fff64f2f20fb33ecdcf32c8f24362f81108d02a36d16a117f43ae49
fetched_at: '2026-06-29T00:08:34.264712+00:00'
page_id: '274655977'
product: rm
source: tdn-rm
title: 813652 FINANCEIRO01-702 BAIXA
type: documentation
url: https://tdn.totvs.com/display/LRM/813652+FINANCEIRO01-702+BAIXA
version: 96
---

# Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Função:** | Baixa. |
| **Situação/Requisito:** | Ao baixar um único lançamento, onde a data de default no lançamentos está coincidindo com final de semana ou feriado, o sistema não está sugerindo o próximo dia útil ou dia útil anterior conforme parametrização do sistema. |
| **Solução/Implementação:** | Quando nos parâmetros do sistema, os parâmetros “Aceita Baixas a Receber em finais de semana” e “Aceita Baixas a Pagar em finais de semana”, estiverem configurados para “Primeiro Dia Útil Posterior” ou “Primeiro Dia Útil Anterior”, o sistema irá sugerir automaticamente a Data do Útil conforme parametrização do sistema, observando os cenários abaixo:  Cenário 1 – Baixa de um lançamento.  Caso a “Data Default de Baixa a Pagar” ou “Data Default de Baixa a Receber” parametrizada, estiver em final de semana ou feriado, o sistema irá sugerir a data do dia útil conforme parametrizado.  Ex1: Lançamento a receber com Data de Previsão de Baixa 30/04/2017 (Domingo). Data Default de Baixa a Receber parametrizada com “Previsão de Baixa” e “Aceita Baixas a Pagar em finais de semana” configurado para “Primeiro Dia Útil Posterior”. O sistema irá buscar a data de previsão de baixa do lançamento 30/04/2017, como está data é domingo, e o sistema está parametrizado para “Primeiro Dia Útil Posterior”, irá buscar o próximo dia útil, como dia 01/05/2017 é dia do trabalhador (feriado), a data sugerida irá depender do calendário do sistema. Se o dia 01/05/2017 estiver como feriado no calendário do sistema, o dia de baixa sugerido será 02/05/2017, caso contrário 01/05/2017.  Ex2: Lançamento a receber com Data de Vencimento 30/04/2017 (Domingo). Data Default de Baixa a Receber parametrizada com “Data de Vencimento” e “Aceita Baixas a Pagar em finais de semana” configurado para “Primeiro Dia Útil Anterior”. O sistema irá buscar a data de vencimento do lançamento 30/04/2017, como está data é domingo, e o sistema está parametrizado para “Primeiro Dia Útil Anterior”, irá buscar o dia útil anterior, como dia 29/04/2017 é sábado, a data sugerida irá depender do parâmetro “Considerar Sábado como dia útil”. Se o sistema estiver configurado para considerar sábado como dia útil, o dia de baixa sugerido será 29/04/2017 (sábado), caso contrário 28/04/2017.  Cenário 2 – Baixa de vários lançamentos com datas iguais.  Caso a “Data Default de Baixa a Pagar” ou “Data Default de Baixa a Receber” parametrizada, de todos os lançamentos que estão sendo baixados forem iguais, o sistema irá apresentar a data do dia útil conforme parametrizado.    Ex1: Vários lançamentos a receber com Data de Previsão de Baixa 30/04/2017 (Domingo). Data Default de Baixa a Receber parametrizada com “Previsão de Baixa” e “Aceita Baixas a Pagar em finais de semana” configurado para “Primeiro Dia Útil Posterior”. O sistema irá verificar se as datas de previsão de baixa de todos os lançamentos são iguais, ou seja, 30/04/2017, se sim o sistema irá utilizar a data de previsão de baixa. como está data é domingo, e o sistema está parametrizado para “Primeiro Dia Útil Posterior”, irá buscar o próximo dia útil, como dia 01/05/2017 é dia do trabalhador (feriado), a data sugerida irá depender do calendário do sistema. Se o dia 01/05/2017 estiver como feriado no calendário do sistema, o dia de baixa sugerido será 02/05/2017, caso contrário 01/05/2017.  Ex2: Vários lançamentos a receber com Data de Vencimento 30/04/2017 (Domingo). Data Default de Baixa a Receber parametrizada com “Data de Vencimento” e “Aceita Baixas a Pagar em finais de semana” configurado para “Primeiro Dia Útil Anterior”. O sistema irá verificar se as datas de vencimento de todos os lançamentos são iguais, ou seja, 30/04/2017, se sim, como está data é domingo, e o sistema está parametrizado para “Primeiro Dia Útil Anterior”, irá buscar o dia útil anterior, como dia 29/04/2017 é sábado, a data sugerida irá depender do parâmetro “Considerar Sábado como dia útil”. Se o sistema estiver configurado para considerar sábado como dia útil, o dia de baixa sugerido será 29/04/2017 (sábado), caso contrário 28/04/2017.    Cenário 3 – Baixa de vários lançamentos com datas diferentes.  Caso a “Data Default de Baixa a Pagar” ou “Data Default de Baixa a Receber” parametrizada, de algum dos lançamentos que estão sendo baixados for diferente dos demais, o sistema irá sugerir a data de baixa como a data do sistema. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040. |

divs
