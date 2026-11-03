---
article_id: 36224129533463
category: Financeiro - Conciliador Backoffice
content_hash: 2bbb332f3258648fbdf71ec313009ec01f1684ae14c666813e938a77b3da1271
fetched_at: '2026-06-28T22:37:47.289529+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliação
  é removida após atualização de filtro
type: support-article
updated_at: '2025-11-19T20:07:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36224129533463-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Concilia%C3%A7%C3%A3o-%C3%A9-removida-ap%C3%B3s-atualiza%C3%A7%C3%A3o-de-filtro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36224129523735) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Ao realizar a conciliação e atualizar a rotina ou o filtro da rotina, o sistema exibe os registros na aba **“Dados não encontrados”**.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.2210  
  
**Solução**

A rotina de **conciliação bancária** mantém os dados como conciliados apenas quando há preenchimento das informações na **SIG**, com os devidos flags nos campos **E5\_RECONC** e **FK5\_DTCONC**.

O sistema reconhece a conciliação a partir do cruzamento entre os campos **MSUIDT** da tabela **FK5** e **MSUIDT** da tabela **SIG**, ambos com o mesmo número de código da conciliação (QLD\_CODCON) na tabela QLD.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36257758297879)

Caso esse vínculo ainda não tenha sido efetivado, ao atualizar os filtros da rotina, o registro voltará a aparecer na aba **“Dados não encontrados”**, uma vez que o preenchimento da **SIG** ocorre apenas após a **efetivação (botão aplicar conciliação)** do registro na rotina **CTBA940**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36452341661975)

Essas orientações reforçam a importância de **efetivar corretamente a conciliação**, garantindo que as informações sejam gravadas de forma definitiva no banco de dados. Se houver atualização de filtros, queda de conexão ou fechamento da rotina antes da efetivação, os dados permanecem apenas em tabela temporária e, por isso, não são apresentados novamente na consulta.
