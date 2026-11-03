---
article_id: 15478798420247
category: Escrita Fiscal - Configurador de Tributos
content_hash: f880ce32efc544e6e4ad1d50b82a23ccedc9ace2e11938d43fd6c9b1b8116f13
fetched_at: '2026-06-28T22:39:17.304370+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular
  Difal EC/87 com redução de base calculo Conv 52/91?
type: support-article
updated_at: '2025-11-14T22:24:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15478798420247-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-Difal-EC-87-com-redu%C3%A7%C3%A3o-de-base-calculo-Conv-52-91
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15478751557783) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como Calcular Difal EC/87 com redução de base calculo Conv 52/91 pelo FISA170?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Calculo

**EXEMPLO 1 - Operações com Máquinas e Equipamentos Industriais - Estado Origem (Sul, Sudeste, exceto Espírito Santo)**

Valor da Mercadoria com o ICMS embutido = 1.000,00

**Alíquota interestadual ICMS = 7%**

**Carga efetiva (Percentual de Redução) = 5,14%**

ICMS com a redução aplicada = 1.000,00 x 5,14% = 51,40

**ICMS Destacado na NF-e = 51,40**

ou

Aplicando a regra de 3:

BC x 7% = 100 x 5,14

BC = 514 / 7

**% BC Reduzida = 73,43%**

Base de Cálculo com percentual de redução embutido = 1.000,00 x 73,43%

Base de Cálculo Reduzida = 734,30 - Conforme Destaque na NF-e

**ICMS Destacado na NF-e = 734,30 x 7% = 51,40**

Valor da Mercadoria sem o ICMS NF-e = 948,60

**Alíquota interna ICMS = 17%**

**Carga efetiva (Percentual de Redução) = 8,80%**

Base de Cálculo com percentual de redução embutido = 948,60 / (1 - 0,0880)

Base de Cálculo com percentual de redução embutido = 948,60 / 0,912 = 1.040,13

ICMS com a redução aplicada = 1.040,13 x 8,80% = 91,53

**ICMS Destino = 91,53**

ou

Aplicando a regra de 3:

BC x 17% = 100 x 8,80

BC = 880 / 17

**% BC Reduzida = 51,76%**

Base de Cálculo com percentual de redução embutido = 1.040,13 x 51,76%

Base de Cálculo Reduzida = 538,37

**ICMS Destino = 538,38 x 17% = 91,53**

**Difal = 91,53 (ICMS Destino) - 51,40 (ICMS Destacado NF-e - Origem)**

**Difal = 40,13**

Conforme parecer da Consultoria

<https://tdn.totvs.com/pages/releaseview.action?pageId=741849842>

Configurações do Fisa170 de acordo com o boletim conv52/91

<https://tdn.totvs.com/pages/releaseview.action?pageId=754944152>

* Parâmetro

MV\_ESTADO= RS

* Cadastro do Cliente

Cliente = SC

Consumidor Final

Contribuinte = não

* Cadastro de Produto

origem = 0

* Cadastro do TES

CFOP  = 6108 / 6107

Calcula icms = não

Calc dif icm = não

Calc difal = não

Mat consumo = não

L fiscal icms = não

Rotina FISA170

Código receita

![](https://totvssuporte.zendesk.com/attachments/token/E8T4rI0LiSVOmLLSIwXoR39zW/?name=image.png)

Perfis (Demonstraremos no vídeo)

Regra de base de calculo do ICMS

![](https://totvssuporte.zendesk.com/attachments/token/BzQ2pAuvQacS9AuaqCzU3D10v/?name=image.png)

Regra de alíquota

![](https://totvssuporte.zendesk.com/attachments/token/NvGA7gkizPwbWuiaSLCSprhH2/?name=image.png)

Regra de Escrituração

![](https://totvssuporte.zendesk.com/attachments/token/hszJv6vUoxBAmIKbz7ViIMBS8/?name=image.png)

Regra de Calculo - Documentos Fiscais

![](https://totvssuporte.zendesk.com/attachments/token/YTfWiFfGzcvZ0dxj0x20iKqPF/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/hiHzTxj2ck9MUdGFDlpwFRTnW/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/TTClA5VGymVnLHn4RxgSWI7BZ/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/mIvnizc9tpVQbQftbVgr7gjNT/?name=image.png)

Regra base de calculo - Difal - Para as notas fiscais de vendas a consumidor final com calculo do Difal EC/87 deve ser usado o ID - DIFAL

![](https://totvssuporte.zendesk.com/attachments/token/ECUjnEoAw0FQTiyW6ecXtheF5/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/aHRETVTPEzv6zbY8XibMT3C2n/?name=image.png)

Demonstração do preenchimento da base de calculo do DIFAL

* [2.3.1 Regra de Base de Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=754944152#CFGTRIBC%C3%A1lculodeDiferencialdeAl%C3%ADquotasConv%C3%AAnioICMS52/91-2.3.1RegradeBasedeC%C3%A1lculo)

Regra da alíquota

![](https://totvssuporte.zendesk.com/attachments/token/0inVQFd9oqkwfmhbf4SfdNo8N/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/TD4CTeq8FCCWt9zzkXDjYrRvt/?name=image.png)

Regra de Escrituração (a mesma do ICMS)

Regra de Calculo - Documentos Fiscais - DIFAL

![](https://totvssuporte.zendesk.com/attachments/token/VL0xzZ3BFD0nq38Z9Hx56O5zp/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/H5gri7vnt3sXLelR2FunTB3jj/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/kEJtS74nJAWdjb4yN1yUk4hp8/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/mnDK1Ejr8LhSrZirZEETrjTTD/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/VU8l3UyHWA3FjTlIUSKJ5PnnA/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/8fVh9swGTWmJqy9ajTqbE8MOa/?name=image.png)

Pedido de Vendas

![](https://totvssuporte.zendesk.com/attachments/token/NCmXromKtIxTXBDZsDYLkhuaQ/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/N6nTMLuozmFtdWxknW4BQ0sLw/?name=image.png)

Escrituração

![](https://totvssuporte.zendesk.com/attachments/token/ZeMct0ct6kkLbjM6AeQDV5I2n/?name=image.png)

Tabela CD2

![](https://totvssuporte.zendesk.com/attachments/token/2gfDNa9w3SvC2yJel7tsU4BuZ/?name=image.png)

Tabela SFT

![](https://totvssuporte.zendesk.com/attachments/token/hY96HNoVsLB9gzgQKJEULT2dw/?name=image.png)
