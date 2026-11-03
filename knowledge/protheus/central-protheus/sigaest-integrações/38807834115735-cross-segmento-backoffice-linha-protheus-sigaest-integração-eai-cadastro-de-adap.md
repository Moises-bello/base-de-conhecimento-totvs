---
article_id: 38807834115735
category: SIGAEST - INTEGRAÇÕES
content_hash: d9a667300ad726c4b23a6199c2c19b3e4afc7c48764a49b9551a6b96c3c62045
fetched_at: '2026-06-28T22:38:46.164308+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração EAI: Cadastro
  de Adapters'
type: support-article
updated_at: '2026-03-24T13:53:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38807834115735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-EAI-Cadastro-de-Adapters
---

Adapters na Integração EAI do Protheus funcionam como tradutores entre a linguagem interna do sistema e sistemas externos, permitindo a comunicação via XML ou JSON. Eles mapeiam mensagens, direcionam funções no Protheus e garantem a padronização segundo o padrão TOTVS EAI. O cadastro dos Adapters é feito no módulo Configurador (SIGACFG).

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38807834100631) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
O que são Adapters na Integração EAI?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**  
O Adapter é como um tradutor. O Protheus possui uma linguagem interna (com suas tabelas e campos), e o sistema externo pode possuir outra. O Adapter é o componente que orienta ao Protheus como ler, validar e transformar os dados para que essa comunicação aconteça via mensagens XML ou JSON.

Veja um vídeo sobre o processo:

[![Cadastro de Adapters.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39256649818519)](https://youtu.be/DVWzcQQNpgc?si=pv8cCzjmwwuX9QFT)

Principais funções desse cadastro:

* **Mapeamento de Mensagens:** Ele define qual mensagem única (Message Unique) será utilizada para determinada rotina (ex: Clientes, Pedidos de Venda, Fornecedores);
* **Direcionamento:** Indica qual Função/Rotina do Protheus deve ser executada quando uma mensagem chegar ou sair;
* **Padronização:** Garante que a integração siga o padrão TOTVS EAI, que utiliza o conceito de mensagens únicas para que diferentes softwares da marca se comuniquem sem esforço extra.

O Cadastro de Adapters fica no módulo Configurador (SIGACFG), através do caminho: Ambiente > Schedule > Adapter EAI  
  
***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Integrações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)

[Cadastro de Adapter EAI](https://tdn.totvs.com/x/O__lL)
