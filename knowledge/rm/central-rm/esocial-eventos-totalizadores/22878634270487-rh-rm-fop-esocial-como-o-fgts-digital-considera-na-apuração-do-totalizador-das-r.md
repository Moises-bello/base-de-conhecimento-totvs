---
article_id: 22878634270487
category: eSocial - Eventos Totalizadores
content_hash: 0b9bfe1f504edbeb6c01c020a14c82f63a01f33c8883b707c2f6fb301ce15f21
fetched_at: '2026-06-28T22:47:06.992521+00:00'
product: rm
section_id: 1500000834481
source: central-rm
title: RH - RM - FOP - eSocial - Como o FGTS Digital considera na apuração do totalizador
  das remunerações, bases negativas de FGTS e/ou FGTS 13º Salário
type: support-article
updated_at: '2025-07-02T17:05:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22878634270487-RH-RM-FOP-eSocial-Como-o-FGTS-Digital-considera-na-apura%C3%A7%C3%A3o-do-totalizador-das-remunera%C3%A7%C3%B5es-bases-negativas-de-FGTS-e-ou-FGTS-13%C2%BA-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22878657827223) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como o FGTS Digital considera na apuração do totalizador das remunerações, bases negativas de FGTS e/ou FGTS 13o. Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir das versões 12.1.2306.240, 12.1.2310.182, 12.1.2402.117 e Superiores.  
  
**Solução**Com a implementação do FGTS Digital, foram realizadas alterações na demonstração das bases de FGTS para os seguintes cenários:

1. Quando o funcionário demitido tem desconto de adiantamento de 13o. Salário superior ao valor pago.
2. Quando o funcionário demitido tem um estorno de FGTS maior que os proventos.

Nestes cenários o governo não considera a base para totalizar o S-5003 e consequentemente o S-5013. Conforme informado no [Manual de Orientação do FGTS DIGITAL](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-1-01-03-2024.pdf).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22878972072855)

De acordo com o leiaute, são considerados os seguintes tipos de valores, para apuração do FGTS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22878657829655)

Abaixo um exemplo de como é considerado para o FGTS Digital:

* No envelope de pagamento da rescisão há dois eventos do tipo provento com incidência em FGTS 13° Salário;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22879500684439)

* Para este funcionário foi antecipado a primeira parcela do 13° Salário, juntamente com as férias. Neste caso, foi lançado no envelope o evento de adiantamento do 13° Salário, do tipo desconto, estornando o FGTS;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22879500716311)

* O cálculo realizado para o tpValor 22 - FGTS 13° salário rescisório será R$ 1.023,46 + R$ 514,67 - R$ 2.046,91, totalizando **-R$ 508,78**. Sendo assim, neste caso, o governo irá desconsiderar o tpValor 22 e considerar somente as demais bases que a soma encontra-se maior que zero.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22879500744599)

Para realizar essa tratativa foi necessário a criação de novos campos no produto para que os existentes não sejam afetados e ocorra efeitos colaterais. Sendo os novos campos que poderão ser identificados no Relatório de Conferência FGTS e na Folha Analítica, conforme consta no artigo abaixo:

[DT - FGTS Digital - Tratativa quando há base negativa de FGTS e/ou FGTS 13o. Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=832650111)  
  
**Importante**

Tal correção só foi realizada, até o momento, para os relatórios de Conferência FGTS (eSocial) e na Folha Analítica. A correção para o envelope, aba incidências, será liberada em um próximo momento.
