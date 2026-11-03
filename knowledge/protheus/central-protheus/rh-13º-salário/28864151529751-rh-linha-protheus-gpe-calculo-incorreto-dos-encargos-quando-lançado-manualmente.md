---
article_id: 28864151529751
category: RH - 13º salário
content_hash: b593b20759b6fc78f1bfce7a40db6205d1667e121728371a7a975f9c4cf6ce8f
fetched_at: '2026-06-28T22:44:00.491419+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo incorreto dos encargos quando lançado manualmente
  a verba de id 0028
type: support-article
updated_at: '2025-08-20T13:17:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28864151529751-RH-Linha-Protheus-GPE-Calculo-incorreto-dos-encargos-quando-lan%C3%A7ado-manualmente-a-verba-de-id-0028
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28864177848983) Tempo aproximado para leitura: **00:02:00 min** **Ocorrência**Ao realizar o lançamento manual da verba de id 0028, sistema calcula os encargos com valores diferentes da verba de complemento.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões  
  
**Causa**  
Os encargos não são recalculados conforme valor lançado quando mnemônico P\_CCOMP13 está habilitado.  
  
**Solução**Desabilitando o mnemônico, o sistema não valida o cálculo da 2ª parcela, calcula os encargos só considerando o complemento.  
  
Exemplo:  
Lançamento da verba de ID 0028 com o mnemônico P\_CCOMP13 habilitado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28864151506455)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28864177853335)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28864151510167)  
  
Para ajustar é necessário desabilitar o mnemônico P\_CCOMP13, lançar de id 0028 e recalcular o roteiro FOL:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28864151511447)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28864151512855)

**Saiba mais:  
Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>**

1. [RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)
