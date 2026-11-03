---
content_hash: ff8f5bb413c862d3a54558a4d129a2abaef17f5f067c3058aa7f98ac8aae49cf
fetched_at: '2026-06-29T00:09:23.160778+00:00'
page_id: '422546057'
product: rm
source: tdn-rm
title: Origem dos Dados (Bloco P)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546057
version: 3
---

**Registro  P001 - Abertura do bloco P**

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **DESCRIÇÃO DO CAMPO** | **ORIGEM DOS DADOS** |
| REG | Texto fixo contendo P001 | Gerado automaticamente pelo processo da rotina |
| IND\_MOV | Indicador de movimento:   0 - Bloco com dados   1 - Bloco sem dados | Gerado automaticamente pelo processo da rotina |

**Registro P010 - Identificação do Estabelecimento**

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **DESCRIÇÃO DO CAMPO** | **ORIGEM DOS DADOS** |
| REG | Texto fixo contendo P010 | Gerado automaticamente pelo processo da rotina |
| CNPJ | Número de inscrição do   estabelecimento no CNPJ | CNPJ da filial que está apurando a Contribuição |

**Registro P100 - Contribuição Previdenciária sobre a Receita Bruta**

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **DESCRIÇÃO DO CAMPO** | **ORIGEM DOS DADOS** |
| REG | Texto fixo contendo P100 | Gerado automaticamente pelo processo da rotina |
| DT\_INI | Data inicial da apuração | Parâmetro da tela de geração da rotina |
| DT\_FIM | Data final da apuração | Parâmetro da tela de geração da rotina |
| VL\_REC\_TOT\_EST | Valor da receita Bruta Total do estabelecimento no período | Recebe o valor do campo 03-VL\_REC\_TOT do registro 0145. Esta informação é carregada do Período de Apuração. |
| COD\_ATIV\_ECON | Código de indicador correspondente a atividade sujeita a incidência da contribuição previdenciária sobre a receita bruta, conforme tabela 5.1.1 da EFD | Gerado com a conversão do NCM do cadastro de Produto para a tabela 5.1.1 constante no guia da EFD. |
| VL\_REC\_ATIV\_ESTAB | Valor da receita bruta do estabelecimento correspondente as atividades referidas  no campo COD\_ATIV\_ECON | Gerado com o valor da mercadoria dos itens dos lançamentos que possuem o tributo Contr. Previdenciária |
| VL\_EXC | Valor das exclusões da receita bruta informada no campo VL\_REC\_ATIV\_ESTAB | Este campo não será gerado |
| VL\_BC\_CONT | Valor da base de cálculo da contribuição previdenciária sobre a receita bruta | Gerado com o somatório das bases de cálculo de todos os itens de lançamentos que possuam o tributo Cont. Previdenciária |
| ALIQ\_CONT | Alíquota da contribuição previdenciária sobre a receita bruta | Gerado com a alíquota do tributo Cont. Previdenciária dos itens dos lançamentos que o possuem esta tributação. |
| VL\_CONT\_APU | Valor da contribuição previdenciária apurada sobre a receita bruta | Somatório do tributo Cont. Previdenciária dos itens dos lançamentos que possuem esta tributação. |
| COD\_CTA | Código da conta analítica contábil referente a contribuição previdenciária sobre a receita bruta | Este valor não será gerado. |
| INFO\_COMPL | Informação complementar do registro | Este valor não será gerado. |

**Registro P110 - Complemento da Escrituração - Detalhamento da Apuração da Contribuição**  
 **Este registro não será gerado**

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **DESCRIÇÃO** | **ORIGEM DOS DADOS** |
| REG | Texto Fixo contendo P110 | Não será gerado |
| NUM\_CAMPO | Informa o número do campo do registro P100 objetivo de detalhamento neste registro | Não será gerado |
| COD\_DET | Código do tipo de detalhamento conforme tabela 5.1.2 da EFD | Não será gerado |
| DET\_VALOR | Valor detalhamento referente ao campo 02 deste registro | Não será gerado |
| INF\_COMPL | Informação complementar do detalhamento | Não será gerado |

**Registro P199 - Processo Referenciado**   
 **Este registro não será gerado**

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **DESCRIÇÃO** | **ORIGEM DOS DADOS** |
| REG | Texto fixo contendo P199 | Não será gerado |
| NUM\_PROC | Identificação do processo ou ato concessório | Não será gerado |
| IND\_PROC | Indicador da origem do processo:   1 - Justiça federal   2 - Secretaria da receita federal do Brasil   3 - Outros | Não será gerado |

**Registro P200 - Consolidação da Contribuição Previdenciária sobre a Receita Bruta**

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **DESCRIÇÃO** | **ORIGEM DOS DADOS** |
| REG | Texto fixo contendo P200 | Gerado tela rotina |
| PER\_REF | Período de referência da escrituração | Gerado com base no período de geração da rotina |
| VL\_TOT\_CONT\_APU | Valor total apurado da contribuição previdenciária sobre a receita   bruta | somatório do campo VL\_CONT\_APU    do registro P100 |
| VL\_TOT\_AJ\_REDUC | Valor total de ajuste de redução | Registro P210, VL\_AJ quando campo   IND\_AJ for igual a 0 |
| VL\_TOT\_AJ\_ACRES | Valor total de ajustes de acréscimo | Registro P210, VL\_AJ  quando campo   IND\_AJ for igual a 1 |
| VL\_TOT\_CONT\_DEV | Valor total da contribuição previdenciária sobre a receita bruta a   recolher. | VL\_TOT\_CONT\_APU + VL\_TOT\_AJ\_REDUC + VL\_TOT\_AJ\_ACRES |
| COD\_REC | Código da receita referente a contribuição previdenciária | Carregado do cadastro do tributo Cont. Previdenciária |

**Registro P210 - Ajuste da Contribuição Previdenciária sobre a Receita Bruta**

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **DESCRIÇÃO** | **ORIGEM DOS DADOS** |
| REG | Texto fixo contendo P210 | Gerado pela rotina |
| IND\_AJ | Indicador do tipo de ajuste:   0 - Ajuste de redução   1 - Ajuste de acréscimo | Se o lançamento for de Crédito, recebe    valor "0". Se for do tipo débito recebe valor "1" |
| VL\_AJ | Valor Ajuste | Recebe o valor do lançamento de Outros   Débitos/Créditos |
| COD\_AJ | Código do ajuste conforme tabela indicada no item 4.3.8 da EFD | Recebe o valor gravado no campo "Código Ajuste SPED"   da tela de inclusão de Outros Débitos e Créditos. |
| NUM\_DOC | Número do processo, documento ou ato concessório no qual o ajuste está vinculado | Recebe o valor do campo Processo Judicial ou Administrativo   da tela de inclusão do lançamento de Outros Créditos/Débitos. |
| DESCR\_AJ | Descrição resumida do ajuste | Recebe o valor do campo Histórico do lançamentos de Outros Débitos/Créditos. |
| DT\_REF | Data  de referência do ajuste (ddmmaaaa) | Não será gerado |

**Registro P990 - Encerramento do bloco P**

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **DESCRIÇÃO** | **ORIGEM DOS DADOS** |
| REG | Texto fixo contendo P990 | Gerado automaticamente pela rotina |
| QTD\_LIN\_P | Quantidade total de linhas do bloco P | Gerado automaticamente pela rotina |
