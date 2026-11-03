---
article_id: 38822176270871
category: SIGAEST - INTEGRAÇÕES
content_hash: 884bf9c50f5e56faa7fe5e24b494d6aae7ab615702651cb13e46d0847d835e94
fetched_at: '2026-06-28T22:38:46.158997+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração EAI: Síncrona
  e Assíncrona'
type: support-article
updated_at: '2026-03-25T19:00:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38822176270871-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-EAI-S%C3%ADncrona-e-Ass%C3%ADncrona
---

No Protheus, integração síncrona exige que o sistema remetente espere a resposta antes de continuar, garantindo confirmação imediata, mas pode causar bloqueios se o destino estiver lento. Já a integração assíncrona envia mensagens para uma fila, liberando o sistema imediatamente, oferecendo mais performance e resiliência, porém requer monitoramento posterior para erros. A escolha depende do uso, com síncrona para operações que precisam de resposta imediata e assíncrona para grandes volumes de dados.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38822148102551) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
O que é uma mensagem Síncrona e uma Assíncrona na Integração EAI?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**  
No contexto do **EAI (Enterprise Application Integration)** do Protheus, a diferença entre síncrona e assíncrona resume-se a uma pergunta simples: **o sistema que enviou o dado precisa esperar a resposta para continuar trabalhando?**

Clique na imagem abaixo, para ver um vídeo sobre o processo:

[![Sincrona e Assincrona.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39256857940759)](https://youtu.be/1uE9-R3Sk5Q?si=sMSLfbu0gvRALmSu)

---

## 1. Integração Síncrona (Tempo Real)

Na integração síncrona, a comunicação acontece de forma imediata. O sistema remetente envia a mensagem e **fica parado** aguardando a confirmação de que o processamento no destino foi concluído.

* **Como funciona:** O Protheus envia um dado e espera a confirmação de gravação ou uma mensagem de erro. Só depois dessa resposta é que o usuário recupera o controle da tela no Protheus.
* **Vantagem:** Você tem a confirmação imediata do sucesso ou erro.
* **Desvantagem:** Se o sistema de destino estiver lento ou fora do ar, o Protheus também pode ficar aguardando para concluir o processo ou exibir um erro de "*timeout"*.

## 2. Integração Assíncrona (Fila de Processamento)

Na integração assíncrona, o sistema remetente envia a mensagem para uma **fila** e conclui a execução. Ele não espera o processamento final do destino.

* **Como funciona:** O Protheus gera uma nota fiscal e joga a mensagem no EAI. O EAI recebe a mensagem e aguarda o processamento do Schedule. O Protheus libera a tela para o usuário imediatamente. O destino processa essa mensagem quando o Schedule executar o envio programado.
* **Vantagem:** Muito mais performance e resiliência. Se o sistema de destino cair, a mensagem fica na fila e é processada assim que ele voltar, sem perder dados.
* **Desvantagem:** Você não sabe se deu erro na hora. Precisa monitorar o **Monitor do EAI** para ver se alguma mensagem falhou depois.

---

## Comparativo Rápido

| **Característica** | **Síncrona** | **Assíncrona** |
| --- | --- | --- |
| **Aguardar Resposta** | Sim (Bloqueia a execução) | Não (Libera a execução) |
| **Uso Comum** | Consultas (ex: saldo em estoque) | Cadastros (ex: inclusão de cliente) |
| **Conexão** | Exige que ambos estejam online | Tolera quedas temporárias |
| **Feedback** | Imediato ao usuário | Via monitoramento de filas |

---

## Qual escolher no Protheus?

No cadastro de **Adapters**, você define isso no campo "Método". Geralmente, para grandes volumes de dados (como carga de produtos), usa-se **Assíncrona**. Para operações que dependem de uma resposta externa para o próximo passo do usuário, usa-se **Síncrona**.

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Integrações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)

[Cadastro de Adapter EAI](https://tdn.totvs.com/x/O__lL)
