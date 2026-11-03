---
article_id: 360025179531
category: Materiais - Compras (SIGACOM)
content_hash: d6ea9e072a4453e61076f84d9108c579c4df93cfdd328914dae116dedb64d3fe
fetched_at: '2026-06-28T22:41:10.392728+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a utilidade do
  Cadastro de Aprovadores (MATA095)?
type: support-article
updated_at: '2025-09-09T16:34:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025179531-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-utilidade-do-Cadastro-de-Aprovadores-MATA095
---

**Dúvida**Qual a utilidade do cadastro de Aprovadores (MATA095) ?

**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**O Cadastro de aprovadores define quais usuários do sistema são responsáveis pela aprovação dos diversos Documentos de Compras que forem submetidos ao Fluxo de Alçadas. Neste cadastro, definem-se o aprovador superior (que pode substituir a aprovação do aprovador, quando necessário), limite que será atribuído ao aprovador de acordo com seu tipo (verba) e tipo de limite (diário, semanal ou mensal). O Superior informado neste cadastro pode aprovar ou bloquear Pedidos de compras se o limite do aprovador principal tenha se excedido ou, ainda, quando este aprovador estiver ausente da empresa, sendo assim possível dar continuidade ao Processo de Compras.

Exemplo da rotina:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026323451)

Saiba como cadastrar um Aprovador acessando nossa pagina no YouTube: [How To | MP - SIGACOM - Cadastro de Aprovadores](https://www.youtube.com/watch?v=TDkhO9Wqfmw)

**Obs:**

O limite de saldo de aprovação é controlado a partir da data da primeira aprovação.

Ex: Limite de 10 mil mensal, primeira aprovação no dia 20/06, será contado 30 dias da primeira aprovação ou seja será renovado dia 20/07 e não contado como o mês do dia 1 ao dia 30.

Para consultar a soma da aprovação deve verificar a **tabela SCS - Saldo dos Aprovadores**

**Obs2:**

Quando for necessário seguir a regra do grupo de aprovação que exige a presença de um mesmo aprovador mais de uma vez, é preciso criar um novo cadastro de aprovador vinculando o mesmo usuário, a fim de permitir essa inclusão no sistema.

**Obs3:**

Caso queira utilizar uma moeda diferente da moeda 01-Real, é necessário cadastrar a moeda na rotina **Cadastro de Moedas Contábeis(CTBA140)**

Caso não seja cadastrada a moeda diferente da moeda 01-Real no Cadastro de Moedas Contabeis (CTBA140), ao informar esta outra moeda no cadastro de Aprovadores ocorrerá o Help "Moeda" da imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34812743721495)

***Saiba mais:***

[PCOM09014 - Aprovadores (MATA095)](https://tdn.totvs.com/pages/releaseview.action?pageId=274633562)

[Cross Segmento - Backoffice Protheus - SIGACOM - Campos AK\_LIMMIN e AK\_LIMMAX Descontinuados do Cadastro Aprovadores](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011227842-Cross-Segmento-Backoffice-Protheus-SIGACOM-Campos-AK-LIMMIN-e-AK-LIMMAX-Descontinuados-do-Cadastro-Aprovadores?source=search)

[MP - SIGACOM - Qual a utilidade do cadastro do Perfil de Aprovação ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024881732-MP-SIGACOM-Qual-a-utilidade-do-cadastro-do-Perfil-de-Aprova%C3%A7%C3%A3o-?source=search)

[PCOM09010 - Grupo de Aprovação (MATA114)](https://tdn.totvs.com/pages/releaseview.action?pageId=274637723)

[MP - SIGACOM - Conceito do Tipo de Liberação no Grupo de Aprovação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018595131-MP-SIGACOM-Conceito-do-Tipo-de-Libera%C3%A7%C3%A3o-no-Grupo-de-Aprova%C3%A7%C3%A3o?source=search)

[MP - SIGACOM - Em quais processos o Grupo de Aprovação (MATA114) é validado ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024652012-MP-SIGACOM-Em-quais-processos-o-Grupo-de-Aprova%C3%A7%C3%A3o-MATA114-%C3%A9-validado-?source=search)

[MP - SIGACOM - Grupo de Aprovação irá considerar ou não os valores do Perfil de Aprovação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058057973-MP-SIGACOM-Grupo-de-Aprova%C3%A7%C3%A3o-ir%C3%A1-considerar-ou-n%C3%A3o-os-valores-do-Perfil-de-Aprova%C3%A7%C3%A3o-?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
