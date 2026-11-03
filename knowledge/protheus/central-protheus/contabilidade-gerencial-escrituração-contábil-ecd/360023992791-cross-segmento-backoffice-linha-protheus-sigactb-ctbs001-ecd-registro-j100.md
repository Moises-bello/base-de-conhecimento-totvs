---
article_id: 360023992791
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 738407a1e1af2d119c727bf6b51d0d3a8e0c6b6f4d44570e4fe76b3333f509b8
fetched_at: '2026-06-28T22:40:45.614546+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD Registro
  J100
type: support-article
updated_at: '2025-06-26T14:40:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Registro-J100
---

**Dúvida**

Como o registro J100 da ECD é gerado?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade gerencial - Todas as versões

**Solução**

* Através da rotina Lançamento contábeis**(CTBA102)** Verifique os lançamento Contábeis

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021700311)

* Emita o relatório Razão e verifique os valores

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021735532)

* Emita o relatório balancete e verifique os valores

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021700731)

 Emita o relatório Balaço Patrimonial (CTBR500) e verifique os valores estão correto e compatível com os relatório anteriores

* Caso esteja correto gere o arquivo da ECD com a mesma visão gerencial informada no relatório Balaço Patrimonial (CTBR500)
* Caso Não esteja correto verifique se a visão gerencial (CTBA161) está configurada corretamente , pois o relatório depende da configuração da visão para apresentação de saldo

* Través do cadastro de plano de contas (CTBA020) verifique a natureza da conta e a natureza da conta superior

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021736112)

* Através do cadastro da visão gerencial (CTBA161) Verifique os campos abaixo
* Não Informe "Formula" no cadastro da visão gerencial
* Campo "Total geral" deve ser informado para entidade Sintética totalizador Ativo e Passivo , as demais sintéticas não precisão dessa configuração

Totalizadora do Ativo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32746493385367)

Totalizadora do Passivo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32746493387159)

* Quando Ativo "Coluna =1"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32746493388823)

* Quando passivo "Coluna =2"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026905312)

* Ao gerar o arquivo da ECD através da rotina de escrituração contábil(CTBS001) , verifique a Visão gerencial que esta sendo informada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071456463767)

* Gere o arquivo e veja se o Valor apresentado corresponde ao mesmo valor apresentado no razão e no balancete

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026922211)

* Estrutura do Registro com base no manual da receita

|J100|001211|D|3|00121|**P**|FORNECEDORES|0,00|C|2500,00|C||

Campo 01 – Tipo de Registro: J100  
Campo 02 – Código de Aglutinação: 001211  
Campo 03 – Indicador do Tipo de Código de Aglutinação: D  
Campo 04 – Nível do Código de Aglutinação: 3  
Campo 05 – Código de Aglutinação de Nível Superior: 00121  
Campo 06 – Indicador de Grupo do Balanço: **P (Passivo**)  
Campo 07 – Descrição do Código de Aglutinação: FORNECEDORES  
Campo 08 – Valor Inicial do Código de Aglutinação: 0,00 (0,00)  
Campo 09 – Indicador da Situação do Saldo Informado no Campo Anterior: C (Credito)  
Campo 10 – Valor Final do Código de Aglutinação: 2500,00 (2.500,00)  
Campo 11 – Indicador da Situação do Saldo Informado no Campo Anterior: C (Credito)  
Campo 12 – Referência à Numeração das Notas Explicativas: Não há

* Verifique se o nível de aglutinação criada na Visão segue "(mesmo conceito do plano de contas – Registro I050)"
* [MP-SIGACTB-ECD I050 : 5 - NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)
* Veja o que o manual da receita descreve sobre o NIVEL\_AGL do J100(Balanço)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029390632)

Com isso as no cadastro da visão gerencial [sintéticas e analíticas deve conter](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)  a somatoria de  [no mínimo 4 níveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-MP-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010-?source=search)

Para mais detalhes veja: [Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD - ESTRUTURA NIVEL VISÃO GERENCIAL J100 E J150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33071442613271-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-EXTRUTURA-NIVEL-VIS%C3%83O-GERENCIAL-J100-E-J150)

Verifique todos os pontos : [MP - SIGACTB :ECD : J005 IND\_COD\_AGL ,VL\_CTA\_INI e IND\_GRP\_BAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028866271-MP-SIGACTB-ECD-J005-IND-COD-AGL-VL-CTA-INI-e-IND-GRP-BAL?source=search)

Tabelas envolvidas, verifique

Veja o compartilhamento as tabelas  :

[Compartilhamento de tabelas no Contabilidade Gerencial (SIGACTB)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search)

|  |  |
| --- | --- |
| • | CTS - Entidade Gerencial |

|  |  |
| --- | --- |
| • | CVE - Visão gerencial |

|  |  |
| --- | --- |
| • | CVF - Itens da Visão Gerencial |

|  |  |
| --- | --- |
| • | CT1 - Cadastro Plano de Contas. |

|  |  |
| --- | --- |
| • | CTT- Cadastro Centros de Custo. |

|  |  |
| --- | --- |
| • | SL - Tabela de Tipos de Saldos. |

 

|  |  |
| --- | --- |
| • | CTG - Calendários Contábeis |

|  |  |
| --- | --- |
| • | CTN - Configuração de Livros Contábeis |

|  |  |
| --- | --- |
| • | CTO - Moedas |

 [TABELAS ECD E ECF COMPARTILHAMENTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF-COMPARTILHAMENTO?source=search)

|  |  |
| --- | --- |
| • | CSE - Balanço cabeçalho |

|  |  |
| --- | --- |
| • | CSD - Balanço Itens |

Veja mais:

[MP-SIGACTB -ECD - GRUPO BALANÇO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007046411-MP-SIGACTB-ECD-GRUPO-BALAN%C3%87O-?source=search)

[MP\_SIGACTB - ECD - J150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006972612-MP-SIGACTB-ECD-J150-?source=search)

[NOTA\_EXP\_REF: Conteúdo do campo inválido.](http://tdn.totvs.com/pages/releaseview.action?pageId=338363903)

[ECD0001\_ECD\_ADVERTENCIA\_J150\_J100](http://tdn.totvs.com/display/public/PROT/ECD0001_ECD_ADVERTENCIA_J150_J100)

[J150\_VL\_CTA\_ULT\_DRE\_ACUMULADO](http://tdn.totvs.com/display/public/PROT/ECD0028_J150_VL_CTA_ULT_DRE_ACUMULADO)

[MP-SIGACTB-ECD RELATORIO J150 (DRE) NO PGE NÃO CORRESPONDE AO EMITIDO NO PROTHEUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026626772-MP-SIGACTB-ECD-RELATORIO-J150-DRE-NO-PGE-N%C3%83O-CORRESPONDE-AO-EMITIDO-NO-PROTHEUS?source=search)

[MP-SIGACTB ECD : J100 e J150 MV\_GRVISOR ORDEM DA VISAO GERENCIAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026127292-MP-SIGACTB-ECD-J100-e-J150-MV-GRVISOR-ORDEM-DA-VISAO-GERENCIAL?source=search)
