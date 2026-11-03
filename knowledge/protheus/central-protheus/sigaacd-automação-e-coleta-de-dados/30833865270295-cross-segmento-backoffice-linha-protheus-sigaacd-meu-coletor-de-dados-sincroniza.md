---
article_id: 30833865270295
category: SIGAACD - Automação e Coleta de Dados
content_hash: 7e77aa1d73beeacf3f099966cadba04fc1e6cc5113b0bad1844e1cf6462bf298
fetched_at: '2026-06-28T22:39:12.792653+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Meu Coletor de Dados
  - Sincronização dos armazéns no App Meu Coletor de Dados
type: support-article
updated_at: '2025-03-24T11:53:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30833865270295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Meu-Coletor-de-Dados-Sincroniza%C3%A7%C3%A3o-dos-armaz%C3%A9ns-no-App-Meu-Coletor-de-Dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30833865239191) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como é realizada a carga de armazéns no processo de sincronização do App Meu Coletor de Dados?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**A carga dos armazéns na sincronização do app Meu Coletor de Dados ocorre via API(Warehouse). Nela o app realiza uma verificação para carregar os armazéns.  
  
**Fonte responsável por essa API: ACDM010**

**EndPoint da API**: http://(ip do REST):(porta do REST)/rest/acdmob/warehouse?page=1&PageSize=3000

O EndPoint citado acima, é onde ocorre a requisição que o app irá utilizar para sincronizar a lista dos armazéns podendo ser validado também em outras aplicações no caso de testes, exemplo: Postman, SoupUi, etc.

O parâmetro "Page" é o número da página carregada pela aplicação. O "PageSize" é a quantidade de registros carregados pela aplicação. Caso na primeira requisição, o app identificar que a quantidade é maior do que 3000(padrão do app Meu Coletor), ele carrega outra requisição, incrementando mais um ao parâmetro "Page".

**(OBS)**: Os armazéns serão carregados somente no processo de sincronização, e serão mantidos no app para uso de suas funcionalidades. Caso seja realizado um novo cadastro de armazém no Protheus após essa sincronização, será necessário sincronizar novamente.

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30833865243543)

***Saiba mais:***

# [Configuração do REST Mobile](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043179314-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configura%C3%A7%C3%A3o-do-REST-Mobile)

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
