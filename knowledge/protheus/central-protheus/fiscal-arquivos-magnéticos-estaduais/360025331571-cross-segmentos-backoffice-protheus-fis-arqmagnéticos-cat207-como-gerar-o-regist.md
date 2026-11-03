---
article_id: 360025331571
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 80b8ed0cd81f925b2c5ec72398682db654fd9a782352acb317a4c56846f91ae2
fetched_at: '2026-06-28T22:42:10.281417+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - CAT207 Como
  gerar o Registro 0300
type: support-article
updated_at: '2022-08-17T20:03:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025331571-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-CAT207-Como-gerar-o-Registro-0300
---

**Dúvida**Como gerar o **Registro 0300** (Enquadramento legal da operação/prestação geradora de crédito acumulado do ICMS) da Portaria **CAT207**?  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**A  rotina **CAT207** – de 13/10/2009, contempla dados sobre a movimentação das Notas Fiscais emitidas e o **Registro tipo 0300** é o Enquadramento legal da operação/prestação geradora de crédito acumulado do **ICMS**, esse registro é gerado a partir das informações contidas no complemento de cada nota Fiscal*,* tabela **CFF**.

Importante: Para notas que necessitam do preenchimento da **tabela CFF**, mas já foram faturadas, foi criado a rotina **FISA118** para reprocessamento da tabela.

1. Cadastre as informações na tabela **CFE**, acesse a rotina **Crédito Acumulado de ICMS**(**FISA071**) e efetue o cadastro conforme segue:

**Código Enquadramento Legal**Informe o código do enquadramento legal.  
**Descrição**Selecione o código relativo à hipótese de geração, conforme o inciso do artigo 71 do **RICMS/00**.  
**Anexo do RICMS**Informe o anexo do **RICMS** referente ao enquadramento legal da operação ou prestação geradora do crédito acumulado do **ICMS**, se existir.  
**Artigo do RICMS**Informe o artigo do **RICMS** referente ao enquadramento legal da operação ou prestação geradora do crédito acumulado.  
**Inciso do RICMS**Informe o inciso do **RICMS** referente ao enquadramento legal da operação ou prestação geradora do crédito acumulado do **ICMS**, se existir.  
**Alínea do RICMS**Informe a alínea do **RICMS** referente ao enquadramento legal da operação ou prestação geradora do crédito acumulado do **ICMS**, se existir.  
**Item do RICMS**Informe o item do **RICMS** referente ao enquadramento legal da operação ou prestação geradora do crédito acumulado do **ICMS**, se existir.  
**Letra do RICMS**Informe a letra do **RICMS** referente ao enquadramento legal da operação ou prestação geradora do crédito acumulado do **ICMS**, se existir.

2. Acesse a rotina **Complementos por Documento Fiscal**(**MATA920**), opção “**Crédito Acumulado de ICMS**” e selecione o Enquadramento Legal, esta é a informação complementar referente ao enquadramento legal da operação ou prestação geradora do crédito acumulado do **ICMS**.

Importante: O sistema gera um número sequencial, tamanho 4, no campo **02 COD\_LEGAL** (Código do Enquadramento Legal).  
Exemplo: 0001  
              0002  
              0003

0300|**0001**|30|33|111|11|11|11|1|teste|teste  
5325|**0001**|0,0500|20,0000|1333,33|73,33

O campo **02 COD\_LEGAL** do **Registro** **0300** deve ser igual ao campo **02 COD\_LEGAL** do **Registro 5325**.  
  
Abaixo está a *Query* que o **Protheus** realiza para identificar o motivo do **Registro 0300** não gerar no arquivo.

SELECT     SFT.FT\_FILIAL, SFT.FT\_EMISSAO, SFT.FT\_NFISCAL, SFT.FT\_SERIE, SFT.FT\_CLIEFOR, SFT.FT\_LOJA, SFT.FT\_TIPO, SFT.FT\_BASEICM, SFT.FT\_ALIQICM, SFT.FT\_VALICM, SFT.FT\_NFORI, SFT.FT\_ITEMORI, SFT.FT\_SERORI, SFT.FT\_PRODUTO, SFT.FT\_ESPECIE, SFT.FT\_VALCONT, SFT.FT\_VALIPI, SFT.FT\_ESTADO, SF4.F4\_PERCMED, SF4.F4\_CRDACUM, SF4.F4\_IVAUTIL, SF4.F4\_CROUTSP, SF4.F4\_LFICM, CFF.CFF\_ITEMNF, CFF.CFF\_CODLEG, CFF.CFF\_CODIGO, CFF.CFF\_ANEXO, CFF.CFF\_ART, CFF.CFF\_INC, CFF.CFF\_ALIN, CFF.CFF\_PRG, CFF.CFF\_ITM, CFF.CFF\_LTR, CFF.CFF\_OBS  
  
*FROM* SFT990 AS SFT *INNER JOIN*   
SD2990 AS SD2 ON SD2.D2\_FILIAL = '01' AND SFT.FT\_NFISCAL = SD2.D2\_DOC AND SFT.FT\_SERIE = SD2.D2\_SERIE AND SFT.FT\_CLIEFOR = SD2.D2\_CLIENTE AND  
SFT.FT\_LOJA = SD2.D2\_LOJA AND SFT.FT\_PRODUTO = SD2.D2\_COD AND SFT.FT\_ITEM = SD2.D2\_ITEM AND SD2.D\_E\_L\_E\_T\_ = '' *INNER JOIN*  
SF4990 AS SF4 ON SF4.F4\_FILIAL = '01' AND SF4.F4\_CODIGO = SD2.D2\_TES AND SF4.D\_E\_L\_E\_T\_ = '' *LEFT OUTER JOIN*  
CFF990 AS CFF ON CFF.CFF\_FILIAL = '01' AND CFF.CFF\_NUMDOC = SFT.FT\_NFISCAL AND CFF.CFF\_SERIE = SFT.FT\_SERIE AND CFF.CFF\_ITEMNF = SFT.FT\_ITEM AND  
CFF.CFF\_CLIFOR = SFT.FT\_CLIEFOR AND   
CFF.CFF\_LOJA = SFT.FT\_LOJA AND CFF.D\_E\_L\_E\_T\_ =' '  
  
*WHERE* SFT.FT\_FILIAL = '01'  
AND SFT.FT\_EMISSAO >= '20190314'  
AND SFT.FT\_EMISSAO <= '20190314'  
AND SFT.FT\_NFISCAL = '000049'  
AND SFT.FT\_SERIE = '1'  
AND SFT.FT\_TIPO <> 'S'  
AND SFT.D\_E\_L\_E\_T\_ = ''  
*ORDER BY* SFT.FT\_FILIAL, SFT.FT\_EMISSAO

Importante:   
Para gerar o **Registro 0300** (Enquadramento Legal da Operação/Prestação Geradora de Crédito Acumulado do ICMS) deve ser gerado o **Registro 5325** (Operações Geradoras de Crédito Acumulado)
