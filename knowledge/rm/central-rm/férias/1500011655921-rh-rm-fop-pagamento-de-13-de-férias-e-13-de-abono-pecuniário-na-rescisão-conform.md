---
article_id: 1500011655921
category: Férias
content_hash: 8e3b090e2a0a1aaca99819c2cf4f153ee77adb6f09cdee212798a67945ee7045
fetched_at: '2026-06-28T22:46:56.398871+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Pagamento de 1/3 de Férias e 1/3 de abono pecuniário na Rescisão
  conforme MP 1.046/2021
type: support-article
updated_at: '2025-03-07T14:55:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011655921-RH-RM-FOP-Pagamento-de-1-3-de-F%C3%A9rias-e-1-3-de-abono-pecuni%C3%A1rio-na-Rescis%C3%A3o-conforme-MP-1-046-2021
---

**Dúvida**

Como realizar o pagamento de 1/3 de férias e 1/3 de abono pecuniário na Rescisão conforme a MP1.046?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir das versões:

* 12.1.29.250
* 12.1.31.154
* 12.1.32.101 e superiores.

**Solução**

Conforme a MP 1046, Art. 10, na hipótese de dispensa do empregado, o empregador pagará, juntamente com o pagamento dos haveres rescisórios, os valores ainda não adimplidos relativos às férias.

No TOTVS Folha de Pagamento, quando as férias são finalizadas, o período é fechado e é aberto um novo período aquisitivo. O cálculo das verbas rescisórias verifica somente o período aquisitivo de férias aberto para calcular as férias proporcionais e/ou indenizadas.

Para atender a MP, orientamos fazer o lançamento do evento calculado por fórmula na rescisão se os mesmos forem devidos, usando uma das opções: Entrada de movimento, Grupo de eventos, Código Fixos, Eventos Programados, Incluir no Envelope de Pagamento, Importação de Movimento ou inserir nos Eventos Adicionais no parametrizador.

Considerando o cenário, onde o funcionário teve as férias de 2021 e 2022 concedidas, sem o pagamento de 1/3 de férias e de 1/3 de abono pecuniário. No período vencido, o funcionário tinha 30 dias de direto, porém vendeu 10 dias. O mesmo foi concedido em Maio/2021 com pagamento em Junho/2021. Os eventos de base de 1/3 de Férias e 1/3 de Abono foram lançados no recibo e envelope de pagamento:  
  
![](https://tdn.totvs.com/download/attachments/615919977/image2021-5-6_15-27-30.png?version=1&modificationDate=1620325650543&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/615919977/image2021-5-6_15-28-22.png?version=1&modificationDate=1620325702160&api=v2)  
  
Após a finalização das férias concedidas acima foi criado um novo período aquisitivo de férias entre 01/09/2020 a 31/08/2021. Este período foi antecipado concedendo ao empregado 30 dias de férias, na competência de Junho/2021 com pagamento para 07/07/2021 sem o pagamento do 1/3 de férias. Neste caso não teve o pagamento de abono. O Evento de base de 1/3 de férias foi lançado no recibo e envelope:  
  
![](https://tdn.totvs.com/download/attachments/615919977/image2021-5-6_15-33-13.png?version=1&modificationDate=1620325993637&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/615919977/image2021-5-6_15-35-45.png?version=1&modificationDate=1620326145583&api=v2)  
  
Ao finalizar as férias concedidas acima, foi criado um novo período aquisitivo de férias: 01/09/2021 a 31/08/2022:  
  
![](https://tdn.totvs.com/download/attachments/615919977/image2021-5-6_15-37-23.png?version=1&modificationDate=1620326244047&api=v2)  
  
Em Julho/2021 o funcionário foi demitido. O produto não irá calcular nenhuma verba de férias para o funcionário, pois o período aberto inicia em Setembro/2021.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019055101/mceclip0.png)  
  
Fórmula para adicional de férias antecipado que deve ser pago de forma proporcional

**1)** Criar a consulta SQL para retornar os funcionários que tiveram as férias concedidas antecipadas. Nesta consulta é retornado somente os funcionários com o período antecipado e o evento de base de Cálculo que tem o ⅓ de férias lançado, conforme orientado no documento [MP 1046 - Adicional de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=615912658)

**Consulta SQL- Pagamento de 1/3 de Férias Proporcionais**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019055441/mceclip2.png)

**2)** Criar a fórmula abaixo que retorna os dados da consulta SQL criada no passo 1, que é referente ao valor de ⅓ de férias do período antecipado e que a data final do período aquisitivo é maior que a data de demissão:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019055761/mceclip5.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019055721/mceclip4.png)

Executando a fórmula a mesma retornou o valor do evento de Base de Cálculo B099 lançado na Ficha Financeira do pagamento de férias antecipadas:  
  
![](https://tdn.totvs.com/download/attachments/615919977/image2021-5-6_16-25-54.png?version=1&modificationDate=1620329154307&api=v2)  
  
**3)** Criar um evento de provento e associar a fórmula neste provento:  
  
![](https://tdn.totvs.com/download/attachments/615919977/image2021-5-6_17-16-15.png?version=1&modificationDate=1620332176150&api=v2)  
  
Saiba mais: [Fórmula para adicional de férias antecipado que deve ser pago de forma proporcional](https://tdn.totvs.com/pages/releaseview.action?pageId=615919977)
