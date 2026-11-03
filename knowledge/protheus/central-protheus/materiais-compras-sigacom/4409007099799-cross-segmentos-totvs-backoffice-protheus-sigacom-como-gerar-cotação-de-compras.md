---
article_id: 4409007099799
category: Materiais - Compras (SIGACOM)
content_hash: 869af3e1641127315c8eb21a956423405cd222fa5a360b443327debb5c65e598
fetched_at: '2026-06-28T22:41:15.882985+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como gerar Cotação
  de Compras?
type: support-article
updated_at: '2021-09-22T10:17:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409007099799-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-gerar-Cota%C3%A7%C3%A3o-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como gerar Cotação no módulo de Compras ?  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**Para a geração de uma Cotação de Compras, é necessário, primeiramente, possuir ao menos uma Solicitação de Compras cadastrada no sistema.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409013290391/mceclip0.png)

Para o(s) Produto(s) existente(s) nessa Solicitação de Compras é necessário possuir ao menos um deles com o vínculo realizado com um Fornecedor através do Cadastro de "Produto x Fornecedor" (***MATA061***) ou "Grupo x Fornecedor" (***MATA065***):

Cadastro Produto x Fornecedor:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409013371031/mceclip1.png)

Posteriormente, utiliza-se da rotina ***Gera Cotação (MATA131)*** para realizar a geração da cotação. Ao entrar na rotina, selecionar os parâmetros conforme a necessidade:

***Obs:*** no Parâmetro ***"Utiliza Amarração ?"***, é onde é define se será utilizada a amarração de "Produto x Fornecedor", "Grupo x Fornecedor" ou "Ambas" que existe cadastradas cadastradas.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409013392407/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409013395479/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409013396631/mceclip4.png)

Ao confirmar os parâmetros, serão listadas as Solicitações de Compras conforme parâmetros escolhidos:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409013421975/mceclip5.png)

Ao selecionar as SCs desejadas, e clicar em ***"Gerar Cotação",*** caso esteja habilitado o parâmetro "MV\_SELFOR", pode ser selecionado o "Número máximo de Fornecedores" participantes e "Quantos últimos Fornecedores" a serem listados para geração da Cotação:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409013429527/mceclip6.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409013434519/mceclip7.png)

Onde ao confirmar, é aberta a tela para visualização das informações a serem geradas na cotação e também até inclusão de novos fornecedores participantes para a cotação:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409006968983/mceclip8.png)

Ao confirmar, é gerada a cotação para a seleção das Solicitações de Compras e Fornecedores realizados:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409006977943/mceclip9.png)

E a cotação já pode ser visualizada na rotina "Atualiza Cotações" para informação dos preços e continuação do processo de Cotação para posterior Analise da Cotação:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409007002263/mceclip10.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
