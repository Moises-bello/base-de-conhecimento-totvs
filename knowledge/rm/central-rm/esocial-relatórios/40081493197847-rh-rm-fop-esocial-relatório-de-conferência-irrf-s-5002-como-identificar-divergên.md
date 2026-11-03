---
article_id: 40081493197847
category: eSocial - Relatórios
content_hash: f1fc76383255efbc19641c6548f1d3bcb5ce350c09673d43f15f49f0d6316da3
fetched_at: '2026-06-28T22:47:04.886915+00:00'
product: rm
section_id: 1500000861002
source: central-rm
title: 'RH - RM - FOP - eSocial - Relatório de Conferência IRRF S-5002: Como identificar
  divergências no campo Rendimento Tributável'
type: support-article
updated_at: '2026-05-11T19:34:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40081493197847-RH-RM-FOP-eSocial-Relat%C3%B3rio-de-Confer%C3%AAncia-IRRF-S-5002-Como-identificar-diverg%C3%AAncias-no-campo-Rendimento-Tribut%C3%A1vel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40081463707031) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao executar o **Relatório de Conferência (IRRF) - Informações Complementares**, foi apresentado divergência no campo **Rendimento Tributável**. Como identificar tal divergência?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da versão 12.1.2502.293, 12.1.2506.262, 12.1.2510.182, 12.1.2602.106 e Superiores.   
  
**Solução**  
O campo **Rendimento Tributável** apresentará as informações de valores relativos ao rendimento tributável mensal e de férias. Sua composição será conforme abaixo:

**Origem Folha**

Somatório das verbas que possuem ***codIncIRRF*****11**(Mensal) ou **13**(Férias).

Para retornar na tag***codIncIRRF***o valor**11**, o evento (PEVENTO) deve atender uma das seguintes condições:

* `INCIRRF` (incidência de IRRF) = **VERDADEIRO**
* `INCIRRFSUSPENSA`(incidência suspensa) = **VERDADEIRO**
* **DEDUTIVELIRRF**(dedutível IRRF)**= VERDADEIRO**
* `CODIGOCALCULO` = **204**

Para retornar na tag***codIncIRRF***o valor**13,**o evento (PEVENTO) deve atender uma das seguintes condições:

* `INCIRRFFERIAS` (incidência IRRF férias) = **VERDADEIRO**
* `INCIRRFSUSPENSA`(incidência suspensa)= **VERDADEIRO**
* `DEDUTIVELIRRFFERIAS`(dedutível IRRF Férias) = **VERDADEIRO**
* `CODIGOCALCULO` ∈ **{208, 381}**

**Origem Governo**

Valor da Tag ***vlrRendTrib***do grupo ***consolidApurMen***, presente no totalizador S-5002 do período de apuração em questão.

Veja na documentação abaixo orientações sobre **possíveis causas** de inconsistências neste campo do relatório e **como realizar sua validação**:

* [**Middleware - Como validar divergências no Relatório de Conferência (IRRF) - Informações Complementares**](https://tdn.totvs.com/pages/viewpage.action?pageId=1062889046)

**Saiba mais**  
Para mais informações, acesse:

* [Middleware - Relatório de Conferência IRRF S-5002](https://tdn.totvs.com/pages/viewpage.action?pageId=1028947938)
* [Middleware - Relatório de Conferência IRRF S-5002 - MAPEAMENTO e ORIENTAÇÕES](https://tdn.totvs.com/pages/viewpage.action?pageId=1040994699)
