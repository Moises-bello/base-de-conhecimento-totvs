---
article_id: 360022216532
category: Escrita Fiscal - Impostos - ICMS - Regime de Processamento
content_hash: 45bf1549cdeb05d532b43ecb766374e1939fa5d35270d61c4628f3b2de1b3691
fetched_at: '2026-06-28T22:39:22.864462+00:00'
product: protheus
section_id: 1500001549862
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Relatórios Fiscais
  - Demonstração das UF'S para CTe ao gerar relatórios Listagem p/ Transcrição (MATR920)
  e Regime de Processamento de Dados (MATR930)
type: support-article
updated_at: '2021-07-28T13:47:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022216532-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Relat%C3%B3rios-Fiscais-Demonstra%C3%A7%C3%A3o-das-UF-S-para-CTe-ao-gerar-relat%C3%B3rios-Listagem-p-Transcri%C3%A7%C3%A3o-MATR920-e-Regime-de-Processamento-de-Dados-MATR930
---

**Dúvida**Ao lançar um documento de entrada do tipo Cte informando as UF's nos campos F1\_UFORITR e F1\_UFDESTR, qual será a UF demonstrada na geração dos Livros Fiscais?  
   
 **Ambiente**P12.1.17

**Solução**

Ao lançar o documento de entrada o sistema irá gravar os campos F3\_ESTADO e FT\_ESTADO com a primeira UF que caracteriza a operação como interestadual, conforme citado no exemplo abaixo:

1º Exemplo:

MV\_ESTADO = SP

UF Origem Transporte (F1\_UFORITR) = MG

UF Destino Transporte (F1\_UFDESTR) = PR

O sistema irá gravar os campos F3\_ESTADO e FT\_ESTADO = MG

 2ºExemplo:

MV\_ESTADO = SP

UF Origem Transporte (F1\_UFORITR) = SP

UF Destino Transporte (F1\_UFDESTR) = PR

O sistema irá gravar os campos F3\_ESTADO e FT\_ESTADO = PR

Esse será o critério utilizado ao gerar os relatórios MATR920 e MATR930.

Somente para o Regime de Processamento de Dados (MATR930) existe o parâmetro MV\_NFCTEUF para definir qual UF será apresentada no relatório, onde:

MV\_NFCTEUF = 0 irá considerar o conteúdo do campo F3\_ESTADO

MV\_NFCTEUF = 1 irá considerar o conteúdo do campo F3\_CLIEFOR
