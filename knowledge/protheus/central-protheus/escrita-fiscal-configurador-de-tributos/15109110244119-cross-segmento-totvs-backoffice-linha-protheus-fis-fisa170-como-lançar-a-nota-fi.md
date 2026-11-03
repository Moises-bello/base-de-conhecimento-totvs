---
article_id: 15109110244119
category: Escrita Fiscal - Configurador de Tributos
content_hash: 797c97ea841cd7d59b97e23a9dde96b3446f96117a6f7b2848e4c331504b5295
fetched_at: '2026-06-28T22:39:17.477213+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como lançar
  a nota fiscal de compra de Gasolina CST 15?
type: support-article
updated_at: '2024-11-14T18:39:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15109110244119-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-lan%C3%A7ar-a-nota-fiscal-de-compra-de-Gasolina-CST-15
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27782011398423) Tempo aproximado para leitura: **00:08:00 min** **Dúvida**Como lançar a nota fiscal de compra de Gasolina CST 15?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões

**Solução**

Gasolina Considerando o calculo abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/XtLkguzTKDZzeMhLAH0KXp6O5/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/8nsrwQwz4UOYkTcEyGgP9H4vX/?name=image.png)

FISA170

![](https://totvssuporte.zendesk.com/attachments/token/hywGsVhaMt5fkZ0NzQZSRyeQY/?name=image.png)

Perfis

Perfil do cadastro de Produtos

000019 = Gasolina A

![](https://totvssuporte.zendesk.com/attachments/token/9VIwmYMc23UZ8gmTFLvjLiIfH/?name=image.png)

Cadastro de produtos = SB1

![](https://totvssuporte.zendesk.com/attachments/token/yz0gzHFkOjv34y4mzP7lYRq5S/?name=image.png)

Perfil de operação = 000013

![](https://totvssuporte.zendesk.com/attachments/token/ygXv939MjXNxqW1jDnly6r5dt/?name=image.png)

Perfil do Participante = 000019

![](https://totvssuporte.zendesk.com/attachments/token/K96J7T8QerOcOxAIHXsZT6bWz/?name=image.png)

SA2

![](https://totvssuporte.zendesk.com/attachments/token/8RuSya9nO9CLFhwlDq1p3hEGr/?name=image.png)

Perfil Origem / Destino

![](https://totvssuporte.zendesk.com/attachments/token/Oob32NyURowSou0VGouBlJ0QX/?name=image.png)

MV\_ESTADO = PR

Regra de base de calculo

000019 = ICMS Monofásico Gasolina A

![](https://totvssuporte.zendesk.com/attachments/token/FxW5Mf2QRMtmCHARPVYlfOSSQ/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/qecaeOI8ecrK0UEMmO7I8fsAC/?name=image.png)

Regra de alíquota

000019 =  ICMS Monofásico Gasolina A

![](https://totvssuporte.zendesk.com/attachments/token/ZqSAeIZgfTdWGSmALZUCbZKgV/?name=image.png)

Regra de Escrituração

000019 - ICMS Monofásico Gasolina A

![](https://totvssuporte.zendesk.com/attachments/token/OS8k2K34VrqsEm2IEq1QBXUg9/?name=image.png)

Se entender que o CST deve ser 61, altere

Regra de Calculo do Documento Fiscal = 000019 ICMS Monofásico Gasolina A

![](https://totvssuporte.zendesk.com/attachments/token/r5hmAMkOHdL2ojhRRsBIeZzUR/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/Nr4nbo7XDR8fMnyQ0fxhwNI4N/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/uLg8w7X97egE4PkBH51wJuDLa/?name=image.png)

Formula

![](https://totvssuporte.zendesk.com/attachments/token/7y4JjrhgmsVBXz0ZJXjPGzxQM/?name=image.png)

Aba outros do ICMS monofásico

![](https://totvssuporte.zendesk.com/attachments/token/1C5sZljfvqL8j3LhzzUB83fnK/?name=image.png)

Regra de Base de Calculo 000020 - ICMS ST Monofásico gasolina A

![](https://totvssuporte.zendesk.com/attachments/token/vTddsP7lVcjIMS1HeXOz9nUw2/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/vpyirHt1S1doBAQ6WqgwPl55U/?name=image.png)

Regra de Alíquota  para o ICMS ST Monofásico Gasolina A

Como temos a mesma alíquota do icms monofásico da Gasolina = 1,22 vou usar o mesmo cadastro

![](https://totvssuporte.zendesk.com/attachments/token/7zEItU9wJnG8ci4oShmnsmU4a/?name=image.png)

Índice de Conversão para o Calculo do ICMS ST Monofásico Gasolina A = 73%

![](https://totvssuporte.zendesk.com/attachments/token/TI4k0giMYtUD3K4FfDkXKz73t/?name=image.png)

Perfio da Gasolina 27% para calculo da base de calculo do ICMS ST Monofásico Gasolina A

![](https://totvssuporte.zendesk.com/attachments/token/r5ygUQ5WLLO0NeNDH44W9CZzP/?name=image.png)

Regra de Escrituração = 000020 ICMS ST monofásico Gasolina A

![](https://totvssuporte.zendesk.com/attachments/token/Fy8xhOaGox6OqdRTCW1XQH9id/?name=image.png)

Regra de Calculo Documento Fiscal = 000020 ICMS ST Monofásico Gasolina A

![](https://totvssuporte.zendesk.com/attachments/token/8pmnz6tp4d08Zkx67YcP1im0b/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/njF68SL781QyDe2aN634erNIE/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/ZGyKELfG9OYDGJZaY8l0AOdKg/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/ayfQhFeWJXcpFx7EbZ1dB3cJT/?name=image.png)

TES

Gera duplicata = sim

Calcula icms =sim

L fiscal icms = de acordo com a sua necessidade

Cred icms st = de acordo com a sua necessidade

Agrega valor = sim

Agrega solid = sim

Sit trib icm = 15

CFOP = 1652

MATA103

Documento de entradas

![](https://totvssuporte.zendesk.com/attachments/token/CjDKvgphfzWZFVpkGcvNEh8l3/?name=image.png)

Livro fiscal

![](https://totvssuporte.zendesk.com/attachments/token/HgCh3YBcgF55gpPRetxcHbxvo/?name=image.png)
