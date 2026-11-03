---
article_id: 360027793151
category: Cálculo
content_hash: 8f70f3c3f5315466cfc357670b621ae797de466beddbd73a999ed964ff6b9051
fetched_at: '2026-06-28T22:46:29.219347+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Fracionamento de JOBS ao recalcular
type: support-article
updated_at: '2025-02-04T16:29:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027793151-RH-RM-PTO-Fracionamento-de-JOBS-ao-recalcular
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19409075928983) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Como realizar o fracionamento da execução de Jobs para o processo de recalculo do ponto?  
  
**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 12.1.4

**Solução**

Para definir fracionamento de Jobs ao recalcular o ponto, é necessário liberar a opção de fracionamento para o usuário, assim será apresentada a opção de fracionamento ao executar o recalculo. Dessa forma siga os passos abaixo:

1. Acesse no modulo de **Serviços Globais** o menu, **Segurança | Usuários**, selecione o sistema **Automação de Ponto**. Selecione e edite o usuário desejado e clique na aba segurança e valide quais são os perfis associados ao usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13734332648983)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13734336834967)

2. Ainda no modulo de Serviços Globais o menu **Segurança | Perfis**, selecione o sistema **Automação de Ponto**. Selecione e edite o perfil vinculado ao usuário e clique na aba acesso a menus confira se o item **03.01.01.15 - Fracionamento do Recalculo está liberado:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13736828208407)

3. Após liberar o perfil de acesso ao usuário. Acesse no modulo **Automação de Ponto**, o menu **Movimento | calcular e** **clique** no **botão Excetuar.** ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13736923906327)

4. Ao clicar em executar, será apresentado a tela com a pergunta '***Deseja fracionar o recalculo em N processos?',*** clique em **sim**.      
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13736997189143)

5. Será apresenta a tela fracionamento, onde deve **informar em quantas partes você deseja dividir o processo atual** e clique no botão próximo:    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13737168868887)

6. Será apresentado a tela de visualização da forma de agrupamento definida e clique em **Executar**:    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13737294652823)

7. Ao executar o processo, será exibido um recurso onde o usuário irá acompanhar a execução dos Jobs disparados.   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13737297316119)

**Saiba Mais**[Fracionamento do cálculo](http://tdn.totvs.com/display/public/LRM/DT_Fracionamento_Calculo)
