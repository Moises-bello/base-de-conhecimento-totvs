---
article_id: 360058879593
category: RH - Contrato Intermitente
content_hash: 79e5dab20e6febcd020245905707256ada2af90a8fef9452823f04fa3b8e3c65
fetched_at: '2026-06-28T22:43:40.089742+00:00'
product: protheus
section_id: 360003139951
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir uma convocação para funcionário intermitente
type: support-article
updated_at: '2025-04-15T12:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058879593-RH-Linha-Protheus-GPE-Como-incluir-uma-convoca%C3%A7%C3%A3o-para-funcion%C3%A1rio-intermitente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25976755265047)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como incluir uma convocação para funcionário intermitente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Após realizar o cadastro do funcionário intermitente, acesse o caminho Atualizações > Funcionários > Funcionários;  
2. Selecione o funcionário e em Outras Ações clique em **Convocações**:

Ao incluir uma nova convocação os seguintes campos devem ser informados com atenção:

Data **inicio** da atividade (V7\_DTINI) - Data efetiva do começo do trabalho

Data **final** da atividade (V7\_DTFIM) - Data do fim do trabalho

**Horas** dia (V7\_HRSDIA) - Horas trabalhadas por dia durante a convocação

**Salário** (V7\_SALAR) - Salário Hora pago durante a convocação

Esses campos serão a base para o cálculo da folha de pagamento dos funcionários com contrato intermitente.

![](https://tdn.totvs.com/download/attachments/327324780/image2017-12-29_14-32-9.png?version=1&modificationDate=1514565130000&api=v2)

As informações sobre as convocações do funcionário serão enviadas para o eSocial  através do evento S-2260 - Convocação para Trabalho Intermitente

Para o eSocial, além dos campos citados acima, vale destacar os campos

**Convocação** (V7\_CONVC) - Código para identificar a convocação

**Tipo Local** (V7\_TPLOC) - Informa onde o atividade da convocação será realizada, no estabelecimento, fora do estabelecimento ou em mais de um lugar

**Local** (V7\_LOCAL) - Código do local, caso seja fora do estabelecimento

![](https://tdn.totvs.com/download/attachments/327324780/image2017-12-29_14-51-16.png?version=1&modificationDate=1514566276000&api=v2)

Quando o tipo de **Local form 1** - Em um local fora do estabelecimento o campo Local passa a ser de preenchimento obrigatório, para reunir as informações necessárias sobre o local foi criada uma noca rotina **GPEA017 - Cadastro de Locais**onde será informado o tipo de logradouro, descrição, número, CEP...

![](https://tdn.totvs.com/download/attachments/327324780/image2017-12-29_15-2-54.png?version=1&modificationDate=1514566975000&api=v2)  
  
**Saiba Mais**

[Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003139951-RH-Contrato-Intermitente)
