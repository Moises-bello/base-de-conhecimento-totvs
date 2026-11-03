---
article_id: 360024618274
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: fb5a1a301cfb83c2d853acfe564050f3e210e5612f32ccb262c39a5e4b53fc76
fetched_at: '2026-06-28T22:38:45.179362+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Help MV_DATAFIS na Exclusão da Nota Fiscal de Saída
type: support-article
updated_at: '2021-04-28T15:13:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024618274-MP-FAT-Help-MV-DATAFIS-na-Exclus%C3%A3o-da-Nota-Fiscal-de-Sa%C3%ADda
---

**Ocorrência**

Help MV\_DATAFIS na Exclusão da Nota Fiscal de Saída.  
  
**Ambiente**

Microsiga Protheus -  a partir da versão 12.  
  
**Causa**

Ao excluir uma NF de saída o sistema emite o Help **MV\_DATAFIS** .  
  
**Solução**

O sistema valida se a data base é menor ou igual ao parâmetro **MV\_DATAFIS** e, também, valida se o cliente não utiliza o ponto de entrada **FistMov,** caso a data base seja inferior ocorre a mensagem do parâmetro **MV\_DATAFIS** de bloqueio.  
  
Para solucionar é necessário :

1) Verificar a Database em relação a data informada no parâmetro;

2) Verificar se o SX6 está exclusivo ou compartilhado (se estiver exclusivo será necessário gravar o campo de filial);

3) Realizar um teste sem o uso de pontos de entrada (utilizar a Chave IXBLOG=NORUN) - Lembrando que o ixblog =norun não valida pontos de entradas existentes na validação do dicionário de dados (SX3);   
  
4) Avaliar se algum dos campos de data do cabeçalho da NF **(F2\_DTSERV, F2\_EMISSAO, F2\_DTLANC, F2\_DTBASE1, F2\_DTENTR, F2\_ENINFE, F2\_DTDIGIT, F2\_DAUTNFE, F2\_TXREF)** estão fora do período determinado no parâmetro.
