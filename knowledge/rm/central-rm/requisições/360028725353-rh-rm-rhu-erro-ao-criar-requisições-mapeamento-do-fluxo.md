---
article_id: 360028725353
category: Requisições
content_hash: 243a09425b8d097075bf3c91f8430c08dd9fb96bbf386e8074d8abebb766be5b
fetched_at: '2026-06-28T22:47:25.369192+00:00'
product: rm
section_id: 1500000861382
source: central-rm
title: 'RH - RM - RHU - Erro ao criar requisições: mapeamento do fluxo'
type: support-article
updated_at: '2025-08-11T12:44:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028725353-RH-RM-RHU-Erro-ao-criar-requisi%C3%A7%C3%B5es-mapeamento-do-fluxo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34091656116631)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Durante a *abertura* de **Requisições** no RH via portal ou o sistema apresenta a seguinte mensagem de erro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042774373)  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas  - Todas as Versões  
  
**Causa**

No *cadastro* do **Tipo de Requisição** foi informado um **Tipo de Atendimento** que não *pertence* ao **Grupo de Atendimento** informado no mesmo cadastro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34091656118807)  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Editar a tela de cadastro da *requisição* e clicar sobre a opção **Redefinir Fluxo**;  
2. Informe o código do **Grupo de Atendimento,** dê um duplo clique sobre registro para acessar a *tela de cadastro* do grupo;  
3. Na tela de *cadastro do grupo*, através do menu Anexos | Tipo de Atendimento do Grupo de Atendimento;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34091672640407)

4. Adicione o **Tipo de Atendimento** ao *grupo,* sair das telas clicando sobre o opção **Salvar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34091656123159)

**Saiba mais**

Para maiores informações, acesse:

[Tipos de Requisição](https://tdn.totvs.com/pages/releaseview.action?pageId=452719406)
