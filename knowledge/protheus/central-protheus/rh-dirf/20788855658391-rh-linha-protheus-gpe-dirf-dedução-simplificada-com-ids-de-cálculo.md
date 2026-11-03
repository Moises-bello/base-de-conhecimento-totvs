---
article_id: 20788855658391
category: RH – DIRF
content_hash: 6d4b342973de22eeca43fac7a1c42da13773b61f1ab5334cf3805f0248bdc68e
fetched_at: '2026-06-28T22:44:06.963167+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - DIRF Dedução Simplificada com IDs de Cálculo
type: support-article
updated_at: '2024-01-31T17:41:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20788855658391-RH-Linha-Protheus-GPE-DIRF-Dedu%C3%A7%C3%A3o-Simplificada-com-IDs-de-C%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20788855638935) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar a DIRF com Dedução simplificada com Identificadores de cálculo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - À partir do release 12.1.33  
  
**Solução**Conforme Leiaute da DIRF 2024, será utilizada uma nova coluna para a Dedução Simplificada e para isso, os valores deverão estar vinculados à novos Tipos de Rendimento na tabela genérica 36, conforme publicado em [Novos Tipos de Rendimentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20772420455703).  
A Manutenção da DIRF deverá exibir as novas colunas e a Geração da DIRF deverá ser responsável por gerá-las.  
Implementado ajuste para que sejam gravados os novos Tipos de Rendimentos, através da Geração da DIRF.  
Serão exibidos em 3 novas colunas na rotina da Manutenção da DIRF.  
As colunas terão valores somente quando a Dedução Simplificada for utilizada, caso contrário, essas colunas estarão com valores zerados.  
Os valores das deduções legais seguem incorporados normalmente a DIRF, em qualquer cenário.

1. **Ded. Simplificada**:  
Contempla os valores das verbas com Tipo de Rendimento igual a B4 - lembrando que a dedução é única dentro da competência de pagamento, mesmo que as verbas vinculadas sejam geradas em mais de um roteiro de cálculo (Folha de Pagamento/Adiantamento/Férias), a geração da DIRF irá respeitar a Data de Pagamento dessas verbas assim como as demais verbas geradas para DIRF.  
  
2. **Ded. Simplificada 13o**:  
Contempla os valores das verbas com o Tipo de Rendimento igual a B5.  
  
3. **Trb. Leg. Susp**:  
Contempla os valores das verbas com o Tipo de Rendimento igual a B6.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21014136954903)  
  
  
**Saiba Mais:**  
[DIRF com Dedução Simplificada com IDs de Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=819498302)   
[DIRF com Dedução Simplificada sem IDs de Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=819527400)   
[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
