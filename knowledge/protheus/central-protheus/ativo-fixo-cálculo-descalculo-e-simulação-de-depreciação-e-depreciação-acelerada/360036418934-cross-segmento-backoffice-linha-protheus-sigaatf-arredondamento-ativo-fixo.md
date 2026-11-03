---
article_id: 360036418934
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 5645d78f50c1b2f733b0a62e2d4a498d44e4769806d991e2c459f017924f078b
fetched_at: '2026-06-28T22:41:43.237570+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ARREDONDAMENTO ATIVO
  FIXO
type: support-article
updated_at: '2023-11-30T17:20:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036418934-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ARREDONDAMENTO-ATIVO-FIXO
---

**Ocorrência**  
 No módulo Ativo Fixo, ao realizar o Cálculo de depreciação (ATFA050), o valor é calculado com arredondamento indevido.

**Ambiente**

Protheus - Contabilidade Gerencial – A partir da versão 12

**Solução**  
 Para solucionar essa ocorrência, configure a instrução FloatingPointPrecise.

Exemplo:

```
[General]
FloatingPointPrecise=1
```

em seu AppServer.ini

Para maiores detalhes: <https://tdn.totvs.com/display/tec/FloatingPointPrecise>

OBS: O arredondamento do ativo funciona baseado nas regras matemáticas.

Portanto, quando o algarismo imediatamente seguinte ao último algarismo a ser conservado for igual ou superior a 5 for seguido de no mínimo um algarismo diferente de zero, o último algarismo a ser conservado deverá ser aumentado de uma unidade.

Exemplo A: 1,666 6 arredondado à primeira decimal temos: 1,7.  
Exemplo B: 4,850 5 arredondados à primeira decimal temos: 4,9
