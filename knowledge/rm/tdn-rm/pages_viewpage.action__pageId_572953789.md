---
content_hash: 57b6ab52d5e7d84072291dd56157d2e9cc7d6be65b6a43328e658c4153c152f3
fetched_at: '2026-06-29T00:10:52.846191+00:00'
page_id: '572953789'
product: rm
source: tdn-rm
title: Layout - Parâmetros do Sindicato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572953789
version: 5
---

* **Parâmetros**

Para a importação dos parâmetros do sindicato, é necessário preencher os diversos dados conforme a tabela APARCOL. Segue abaixo a lista de parâmetros e campos que não podem ser nulos.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Descrição | Tipo | Tamanho | Coluna | Nro Campo |
| Código | String | 4 | 1 | 1 |
| Descrição | String | 60 | 6 | 2 |
| Tempo mínimo entre batidas | Hora | 5 | 67 | 3 |
| 1a. Faixa de hora extra normal | Hora | 6 | 73 | 4 |
| 2a. Faixa de hora extra normal | Hora | 6 | 80 | 5 |
| 3a. Faixa de hora extra normal | Hora | 6 | 87 | 6 |
| 4a. Faixa de hora extra normal | Hora | 6 | 94 | 7 |
| 5a. Faixa de hora extra normal | Hora | 6 | 101 | 8 |
| 1a. Faixa hora extra em dia de descanso | Hora | 6 | 108 | 9 |
| 1a. Faixa hora extra em dia de feriado | Hora | 6 | 115 | 10 |
| 1a. Faixa hora extra em dia de compensado | Hora | 6 | 122 | 11 |
| Carência semanal do DSR | Hora | 6 | 129 | 12 |
| Considera intervalo para o cálculo do DSR | Inteiro | 1 | 136 | 13 |
| Usa tabela de atraso por dia | Inteiro | 1 | 138 | 14 |
| Considera feriado para o cálculo do DSR | Inteiro | 1 | 140 | 15 |
| Considera intervalo para horário flexível | Inteiro | 1 | 142 | 16 |
| Dia da semana considerado como de DSR | Inteiro | 1 | 144 | 17 |
| Usa controle de saídas intermediárias | Inteiro | 1 | 146 | 18 |
| Código do abono de saídas intermediárias | String | 4 | 148 | 19 |
| Controla limite de horas por dia | Inteiro | 1 | 153 | 20 |
| Limite de horas por dia | Hora | 5 | 155 | 21 |
| Compensa extras de descanso no banco de horas por período | Inteiro | 1 | 161 | 22 |
| Percentual de extras de descanso para a compensação | Valor | 15 | 163 | 23 |
| Compensa extras de compensado no banco de horas por período | Inteiro | 1 | 179 | 24 |
| Percentual de extras de compensado para a compensação | Valor | 15 | 181 | 25 |
| Compensa extras de feriado no banco de horas por período | Inteiro | 1 | 197 | 26 |
| Percentual de extras de feriado para a compensação | Valor | 15 | 199 | 27 |
| Percentual de extras normais para a compensação | Valor | 15 | 215 | 28 |
| Distribui extra considerando jornada | Inteiro | 1 | 231 | 29 |
| Utiliza banco de horas | Inteiro | 1 | 233 | 30 |
| Tipo de banco de horas | Inteiro | 1 | 235 | 31 |
| Desconsidera atraso para DSR | Inteiro | 1 | 237 | 32 |
| Início da compensação do banco de horas | Inteiro | 1 | 239 | 33 |
| Indica banco de horas por ocorrência | Inteiro | 1 | 241 | 34 |
| Calcula adicional noturno para o intervalo de refeição | Inteiro | 1 | 243 | 35 |
| Considera feriado de acordo com a 1ª batida do horário | Inteiro | 1 | 245 | 36 |
| Utiliza limite mínimo de horas semanais | Inteiro | 1 | 247 | 37 |
| Limite de horas por semana | Hora | 5 | 249 | 38 |
| Controla limite de horas por semana | Inteiro | 1 | 255 | 39 |
| Limite de horas mínimo semanais | Hora | 5 | 257 | 40 |
| Opção para considerar a tabela de extra | Inteiro | 1 | 263 | 41 |
| Considera. feriado a partir da saída da jornada | Inteiro | 1 | 265 | 42 |
| Desc. tempo mínimo batidas refeitório | Inteiro | 1 | 267 | 43 |
| Desc. jornada na volta de férias/afast. | Inteiro | 1 | 269 | 44 |
| Cons. jornada no início de férias/afast. | Inteiro | 1 | 271 | 45 |
| Número de horas de falta | Hora | 5 | 273 | 46 |
| Acrescenta a nona hora às horas extras | Inteiro | 1 | 279 | 47 |
| Cons. dist. extra jor. comp.,desc.,fer. | Inteiro | 1 | 281 | 48 |
| Cons. percentual ad. noturno | Inteiro | 1 | 283 | 49 |
| Cons. nona hora total | Inteiro | 1 | 285 | 50 |
| Insere int. refeição realizado ad.not. | Inteiro | 1 | 287 | 51 |
| Desc. lim. refeição sem total batidas | Inteiro | 1 | 289 | 52 |
| Cons. Falta por falta de batida | Inteiro | 1 | 291 | 53 |
| Cons. Extra autorizada após compensação | Inteiro | 1 | 293 | 54 |
| Op. Extras normais banco de horas diário  0 = Compensar  1 = Pagar | Inteiro | 1 | 295 | 55 |
| Op. Atraso banco de horas diário  0 = Compensar  1 = Descontar | Inteiro | 1 | 297 | 56 |
| Op. Falta banco de horas diário  0 = Compensar  1 = Descontar | Inteiro | 1 | 299 | 57 |
| Op. Extra de Feriado banco de horas diário  0 = Compensar  1 = Pagar | Inteiro | 1 | 301 | 58 |
| Op. Extra de Descanso banco de horas diário  0 = Compensar  1 = Pagar | Inteiro | 1 | 303 | 59 |
| Op. Extra de Compensado banco de horas diário  0 = Compensar  1 = Pagar | Inteiro | 1 | 305 | 60 |
| Início do perí[odo.de](http://odo.de) Adicional noturno | Hora | 5 | 307 | 61 |
| Fim do período de Adicional notruno | Hora | 5 | 313 | 62 |
| Considera Tabela de extra/atraso após compensação  0 = Não Considerar  1 = Considerar | Inteiro | 1 | 319 | 63 |
| Tolerância sobre refeição na entrada posterior  0 = Não Considerar  1 = Considerar | Iteiro | 1 | 321 | 64 |
| Desconsidera intervalo de refeição em feriado  0 = Considerar  1 = Desconsiderar | Inteiro | 1 | 323 | 65 |
| Desconsidera jornada após feriado  0 = Considerar  1 = Desconsiderar | Inteiro | 1 | 325 | 66 |
| Considera Compensação por Jornada  0 = Não Considerar  1 = Considerar | Inteiro | 1 | 327 | 67 |
| Considera tempo mínimo para batidas de acesso  0 = Desconsiderar  1 = Considerar | Inteiro | 1 | 329 | 68 |
| Considera tolerância após dia ponte  0 = Desconsiderar  1 = Considerar | Inteiro | 1 | 331 | 69 |
| Considera D. S. R. proporcional  0 = Desconsiderar  1 = Considerar | Inteiro | 1 | 333 | 70 |
| Controla limite de extras por semana  0 = Não controlar  1 = Controlar | Inteiro | 1 | 335 | 71 |
| Limite de extras por semana | Inteiro | 3 | 337 | 72 |
| Considera Extras até o fim da jornada  0 = Desconsiderar  1 = Considerar | Inteiro | 1 | 343 | 73 |
| Considera falta último dia do período sem batida  0 = Desconsiderar  1 = Considerar | Inteiro | 1 | 345 | 74 |
| Considera jornada de trabalho para Distribuição das Extras  0 = Desconsiderar  1 = Considerar | Inteiro | 1 | 347 | 75 |
| Distribui adicional noturno considerando a jornada  0 = Desconsiderar  1 = Considerar | Inteiro | 1 | 349 | 76 |
| Paga adicional noturno sobre extras realizadas  0 = Não pagar  1 = Pagar | Inteiro | 1 | 351 | 77 |
| Calcula funcionário sem movimento  0 = Não calcular  1 = Calcular | Inteiro | 1 | 353 | 78 |
| Não insere horas do Int. Ref. Adc. Noturno  0 = Não inserir  1 = Inserir | Inteiro | 1 | 355 | 79 |
| Cons. extra noturna considerando percent  0 = Desconsiderar  1 = Considerar | Inteiro | 1 | 357 | 80 |
| Abate tolerância de Adicional Noturno  0 = Não abater  1 = Abater | Inteiro | 1 | 359 | 81 |
| Cons. Faixas Extras por Intervalo Horas | Inteiro | 1 | 361 | 82 |
| Ação dos eventos calculados por fórmula | Inteiro | 1 | 363 | 83 |
| Tipo carência DSR  D = Diária  S = Semanal | String | 1 | 365 | 84 |
| Não considera DSR feriado coincide descanso | Inteiro | 1 | 367 | 85 |
| Não calcula extra adicional noturno horário flexível | Inteiro | 1 | 369 | 86 |
