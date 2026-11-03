---
article_id: 7583138250263
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 9e92823ddccf8702f49f02db15672891de14429b4977834d4130100f7fdc5dd4
fetched_at: '2026-06-28T22:47:29.491282+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Como utilizar a API do Portal Meu RH
type: support-article
updated_at: '2025-02-03T13:24:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7583138250263-RH-RM-Meu-RH-Como-utilizar-a-API-do-Portal-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24074790226967) Tempo aproximado para leitura: **00:02:12 min** **Dúvida**Como utilizar a API do Portal Meu RH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**

O **Swagger** descreve a estrutura de **API's** de uma forma facilitada onde é possível ter algumas informações como:

* Quais são as **API's** disponíveis no Sistema **RM**;
* Quais são os parâmetros da **API** e o que ela retorna;
* Se a **API** precisa de alguma autorização;

O **Swagger** está disponível (após a inicialização do serviço de Host em seu ambiente) no endereço [http://{dominio}:{ApiPort}/api/swagger/](http://localhost:8099/api/swagger/) ;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24074819589783)  
  
É possível acessa-las e verificar os métodos que podem ser utilizados através do **Swagger**, basta pesquisar por **Meu RH** para encontrar as informações de forma mais rápida utilizando o atalho **CTRL+F.**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7582747136535)  
  
Pela aplicação **Meu RH** via *Desktop*, o usuário poderá acessar a tela desejada e executar o processo desejado teclando **F12**, na aba *Network* poderá encontrar a API correta através da URL retornada pelo **Header**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7583023719831)
