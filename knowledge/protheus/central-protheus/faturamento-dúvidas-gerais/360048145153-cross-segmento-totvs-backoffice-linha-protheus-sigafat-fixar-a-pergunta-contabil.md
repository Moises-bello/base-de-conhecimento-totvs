---
article_id: 360048145153
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: a9968f93dae977b9cf7656124df90ebcb5d75b2ac986e9f40592cf814d1f422b
fetched_at: '2026-06-28T22:38:28.569510+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Fixar a pergunta
  contabiliza on line como Sim na rotina de exclusão da nota
type: support-article
updated_at: '2023-08-30T21:31:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048145153-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Fixar-a-pergunta-contabiliza-on-line-como-Sim-na-rotina-de-exclus%C3%A3o-da-nota
---

**Dúvida**

Como fixar a pergunta do menu **F12** do browser da exclusão da nota (**MATA521A**) para que os usuários não alterem?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Em Configurador, Usuário, Configuração de Perguntas(**CFGA540**), inclua uma nova configuração para a perguntas **MTA521**, deixando a opção ***Contabiliza On line*** como ***Sim***;

2. Para que acate a configuração, clique na tecla ***Delete*** do teclado para que a linha fique editável;

3. Atribua a configuração a um ***Usuário*** do Configurador ou a um ***Grupo de Usuário***. Lembrando que se for atribuído a um grupo de usuário, deverá verificar se este usuário pertence ao grupo no qual configurou o pergunte;

4. Acesse o módulo de ***Faturamento*** (***com o usuário diferente de Administrador e que pertença ao Grupo a qual o pergunte foi configurado***), Faturamento, Exclusão de Documento de Saída;

5.Ao entrar no Browser de Exclusão da Nota, clique na tela **F12** para a visualização do menu;

6-Verifique que a pergunta aparece como deletada e já fixada com a resposta Sim.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069572414)

As telas do passo a passo completo pode ser visualizado no anexo deste artigo.
