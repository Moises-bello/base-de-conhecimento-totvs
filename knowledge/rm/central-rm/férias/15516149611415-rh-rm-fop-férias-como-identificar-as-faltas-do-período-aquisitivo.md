---
article_id: 15516149611415
category: Férias
content_hash: 2a756ab0e8758452f8daffcf19244198ea40fc6b6f702b1a9ce2b36b7df8fe20
fetched_at: '2026-06-28T22:46:56.198117+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Como identificar as faltas do período aquisitivo?'
type: support-article
updated_at: '2023-06-23T11:15:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15516149611415-RH-RM-FOP-F%C3%A9rias-Como-identificar-as-faltas-do-per%C3%ADodo-aquisitivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15516159662999) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como identificar a quantidade de faltas no cadastro de férias?  
   
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para facilitar e ajudar na identificação da origem das faltas, trouxemos as opções abaixo:

**Exemplo:**

1. No **print 1** abaixo temos 6 dias de faltas, sendo 4 dias no período aquisitivo vencido e 2 dias no período proporcional:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15515130020759)

2. Veja que agora no **print 2** aparecem 5 dias de faltas, conforme demonstra a imagem abaixo: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15515072964375)

**Para melhor entendimento, veja a composição dos campos:**

**Faltas período:** Computando 4 dias (falta) descontados no período aquisitivo vencido.

**Faltas prop.:** Computando 2 dias (falta) lançado no período aquisitivo proporcional, menos 1 dia (falta) lançado no evento de código de cálculo 128 (base de cálculo no mesmo período) como estorno de falta.

Observe que no campo **"Faltas prop."** está computando apenas 1 dia:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15515072964375)

3. Para facilitar a identificação e a origem das faltas, verifique as duas opções:

**Opção 1:**  Se a sua base estiver configurada para utilizar o controle de faltas para o cálculo de avos, a origem será conforme documentação 1 abaixo.

[RH - RM - FOP - Utiliza Controle de Faltas para Cálculo de Avos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020486611-RH-RM-FOP-Utiliza-Controle-de-Faltas-para-C%C3%A1lculo-de-Avos?source=search)

**Opção 2:** Irá considerar os eventos de falta lançados na ficha financeira, sendo os eventos de Código de Cálculo [8 - Faltas](https://tdn.totvs.com/pages/viewpage.action?pageId=452718542) e Código de cálculo [128 - Estorno de Faltas](https://tdn.totvs.com/pages/viewpage.action?pageId=452718655)

Para ajudar na identificação dos eventos acima lançados na ficha financeira, o cliente poderá utilizar o recurso de sentença SQL, semelhante ao exemplo abaixo. Para isso basta alterar a coligada,  chapa do funcionário e o ano de competência.

```
SELECT PFFINANC.CODEVENTO,PFFINANC.ANOCOMP,PFFINANC.MESCOMP, PEVENTO.CODIGOCALCULO,PFFINANC.REF, PFFINANC.HORA/60 AS HORA  
FROM PFFINANC  
LEFT JOIN PEVENTO ON PEVENTO.CODCOLIGADA = PFFINANC.CODCOLIGADA AND PEVENTO.CODIGO = PFFINANC.CODEVENTO  
WHERE PFFINANC.CODCOLIGADA = 1  
AND PEVENTO.CODIGOCALCULO IN ('8','128')  
AND PFFINANC.CHAPA ='00001'  
AND PFFINANC.ANOCOMP=2023
```

**IMPORTANTE! A sentença apresentada acima, é apenas um exemplo em SQL. Caso identifique a necessidade de uma sentença mais específica, sugerimos acionar o DBA da empresa ou consultar condições de desenvolvimento junto ao time de Consultoria da TOTVS.**

Verifique o resultado com base na sentença que foi apresentada: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15515749022359)

**Saiba Mais**

[RH - RM - FOP - Apuração de faltas período aquisitivo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10124252575511-RH-RM-FOP-Apura%C3%A7%C3%A3o-de-faltas-per%C3%ADodo-aquisitivo?source=search)
