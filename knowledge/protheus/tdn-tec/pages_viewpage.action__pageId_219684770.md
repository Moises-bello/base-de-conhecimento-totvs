---
content_hash: dcb3db30070bebe7af7680d3d4697366a0974dca75c7dd7825b5b0c82f798a0b
fetched_at: '2026-07-02T19:24:18.688105+00:00'
page_id: '219684770'
product: protheus
source: tdn-tec
title: Implementação - Nova chave EnableMemInfoCSV na seção [GENERAL]
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219684770
version: 2
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Relatório de monitoramento de consumo de memória do Appserver |
| Ocorrência | Houve a necessidade de logar em uma forma mais fácil de visualização as informações de alocação de memória, para conseguir visualizar pontos de onde podem ocorrer um crescimento no consumo de memória no Appserver. |
| Implementação | Foi criado a chave EnableMemInfoCSV=1 para logar em um arquivo que pode ser usado em alguma planilha eletrônica a fim de realizar relatórios de visualização de consumo de memória. |
| Informações adicionais | * Referente ao chamado: SSIM-114 * Referente à ocorrência: TEC-6968 * Disponível em builds superiores a 7.00.131227A-20151201 * Mais informações: |
