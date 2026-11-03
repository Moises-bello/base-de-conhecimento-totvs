---
article_id: 22923504510999
category: eSocial - Eventos Totalizadores
content_hash: f3104fbd2d95239f120eb7ee1fcb5cf154dbf7e832cab0b1dbe0377edee886ce
fetched_at: '2026-06-28T22:47:06.987806+00:00'
product: rm
section_id: 1500000834481
source: central-rm
title: RH - RM - FOP - eSocial - Como é considerado no FGTS Digital o 13° Salário
  Indenizado e Aviso Prévio Indenizado
type: support-article
updated_at: '2025-07-02T17:21:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22923504510999-RH-RM-FOP-eSocial-Como-%C3%A9-considerado-no-FGTS-Digital-o-13-Sal%C3%A1rio-Indenizado-e-Aviso-Pr%C3%A9vio-Indenizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22923504480023) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como é considerado no FGTS Digital o 13° Salário Indenizado e Aviso Prévio Indenizado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2306.240, 12.1.2310.182, 12.1.2402.117 e Superiores.

**Solução**

Conforme descrito no Manual de Orientação do Sistema (MOS) no item descrito no MOS no item "9. Projeção do aviso prévio indenizado sobre o 13º salário", relata que:

**"9.1. No cadastramento de rubrica relativa à projeção do aviso prévio indenizado sobre o 13º salário, deve ser indicada a incidência de FGTS {codIncFGTS} = 21 ou 93, pois essa verba deriva do aviso prévio indenizado e deve acompanhá-lo para fins de apuração da base de cálculo do FGTS. "**

No contexto do programa FGTS Digital, a base "FGTS Aviso Prévio Indenizado" consiste na soma do Aviso Prévio Indenizado com o 13º Salário Indenizado (codIncFGTS = 21). Portanto, o desconto de adiantamento de 13º Salário (codIncFGTS = 12) não pode estornar a base de FGTS do 13º Indenizado, assim como eventos de estorno de FGTS (codIncFGTS = 11), como faltas, não podem estornar a base de FGTS do Aviso Prévio Indenizado.

Para realizar essa tratativa foi necessário a criação de novos campos para que os existentes não sejam afetados e ocorra efeitos colaterais. Sendo os novos campos

* **Base FGTS eSocial** (eventos que incidem FGTS - eventos que estornam FGTS) desconsiderando os códigos de cálculos: 62, 99, 219 e 140;
* **Base FGTS 13º Salário eSocial** (eventos que incidem FGTS 13 - eventos que estornam FGTS 13) desconsiderando os códigos de cálculos 71, 98 e 220;
* **Base FGTS Indenizado eSocial** considerando somente os códigos de cálculos: 62, 99, 219, 140 e 71, 98 e 220;
* **FGTS eSocial**;
* **FGTS 13° Salário eSocial**;
* **FGTS Indenizado eSocial**.

**Exemplo Folha analítica:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22923504487831)

**Saiba mais**  
Para mais informações acesse:  
- [FGTS Digital - Tratativa quando há base negativa de FGTS e/ou FGTS 13o. Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=832650111#Aba1-1)
