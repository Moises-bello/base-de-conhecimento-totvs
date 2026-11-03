---
article_id: 14193357628823
category: Escrita Fiscal - Configurador de Tributos
content_hash: 731621e49ace7d6b376cc17a590c22077fac814cf01c686aa926c9ff2ee1eaa0
fetched_at: '2026-06-28T22:39:17.178092+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como Configurar
  Difal da EC/87 com Base dupla no fisa170?
type: support-article
updated_at: '2026-05-29T14:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14193357628823-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-Configurar-Difal-da-EC-87-com-Base-dupla-no-fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24265685204887) Tempo aproximado para leitura: 00:10:00**min**  
  
**Dúvida**  
Como Configurar Difal da EC/87 com Base dupla no Fisa170 ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Calculo solicitado

![](https://totvssuporte.zendesk.com/attachments/token/trN6oBOWt7wAZcTybV0cO8QRa/?name=image.png)

Exemplo de MS X SP

Valor da mercadoria R$335,80

Alíquota ICMS interestadual = 4%

Alíquota interna no destino =  18%

Diferença entre alíquotas = 14%

R$335,80 / 0,96 = R$349,79 / 0,86 = R$406,73 \* 14% = **R$56,94** (DIFAL)

Fisa170

Tributos já estão cadastrados

![](https://totvssuporte.zendesk.com/attachments/token/SqPE9pjLq6lVLwPXOOuKVZvG7/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/094fwXDSVAnhFIaFCkwlAf1Fx/?name=image.png)

Para esse calculo não vamos configurar esses cadastrados

![](https://totvssuporte.zendesk.com/attachments/token/NxBmrAKpIOy2CE3mF00OnyIOk/?name=image.png)

Perfis

**Perfil do Produto**

![](https://totvssuporte.zendesk.com/attachments/token/ovjmcKO8MSNI85hA5mEcdRGRn/?name=image.png)

SB1

![](https://totvssuporte.zendesk.com/attachments/token/0F690ma48Ycd7nCFV4bUBC8VE/?name=image.png)

No perfil de produtos coloque quantos produtos precisar, fiz uma amarração pela origem , como se trata de alíquota de 4% amarrei na origem 1/2/3 e 8

**Perfil de Operação**

![](https://totvssuporte.zendesk.com/attachments/token/fOiHdsvhVqamB9cUxRAyLFaA3/?name=image.png)

Esse perfil é padrão do sistema pode escolher Vendas Interestaduais ou Revenda Interestaduais

Na TES não precisa ter o CFOP 6108 pois se estiver cadastrado 5102 o sistema faz a conversão do mesmo.

**Perfil do Participante**

![](https://totvssuporte.zendesk.com/attachments/token/of3DpXrzKFG14SK5QY5tXDGDS/?name=image.png)

Acresente quantos clientes precisar , ou configure todos

SA1

![](https://totvssuporte.zendesk.com/attachments/token/fK5JZnJTqOUYIJGOXMnwKEV0u/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/YajEHgz3H9gR1HdDJugZG69PU/?name=image.png)

**Perfil de Origem / Destino**

![](https://totvssuporte.zendesk.com/attachments/token/5vnzsizFMbkVSsCuJz09eaROo/?name=image.png)

Pode acrescentar os outros estados se precisar

Regras de Calculo Documento Fiscal

**Regra de base de calculo**

a) ICMS

![](https://totvssuporte.zendesk.com/attachments/token/wEj1yDqtbCFPIH3ngNFJ5Riye/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/7xqGZBqCcXqMlQAvowCUfBmxn/?name=image.png)

b) Difal

![](https://totvssuporte.zendesk.com/attachments/token/2fZo5GDcknt2g7xYIKRQIeq9T/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/HN2QxJ7QPn7Pse5rNRQKspOVJ/?name=image.png)

**Regra da Alíquota**

![](https://totvssuporte.zendesk.com/attachments/token/bAJPX5y5BxclPlr7p9P3SvaxD/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/45gMWD9IdWzMWnHA95ZpkKkJC/?name=image.png)

**Regra de Escrituração**

![](https://totvssuporte.zendesk.com/attachments/token/qmQf2UeQLJd98pguvtQ0DKVeI/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/P5YNUXyGzuircXqV6N0kiDDWR/?name=image.png)

**Regra de Calculo - Documentos Fiscais**

a) ICMS

![](https://totvssuporte.zendesk.com/attachments/token/zZp9uPIz8XtSslEf7mhb4eRJ0/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/MTVQxYMOQwe7dn1o7qdBt9Jil/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/2o6L2c1mBAPguuYeEcYpqtQnd/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/eefZix1NSPAm0tfcpJeqsIoEm/?name=image.png)

b) Difal

![](https://totvssuporte.zendesk.com/attachments/token/c7jSbdAJUlwJVnpus9O6fSWah/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/XphdQwAQKcD0pIEhTId5bVddf/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/cXuex5wZq34kOInPFkDQZLZTN/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/enMYGmQJPhCCoAdnNwfqX5kkL/?name=image.png)

Lançamento do pedido de vendas

![](https://totvssuporte.zendesk.com/attachments/token/obSBccWo322DmtJ6P4uA6VS8B/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/01D4slocwLdSpSu4kTZwnt8fD/?name=image.png)

Para Produtos nacionais que a alíquota é 12% para a região sul / sudeste criar uma regra .
