---
content_hash: 4b7658a1a5098c98485713195c2a6414678d4874f16c0d641a8068adb06a7767
fetched_at: '2026-06-29T00:09:24.021851+00:00'
page_id: '422548123'
product: rm
source: tdn-rm
title: 3840614 FISCAL01-6624 DT Lote Fiscal - Liberar Lote de Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422548123
version: 1
---

# Escrituração de Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Escrituração de Lançamentos |
| **Situação/Requisito:** | Ao tentar liberar o lote de lançamentos fiscais ocorre a mensagem abaixo:  Lote 227 - Filial 1- Tipo Entrada com o Valor das Notas diferente do total do lote. |
| **Solução/Implementação:** | O processo de *Liberar Lote*, estava apresentando o erro de *Tipo Entrada* com o *Valor das Notas* diferente do total do *Lote*. Isto estava acontecendo pois o campo Saldo Contábil estava apresentando um valor com 4 casas decimais e realizando o arredondamento, assim o valor da capa era diferente do valor real no banco de dados.    Este problema ocorria na *Escrituração do Lote Fiscal* no Nucleus, onde o cálculo de ICMS Indexado resultava num valor de dízima periódica. Para corrigir, o valor do Saldo Contábil foi arredondado antes de salvar na base de dados.  **Obs**: Para Liberar Lotes que já foram lançados anteriormente a esta correção, é necessário seguir os passos a seguir:   1. No Nucleus em Integrações > Escrituração de Lançamentos  realizar o processo Estorno da Escrituração do Lote que apresenta erro no Saldo Contábil. 2. Após realizar o processo de estorno de todos os lançamentos fiscais do lote, deverá ser executado o serviço para recalcular o Saldo Contábil. Vá BackOffice do Gestão Fiscal, em Obrigações Principais > Mais > Geração de Saldo de Lotes Fiscais e preencha as informações referente ao Lote estornado anteriormente. 3. No Nucleus em Integrações > Escrituração de Lançamentos  realizar o processo de Escrituração do Lote Fiscal, para o lote em questão. 4. De volta ao Gestão Fiscal,  em Lotes Fiscal Entrada,m preencher Quantidade de Notas e Total Contábil e realizar o processo de Liberar Lote. |
| **Requisito:** | FIS000236 |
