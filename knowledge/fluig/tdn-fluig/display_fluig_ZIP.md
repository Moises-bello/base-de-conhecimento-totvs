---
content_hash: a3188366c94c44f81845571ef086f976f7ecc6586ccf8d0c5eab3e40b12a38e0
fetched_at: '2026-06-28T21:35:28.079653+00:00'
page_id: '6066572'
product: fluig
source: tdn-fluig
title: ZIP
type: documentation
url: https://tdn.totvs.com/display/fluig/ZIP
version: 7
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

Em muitas situações, utiliza-se a internet para transmitir e receber informações. Sendo assim, é extremamente importante que ele seja otimizado para não sofrer perda de performance em função da largura de banda da internet.

A melhor maneira de se fazer isto é por intermédio da compactação dos dados, que diminui a quantidade de informações trafegadas. Como a natureza da informação normalmente é texto, podem-se conseguir taxas bastante altas de compressão dos dados.

O componente ZIP é capaz de compactar a informação trafegada por ele utilizando o algoritmo ZIP, podendo também ler informações compactadas com ZIP.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Action | Selecionar a ação a ser realizada com o objeto ZIP:  1. **Create**: cria um arquivo compactado a partir das informações lidas; 2. **Open**: lê as informações compactadas para descompactá-las. |
| Ignore if not Zip Format | Quando selecionado, indica que arquivos que não sejam do formato Zip terão sua leitura ignorada. Este campo só está habilitado caso seja selecionada a opção *Open*. |
