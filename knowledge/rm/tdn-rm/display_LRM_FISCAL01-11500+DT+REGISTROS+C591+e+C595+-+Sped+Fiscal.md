---
content_hash: b45116ee82fe4109bf9b9516a833a657e66bc7d27fea9722e1cda03ee7e163bd
fetched_at: '2026-06-29T00:10:32.032536+00:00'
page_id: '525017680'
product: rm
source: tdn-rm
title: FISCAL01-11500 DT REGISTROS C591 e C595 - Sped Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11500+DT+REGISTROS+C591+e+C595+-+Sped+Fiscal
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Sped Fiscal |
| Ticket: | FISCAL01-11500 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11500 |

## **02. SITUAÇÃO/REQUISITO**

Implementar os Registros:

#### **REGISTRO C591 - INFORMAÇÕES DO FUNDO DE COMBATE À POBREZA – FCP NA NF3e (CÓDIGO 66)**

Este registro tem por objetivo prestar informações do Fundo de Combate à Pobreza (FCP), constante na NF3e (Modelo 66).

Filho do Registro C590.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C591” |  |
| 02 | VL\_FCP\_OP | Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação própria, na combinação de CST\_ICMS, CFOP e alíquota do ICMS | Gerado com o valor do FECP do ICMS  Próprio do Lançamento Fiscal |
| 03 | VL\_FCP\_ST | Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação de substituição tributária, na combinação de CST\_ICMS, CFOP e alíquota do ICMS. | Gerado com o valor do FECP do ICMS  ST do Lançamento Fiscal |

#### **REGISTRO C595 - OBSERVAÇÕES DO LANÇAMENTO FISCAL (CÓDIGOS 06, 28, 29 e 66)**

Este registro também foi incluído a partir deste layout e  deverá ser utilizado em caso de ajuste de legislações estaduais para os documentos sobre os modelos (Códigos 06, 28, 29 E 66) .

Filho do Registro C590

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C595” |  |
| 02 | COD\_OBS | Código da observação do lançamento fiscal (campo 02 do Registro 0460) | Referência o registro 0460. Deve conter o valor do campo 2 do registro 0460 para fazer relacionamento com o mesmo. |
| 03 | TXT\_COMPL | Descrição complementar do código de observação. | Referência o registro 0460. Deve conter o valor do campo 3 do registro 0460 para fazer relacionamento com o mesmo. |

Estes registros equivalem aos registros C191 e C195, respectivamente.

Implementar a partir da versão 12.1.24.

Os ajustes da automação do SPED serão realizados ao final de toda a implementação.

Documentação complementa das alterações em: [https://docs.google.com/document/d/1kyP4gwChIGLBO56DIj879AMz1J9a1PBH1wKbOIm2Jrc/edit?pli=1#](https://docs.google.com/document/d/1kyP4gwChIGLBO56DIj879AMz1J9a1PBH1wKbOIm2Jrc/edit?pli=1)

## **03. SOLUÇÃO**

Implementação dos registros C591 e C595

Geração apenas a partir de 2020

C591:  
Este registro tem por objetivo prestar informações do Fundo de   
Combate à Pobreza (FCP), constante na NF3e (Modelo 66).

Gerado com o valor do FECP do ICMS Próprio do Lançamento Fiscal e   
valor do FECP do ICMS ST do Lançamento Fiscal

Campo 02 (VL\_FCP\_OP) – Preenchimento: informar o valor total do Fundo de Combate à Pobreza (FCP) vinculado à  
operação própria, relativo aos itens com mesma combinação de CST\_ICMS, CFOP e alíquota do ICMS informada no registro  
pai, C590.  
Validação: Somente pode ser preenchido quando o campo CST\_ICMS do registro C590 assumir o valor x00 ou x20.  
Campo 03 (VL\_FCP\_ST) – Preenchimento: informar o valor do Fundo de Combate à Pobreza (FCP) vinculado à operação  
de substituição tributária, relativo aos itens com mesma combinação de CST\_ICMS, CFOP e alíquota do ICMS informada no  
registro pai, C590.  
Validação: Somente pode ser preenchido quando o campo CST\_ICMS do registro C590 assumir o valor x10.

C595:  
Este registro também foi incluído a partir deste layout e  deverá ser utilizado em caso de ajuste de   
legislações estaduais para os documentos sobre os modelos (Códigos 06, 28, 29 E 66) .

Campo 02 (COD\_OBS) – Preenchimento: as observações de lançamento devem ser informadas neste campo, exceto  
quando a legislação estadual prever o preenchimento do campo COD\_OBS do registro C590.  
Validação: o código informado deve constar do registro 0460.  
Campo 03 (TXT\_COMPL) - Preenchimento: utilizado para complementar observação cujo código seja de informação  
genérica.
