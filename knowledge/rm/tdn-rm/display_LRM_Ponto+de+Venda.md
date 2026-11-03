---
content_hash: cf9f6d218f120c2b0b1bf752a1d1a7d223ce23005d1a67154cef63ff836eb0f0
fetched_at: '2026-06-29T00:09:29.107516+00:00'
page_id: '423938811'
product: rm
source: tdn-rm
title: Ponto de Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/Ponto+de+Venda
version: 7
---

O Cadastro de Pontos de Venda é utilizado na importação/exportação de dados para integração com parceiros TOTVS. Onde um ponto de Venda representa um local físico onde são emitidos os cupons fiscais como por exemplo: caixa de supermercado, bomba de gasolina, etc.   
Neste modelo os pontos de venda são agrupados por Local / Filial onde cada grupo tem informações especificas para a integração com parceiros TOTVS.  
Também é possível definir a Prioridade na ordem de processamento dos movimentos em modo Server como baixa, média e alta.  
O cadastro de Ponto de Venda poderá ser acessado em: **Cadastros | Mais... | Tabelas Auxiliares | Pontos de Venda**.

A partir da versão 12.1.2402, fizemos uma pequena evolução neste cadastro para que ao informar dados nos campos **Diretório de Entrada** e **Diretório de Saída**, caso não exista o diretório ele será criado no caminho informado.

## **Multi Tenant**

Para ambientes Multi Tenant o diretório deverá ser informado manualmente (não será possível selecionar). Isso se faz necessário, pois o diretório escolhido será uma subpasta do **FileServerpath****,**(para mais informações acesse: [Configuracao das Tags FileServerPath e LogPath](https://tdn.totvs.com/display/LRM/Configuracao+das+Tags+FileServerPath+e+LogPath)).  Dessa forma, não deverá ser informado um caminho com uma raiz (exemplo: C:\pasta), será definida apenas a subpasta para ser utilizada no **FileServerpath.** Conforme exemplo abaixo:

Atenção

O diretório deverá estar compartilhado em rede com todos os usuários, permitindo leitura e gravação.

Esta configuração para ambiente Multi Tenant está disponível a partir da versão 12.1.2402

**Tabelas Utilizadas**

| Tabela | Referência |
| --- | --- |
| TGRPPONTOVENDA | Cadastro de Grupos de Ponto de Venda |
| TPONTOVENDA | Cadastro de Pontos de Venda |
