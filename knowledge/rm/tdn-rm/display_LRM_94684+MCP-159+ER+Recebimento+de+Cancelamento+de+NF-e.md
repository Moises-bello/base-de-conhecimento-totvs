---
content_hash: 917ef1b2eaac8c2c1ec70cc624c41c3a0f8ff436348f3904d2a087f1b6a8b5cc
fetched_at: '2026-06-29T00:08:28.775041+00:00'
page_id: '271850575'
product: rm
source: tdn-rm
title: 94684 MCP-159 ER Recebimento de Cancelamento de NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/94684+MCP-159+ER+Recebimento+de+Cancelamento+de+NF-e
version: 105
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Recebimento de NF-e |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado/Ticket** | 94684 | | |
| **País** | Brasil | | |

  

## Objetivo

 Possibilitar o recebimento dos registros de NF-e canceladas e as respectivas atualizações nos dados dos movimentos.

## Definição da Regra de Negócio

 

A legislação prevê que uma NF-e poderá ser cancelada somente se o uso tenha sido previamente autorizado pelo Fisco (protocolo “Autorização de Uso”) e desde que não tenha ainda ocorrido o fato gerador, ou seja, a saída da mercadoria do estabelecimento ainda não tenha ocorrido. Atualmente o prazo máximo para cancelamento de uma NF-e é de 24 horas, contadas a partir da autorização de uso.

Para garantir que os fornecedores não executem o cancelamento indevidamente, o NeoGrid NF-e executa uma nova verificação automaticamente 2 dias após a data de autorização de uso. Esta nova validação é executada apenas para NF-es que resultaram em “Uso Autorizado” na verificação ao receber o XML do fornecedor.

Ao executar a verificação em 2 dias, as NF-es que estiverem autorizadas e que constarem como canceladas na SEFAZ serão disponibilizadas para o RM no layout procNFe com status 367 e descrição evidenciando o cancelamento.

O TOTVS Gestão de Estoque, Compras e Faturamento irá, através da chave de acesso, buscar essa NF na tabela TNFEENTRADA.

 Irá verificar na TNFEENTRADA se existe movimento vinculado à NFe e em caso positivo irá cancelá-lo (verificar todas as consistências de um processo de cancelamento de movimento tais como contábil, fiscal, financeiro, etc.).

Tendo encontrado o movimento ou não o sistema deverá também atualizar o status do registro da TNFEENTRADA para cancelado.

Caso o XML não seja encontrado na TNFEENTRADA, mesmo assim o sistema deverá procurar na base de dados se existe movimento com mesmo nº, série e fornecedor e cancelá-lo caso exista.

Assim,  partir do recebimento de um XML com o status 367 o TOTVS Gestão de Estoque, Compras e Faturamento irá verificar se já existe movimento vinculado ao mesmo.

Na tabela dos XML existentes (TNFEENTRADA), o sistema irá localizar através da chave de acesso, qual o XML a ser cancelado e atualizará o status do mesmo para a situação Cancelada.

Em seguida irá verificar neste cadastro se existe movimento vinculado ao XML e em caso positivo irá cancelá-lo (deverão ser feitas todas as consistências de um processo de cancelamento de movimento).

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
