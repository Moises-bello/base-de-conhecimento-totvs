---
article_id: 360012403451
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: d4ddad1641d1b2b0a567e5573d673cfbee7e3ead2964f58a24d069dcd38a0e7c
fetched_at: '2026-06-28T22:37:23.959325+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ocorrência do Help
  CNNOTRANS ao realizar a Medição e/ou visualizar/alterar  um contrato
type: support-article
updated_at: '2026-05-26T19:10:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012403451-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ocorr%C3%AAncia-do-Help-CNNOTRANS-ao-realizar-a-Medi%C3%A7%C3%A3o-e-ou-visualizar-alterar-um-contrato
---

**Ocorrência**  
Ocorrência do Help CNNOTRANS ao realizar a Medição  
  
**Ambiente**  
Microsiga Protheus – Gestão de Contratos – Versão 12  
  
**Causa**

Após migração ou com contratos já migrados, ao digitar o número do contrato manualmente no campo de busca da medição, sistema apresenta o Help **CNNOTRANS**.

Essa ocorrência é exibida quando o sistema identifica que por algum motivo o processamento acionado não pode ser realizado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verificar se o contrato possui controle de acesso - CN9\_VLDCTR;  
2. Verifique se as tabelas CNN e CNO estão preenchidas com as informações dos contratos e no que tange a acessos dos usuários;  
3. Verificar os controles de acessos na opção "Outras Ações->Acessos" da rotina CNTA300, do artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Controle de Acesso ao contrato no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016499391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Controle-de-Acesso-ao-contrato-no-Gest%C3%A3o-de-Contratos)

4.  Verificar na aba Grupos, conforme print abaixo, se o mesmo encontra-se vazio, pois pode ocorrer do acesso ter sido concedido a um usuário pertencente algum "**GRUPO DE USUÁRIO**",  o qual foi excluído no módulo configurador.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418578856727)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Controle de Acesso ao contrato no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016499391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Controle-de-Acesso-ao-contrato-no-Gest%C3%A3o-de-Contratos)

[Aviso de Help CNNOTRANS ao realizar a Medição](http://tdn.totvs.com/pages/releaseview.action?pageId=318606402)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
