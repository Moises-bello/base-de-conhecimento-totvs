---
article_id: 40906864798359
category: SIGAACD - Automação e Coleta de Dados
content_hash: bea73973c5e9a2184b61cd3e6dd3a4cc1a3769dbcf15f8021dee216539a848ff
fetched_at: '2026-06-28T22:39:13.915738+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAACD - O app Meu Coletor
  de Dados funciona offline?
type: support-article
updated_at: '2026-06-02T14:11:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40906864798359-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAACD-O-app-Meu-Coletor-de-Dados-funciona-offline
---

O aplicativo Meu Coletor de Dados funciona offline de forma parcial, atuando como contingência para quedas de conexão. Ele permite continuar processos iniciados online, como inventário, durante a perda de internet e envia automaticamente os dados ao Protheus quando a conexão é restabelecida.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40906861036567) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**

O aplicativo Meu Coletor de Dados funciona em modo offline para a realizar os processos nas rotinas?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados (SIGAACD) - Todas as versões.

**Solução**

O funcionamento offline do aplicativo Meu Coletor de Dados ocorre de forma parcial, atuando especificamente como uma contingência para quedas de rede, e não como um modo de operação contínuo.

O aplicativo não permite navegação pelos menus sem conexão. O modo offline entrará em ação apenas se você perder a conexão com a internet. Utilizando o processo de inventário como exemplo, ele funcionará no momento em que já estiver na tela de contagem (após ter clicado em "Iniciar Contagem").

Neste cenário de perda repentina de conexão durante a execução da tarefa, você conseguirá prosseguir com a contagem daquele item e finalizá-la no aplicativo. Assim que o dispositivo restabelecer a conexão com a internet, as informações armazenadas localmente serão enviadas de forma automática para o Protheus, atualizando o status da tarefa no sistema.

Essa característica não se restringe apenas à rotina de Inventário, sendo válida também para os outros processos do aplicativo.

**Passos para o cenário de contingência:**

1. Acesse o aplicativo e inicie a rotina desejada (exemplo: Inventário > Iniciar Contagem) com o dispositivo conectado à internet.
2. Em caso de queda ou perda de conexão (modo offline) durante esta etapa, continue o apontamento das quantidades do item normalmente.
3. Finalize a contagem do item no aplicativo.
4. Restabeleça a conexão com a internet.
5. O aplicativo enviará automaticamente os dados gravados para o Protheus, alterando o status da contagem no sistema de "Em andamento" para "Finalizado".

**Saiba mais:**

[**Meu Coletor de Dados : Guia de Referência**](https://tdn.totvs.com/pages/releaseview.action?pageId=506994322)

[**Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como configurar o App Meu Coletor de Dados?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30317999783703)

[***Clique aqui e veja mais artigos sobre Automação e Coleta de Dados***](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
