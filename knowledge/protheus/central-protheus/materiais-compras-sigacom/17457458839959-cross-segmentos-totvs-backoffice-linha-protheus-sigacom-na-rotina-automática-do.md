---
article_id: 17457458839959
category: Materiais - Compras (SIGACOM)
content_hash: 6567a72918244450a81391b60fa5ae8373d6d9945a570f4aff6ab23637a43124
fetched_at: '2026-06-28T22:41:12.758626+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGACOM - Na rotina Automática
  do Cadastro de Fornecedor existe como automatizar inclusão de chave PIX ?
type: support-article
updated_at: '2023-09-12T11:36:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17457458839959-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Na-rotina-Autom%C3%A1tica-do-Cadastro-de-Fornecedor-existe-como-automatizar-inclus%C3%A3o-de-chave-PIX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17457466443799) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Há com realizar cadastro preenchimento da chave PIX via execauto MVC MATA020?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**Na rotina MATA020 não possui a validação da tabela F72, referente a PIX, por este motivo não existe um submodelo, não é possível efetuar a inclusão através da rotina automática MATA020, pois a chave Pix é tratada pela rotina FINA885 do Financeiro.  
   
***Obs;***

Pode-se realizar um consulta junto ao suporte do Financeiro, para verificar se a rotina FINA885 possui Execauto.

***Saiba Mais :***

[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Rotina automática MVC MATA020](https://tdn.totvs.com/display/public/PROT/Pontos+de+Entrada+-+Fiscal+-+P12)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
