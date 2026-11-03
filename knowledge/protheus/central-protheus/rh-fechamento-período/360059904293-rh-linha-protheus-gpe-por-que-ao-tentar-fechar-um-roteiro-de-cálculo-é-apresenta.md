---
article_id: 360059904293
category: RH - Fechamento Período
content_hash: 6f3250c706ceecba8a77929f561fa9085d4f97c71fa7488e9d66590808cdedfe
fetched_at: '2026-06-28T22:43:24.481687+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: 'RH - Linha Protheus - GPE - Por que ao tentar fechar um roteiro de cálculo
  é apresentada a mensagem: Roteiro foi encontrado como sendo o próximo período a
  ser processado, mas o período subsequente já foi fechado'
type: support-article
updated_at: '2025-04-16T12:03:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059904293-RH-Linha-Protheus-GPE-Por-que-ao-tentar-fechar-um-roteiro-de-c%C3%A1lculo-%C3%A9-apresentada-a-mensagem-Roteiro-foi-encontrado-como-sendo-o-pr%C3%B3ximo-per%C3%ADodo-a-ser-processado-mas-o-per%C3%ADodo-subsequente-j%C3%A1-foi-fechado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24910267944599) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Por que ao tentar fechar um roteiro de cálculo é apresentada a mensagem: Roteiro foi encontrado como sendo o próximo período a ser processado, mas o período subsequente já foi fechado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**A mensagem é apresentada porque para o período subsequente, foi preenchido manualmente o campo data de fechamento em cadastro de período. Deletando o lançamento da data, a mensagem não será mais apresentada.

**Exemplo:**

**Mensagem**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098422914)

Neste exemplo ao fechar o roteiro AUT do período Novembro/2020 foi apresentada a informação, pois para o período Dezembro/2020, foi informada manualmente a data de fechamento. Para ajustar acesse a rotina Período em **Atualizações > Definições de Cálculos > Períodos (GPEA400)**, selecione o período de Dezembro/2020 e delete a data do campo Data Fechamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24910267954839)

**Saiba mais:**

[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
