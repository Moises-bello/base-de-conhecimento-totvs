---
article_id: 360050371853
category: RH - Diversos
content_hash: d5c5576f4ccd80ecc474a89e2f5cabca9282371d23ff582d9be7eba245226aae
fetched_at: '2026-06-28T22:44:50.256511+00:00'
product: protheus
section_id: 32419184463255
source: central-protheus
title: RH - Linha Protheus - PON - Configuração de Tolerância para Atraso e Saída
  Antecipada por Marcação
type: support-article
updated_at: '2025-08-20T16:55:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050371853-RH-Linha-Protheus-PON-Configura%C3%A7%C3%A3o-de-Toler%C3%A2ncia-para-Atraso-e-Sa%C3%ADda-Antecipada-por-Marca%C3%A7%C3%A3o
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34321746285079) Tempo aproximado para leitura: 00:01:00 min**  
Dúvida**Como fazer a configuração de tolerância para atraso e saída antecipada apenas por marcação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para os exemplos abaixo, foi considerado um funcionário com Horário 08:00 - 12:00 - 13:00 - 17:00 e uma tolerância de 5 minutos por marcação.

Em **Atualizações - Cadastro Ponto - Regra de Apontamento**, defina uma tolerância de 00:05 por marcação (tolerâncias por período, tanto para atraso, quanto para saída antecipada e horas não realizadas devem ficar com 0,00)

![Capturar.PNG](https://tdn.totvs.com/download/attachments/496398394/Capturar.PNG?version=7&modificationDate=1579725285567&api=v2)

No apontamento, apenas as **marcações que ultrapassaram a tolerância são geradas**.

Na imagem abaixo, as marcações sublinhadas com azul estão dentro da tolerância e as vermelhas geraram algum evento de desconto.

![Capturar2.PNG](https://tdn.totvs.com/download/attachments/496398394/Capturar2.PNG?version=2&modificationDate=1579776694413&api=v2)

**Saiba mais**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
