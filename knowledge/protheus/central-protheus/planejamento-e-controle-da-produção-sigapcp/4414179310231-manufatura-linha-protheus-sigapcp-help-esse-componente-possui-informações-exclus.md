---
article_id: 4414179310231
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: caf087f70c7ef37e1c36119cb87ba7c9ae153b6dd862562e0d2ba68b181e4e66
fetched_at: '2026-06-28T22:42:43.360426+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Help: Esse componente possui informações
  exclusivas do novo programa de cadastro de estrutura. A alteração será permitida
  apenas no PCPA200'
type: support-article
updated_at: '2022-09-27T18:47:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414179310231-Manufatura-Linha-Protheus-SIGAPCP-Help-Esse-componente-possui-informa%C3%A7%C3%B5es-exclusivas-do-novo-programa-de-cadastro-de-estrutura-A-altera%C3%A7%C3%A3o-ser%C3%A1-permitida-apenas-no-PCPA200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:50 min****Ocorrência**Ao tentar realizar a alteração de um componente no **MATA200 - Estrutura** é apresentada o *help*: **Esse componente possui informações exclusivas do novo programa de cadastro de estrutura. A alteração será permitida apenas no PCPA200**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Mensagem ocorre quando o campo **G1\_LISTA - Lista** ou **G1\_FANTASM - Fantasma** foram preenchidos no **PCPA200 - Estrutura (Nova Versão)**.  
  
**Solução**Por ter sido preenchido o campo **G1\_LISTA** ou **G1\_FANTASM** a alteração do componente deverá ser realizada apenas através do **PCPA200**. **Importante**Caso seja utilizado algum ponto de entrada no **MATA200** é necessário verificar o respectivo ponto de entrada no **PCPA200**.  
A rotina **MATA200** tem previsão de ser descontinuada no dia **31/08/22**.
