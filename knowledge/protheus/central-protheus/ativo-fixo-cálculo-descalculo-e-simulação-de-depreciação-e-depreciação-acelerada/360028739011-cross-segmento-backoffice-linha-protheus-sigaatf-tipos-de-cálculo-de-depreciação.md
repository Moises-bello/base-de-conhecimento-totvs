---
article_id: 360028739011
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: baaf6dacebb657b1444065b83ffebd964accb9263e814e5dd14b32345c17f00c
fetched_at: '2026-06-28T22:41:43.183094+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF -  Tipos de Cálculo de
  Depreciação
type: support-article
updated_at: '2025-11-26T12:51:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028739011-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Tipos-de-C%C3%A1lculo-de-Deprecia%C3%A7%C3%A3o
---

**Dúvida**

Utilização dos métodos de depreciação gerencial  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Ativo fixo -  A partir da versão 11.80

**Solução**

Conforme análise dos métodos de depreciação gerenciais comumente utilizados pelos profissionais de contabilidade e patrimônio, estão disponíveis no sistema, as seguintes opções de cálculo:

* Depreciação Gerencial: Linear ou Quotas Constantes
* Depreciação Gerencial: Soma dos Dígitos
* Depreciação Gerencial: Redução de saldos;
* Depreciação Gerencial: Unidades produzidas;
* Depreciação gerencial: Horas trabalhadas;
* Depreciação Gerencial: Linear com valor máximo de depreciação.

No link abaixo, é possível consultar o procedimento para a parametrização de cada tipo de cálculo de depreciação:  
[Tipos de cálculo de depreciação](https://tdn.totvs.com/pages/releaseview.action?pageId=6067612)

Para gerar o movimento de cálculo referente aos tipos de depreciação (N3\_TPDEPR) 4, 5, 8 e 9, respectivamente:

```
4 - Unidades Produzidas

5 - Horas Trabalhadas

8 - Exaustão Linear

9 - Exaustão por Saldo Residual
```

É necessário que a procedure esteja instalada e que o parâmetro MV\_ATFCTAP seja configurado para determinar se o apontamento de produção será realizado pela rotina ATFA110.

Para gerar o movimento de cálculo utilizando a rotina de apontamento de produção (ATFA110), consulte as informações disponíveis na documentação a seguir.

[Cross Segmento - Backoffice Linha Protheus - SIGAATF - DEPRECIAÇÃO POR EXAUSTÃO E APONTAMENTOS DE PRODUÇÃO - ATFA110](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015627052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-DEPRECIA%C3%87%C3%83O-POR-EXAUST%C3%83O-E-APONTAMENTOS-DE-PRODU%C3%87%C3%83O-ATFA110?source=search)

[Ativos com apontamento de produção](https://tdn.totvs.com/pages/releaseview.action?pageId=642962012)

**Saiba mais**

[CPC - Impactos da Convergência Contábil entre IFRS e CPC nos Módulos da Controladoria Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=347451139)

[Classificação de Ativos N3\_TIPO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035878114-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Tipos-de-ativo-campo-N3-TIPO-)

[Depreciação de Ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007812091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Deprecia%C3%A7%C3%A3o-de-Ativo?source=search)
