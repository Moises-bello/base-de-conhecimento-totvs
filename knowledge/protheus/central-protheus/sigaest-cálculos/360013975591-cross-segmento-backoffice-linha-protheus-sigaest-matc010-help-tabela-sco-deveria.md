---
article_id: 360013975591
category: SIGAEST - CÁLCULOS
content_hash: 56181bcaa625ac3e13dbc470c10a9084362d3b3a4b9ac434e3db48e94fc593c9
fetched_at: '2026-06-28T22:39:04.016398+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATC010 - HELP Tabela
  SCO deveria conter dados autocontidos
type: support-article
updated_at: '2025-03-12T12:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013975591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATC010-HELP-Tabela-SCO-deveria-conter-dados-autocontidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503168953623) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Ao acessar a rotina MATC010 é apresentado o help conforme imagem abaixo.

![HELP.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009480291)

**Ambiente**

Protheus - Estoque - à partir da verão 12.1.17

**Solução**

Para a correção do problema é preciso realizar a alimentação da tabela **SCO**, realizando o append via APSDU.

Verificar a configuração do parâmetro **MV\_REVPLAN**

1 – Faça o download do arquivo SCO.dtc no link do final do artigo;

2 – Descompacte e abra arquivo SCO.dtc via APSDU;

OBS: Antes de efetuar o append, caso necessário, faça o ajuste do campo filial para que se adapte ao usado em sua empresa.

3 – Abra a tabela SCO e faça o append do arquivo  SCO.dtc conforme imagem abaixo.

![TABELA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009480551)

Após a importação (append) o erro será corrigido.

OBS: **É importante que seja feita a correção do campo da filial conforme o padrão usado na empresa.**

**Saiba mais:**

*[MP - SIGAEST - Rotina Formação de Preço (MATC010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022184251-MP-SIGAEST-Rotina-Forma%C3%A7%C3%A3o-de-Pre%C3%A7o-MATC010-)*

*[Clique aqui e veja mais artigos sobre Cálculos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199493-SIGAEST-C%C3%81LCULOS)*

Arquivo disponível no link abaixo:
