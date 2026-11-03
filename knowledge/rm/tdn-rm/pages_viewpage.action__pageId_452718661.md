---
content_hash: b5bff1ac67ec77c44fcd4a664e2b1bdf3307eb3214b12907f20980cb8d03bdc5
fetched_at: '2026-06-29T00:10:00.977460+00:00'
page_id: '452718661'
product: rm
source: tdn-rm
title: Código de Cálculo 382 - Estorno Base IRRF Retificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718661
version: 10
---

Base de cálculo do tipo valor, com incidência em 'Estorna IRRF'.

Este código de cálculo será utilizado para somar o valor das bases de IRRF (Imposto de Renda Retido na Fonte) calculados pela retificação no período de lançamento da retificação. A finalidade é ajustar e consolidar os valores de IRRF de forma precisa, garantindo que os estornos sejam corretamente contabilizados.

Este código de cálculo foi criado para situações onde há retificação de meses anterior e a base de IRRF no envelope da época a ser retificada precisa ser zerada, pois a base será trazida para o mês de pagamento através do código de cálculo 385.

**Exemplo:**

Na competência 10/2021, foi identificado que o funcionário 00008 não recebeu uma hora aula no valor de R$5.000,00 na competência 12/2021.

Ao gerar o processo de retificação da rescisão e informar esse valor, o sistema irá criar o envelope com o período 10.000 na competência 10/2021, conforme abaixo:

Lembrando que, essa verba será utilizada para compor o campo "Rendimentos Tributáveis" existentes plataforma do eSocial do evento S-5002.

ATENÇÃO: 

O evento com código de cálculo "382 - Estorno Base IRRF Retificação" não será lançado no movimento se o evento código de cálculo "385 - Base IRRF Retificação" não estiver marcado com a incidência de IRRF. A correta configuração da incidência de IRRF no evento 385 é essencial para que o estorno da base de cálculo seja aplicado corretamente.

---

Códigos de Cálculo
