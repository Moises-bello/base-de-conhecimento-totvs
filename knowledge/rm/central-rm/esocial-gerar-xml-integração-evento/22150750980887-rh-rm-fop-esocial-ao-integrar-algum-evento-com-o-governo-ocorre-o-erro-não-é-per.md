---
article_id: 22150750980887
category: eSocial - Gerar XML/ Integração Evento
content_hash: 242b72c0dab6b2d138e1135b58b36e14b093c59e3cda702ef9598562bc4442b1
fetched_at: '2026-06-28T22:47:11.963090+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao integrar algum evento com o governo ocorre o
  erro: Não é permitido fazer a transmissão de eventos para o ambiente de Produção
  do eSocial através de uma base de dados de Homologação!'
type: support-article
updated_at: '2024-09-23T12:20:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22150750980887-RH-RM-FOP-eSocial-Ao-integrar-algum-evento-com-o-governo-ocorre-o-erro-N%C3%A3o-%C3%A9-permitido-fazer-a-transmiss%C3%A3o-de-eventos-para-o-ambiente-de-Produ%C3%A7%C3%A3o-do-eSocial-atrav%C3%A9s-de-uma-base-de-dados-de-Homologa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22150760910615) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao integrar algum evento com o governo ocorre o erro de processo: RM.Lib.RMSValidateException: Não é permitido fazer a transmissão de eventos para o ambiente de Produção do eSocial através de uma base de dados de Homologação! Para maiores detalhes acesse o documento: <https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719889>. at RM.Fop.Esocial.FopEsocialIntegrarTafProcess.DoExecute(RMSParamsProc Params)  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**O erro ocorre quando o Tipo de Ambiente no Parametrizador do eSocial não está condizente com o Tipo de Ambiente da Base de Dados do RM.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse **Configurações | Parametrizador | eSocial** e verifique qual é o tipo de ambiente utilizado;

![](https://totvssuporte.zendesk.com/attachments/token/al0waaEgtyY3ilrIYSqVo02gD/?name=image.png)  
 

2. Após acesse **Serviços Globais** | **Menu Serviços** | **Tipo de ambiente**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22151090586263)

3. Realize o ajuste dos ambientes, de acordo com o desejado, no Parametrizador x Base de Dados, após rode o RM.Atualizador para o ambiente desejado.

**Saiba mais**Para mais informações acesse:  
- [RM - Frame - Tipo de Ambiente RMAtualizador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003443352-RM-Frame-Tipo-de-Ambiente-RMAtualizador?source=search)   
- [Integrar com TAF / Middleware](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719889)
