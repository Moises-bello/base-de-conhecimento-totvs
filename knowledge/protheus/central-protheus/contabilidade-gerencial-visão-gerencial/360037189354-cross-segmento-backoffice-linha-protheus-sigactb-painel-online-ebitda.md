---
article_id: 360037189354
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 3692076bcf8fe057586f375d83aad5f300615b9e0f3ac0da00b57224f2019260
fetched_at: '2026-06-28T22:40:50.630779+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Painel online EBITDA
type: support-article
updated_at: '2022-09-12T11:59:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037189354-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Painel-online-EBITDA
---

**Dúvida**Como configurar o Painel online, Ebitda?  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80.  
  
**Solução:**

Para que as informações sobre a evolução mensal do ***EBITDA*** sejam exibidas no painel online do módulo Contabilidade Gerencial (**SIGACTB**) do **PROTHEUS**, será necessário criar uma **visão gerencial** de maneira que a entidade sintética deste cadastro represente o valor total do ***EBITDA***.

O painel online irá exibir na tela inicial do módulo o resultado da visão gerencial configurada pelo usuário de acordo com os filtros estipulados nos parâmetros da rotina.

* Caso ainda não tenha o painel online configurado, acessar a documentação.

<https://tdn.totvs.com/display/public/PROT/Configurar+o+recurso+Painel+Online>

* Acesse a documentação sobre visão gerencial

<https://tdn.totvs.com/pages/viewpage.action?pageId=334337892>

Documentação necessária para configuração:

<https://tdn.totvs.com/pages/releaseview.action?pageId=437258651>

Importante:

* Configurado um appserver separado para o Painel.
* Permissão ao painel no cadastro de grupos.
* Permissão ao painel ao usuário que terá acesso.

![](https://totvssuporte.zendesk.com/attachments/token/OXClWvcuH917nPjIG7qVkHKqJ/?name=inline-1280449477.png)​  
  
Acessar como SIGAMDI 

![](https://mail.google.com/mail/u/0?ui=2&ik=3ae937b27b&attid=0.3&permmsgid=msg-a:r-3739097606605220478&th=16dd094a059b0280&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ9Lz598_b1X3AJLzzwaPAgDMNWLzlKIA-2xCVSKHPbNSM4NxKdFo-olsxoZ-yz0I57gCRTaeeUVKeE1IMHEqFLcD1-cMkPRpODA6QS77ac7ZS3ncaL5G1CPFEE&disp=emb&realattid=ii_k1s4uqlf2)

* **Atenção: Não é possível acessar o Painel com o usuário "ADMIN". Este usuário somente deve ser utilizado para criar os usuários administradores do Sistema e definir a Política de Segurança da empresa.**
