---
article_id: 14439350190871
category: SIGAACD - Automação e Coleta de Dados
content_hash: 3526f2084841b938cdbac66f84c20290664af81e024adb043297e5b2b53cad30
fetched_at: '2026-06-28T22:39:11.191432+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA100 - Como gerar
  Ordem de Separação para produtos com saldo negativo?
type: support-article
updated_at: '2023-05-08T13:57:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14439350190871-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA100-Como-gerar-Ordem-de-Separa%C3%A7%C3%A3o-para-produtos-com-saldo-negativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:17 min** **Dúvida**É possível gerar uma Ordem de Separação sem que a rotina valide que o Saldo do produto está negativo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**No produto SIGAACD padrão, por meio da rotina Geração de Ordens de Separação - ACDA100 - realmente faz a validação do saldo disponível de Estoque para permitir ou não gerar a Ordem de Separação. Pelo fato de, por se tratar de um contexto real, a separação física de produtos necessita da existência dos saldos fisicamente nos armazéns. Porém, para clientes que trabalham com estoque negativo e possuem a necessidade de Separar produtos com saldo negativo, temos os seguintes pontos de entrada que podem eventualmente serem utilizados para fins de customizações internas de forma a atender a necessidade da empresa:

***ACD100ALT - Validação após gravação da alteração da Órdem de Separação***  
***<https://tdn.totvs.com/pages/releaseview.action?pageId=6091070>***

***ACD100FI - Filtra Itens em Pedidos de Venda***  
***<https://tdn.totvs.com/display/public/mp/ACD100FI+-+Filtra+Itens+em+Pedidos+de+Venda+--+30561>***  
  
***ACD100VG - Valida Geração Ordens de Separação***  
***<https://tdn.totvs.com/pages/releaseview.action?pageId=6090963>***  
  
***ACDA100I - Filtra Itens na geração de Ordens de Separação***  
***<https://tdn.totvs.com/pages/releaseview.action?pageId=6091043>***

**Observação:** é importante enfatizar que o uso e criação de regras customizáveis nos Pontos de Entrada é de inteira responsabilidade do desenvolvedor da empresa e/ou consultor alocado para essa função. O Suporte Padrão não avalia customizações em pontos de entrada, apenas a chamada dos mesmos de acordo com as documentações de exemplos de chamada.

**Saiba mais;**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](Clique%20aqui%20e%20veja%20mais%20artigos%20sobre%20Automa%C3%A7%C3%A3o%20e%20Coleta%20de%20Dados)
