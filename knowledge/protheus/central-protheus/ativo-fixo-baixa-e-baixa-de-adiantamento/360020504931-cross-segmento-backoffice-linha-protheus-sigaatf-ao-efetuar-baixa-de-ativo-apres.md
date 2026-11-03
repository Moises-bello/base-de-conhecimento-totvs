---
article_id: 360020504931
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: ff321a1de7ea0fa97103de6387e207092db688a6729fc68390ae5804b6468187
fetched_at: '2026-06-28T22:41:55.582401+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus- SIGAATF  AO EFETUAR BAIXA DE ATIVO
  APRESENTA HELP AFDTBAIXA
type: support-article
updated_at: '2024-11-22T16:55:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020504931-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-AO-EFETUAR-BAIXA-DE-ATIVO-APRESENTA-HELP-AFDTBAIXA
---

**Ocorrência**No módulo **Ativo Fixo**, ao tentar realizar (o processo ou a rotina) **Baixa de Ativo**  é apresentada o Help **AFDTBAIXA**

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus  - Ativo Fixo  – A partir da versão 11.80 **Causa**

Pode ocorrer o help acima quando existe alguma divergência de DATA.

**Solução**

Não aceita a data da baixa se houver ocorrência de baixa  posterior ou movimentação com a data da ultima depreciação. Verificar a data da baixa

Verifica se a data da baixa está entre os meses, imediatamente anterior e imediatamente posterior ao ultimo calculo de depreciação

\* Data de baixa < data de aquisição

\* Data de baixa < mv\_ultdepr // pode ocorrer somente se tiver o parâmetro

\* Baixas com data anterior // verificar na tabela SN4 se tem registro de baixa anterior ao que tenta executar

\* Conforme regra padrão, não aceita movimentos fora do mês posterior ao ultimo calculo de depreciação, e nem anteriores ao ultimo calculo

 data de baixa > mv\_ultdepr + (1mês) ou data de baixa <= mv\_ultdepr
