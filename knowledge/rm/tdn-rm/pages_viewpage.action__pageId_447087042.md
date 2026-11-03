---
content_hash: a85b846bc046c3c061e28b65f0985b6ae8f35896e2897f2ae714e94c95f82079
fetched_at: '2026-06-29T00:09:55.161866+00:00'
page_id: '447087042'
product: rm
source: tdn-rm
title: SPED Fiscal Alterações do Layout 2020 - Versão 3.0.3
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=447087042
version: 46
---

Abaixo estão listadas as alterações/implementações feitas na rotina do SPED Fiscal para atender o layout 3.0.3 com efeito a partir de Janeiro de 2020

1lefttrue1Bloco 0

* Registro 0000:

Na tela de geração da rotina, alterado a versão para “**014**”. Essa versão só é válida a partir de 01/01/2020.

Os registros referentes ao ressarcimento de ICMS ST serão solicitados a critério de cada UF. Adicionado a flag na tela de geração do SPED a flag "Gerar ressarcimento/complemento ICMS ST".  

* Registro 0002: Criado o campo  "Classificação do Estabelecimento" na tela de geração do SPED com as seguintes opções:
  + Industrial - Transformação
  + Industrial - Beneficiamento
  + Industrial - Montagem
  + Industrial - Acondicionamento ou Recondicionamento
  + Industrial - Renovação ou Recondicionamento
  + Equiparado a industrial - Por opção
  + Equiparado a industrial - Importação Direta
  + Equiparado a industrial - Por lei específica
  + Equiparado a industrial - Não enquadrado nos códigos 05, 06 ou 07
* Outros
2Bloco 1

* Registro 1391 - Incluído os campos 18 - COD\_ITEM, 19 -TP\_RESIDUO e 20 - QTD\_RESIDUO. Serão preenchidos conforme os novos campos criados no cadastro de Usina.  Documento
3Bloco CBloco C

* Registro C191 -  Incluído na geração o modelo de documento 65 (NFC-e). Documento:

* Registro C500 - Incluído os campos:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | 28 | CHV\_DOCe | Chave da Nota Fiscal de Energia Elétrica Eletrônica | Gerar com a informação do Campo Chave de Acesso do Lançamento Fiscal |
  | 29 | FIN\_DOCe | Finalidade da emissão do documento eletrônico:  1 – Normal 2 – Substituição  3 – Normal com ajuste | Gerar com valor fixo “1”. Este campo só deve ser preenchido se o modelo do documento for “66”. |
  | 30 | CHV\_DOCe\_REF | Chave da nota referenciada. | Não gerar |
  | 31 | IND\_DEST | Indicador do Destinatário/Acessante: 1 – Contribuinte do ICMS;  2 – Contribuinte Isento de Inscrição no Cadastro de Contribuintes do ICMS;  9 – Não Contribuinte | Gerado conforme o Campo Contribuinte do ICMS do Cadastro do Cliente\Fornecedor. FCFO.CONTRIBUINTE |
  | 32 | COD\_MUN\_DEST | Código do município do destinatário conforme a tabela do IBGE | Gerado com o Código do Município do Cadastro do Cli\For |

  Documentação:

* Implementação do Registro C591 - Informações do Fundo de Combate à Pobreza – FCP na NF3e (código 66)

|  |  |  |  |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "C591” |  |
| 02 | VL\_FCP\_OP | Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação própria, na combinação de CST\_ICMS, CFOP e alíquota do ICMS | Gerado com o valor do FECP do ICMS  Próprio do Lançamento Fiscal |
| 03 | VL\_FCP\_ST | Valor do Fundo de Combate à Pobreza (FCP) vinculado à operação de substituição tributária, na combinação de CST\_ICMS, CFOP e alíquota do ICMS. | Gerado com o valor do FECP do ICMS  ST do Lançamento Fiscal |

Documentação: 

* Implementação do Registro C595 - Observações do Lançamento Fiscal (códigos 06, 28, 29 e 66)

Filho do Registro C590

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C595” |  |
| 02 | COD\_OBS | Código da observação do lançamento fiscal (campo 02 do Registro 0460) | Referência o registro 0460. Deve conter o valor do campo 2 do registro 0460 para fazer relacionamento com o mesmo. |
| 03 | TXT\_COMPL | Descrição complementar do código de observação. | Referência o registro 0460. Deve conter o valor do campo 3 do registro 0460 para fazer relacionamento com o mesmo. |

Documentação: 

* Implementação do Registro C597 - Outras Obrigações Tributárias, Ajustes e Informações de Valores Provenientes de Documento Fiscal

