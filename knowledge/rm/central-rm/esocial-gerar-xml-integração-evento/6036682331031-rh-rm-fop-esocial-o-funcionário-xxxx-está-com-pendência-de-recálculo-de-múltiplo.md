---
article_id: 6036682331031
category: eSocial - Gerar XML/ Integração Evento
content_hash: 371a4e8131ac94022839e7edd9a805063b90b08bce62b4d1f5ce73a7b075b36c
fetched_at: '2026-06-28T22:47:13.092843+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - O funcionário 'XXXX' está com pendência de recálculo
  de múltiplos vínculos
type: support-article
updated_at: '2024-06-21T19:22:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6036682331031-RH-RM-FOP-eSocial-O-funcion%C3%A1rio-XXXX-est%C3%A1-com-pend%C3%AAncia-de-rec%C3%A1lculo-de-m%C3%BAltiplos-v%C3%ADnculos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao gerar o XML do evento S-1200 ocorre o erro **O funcionário 'XXXX' está com pendência de recálculo de múltiplos vínculos que pode ocasionar diferença no cálculo do INSS para o eSocial. É obrigatório executar o recálculo para este funcionário.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento -  eSocial - A partir da 12.1.25  
 **Causa**Esse incidente ocorre, pois não foi executado o processo **Recálculo Multi-Coligadas** ou o parâmetro **Não bloquear liberação de competência caso exista pendência de recálculo de múltiplos vínculos** está marcado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1.  Para o correto envio de S-1200 para eSocial do funcionário com múltiplos vínculos, é necessário recalcular a coligada ou o funcionário que possui pendência, fazendo assim, o cálculo de INSS será calculado corretamente. Para isso, acesse:**Folha Mensal | Lançamentos | Recálculo Multi-Coligadas** e selecione as coligadas vinculadas ao funcionário;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4914120739095/mceclip0.png)

2. Em seguida, gere o XML do S-1200 e envie ao eSocial.  
  
**Importante**  
Sugerimos que não marque o parâmetro **Não bloquear liberação de competência caso exista pendência de recálculo de múltiplos vínculos,** para que não permita virar competência sem ter realizado o recálculo, já que não será possível recalcular após liberação da competência**.** Para isso, acesse: **Configurações | Parametrizador | Folha Mensal | Geral.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4914054243095/mceclip1.png)

**Saiba mais**  
Para mais informações, acesse:

     • [Configurações Gerais FOP](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452719263)  
     • [Múltiplos Vínculos que necessitam recálculo](http://tdn.totvs.com.br/pages/releaseview.action?pageId=465386747)  
     • [Cálculo de INSS de múltiplos vínculos conforme o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026059894-RH-RM-FOP-eSocial-C%C3%A1lculo-de-INSS-de-m%C3%BAltiplos-v%C3%ADnculos-conforme-o-eSocial?source=search)
