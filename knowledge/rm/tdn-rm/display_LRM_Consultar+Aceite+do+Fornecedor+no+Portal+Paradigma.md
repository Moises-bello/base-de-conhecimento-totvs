---
content_hash: f58e1c2bcacb678fa04ab1b1ab13a0c520990334748ccb317cb32b4399b3b7e9
fetched_at: '2026-06-29T00:09:26.672362+00:00'
page_id: '423938356'
product: rm
source: tdn-rm
title: Consultar Aceite do Fornecedor no Portal Paradigma
type: documentation
url: https://tdn.totvs.com/display/LRM/Consultar+Aceite+do+Fornecedor+no+Portal+Paradigma
version: 13
---

O processo a seguir, permite que o usuário consulte o aceite de fornecedor referente aos pedidos de compra originados no TOTVS Gestão de Estoque, Compras e Faturamento para o Portal de Compras Paradigma (WBC - Web Business Center).  
O processo de Consultar Aceite de Fornecedor no Portal de Compras Paradigma está disponível na visão de Ordem de Compra na nova MDI(RM.exe) através do caminho Compras | Ordem de Compra | Processos.   
Para acessar este processo é necessário conceder a permissão através do perfil do usuário.  
No processo de Consultar Aceite do Fornecedor no Portal Paradigma o usuário poderá obter a lista de Pedidos de Compra aceitos ou recusados pelo fornecedor no Portal.   
As premissas para execução do processo de integração de Consultar Aceite do Fornecedor no Portal Paradigma são:

* Parâmetro global de integração com **Paradigma ativo**: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Assistente de Implantação de Processos | Movimento | Integrações | Etapa 122 - Definições Gerais - Paradigma/Cicbusiness, marcando o campo "Integrado com Paradigma".
* **Caminho do WebService** Paradigma corretamente parametrizado no caminho Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Assistente de Implantação de Processos | Movimento | Integrações | Etapa 122 - Definições Gerais - Paradigma/Cicbusiness.
* T**ipo de movimento parametrizado** como Pedido de Compra em Ambiente | Configuração | Parâmetros | Assistente de Implantação de Processos | Processos 04.06 - Tipo de Movimento (1.1.XX) | Etapa Compra/Venda - Outros Dados campo Tipo do Movimento de Compra igual a Pedido de Compras.
* Tipo de movimento **parametrizado para Integrado com Portal de Compras Paradigma** em Ambiente | Configuração | Parâmetros | Assistente de Implantação de Processos | Processo: 04.06 - Tipo de Movimento: 1.1.XX | Etapa Integração Paradigma campo Integrado com Portal de Compras Paradigma marcado.
* Ordens de Compra com Status Paradigma igual Aguardando Aceite de Fornecedor: Compras | Ordem de Compra.
