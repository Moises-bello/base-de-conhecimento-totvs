---
article_id: 22920225248151
category: eSocial - Gerar XML/ Integração Evento
content_hash: fc5314d786dc3b459630ef74a3740ed08120ffc820beb42402c2a5b1e8599859
fetched_at: '2026-06-28T22:47:11.884537+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial -  Cálculo utilizado para preenchimento da tag <vrSalFx>
  para salário composto de funcionários mensalistas XML  S-2206 e S-2306
type: support-article
updated_at: '2026-06-01T17:42:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22920225248151-RH-RM-FOP-eSocial-C%C3%A1lculo-utilizado-para-preenchimento-da-tag-vrSalFx-para-sal%C3%A1rio-composto-de-funcion%C3%A1rios-mensalistas-XML-S-2206-e-S-2306
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22920193542423) Tempo aproximado para leitura: **00:02:10 min**  
  
**Dúvida**  
Como o sistema calcula o salário composto para alimentar a tag **<vrSalFx> de funcionários mensalistas** na geração dos eventos S-2206 e S-2306?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Com base na data da alteração registrada no evento S-2206 e S-2306, o sistema verificará no histórico salarial do funcionário todos os registros com datas anteriores a essa data.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22920193543575)

#### Para os funcionários com salário composto, o sistema retornará o último salário de cada número de salário registrado anteriormente a essa data como o exemplo abaixo.

Acesse: **RM | RH | Módulo Folha de Pagamento |Funcionários | Anexos | Histórico salarial**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22920294342807)

Com base no exemplo acima, o valor da tag <vrSalFx> será a soma de todas as linhas destacadas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22920292226583)

**Saiba mais**  
[DT - S-2206 e S-2306 - Geração da tag <vrSalFx>](https://tdn.totvs.com/pages/releaseview.action?pageId=838954096)  
[Evento S-2206](https://tdn.totvs.com/display/public/LRM/Evento+S-2206)  
[Evento S-2306](https://tdn.totvs.com/display/public/LRM/Evento+S-2306)
