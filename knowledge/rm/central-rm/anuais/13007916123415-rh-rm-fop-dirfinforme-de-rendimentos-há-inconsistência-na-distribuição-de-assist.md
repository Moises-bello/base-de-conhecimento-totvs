---
article_id: 13007916123415
category: Anuais
content_hash: f85069d1f1df5f4801a1a62380e23db8d2417f1d5ac1f1ea4b62c8cb44585c34
fetched_at: '2026-06-28T22:46:51.036171+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - DIRF/Informe de Rendimentos: Há inconsistência na distribuição
  de Assistência à Saúde para o titular'
type: support-article
updated_at: '2026-06-17T18:28:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13007916123415-RH-RM-FOP-DIRF-Informe-de-Rendimentos-H%C3%A1-inconsist%C3%AAncia-na-distribui%C3%A7%C3%A3o-de-Assist%C3%AAncia-%C3%A0-Sa%C3%BAde-para-o-titular
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min****Dúvida**Como corrigir o aviso de inconsistências encontradas distribuição de Assistência à Saúde para o titular durante a geração da rotina DIRF/Informe de Rendimentos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**

Ao realizar a geração do informe de rendimento, ocorre o seguinte aviso.

**Avisos encontrados para a Chapa: 'XXXXX - NOME FUNCIONÁRIO'  
Há inconsistência na distribuição de Assistência à Saúde para o titular: 'XXXXX - NOME FUNCIONÁRIO'. Na Operadora: 'OPERADORA DE SAÚDE'.  
Os valores dos dependentes: 'XXXX,XX' serão atribuídos ao Titular com valor atual de: -'XXX,XX'.**

O aviso referente a inconsistências na distribuição de Assistência à Saúde ocorre quando o valor do histórico está maior que o valor informado na Ficha Financeira. Assim, o sistema faz a subtração dos valores e a diferença encontrada é descontada do titular.

Toda a movimentação presente deve bater com a ficha financeira do funcionário, no exemplo a seguir, o histórico do mês 03 totaliza um valor de R$640,00 no evento indicado no histórico, porém ao comparar com ficha financeira, podemos verificar que não há este evento lançado, onde neste caso devemos verificar se os valores estão corretos e lançar os respectivos eventos na ficha financeira.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13002352034199)

   
É necessário conferir e bater os valores de movimentação do histórico de assistência à saúde com a ficha financeira do funcionário. Encontrando a inconsistência, ajuste o histórico e tente processar a DIRF/Informe de Rendimentos novamente.

Outra situação que pode ocorrer são divergências dos valores dos eventos e data de pagamento na ficha financeira.

**Saiba Mais**

**[RH - RM - FOP - DIRF/Informe de Rendimentos: Assistência Médica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021081652)****[RH - RM - FOP - DIRF/Informe de Rendimentos: Parametrização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021081112)**
