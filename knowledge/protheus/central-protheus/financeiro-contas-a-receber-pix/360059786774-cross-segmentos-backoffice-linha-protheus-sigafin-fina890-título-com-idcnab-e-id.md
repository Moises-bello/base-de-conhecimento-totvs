---
article_id: 360059786774
category: Financeiro - Contas a Receber - PIX
content_hash: c3cdaf73e36b3b36b17a8361ea28d4acdaeca22e908ae6d22752eede9c4eb3ad
fetched_at: '2026-06-28T22:38:16.528743+00:00'
product: protheus
section_id: 1500001539301
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA890 - Título com  IDCNAB
  e IDTRAN
type: support-article
updated_at: '2022-08-17T22:44:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059786774-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA890-T%C3%ADtulo-com-IDCNAB-e-IDTRAN
---

**Dúvida**É possível um mesmo título ter IDCNAB e IDTRAN?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Financeiro - FINA890 - A partir das versões 12.1.25  
  
**Solução**Com a solução **PIX**, o sistema passa a permitir que um título seja enviado para um Banco A através de borderô e também um **PIX** gerado eventualmente em até outro banco.  
Todo o conceito e tabelas existentes de **borderô** foi mantido e passamos a controlar o **PIX** em nova entidade.  
Abaixo, cenários possíveis :

* Cenário A : Título com **PIX**
  + **Situação de Cobrança** = K (nova situação criada com a opção **Situação PIX** = Sim)
  + Informação do título na entidade **Monitor PIX**
* Cenário B : Título em **Cobrança Simples**
  + **Situação de Cobrança** = 1 (simples)
  + Não possui informação do título na entidade **Monitor PIX**
* Cenário C : Título em **Cobrança Simples** e **PIX**
  + **Situação de Cobrança** = 1 (simples), prevalecendo a situação do borderô
  + Informação do título na entidade **Monitor PIX**

Para boletos, a chave forte que identifica um título no sistema bancário é o conteúdo do campo **E1\_IDCNAB**.  
No PIX temos também uma chave forte, nos manuais é chamada de **TRANSACTION ID** (TXID) e no sistema fica armazenado na tabela **Monitor PIX**, no campo **F71\_IDTRAN**.  
  
**Saiba mais**[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
