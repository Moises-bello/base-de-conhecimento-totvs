---
article_id: 6493773904535
category: Gestão de Distribuição (SIGAOMS)
content_hash: 0e330064060077ccdd997ee2cf9e3d3410d9f6708dc6c76b15577adf19521cf0
fetched_at: '2026-06-28T22:45:49.689869+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como gerar Totvs Replay, DBTrace e Inspetor
  de Objetos
type: support-article
updated_at: '2022-06-06T13:29:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6493773904535-Log%C3%ADstica-Linha-Protheus-OMS-Como-gerar-Totvs-Replay-DBTrace-e-Inspetor-de-Objetos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como gerar **Totvs Replay**, **DBTrace** e **Inspetor de Objetos**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - **Todas as versões**  
**Solução**1.Para gerar o **TOTVS Replay** efetue os seguintes passos:

* Acesse a rotina que estiver apresentando a inconsistência e **clique em** **SHIFT+F6**, na tela apresentada **clique em avançar** até a **quinta aba TOTVS Replay - clique em Iniciar - Concluir.**
* Execute o processo no Sistema até que seja reproduzido o incidente reportado.
* Após realização do processo **clique em SHIFT+F6**, e na tela apresentada **avance** novamente até a **quinta aba TOTVS Replay e clique em Finalizar**.

![replay.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6493983597975/replay.JPG)

Nesse momento o Sistema apresenta uma janela com o local onde o arquivo foi criado.

![replay_arquivo.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6494325442967/replay_arquivo.JPG)

* Localize o arquivo no diretório onde consta o **SMARTCLIENT** da maquina que foi ativado o **Totvs Replay**. Envie o arquivo gerado via ticket para avaliação.

2.Para gerar o **DBTrace** efetue os seguintes passos:

* Acesse o aplicativo **DbAccess Monitor** e informe o **IP** e **Porta para acesso.** Caso não tenha conhecimento de qual **IP e Porta** informar no campo **Servidor e Porta**, verifique com área interna de **Tecnologia da Informação** da sua empresa.
* Clique na **aba Usuários** e **selecione o usuário que ira executar** a rotina que está apresentando o incidente reportado. Clique no **Botão Rastrear para iniciar o trace do processamento**.
* Veja que ao executar o processamento da rotina as instruções são visualizadas no rastreamento, após o **termino do processamento clique no botão Salvar** para salvar o **Log** gerado.
* Após salvar o arquivo com o **Trace de processamento da rotina,** envie o arquivo gerado via ticket para avaliação.

![DBTRACE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6499319058711/DBTRACE.png)

3.Para gerar o **Inspetor de Objetos** efetue os seguintes passos:

* Acessar uma rotina qualquer dentro no **Protheus**, clique em **SHIFT+F6**, na tela apresentada clique em **Exportar dados.**
* Será apresentada a mensagem abaixo para confirmação da exportação.
* Após a confirmação da exportação, será necessário escolher o diretório onde será salvo o arquivo. É necessário digitar no **campo Nome do Arquivo o nome do arquivo a ser gerado.**
* Será exibida uma mensagem que a exportação ocorreu com sucesso.
* envie o arquivo gerado via ticket para avaliação

**![exportar_dados.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6501575522455/exportar_dados.png)**
