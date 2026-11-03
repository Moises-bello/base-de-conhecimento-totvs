---
article_id: 360051144974
category: RH - Férias
content_hash: 7d99a784ba04176b6a2ea9b724603e0f2acc02746e84c1afdcbc678629958192
fetched_at: '2026-06-28T22:43:58.034905+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular dois períodos de férias dentro do
  mesmo mês
type: support-article
updated_at: '2024-02-14T19:56:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051144974-RH-Linha-Protheus-GPE-Como-calcular-dois-per%C3%ADodos-de-f%C3%A9rias-dentro-do-mesmo-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como calcular dois períodos de férias dentro do mesmo mês?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Quando uma empresa concede a um único funcionário gozo consecutivo a dois períodos de férias e, as respectivas datas de pagamento ocorrem no mesmo mês (fato gerador), é necessário apurar o **Imposto de Renda** e o**INSS** pelo total dos valores pagos em férias nos dois recibos.  
  
**Solução**Desta forma, é necessário ter verbas cadastradas no sistema com os identificadores de cálculo abaixo, obrigatoriamente sendo **Valor** e com tipo **3 - Base Provento**  
  
**ID    Descrição**  
0236 - Base de IR de férias de outros períodos de férias.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11223646547479)

0237 - Valor de IR já descontado em outros períodos de férias.![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11223729720087)

0396 - Base de INSS de férias de outros períodos de férias.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11223804198167)

0397 - Valor de INSS já descontado em outros períodos de férias.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11223809791639)  
  
Referente a **incidência** das verbas, a configuração das Verbas/Rubricas com relação a Natureza e as Incidências Tributárias é algo particular de cada Empresa e que deve ser analisado em conjunto com o departamento Jurídico e Contábil.  
  
**Exemplo**  
Sistema buscará no segundo cálculo de férias, a Base INSS outros períodos (base de INSS do primeiro cálculo de férias) e o Desconto de INSS outros Períodos.  
  
Com isso, o sistema fará uma nova base de cálculo do INSS, somando a base de INSS outros períodos e a base do cálculo atual.  
  
Id 0013 - 2.111,11  
Id 0396 - 4.222,23  
Id 0397 - 450,04  
**Id 0065 - 263,04**

Soma: 6.333,34  
  
Faixa 1 - 78,37  
Faixa 2 - 94,01  
Faixa 3 - 125,37  
Faixa 4 - 415,33  
Total: 713,08 - 450,04 = **263,04**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079853014/mceclip1.png)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080920093/mceclip0.png)

**Para saber mais:**

[RH - Linha Protheus - GPE - Conferência do IRRF de Férias quando Dois Períodos de Gozo são concedidos com Pagamento no mesmo mês](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg8pWfTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB2Wh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyOTA3MDY1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uZmVyJUMzJUFBbmNpYS1kby1JUlJGLWRlLUYlQzMlQTlyaWFzLXF1YW5kby1Eb2lzLVBlciVDMyVBRG9kb3MtZGUtR296by1zJUMzJUEzby1jb25jZWRpZG9zLWNvbS1QYWdhbWVudG8tbm8tbWVzbW8tbSVDMyVBQXMGOwhUOg5zZWFyY2hfaWRJIik2NGU5ZTBjYS0zNmI0LTQ0MDgtOTczYy1lOWIxYmRiYTI2ODAGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgGFUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENvbmZlcsOqbmNpYSBkbyBJUlJGIGRlIEbDqXJpYXMgcXVhbmRvIERvaXMgUGVyw61vZG9zIGRlIEdvem8gc8OjbyBjb25jZWRpZG9zIGNvbSBQYWdhbWVudG8gbm8gbWVzbW8gbcOqcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--43724fe9a68b1383d1582aa7c817274eab6b9af0)
