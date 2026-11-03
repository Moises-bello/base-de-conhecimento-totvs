---
article_id: 9931470611351
category: eSocial - Tabelas/Não Periódicos
content_hash: 40b5c4899def8238fc824bc9547c94bfd0c71d1608784eb7279e72613c0220c5
fetched_at: '2026-06-28T22:47:10.381447+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: Erro na validação do campo ''indConstr'':
  O preenchimento do campo é exclusivo e obrigatório para PJ'
type: support-article
updated_at: '2024-06-14T13:09:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9931470611351-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-Erro-na-valida%C3%A7%C3%A3o-do-campo-indConstr-O-preenchimento-do-campo-%C3%A9-exclusivo-e-obrigat%C3%B3rio-para-PJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar XML do evento S-1000 para o governo é retornado a inconsistência: **Erro na validação do campo 'indConstr': O preenchimento do campo é exclusivo e obrigatório para PJ.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931367906967)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**Este erro ocorre para o evento S-1000 **Informações do Empregador/Contribuinte/Órgão Público** quando o campo de preenchimento **Indicativo de Construtora** e obrigatório para PJ.   
  
**Solução**Para preenchimento do **Indicativo de Construtora**, realize os passos a seguir:  
1. Acesse o menu **Folha de Pagamento | eSocial | Informações do Empregador;**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9799589089175)**

2. Selecione a empresa desejada e verifique se o preenchimento do campo **Indicativo de Construtora** foi realizado de forma correta para PJ;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9938596241559)

3. Após ajuste, na fila de eventos gere o XML e envie ao eSocial
