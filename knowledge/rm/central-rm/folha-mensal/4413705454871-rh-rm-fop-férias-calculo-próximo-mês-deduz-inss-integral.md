---
article_id: 4413705454871
category: Folha Mensal
content_hash: 80e544dd8da088a5eb302bbc0a48f33c477a6230efbf391896ef41a2ff2315f8
fetched_at: '2026-06-28T22:46:59.312547+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Férias: Calculo próximo mês Deduz INSS Integral'
type: support-article
updated_at: '2024-09-16T18:21:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413705454871-RH-RM-FOP-F%C3%A9rias-Calculo-pr%C3%B3ximo-m%C3%AAs-Deduz-INSS-Integral
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22905639864471)**Tempo aproximado para leitura:**00:01:23min  
  
Duvida**Como é realizado o calculo quando possuir férias próximo mês, parametrização Deduz Integral (inclui mês seguinte)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução:**1. Para realizar o lançamento de férias marcadas, siga os passos:  
  
Realize a parametrização antes de qualquer processo **Configurações | Parametrizador | Férias |** aba **Descontos**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10537940210071)

**Deduz integral (inclui mês seguinte)**  
Marcando este parâmetro, o INSS de Férias será descontado integralmente nas férias (incluindo dedução correspondente ao mês seguinte).  
Com este parâmetro desmarcado, o desconto de INSS de férias proporcional, ou seja, apenas o valor referente ao mês corrente. O valor do INSS a ser deduzido da base de IRRF será o mesmo valor a ser descontado.  
  
**Observação**  
Este parâmetro só é considerado no cálculo de férias partidas e a quantidade de dias de férias no mês for maior ou igual a 22 dias.

2.Realize o lançamento das férias:  
  
**Início férias: 15/11/2021**  
**Data fim: 14/12/2021**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413710038039)

Envelope de Novembro:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413704880279)  
  
Envelope de Dezembro, férias finalizadas:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413705106455)  
  
Verifique que não é lançado o evento - INSS FERIAS PROX MÊS, ao visualizarmos o Log de Calculo de Dezembro, encontramos que o valor já foi descontado mês anterior.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413705127831)

**Saiba Mais:**[Férias - Descontos](https://tdn.totvs.com/display/public/LRM/Descontos)
