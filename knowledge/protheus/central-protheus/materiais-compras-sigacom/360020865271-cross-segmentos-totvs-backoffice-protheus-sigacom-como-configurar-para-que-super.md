---
article_id: 360020865271
category: Materiais - Compras (SIGACOM)
content_hash: b03ea3baf51cc93a13d00c08abed11155e524430c5fd39883dcbdacada536b5c
fetched_at: '2026-06-28T22:41:07.572558+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar para
  que Superiores tenham acesso as pendências de subordinados na aprovação de documentos
  ?
type: support-article
updated_at: '2025-09-16T15:53:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020865271-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-para-que-Superiores-tenham-acesso-as-pend%C3%AAncias-de-subordinados-na-aprova%C3%A7%C3%A3o-de-documentos
---

**Dúvida**

Como configurar para que Superiores tenham acesso as pendências de subordinados na aprovação de documentos ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras- Todas as versões  
  
**Solução**

A configuração para que o Aprovador Superior tenha acesso as respectivas pendências do então "Aprovador Ausente" é a seguinte:  
  
**1º -** Vincular o cadastro do Usuário Superior dentro do cadastro do Aprovador Ausente *(MATA095, campo AK\_APROSUP)*:

**2º -** Vincular o cadastro do Usuário Superior no grupo de aprovação em questão, na linha do respectivo Aprovador Ausente *(MATA114 - campo AL\_USERSUP)*:

**3º -**  Acessar a rotina de liberação de documentos *(MATA094)* com o usuário do Superior para realização das aprovações a serem substituídas/transferidas, e clicar em "pendências de subordinados" onde será listado todos os documentos pendentes "parados" na caixa do Aprovador Ausente.

Desta forma, é possível transferi-los e aprová-los na sequência.

Saiba utilizar o conceito de pendências de subordinados o acessando nossa pagina no YouTube: [How To | MP - SIGACOM - Pendências de Subordinados](https://www.youtube.com/watch?v=NHR2IlwmAoI)

***Obs:***

Ao utililzar a opção "pendências de subordinados" e Clicar em "Transferir" será aberta tela abaixo de aviso para ser confirmada de que "todas aprovações pendentes serão transferidas", e não há uma funcionalidade para se transferir ou selecionar apenas um ou alguns documentos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25746172019095)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA DO](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)[COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
