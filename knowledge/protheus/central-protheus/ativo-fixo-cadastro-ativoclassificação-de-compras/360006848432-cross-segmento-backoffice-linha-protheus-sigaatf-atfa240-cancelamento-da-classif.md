---
article_id: 360006848432
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: ffbe82322264a4e2c87c05c8e775ac19b7e26ada86598ac2e11e71d33b2bf7e5
fetched_at: '2026-06-28T22:41:48.249688+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA240 - Cancelamento
  da classificação do bem
type: support-article
updated_at: '2025-04-10T17:13:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006848432-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Cancelamento-da-classifica%C3%A7%C3%A3o-do-bem
---

**Dúvida**

É possível cancelar a classificação do bem do ativo imobilizado?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 12.1.2310

**Causa**Este processo é necessário, por ter os campos desabilitados para alteração.  
  
**Solução**Se houver necessidade de ajuste das informações  do bem após ter sido confirmada sua inclusão, mas ainda não ocorreu cálculo de depreciação, o processo de cancelamento da classificação pode ser executado.

Foi adicionada uma nova funcionalidade em ***Outras Ações → Cancelar Classificação*.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27249730019735)**

Ao posicionar o cursor sobre o bem em questão, o sistema exibirá um help sobre a operação, perguntando se o usuário deseja realmente prosseguir. Se confirmado, o status do bem retornará para "**Não Classificado**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27249792797335)

Condições para o cancelamento:

O bem **não pode** apresentar nenhuma das seguintes características:

* Estar marcado como "Bem a Classificar";
* Estar bloqueado;
* Ser um bem em construção;
* Ter sido transferido;
* Não estar vinculado a uma nota fiscal;
* Apresentar qualquer movimentação registrada (baixa, transferência, depreciação, ampliação, valor recuperável) na tabela *SN4*.

Processo de cancelamento da classificação, seguir a documentação com exemplo:

* [ATFA240 - Classificação de Compras - Melhoria Cancelamento de Classificação](https://tdn.totvs.com/pages/releaseview.action?pageId=830948965#ATFA240Classifica%C3%A7%C3%A3odeComprasMelhoriaCancelamentodeClassifica%C3%A7%C3%A3o-02.EXEMPLODEUTILIZA%C3%87%C3%83O)

Saiba Mais

[Classificação do Bem não gatilha conta contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006575352-MP-SIGAATF-Ao-classificar-um-bem-o-sistema-n%C3%A3o-carrega-a-conta-cont%C3%A1bil)

[Aquisição e classificação do bem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012521571-MP-SIGAATF-AQUISI%C3%87%C3%83O-DE-BEM-OU-IMOBILIZADO-E-CLASSIFICA%C3%87%C3%83O-DE-COMPRAS)
