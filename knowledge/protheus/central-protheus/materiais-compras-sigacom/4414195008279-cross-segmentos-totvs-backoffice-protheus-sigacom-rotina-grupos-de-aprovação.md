---
article_id: 4414195008279
category: Materiais - Compras (SIGACOM)
content_hash: 919a3dc2acc4a53c4659d125b4ff7d0794dfda64d1e75f0e871c9235258afcbd
fetched_at: '2026-06-28T22:41:25.305009+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Grupos de Aprovação
type: support-article
updated_at: '2026-05-14T15:24:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414195008279-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Grupos-de-Aprova%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19283164245911) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Rotina Grupos de Aprovação - MATA114  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões 

**Solução**  
Neste cadastro, os aprovadores são associados em grupos, conforme a hierarquia de aprovação definida pela empresa. O objetivo desse cadastro é fornecer a árvore de aprovação para os documentos de compra. Nesse cadastro é definido o nível de aprovação dos usuários dentro do grupo de aprovação, define também a hierarquia de aprovação do grupo. Ao gerar o fluxo de aprovação, o sistema passa somente ao próximo nível quando o atual estiver aprovado (e assim até todos os níveis aprovarem o documento). Há ainda a possibilidade de configuração de diferentes tipos de aprovação ao utilizar o campo Tipo de Liberação.

Saiba como cadastrar um Grupo de Aprovação acessando nossa pagina no YouTube:  [How To | MP - SIGACOM - Grupo de Aprovação](https://www.youtube.com/watch?v=J_yqoajGT-g)

Para mais informações sobre este cadastro verificar o link abaixo do TDN:

[PCOM09010 - Grupo de Aprovação (MATA114)](https://tdn.totvs.com/x/m6NeE)

**Dúvidas Frequentes**

***Obs1:***

A tabela de Grupos de Aprovação (SAL) por padrão vem como exclusiva, caso queira utilizar um grupo de aprovação para incluir alçada em outra filial. É necessário efetuar a criação do Grupo na mesma filial que será lançado o Pedido/Solicitação.

***Obs2:***

Ao cadastrar na aba de entidades contábeis as chaves referente a alçada por entidade o padrão de preenchimento da chave é de acordo com a imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25280029247767)

***Obs3:***

Ao cadastrar aprovadores é necessário utilizar 2 caracteres no campo AL\_NIVEL para os aprovadores, o sistema não permite ter apenas 1 caractere.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28415644741143)

**Obs4:**

**Posso ter um mesmo aprovador informado duas vezes no grupo de aprovação?**

R. No cadastro de Grupo de Aprovação não é permitida a inclusão de um mesmo cadastro de Aprovador masi de um vez em linha diferentes, onde caso se informe, no padrão é retornada a mensagem "UNIQUELINE" ao tentar sair da linha do código de aprovador duplicado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36699247226263)

O que é possível ser realizado, é cadastrar para o mesmo usuário do Protheus mais de um cadastro de Aprovador, e assim informar esses cadastros de aprovadores diferentes (do mesmo usuário Protheus ) neste mesmo Grupo de Aprovação. Pois, no mesmo grupo de aprovação, não é permitido vincular o mesmo cadastro de aprovador mais de uma vez.

**Obs5:**

Segue abaixo as Definições do campo Tipo Liberação do grupo de aprovação;

* **Tipo Lib.**(AL\_TPLIBER): Identifica o tipo de liberação que será executada pelo aprovador em questão. Pode assumir os seguintes valores:

  + **Usuário:** Realiza a liberação apenas do aprovador em questão. Os demais aprovadores do grupo, inclusive de mesmo nível devem proceder com as respectivas aprovações para que o documento seja liberado.
  + **Nível:** Realiza a liberação de todo o nível ao qual o aprovador pertence no Grupo de Aprovação, disponibilizando o documento para análise do nível seguinte.
  + **Documento:** Realiza a liberação de todo o grupo de aprovação, atualizando o status do documento analisado para **Liberado** e encerrando o **Fluxo de Alçadas**.

***Saiba Mais :***

[7 - Grupo de Aprovação](https://tdn.totvs.com/x/cBs4Hg)

[PCOM09010 - Grupo de Aprovação (MATA114)](https://tdn.totvs.com/x/m6NeE)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
