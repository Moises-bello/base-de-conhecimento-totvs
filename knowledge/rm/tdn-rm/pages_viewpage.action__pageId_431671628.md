---
content_hash: faef3f82533085221a969a217096a80fd1ad13fb13e0f38f6f67d03a8405c9c1
fetched_at: '2026-06-29T00:09:39.469616+00:00'
page_id: '431671628'
product: rm
source: tdn-rm
title: 3955721 FISCAL01-6936 DT Escrituração - Parametrização do Lote Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=431671628
version: 1
---

# Escrituração de Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Escrituração de Lançamentos |
| **Situação/Requisito:** | Cliente entrou em contato informando que ao realizar a escrituração ocorre um erro, informando:  Erro na Inclusão do Registro: Object reference not set to an instance of an object*.* |
| **Solução/Implementação:** | Foi realizada uma correção na tratativa de mensagem do log, ao executar o processo de *Escrituração do Lote Fiscal*  para um tributo principal que não possuía *Período de Apuração* aberto ou o *Tipo de Livro* diferente do do tributo principal.    **OBS**: Após solucionar o problema do cliente e verificar que o erro ocorria devido a parametrização incorreta(e a mensagem devido a um erro de codificação), foi descoberto um bug referente ao processo de *Estorno da Escrituração do Lote Fiscal.*  Esse problema de estorno ocorria, em um loop que adiciona tributos da *Movimentação do Item* em uma lista de tributos. Neste loop, não era verificado se o tributo do item já havia sido adicionado à lista. |
