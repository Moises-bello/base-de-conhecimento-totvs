---
article_id: 360025886634
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b54c54093106a05e7aaa2fb9baabd81f0f9c42d71c56f46f58580345626bb79e
fetched_at: '2026-06-28T22:38:31.109173+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT- Erro de sintaxe perto da palavra chave 'From' na tabela SF2
type: support-article
updated_at: '2021-04-28T15:54:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025886634-MP-FAT-Erro-de-sintaxe-perto-da-palavra-chave-From-na-tabela-SF2
---

**Ocorrência**

Ao tentar efetuar um retorno de nota de saída (**MATA461**) via documento de entrada (**MATA103**), é gerado  um erro de sintaxe perto da palavra chave 'From' na tabela SF2.

**Ambiente**

Microsiga Protheus -  a partir release 12.1.17.  
  
**Causa**

**Erro: Incorrect syntax near the keyword 'FROM'.  
( From tMSSQLConnection::GetQueryFile )**SELECT FROM **F2\_SELECT** F2\_DOC , F2\_SERIE , F2\_CLIENTE , F2\_LOJA , F2\_COND , F2\_DUPL , F2\_EMISSAO , F2\_EST , F2\_FRETE , F2\_SEGURO , F2\_ICMFRET , F2\_TIPOCLI , F2\_VALBRUT , F2\_VALICM , F2\_BASEICM , F2\_VALIPI , F2\_BASEIPI , F2\_VALMERC , F2\_NFORI , F2\_DESCONT , F2\_SERIORI , F2\_TIPO , F2\_ESPECI1 , F2\_ESPECI2 , F2\_ESPECI3 , F2\_ESPECI4 , F2\_VOLUME1 , F2\_VOLUME2 , F2\_VOLUME3 , F2\_VOLUME4 , F2\_ICMSRET , F2\_PLIQUI , F2\_PBRUTO , F2\_TRANSP , F2\_REDESP , F2\_VEND1 , F2\_VEND2 , F2\_VEND3 , F2\_VEND4 , F2\_VEND5 , F2\_OK , F2\_FIMP , F2\_DTLANC , F2\_DTREAJ , F2\_REAJUST , F2\_DTBASE0 , F2\_FATORB0 , F2\_DTBASE1 , F2\_FATORB1 , F2\_VARIAC , F2\_FILIAL , F2\_BASEISS , F2\_VALISS , F2\_VALFAT , F2\_CONTSOC , F2\_BRICMS , F2\_FRETAUT , F2\_ICMAUTO , F2\_DESPESA , F2\_NEXTDOC , F2\_NEXTSER , F2\_ESPECIE , F2\_PDV , F2\_MAPA , F2\_ECF , F2\_PREFIXO , F2\_BASIMP1 , F2\_BASIMP2 , F2\_BASIMP3 , F2\_BASIMP4 , F2\_BASIMP5 , F2\_BASIMP6 , F2\_VALIMP1 , F2\_VALIMP2 , F2\_VALIMP3 , F2\_VALIMP4 , F2\_VALIMP5 , F2\_VALIMP6 , F2\_ORDPAGO , F2\_NFCUPOM , F2\_VALINSS , F2\_HORA , F2\_MOEDA , F2\_REGIAO , F2\_VALCSLL , F2\_VALCOFI , F2\_VALPIS , F2\_LOTE , F2\_TXMOEDA , F2\_CLEOK , F2\_CHVCLE , F2\_IDCLE , F2\_VALIRRF , F2\_RECFAUT , F2\_CARGA , F2\_SEQCAR , F2\_BASEINS , F2\_PEDPEND , F2\_DESCCAB , F2\_DTENTR , F2\_FORMUL , F2\_TIPODOC , F2\_NFEACRS , F2\_TIPOREM , F2\_SEQENT , F2\_ICMSDIF , F2\_VALACRS , F2\_RECISS , F2\_VALCF3 , F2\_ORDSEP , F2\_HORNFE , F2\_CHVNFE , F2\_FLAGDEV , F2\_TPFRETE , F2\_NFELETR , F2\_BASECF3 , F2\_VEICUL2 , F2\_HAW on **A103QRYNF(MATA103R.PRX)** 19/03/2019 08:50:10 line : 278

Nesta ocorrência, o ambiente possui um campo de usuário na tabela **SF2** chamado **F2\_SELECT**, que interfere na gravação do Banco de Dados. Devido a uma deficiência de interpretação da função **ChangeQuery ( LIB)**, ela não consegue montar a query corretamente, se o campo na Base de Dados contiver como parte de sua nomenclatura  nome de comandos de  Banco de Dados como **Select** ou **From**, por exemplo.    
  
**Solução**  
Para solucionar essa ocorrência, o campo deve ser excluído da Base de Dados e gerado um novo campo com um nome diferente, onde não contenha nenhum tipo de comando de Banco de Dados.
