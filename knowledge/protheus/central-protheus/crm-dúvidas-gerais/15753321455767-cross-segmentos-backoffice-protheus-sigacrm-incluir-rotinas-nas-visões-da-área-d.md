---
article_id: 15753321455767
category: CRM - Dúvidas Gerais
content_hash: ac2b5e18bc2cbf36e111e21de964be537f88af5577d66c5dbde089851b25128c
fetched_at: '2026-06-28T22:40:27.695592+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Incluir rotinas nas visões
  da Área de Trabalho
type: support-article
updated_at: '2024-03-21T14:50:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15753321455767-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Incluir-rotinas-nas-vis%C3%B5es-da-%C3%81rea-de-Trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15949386311831) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como incluir uma rotina nas visões da "Área de Trabalho" (CRMA290)?   
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - Todas as versões.  
  
**Solução**

1. Acesse o menu "Atualizações" > "Administração" > "Configuração" > "Controle de Entidade"

Caso já tenha a tabela/rotina cadastrada é necessário verificar se os campos "Área de Trabalho", "Conexão" e "Agrupador" estão habilitados (SIM):

![p1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15753277014807)

2. Após criar o controle de entidade, é necessário acessar a rotina, exemplo "Cadastro de Produtos" (MATA010), selecione a opção "Criar Visão":

**![p2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15753306570135)**

Informe um nome para a visão que deseja criar:

**![p3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15753314652055)**

* Necessário habilitar "Visibilidade" como "Tornar esta visão pública"
* Selecionar uma ordem dos registros

Após isso, é necessário clicar na opção "Campos", onde irá informar os campos que deseja deixar visíveis na área de trabalho:

![p4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15753277021719)

3. Depois da configuração de visão é necessário acessar a área de trabalho (CRMA290) e selecionar a opção "Criar painel". Para mais detalhes do processo à seguir, veja nosso vídeo How To sobre o assunto: [How To | MP - SIGACRM - Área de Trabalho (CRMA290)](https://youtu.be/MhAYbWHxqog)

![p5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15753306574743)

* Informe o nome do painel;
* Selecionar o modelo de painel que deseja;
* Confirme

![p6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15753321433367)

* Deixar o campo "Opção" como "Tabela";
* O campo "Fontes de Dados" com o nome da Tabela/ Rotina que criou a visão;
* No campo "Visão Inicial", selecione a visão criada.

![p7.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15753291543191)

Confirme as configurações:

![p9.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15753306579351)

E confirme a gravação das configurações.

**Saiba mais:**

[Criação de layout na área de trabalho](https://tdn.totvs.com/pages/releaseview.action?pageId=244940762)

[Criar a nova visão quando uma determinada tabela não esta amarrada na rotina: CRMA290](https://tdn.totvs.com/pages/releaseview.action?pageId=270923388)

[Área de Trabalho - CRM - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=344469767)