Filho do Registro C595

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C597” |  |
| 02 | COD\_AJ | Código do ajustes/benefício/incentivo, conforme tabela indicada no item 5.3 | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal – Código de Ajuste associado.  DLAFAJUSTESPED.IDCODIGOAJUSTE |
| 03 | DESCR\_COMPL\_AJ | Descrição complementar do ajuste do documento fiscal | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal. DLAFAJUSTESPED.DESCRICAOCOMPLEMENTAR |
| 04 | COD\_ITEM | Código do item (campo 02 do Registro 0200) |  |
| 05 | VL\_BC\_ICMS | Base de cálculo do ICMS ou do ICMS ST | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal. DLAFAJUSTESPED.BASECALCULO |
| 06 | ALIQ\_ICMS | Alíquota do ICMS | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal. DLAFAJUSTESPED.ALIQUOTA |
| 07 | VL\_ICMS | Valor do ICMS ou do ICMS ST | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal. DLAFAJUSTESPED.VALORICMSICMSST |
| 08 | VL\_OUTROS | Outros valores | Gerado com os Dados da Sub Pasta Ajuste Sped do Lançamento Fiscal. DLAFAJUSTESPED.OUTROSVALORES |

Documento: 

* Implementação do Registro C870 - Itens do Resumo Diário dos Documentos (CF-e-SAT) (código 59)

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "C810” |  |
| 02 | COD\_ITEM | Código do item (campo 02 do Registro 0200) | Gerado com o Código do Produto - TPRD.CODIGOPRD |
| 03 | QTD | Quantidade do item | Gerado com a Quantidade do Item do Lançamento Fiscal - DITEM.QTDEPRD |
| 04 | UNID | Unidade do item (Campo 02 do registro 0190) | Gerado com a Quantidade do Item do Lançamento Fiscal - DITEM.CODUND |
| 05 | CST\_ICMS | Código da Situação Tributária referente ao ICMS | Gerado com o ST do Item do Lançamento Fiscal - DITEM.CST |
| 06 | CFOP | Código Fiscal de Operação e Prestação | Gerar com a CFOP associada ao Lançamento Fiscal - DNATUREZA.CODNAT |

Documentação: 

* [Documento de Referência do Bloco C](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546009#BLOCOC-C001)
4Bloco GBloco G

* Registro G140 - Incluído os campos:

|  |  |  |  |
| --- | --- | --- | --- |
| 04 | QTDE | Quantidade, deste item da nota fiscal, que foi aplicada neste bem, expressa na mesma unidade constante no documento fiscal de entrada | Nas operações de entrada é a quantidade do Item do Lançamento Fiscal.   Nas operações de saída, é a quantidade informada no Patrimônio. |
| 05 | UNID | Unidade do item constante no documento fiscal de entrada | Gerado com a Unidade informado no Item do Lançamento Fiscal. |
| 06 | VL\_ICMS\_OP\_AP LICADO | Valor do ICMS da Operação Própria na entrada do item, proporcional à quantidade aplicada no bem ou componente. | Gerado com o Valor do ICMS Próprio informado na Sub pasta ICMS do Item do Lançamento Fiscal |
| 07 | VL\_ICMS\_ST\_AP LICADO | Valor do ICMS ST na entrada do item, proporcional à quantidade aplicada no bem ou componente. | Gerado com o Valor do ICMS ST informado na Sub pasta ICMS do Item do Lançamento Fiscal |
| 08 | VL\_ICMS\_FRT\_A PLICADO | Valor do ICMS sobre Frete do Conhecimento de Transporte na entrada do item, proporcional à quantidade aplicada no bem ou componente. | Gerado com o Valor do ICMS do Frete informado na Sub pasta ICMS do Item do Lançamento Fiscal |
| 09 | VL\_ICMS\_DIF\_A PLICADO | Valor do ICMS Diferencial de Alíquota, na entrada do item, proporcional à quantidade aplicada no bem ou componente. | Gerado com o Valor do Difal  informado na Sub pasta ICMS do Item do Lançamento Fiscal |

Documentação: 

5Bloco HBloco H

* Implementação do Registro H005 - Totais do inventário:

|  |  |  |  |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "H005” | Fixo “H005” |
| 02 | DT\_INV | Data do inventário | Data final do período da rotina |
| 03 | VL\_INV | Valor total do estoque | Os valores totais do inventário por produto apurados na data do balanço. |
| 04 | MOT\_INV | Informe o motivo do Inventário: | Fixo “06” – Para controle das mercadorias sujeitas ao regime de substituição tributária – restituição/ ressarcimento/ complementação. |

Documentação: 

Informações

Documentação:
