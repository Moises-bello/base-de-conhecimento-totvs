---
article_id: 19197709002391
category: TAF - REINF
content_hash: 368582beaf47fd56940db0481d5b48217a1c3aaf6b9bf98d14d02a0a46e97701
fetched_at: '2026-06-28T22:41:33.701189+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como gerar um pagamento
  sem retenções para  o evento R-4020  manualmente no TAF.
type: support-article
updated_at: '2023-11-20T18:37:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19197709002391-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-gerar-um-pagamento-sem-reten%C3%A7%C3%B5es-para-o-evento-R-4020-manualmente-no-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19197679414807) Tempo aproximado para leitura: 00:04:00 min****Dúvida** Como gerar um pagamento sem retenções para o evento R-4020 manualmente no TAF ?   
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - a partir da versão 12  
  
  
**Solução**

Para gerar um pagamento sem retenções acesse rotina:

**Atualizações -> Movimentos REINF ->  Pagamento TAFA535  -> Incluir.**

Para Reinf existem duas situações para os pagamentos sem retenções:

**1-  Pagamentos  com natureza de rendimento  sem tributação.**

Inclua um documento com uma natureza de rendimento que não esteja sujeita a tributação de acordo com o layout da Reinf 2.1.2. . Como por exemplo:

![ima2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19197699404439)

Informe a  natureza de rendimento no campo **(V3V\_CNATRE )** e o valor do documento no campo  (**V3V\_VALOR)**

![image34.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19197670568599)

No painel reinf será demostrado apenas o valor  bruto:

![image3221.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19197694253591)

**2- Pagamentos com natureza de rendimentos com tributação.**

Para esse caso será necessário incluir uma natureza de rendimentos com tributação e habilitar o  parâmetro **MV\_TAFSTRI** para que o pagamento seja levado no painel reinf.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19197684928407)

Parâmetro Habilitado:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19197708862999)

Inclua  um documento com uma natureza de rendimento com  tributação de acordo com o layout da Reinf 2.1.2.  Como por exemplo:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19197785927063)

Dessa forma o valor bruto será informado corretamente no painel reinf:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19197785932695)

Para mais detalhes acesse a documentação abaixo:

<https://tdn.totvs.com.br/display/public/TAF/18061919+DSERTAF2-18292+DT+R-4020+Fornecedores+simples+nacional>

**IMPORTANTE:** As notas para o evento R-4020 serão demonstradas somente na rotina Painel Reinf, quando o parâmetro **MV\_TAFVLRE** indicar o layout **2\_01\_02**
