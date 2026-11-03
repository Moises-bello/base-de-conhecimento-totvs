---
article_id: 360018247651
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 02d102d455a45dad9bd7eb6da2a86a0c2e38e42c66c188aa6d321c234e244a66
fetched_at: '2026-06-28T22:41:05.109087+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA211 - Limitação número
  documento na apuração de resultado
type: support-article
updated_at: '2022-04-20T17:49:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018247651-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Limita%C3%A7%C3%A3o-n%C3%BAmero-documento-na-apura%C3%A7%C3%A3o-de-resultado
---

**Dúvida**Qual e a limitação do número do documento na apuração de resultado  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

Ao executar a rotina Apuração de Resultados(CTBA211), caso informado nas perguntas  "Lote", "Sub-Lote" e "Documento" os valores 999999, 999 e 999999 respectivamente, o sistema poderá não concluir o processamento, uma vez que o valor máximo atingiu o tamanho destinado a cada campo.

**Exemplo:**

Para o exemplo abaixo, se definido o parâmetro [MV\_NUMLIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006753632-MP-SIGACTB-MV-NUMLIN-MV-NUMMAN?source=search) para 999, não existe disponibilidade para apuração com mais de 999 linhas, pois as informações de Lote + SubLote + Documento chegaram ao seu limite

|  |  |
| --- | --- |
| Lote | 999999 |
| SubLote | 999 |
| Documento | 999999 |

Para minimizar esta ocorrência, foi implementado um bloqueio ao inicio do processamento alertando o usuário que este deve validar as informações contidas nas perguntas  "Lote", "Sub-Lote" e "Documento" , levando em consideração o parametro MV\_NUMLIN.

Durante a Apuração de Resultados, foi inserido a validação para o número de documento, uma vez que existe a limitação deste número até 999999 quando definido o LOTE e SUBLOTE como 999999 e 999.

O Número máximo do documento deve ser 999000, deixando assim a quantidade de 998 lotes disponíveis para efeito de apuração.

Quanto menor este número, maior será a disponibilidade de Lotes durante a apuração.

O Administrador do Sistema, deve avaliar a quantidade de Linhas normalmente utilizada nos lotes, conferir o parâmetro MV\_NUMLIN e chegar no número ideal, orientado o K-user do sistema a não ultrapassar o número definido.

**Exemplo1:**

LOTE: 999999

SUBLOTE: 999

DOCUMENTO: 999999

MV\_NUMLIN: 10

Quantidade de Lotes: 998

Quantidade de Registros:  9980

**Exemplo2:**

LOTE: 999999

SUBLOTE: 999

DOCUMENTO: 999999

MV\_NUMLIN: 10

Quantidade de Lotes: 998

Quantidade de Registros:  9980
