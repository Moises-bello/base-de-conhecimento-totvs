---
article_id: 4414843897879
category: SIGAEST - LEGAIS
content_hash: 583021774c644a0884c01e99ac22b695030698ee8793003b8de3acb68eb98f78
fetched_at: '2026-06-28T22:38:51.816944+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais são as tabelas
  geradas no processamento do SPED Fiscal para os Registros do Bloco K?
type: support-article
updated_at: '2022-10-11T19:50:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414843897879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-s%C3%A3o-as-tabelas-geradas-no-processamento-do-SPED-Fiscal-para-os-Registros-do-Bloco-K
---

**Dúvida**Quais são as tabelas geradas no processamento do SPED Fiscal para os Registros do Bloco K?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Veja abaixo a relação das tabelas geradas no SPED e o Registro do Bloco K correspondente:

|  |  |
| --- | --- |
| **Tabela Gerada no SPED** | **Registro Correspondente** |
| D3H | Registro K100 |
| D3I | Registro K200 |
| D3J | Registro K210 |
| D3L | Registro K215 |
| D3M | Registro K220 |
| D3N | Registro K250 |
| D3O | Registro K255 |
| D3P | Registro K280 |
| D3R | Registro K300 |
| D3S | Registro K301 |
| D3T | Registro K302 |
| D3U | Registro K990 |
| SVS | Registro K230 |
| SVT | Registro K235 |
| SVU | Registro K290 |
| SVV | Registro K291 |
| SVW | Registro K292 |
| T4E | Registro K260 |
| T4G | Registro K270 |
| T4H | Registro K275 |

**Observações**:

- No padrão, não há um relatório ou rotina que permita o usuário comparar os dados da tabela original do movimento (SD1, SD2, SD3) com as tabelas que montam os registros do Bloco K.

- Caso o usuário queira fazer um comparativo de algum determinado movimento que não foi considerado na geração do Bloco K, pode-se efetuar uma query comparando os registros da tabela do Bloco K com os registros da tabela do movimento.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
