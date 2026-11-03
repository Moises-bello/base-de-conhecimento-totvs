---
article_id: 7300237756183
category: PMS - Projetos
content_hash: 79506990fedf9a1147cb15d0f9ffc4dce4e4356eb778f17485cecb8dc18938c3
fetched_at: '2026-06-28T22:37:14.840865+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - PMS - Mensagem Erro01
  na Tarefa '
type: support-article
updated_at: '2022-08-03T12:52:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7300237756183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-PMS-Mensagem-Erro01-na-Tarefa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Ao incluir ou importar um Project no PMS esta gerando a EDT/Tarefa com mensagem de erro:

![erro_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7299926956311/erro_1.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - PMS  - Todas as versões  
  
**Causa**Mensagem de erro gerada como proteção no fonte, para quando incluir e estiver dentro da limitação do campo o sistema ao invés de derrubar o processo e precisar refazer, ele imprimi a mensagem de erro e permite você corrigir recodificando.  
  
**Solução**Para corrigir a mensagem de erro siga o passo a passo abaixo:

* Acesse a rotina de **Projetos**;
* Posicione no projeto e clique em **Alterar Cadastro**;
* Acesse a aba de Código Estruturado;
* O campo delimitador é apresentando quando você gera a tarefa e ele separa por ponto.  
  dessa forma:  
  ![erro_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7300052769559/erro_2.png)
* o campo mascara é o que define os campos de código da tarefa, sendo assim se alterar o campo para 3 ele deixa de apresentar a mensagem de erro00000;
* Após alterar para 3 salve e acesse o projeto, alterando a estrutura;
* Posicione em cima da **EDT** > **Acesse** **Outras** **Ações** > **Ferramentas** > **Recodificar**;
* Clique em Sim na mensagem que ira apresentar na tela e o sistema ira recalcular.
* Ele grava sempre a próxima numeração, então sempre que recodificar ele ira pegar a próxima numeração para manter a integridade dos dados.

Processo detalhado acima:

![pms.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7300539240855/pms.gif)

**Importante!**Essa configuração é por projeto, então se tiver mais de um é necessário recodificar.

**Saiba Mais**
