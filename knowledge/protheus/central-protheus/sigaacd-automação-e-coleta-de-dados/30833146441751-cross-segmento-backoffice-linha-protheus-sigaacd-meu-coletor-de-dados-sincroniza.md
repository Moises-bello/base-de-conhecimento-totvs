---
article_id: 30833146441751
category: SIGAACD - Automação e Coleta de Dados
content_hash: 106240ad7154a3df1118e8754b31a73bd75ff90c4628f0d6f673524ee493067f
fetched_at: '2026-06-28T22:39:12.799842+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Meu Coletor de Dados
  - Sincronização dos produtos no App Meu Coletor de Dados
type: support-article
updated_at: '2025-11-14T16:39:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30833146441751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Meu-Coletor-de-Dados-Sincroniza%C3%A7%C3%A3o-dos-produtos-no-App-Meu-Coletor-de-Dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30833129957527) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como é realizada a carga de produtos no processo de sincronização do App Meu Coletor de Dados?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**A carga dos produtos na sincronização do app Meu Coletor de Dados ocorre via API(Products). Nela o app realiza uma verificação para carregar os produtos.

**Fonte responsável por essa API: ACDM010**

**EndPoint da API**: http://(ip do REST):(porta do REST)/rest/acdmob/products?page=1&PageSize=3000

O EndPoint citado acima, é onde ocorre a requisição que o app irá utilizar para sincronizar a lista dos produtos podendo ser validado também em outras aplicações no caso de testes, exemplo: Postman, SoupUi, etc.

O parâmetro "Page" é o número da página carregada pela aplicação. O "PageSize" é a quantidade de registros carregados pela aplicação. Caso na primeira requisição, o app identificar que a quantidade é maior do que 3000(padrão do app Meu Coletor), ele carrega outra requisição, incrementando mais um ao parâmetro "Page".

**(OBS)**: Os produtos serão carregados somente no processo de sincronização, e serão mantidos no app para uso de suas funcionalidades. Caso seja realizado um novo cadastro de produto no Protheus após essa sincronização, será necessário sincronizar novamente.

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30833129958167)

ATENÇÃO:

Esta documentação tem o intuito de auxiliar em testes para implementação e análise do Aplicativo meu coletor de Dados.

Atualmente, as APIs do produto são de uso exclusivo para componentes internos da nossa plataforma. Por este motivo, não as documentamos ou recomendamos consumo externo.

Como não são APIs públicas, elas estão sujeitas a mudanças (incluindo breaking changes) sem aviso prévio, conforme evoluímos o produto. 

***Saiba mais:***

# [Configuração do REST Mobile](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043179314-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configura%C3%A7%C3%A3o-do-REST-Mobile)

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
