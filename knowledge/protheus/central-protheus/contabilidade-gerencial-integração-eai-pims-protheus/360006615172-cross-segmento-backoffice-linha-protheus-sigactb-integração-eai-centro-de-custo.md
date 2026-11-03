---
article_id: 360006615172
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: 5f82746225fcb8ac4b15fc82bd1475915e487077446d7a0074652f80c62344be
fetched_at: '2026-06-28T22:40:54.187976+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - INTEGRAÇÃO EAI - CENTRO
  DE CUSTO
type: support-article
updated_at: '2023-01-25T13:04:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006615172-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-INTEGRA%C3%87%C3%83O-EAI-CENTRO-DE-CUSTO
---

**Ocorrência**

Ao realizar o procedimento de integração para o Protheus, retorna mensagem de pesquisa não encontrada, exibindo código de centro de custo que não existe, com numeração sequencial de 999 (noves), sendo ocasionado devido a  configuração  no de/para.  
A configuração no  de/para referente a centro de custo,  do valor externo exibe os códigos de centro de custo correto, já o valor interno contem numeração sequencial que não corresponde ao cadastro de centro de custo do Protheus.

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

* Em ambiente teste
* Limpe a XXF somente dos registros da tabela correspondente a CTT da filial, conforme tela que segue

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049524254/mceclip0.png)

* Aplicar procedimento de carga inicial para carregar o de/para corretamente.

  [Selecionando o adapter para a sincronização inicial](http://tdn.totvs.com/display/framework/O+Sincronizador+de+Carga+Inicial+do+EAI+Protheus)
* Após carga inicial verificar se o de/para é carregado corretamente, e se correto, iniciar integração novamente.
* Observação: Esta solução pode ser aplicada também a conta contábil e outras linhas de produto (Logix;RM)
