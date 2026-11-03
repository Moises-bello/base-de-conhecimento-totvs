---
article_id: 40650353709975
category: SIGAACD - Automação e Coleta de Dados
content_hash: ca64c861c8a1f071ad59760991e32ca73b028abcf38bfd6f7bcab8ea4a7b255e
fetched_at: '2026-06-28T22:39:11.076634+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: "Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - \tACDV060 - Falha\
  \ na leitura de código de barras na rotina de Endereçamento"
type: support-article
updated_at: '2026-05-21T20:47:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40650353709975-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV060-Falha-na-leitura-de-c%C3%B3digo-de-barras-na-rotina-de-Endere%C3%A7amento
---

O sistema apresentava falha na leitura de código de barras na rotina de Endereçamento do aplicativo Meu Coletor de Dados (ACDM010), retornando "Nenhum dado encontrado". A correção foi implementada e está disponível para atualização via pacote conforme a versão do sistema TOTVS Protheus. Após aplicar o pacote, deve-se simular a criação e endereçamento de um produto para validar a solução.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40650392437271) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Está ocorrendo falha na leitura de código de barras na rotina de Endereçamento. Ao tentar realizar o endereçamento de um produto no aplicativo Meu Coletor de Dados (rotina ACDM010), o sistema retorna "Nenhum dado encontrado" ao bipar o código de barras.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
  
Foi alterado o programa para que, na rotina de Endereçamento seja realizada a leitura do código de barras do produto corretamente. Para que a correção seja efetivada, é necessário realizar a atualização do sistema através do pacote disponibilizado.  
  
Faça o download e aplique o pacote de correção correspondente à sua release de sistema:

* 12.1.2310: <https://r.totvs.io/p/1250075>
* 12.1.2410: <https://r.totvs.io/p/1250076>
* 12.1.2510: <https://r.totvs.io/p/1250077>

  ---

1. Após a aplicação do pacote, inicie uma nova simulação criando um produto com controle de endereço (Exemplo: B1\_CODBAR = 7893460392531).
2. Aplique o saldo inicial para o produto.
3. Através da rotina MATA265, deixe o saldo "a endereçar".
4. Acesse o aplicativo "Meu Coletor de Dados" no dispositivo e efetue a sincronização dos dados.
5. Acesse a opção "Endereçamento" (ACDM010) e realize a leitura (bipe) do código de barras.

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
