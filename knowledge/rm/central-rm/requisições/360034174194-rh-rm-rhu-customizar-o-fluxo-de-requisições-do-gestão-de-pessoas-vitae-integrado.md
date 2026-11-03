---
article_id: 360034174194
category: Requisições
content_hash: afd4d0584cae66082826dde5189105f00735e8dace62d8ba3a78a178e9238812
fetched_at: '2026-06-28T22:47:25.364415+00:00'
product: rm
section_id: 1500000861382
source: central-rm
title: RH - RM - RHU - Customizar o fluxo de requisições do Gestão de Pessoas (Vitae)
  integrado com o TOTVS Aprovações e Atendimento (Agilis)
type: support-article
updated_at: '2025-10-30T17:51:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034174194-RH-RM-RHU-Customizar-o-fluxo-de-requisi%C3%A7%C3%B5es-do-Gest%C3%A3o-de-Pessoas-Vitae-integrado-com-o-TOTVS-Aprova%C3%A7%C3%B5es-e-Atendimento-Agilis
---

*****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15864226191127)*** Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Como customizar o fluxo de requisições do Gestão de Pessoas (Vitae) integrado com o TOTVS Aprovações e Atendimento (Agilis)?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - Todas as versões  
  
**Solução**Para realizar o processo siga as orientações abaixo:

1- Criar um tipo de atendimento. Para criar um tipo de atendimento acesse o módulo **TOTVS Aprovações e Atendimentos** | **Workflow** | **Tipos**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002284473367)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002317779223)

2 - Criar as etapas que irão compor o fluxo de atendimento.   
Para criar as etapas, acesse o menu **Workflow** | **Tipos**, selecione o tipo criado e acesse a opção **Anexos** | **Etapas.**  

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002284478871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002284482583)

3- Criar o fluxo das etapas. Para criar as etapas, acesse **Workflow** | **Tipos**, selecione o tipo criado e acesse a opção **Anexos** | **Fluxo de Etapas**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002317785623)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002317786903)

Obs: Em todos os procedimentos a caixa "Ativar Fluxo de tarefa" deverá estar marcada para que o procedimento funcione.

4 - Criar um grupo de atendimento. Para criar um tipo de atendimento, acesse o menu **Workflow** | **Grupos**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002284489367)

5 - Vincular o tipo de atendimento criado ao grupo de atendimento criado. Para isso, selecione o grupo criado e acesse a opção **Anexos** | **Tipos de atendimento**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002284495255)

O tipo de atendimento está criado e vinculado ao grupo de atendimento que será utilizado na integração com o Vitae.  Caso deseje, abaixo segue um exemplo de como realizar a configuração acima:

Estrutura Hierárquica:  
• Supervisão (requisitante);  
• Coordenação (aprovador);  
• Gerência (aprovador);  
• Direção (aprovador).  
  
Estrutura das Etapas:

![[image%255B14%255D.png]](http://lh4.ggpht.com/-BYHy5atySjo/ThCk-Suy75I/AAAAAAAABUY/FLqrGiRShyY/s1600/image%25255B14%25255D.png)

Estrutura do Fluxo de Etapas

![[image%255B7%255D.png]](http://lh5.ggpht.com/-3OJfWXQwIs0/ThClE-nta6I/AAAAAAAABUg/3hZ-zonFvAk/s1600/image%25255B7%25255D.png)

Caso deseje, o fluxo e as etapas podem ser customizados de acordo com sua regra de negócio e podem ter fórmulas.

**Importante**

- Lembrando que o suporte não analisa fórmulas. Caso deseje, pode ser acionado o serviço de consultoria telefônica para verificação.

- Qualquer dúvida quanto ao processo de criação do fluxo de Atendimento, deverá entrar em contato com o suporte do RM TOTVS Aprovações e Atendimentos >> RM C&P.

Após as configurações dos fluxos e etapas, deve acessar o Gestão de Pessoas e realizar a parametrização necessária.

1- Acesse no Gestão de Pessoas o menu **Configurações** | **Tipos de Requisição**, e vincule o Grupo e o Tipo de Atendimento criado no Agilis para o tipo de Requisição desejado e clique em salvar.

**Obs:** Caso já tenham um fluxo criado, para colocar o Tipo e Grupo desejado, deverá clicar em 'Redefinir Fluxo'. Este processo só poderá ser executado quando para aquele tipo de requisição não tiverem requisiçoes com o status 'Em andamento'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002284498967)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002284503447)

2 - Devemos alterar o mapeamento do fluxo indicando qual será o status da requisição do Vitae em cada etapa do atendimento do TOTVS Aprovações e Atendimentos (Agilis). Para isso, acesse o menu aba **Mapeamento do Fluxo** presente no cadastro do Tipo da Requisição, conforme o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27002284505751)

**Obs:** É obrigatório ter um parecer com o status **'Aprovado'**. O restante pode ficar em andamento e reprovado, de acordo com a regra de negócio do cliente.

A integração entre o Vitae e o Agilis consiste em ter uma aprovação de requisições de variados tipos. No momento que a requisição está sendo criada, um atendimento é inserido no Agilis. O status do atendimento do Agilis e da requisição do Vitae são independentes, por exemplo: posso ter uma requisição aprovada com o atendimento em andamento.

É recomendado que o status do parecer siga o mesmo status do atendimento.

Por exemplo: na etapa 3 o atendimento será concluído, logo alteramos o status do parecer no RM Vitae, referente a essa etapa, para Aprovado e assim por diante.

**Saiba Mais**

Para maiores informações, acesse:

- [Tipo de Atendimento - TOTVS Aprovações e Atendimento](https://tdn.totvs.com/pages/releaseview.action?pageId=425459518)

- [Etapas](https://tdn.totvs.com/display/public/LRM/Etapas)

- [Fluxo de Etapas](https://tdn.totvs.com/display/public/LRM/Fluxo+de+Etapas)

- [Grupos de Atendimentos](https://tdn.totvs.com/display/public/LRM/Grupos+de+Atendimentos)

- [Tipos de Requisição](https://tdn.totvs.com/pages/releaseview.action?pageId=452719406)
