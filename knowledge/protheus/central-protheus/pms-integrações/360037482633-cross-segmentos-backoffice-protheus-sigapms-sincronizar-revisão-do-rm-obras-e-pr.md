---
article_id: 360037482633
category: PMS - Integrações
content_hash: 44676fa66de7efd304e908fb46a9e4bb71d99fdde3a1905f006adf451ac2a718
fetched_at: '2026-06-28T22:37:16.737603+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAPMS - Sincronizar revisão do RM
  Obras e Projetos com o Protheus PMS '
type: support-article
updated_at: '2024-02-26T18:33:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037482633-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Sincronizar-revis%C3%A3o-do-RM-Obras-e-Projetos-com-o-Protheus-PMS
---

**Ocorrência**

Ao sincronizar uma revisão de projeto do RM para o Protheus ocorre falha no sincronismo das tarefas:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048391494)

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - a partir da versão 12.  
  
**Solução**

Ao realizar uma revisão de venda o código de projeto recebe o sufixo **“\_V”** e dispara a mensagem de integração de um novo projeto com todas as tarefas, de forma que o Protheus terá dois projetos, o principal e o de venda, sendo sempre atualizado o De/Para com o ultimo ID do projeto das revisões.

Para a correção da falha de sincronismo é necessário alterar o grupo de campo do projeto para o tamanho 30, desta forma terá compatibilidade com o tamanho do campo código de Projeto do TOTVS Obras e Projetos (RM).

**Obs.:** **Projeto RM -**É necessário alterar o grupo de campo 097-Projeto do Protheus para o tamanho 30 para que haja compatibilidade com o tamanho do campo código de Projeto do TOTVS Obras e Projetos.

Além da alteração do Projeto é importante se atentar também no aumento dos campos Tarefa e EDT, quando se utiliza o TOP RM, o tamanho deve ser 50.

Maiores detalhes:  [**MP - PMS - AUMENTAR O TAMANHO DO PROJETO, EDT E TAREFA.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046879333-MP-PMS-AUMENTAR-O-TAMANHO-DO-PROJETO-EDT-E-TAREFA-?source=search)
