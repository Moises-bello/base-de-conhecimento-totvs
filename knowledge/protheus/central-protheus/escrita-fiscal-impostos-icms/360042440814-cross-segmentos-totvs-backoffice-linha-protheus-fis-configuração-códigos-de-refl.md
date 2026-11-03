---
article_id: 360042440814
category: Escrita Fiscal - Impostos - ICMS
content_hash: 328f259ddc59065a371da62fea30257f1b90537ca28961fd1d61091593c2d150
fetched_at: '2026-06-28T22:39:24.128357+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Configuração Códigos
  de Reflexo
type: support-article
updated_at: '2021-07-28T02:11:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042440814-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-C%C3%B3digos-de-Reflexo
---

**Dúvida**  
  
Configuração Códigos de Reflexo   
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80

**Solução:**  
  
Com o intuito de automatizar processo de ajustes na EFD ICMS/IPI que são realizados pelos registros C197, D197, E111, E115, E220 e informações que são levadas para a tag cBenef na transmissão dos documentos, o sistema possibilita que o usuário configure lançamentos durante a emissão dos documentos fiscais.

Para que esses ajustes sejam feitos na geração da EFD ICMS/IPI(SPEDFISCAL) e na transmissão das Notas fiscais, será necessário realizar os lançamentos correspondentes na Apuração de ICMS (MATA953 - Tabela CDH), Apuração de IPI (MATA952 - Tabela CDP) ou nas informações adicionais da Apuração (MATA017 - Tabela CDV - tag cBenef).

O sistema possibilita que o usuário configure quando esses lançamentos deverão ser feitos durante a emissão dos documentos fiscais.

Para facilitar o entendimento e a configuração do código de reflexo, temos a lista abaixo que apresenta qual o campo será considerado para realizar a gravação das tabelas CDA (Ajustes que serão levados para a apuração de ICMS/IPI) e CDV (Informações adicionais - tag cBenef). Caso o código de reflexo utilizado esteja apontando para um campo que não foi configurado para ser calculado, o código será retornado vazio.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057554913/mceclip0.png)

**Campo Base de calculo (CE0\_NFBASE)**

CE0\_NFBASE = '1' - Valor da Base de ICMS (Necessário utilizar o campo Calc. ICMS = Sim na TES)

CE0\_NFBASE = '2' - Valor Contabil

CE0\_NFBASE = '3' - Valor do ICMS Normal (Necessário utilizar o campo Calc. ICMS = Sim na TES)

CE0\_NFBASE = '4' - Base do ICMS Solidário (Necessário calcular ICMS ST)

CE0\_NFBASE = '5' - Base do ICMS sobre o frete autônomo (Configuração Frete autônomo: <https://tdn.totvs.com/pages/releaseview.action?pageId=322155990> )

CE0\_NFBASE = '6' - Credito Estimulo de Manaus (Configuração para calculo: <https://tdn.totvs.com/pages/releaseview.action?pageId=286745053> )

CE0\_NFBASE = '7' - Base de ICMS difal do destinatário - (Documentação sobre DIFAL EC87: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018403132-MP-FIS-Diferencial-na-sa%C3%ADda-para-cliente-contribuinte-e-DIFAL-para-n%C3%A3o-contribuinte-?source=search> )

CE0\_NFBASE = '8' - Valor original da Base de ICMS

CE0\_NFBASE = '9' - Valor da Base do IPI (Necessário utilizar o campo Calc. IPI = Sim na TES)

CE0\_NFBASE = 'A' - Base do ICMS de transporte Substituição Tributaria (Configuração para calculo: <https://tdn.totvs.com/display/public/PROT/Documento+Fiscal+para+ICMS-ST+de+Transportes+-+MP11+--+116043> )

CE0\_NFBASE = 'B' - Valor do ICMS de transporte Substituição Tributaria (Configuração para calculo: <https://tdn.totvs.com/display/public/PROT/Documento+Fiscal+para+ICMS-ST+de+Transportes+-+MP11+--+116043> )

CE0\_NFBASE = 'C' - [Valor original da Base de ICMS] - [Valor da Base de ICMS ]

CE0\_NFBASE = 'D' - Base FEEF-RJ (Configuração para calculo: <https://tdn.totvs.com/pages/releaseview.action?pageId=271867033> )

CE0\_NFBASE = 'E' - Não disponível

CE0\_NFBASE = 'F' - Não disponível

CE0\_NFBASE = 'G' - Valor Base ICMS EFETIVO (Configuração para calculo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024680071-MP-FIS-Como-gerar-as-tags-do-ICMS-efetivo-> )

CE0\_NFBASE = 'H' - Valor do IPI (Necessário utilizar o campo Calc. IPI = Sim na TES)

CE0\_NFBASE = 'I' - Campo D1\_BASNDES. Este campo é preenchido manualmente na digitação do documento de entrada.

CE0\_NFBASE = 'J' - Valor do desconto da Zona Franca do item (Configuração para calculo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253-MP-FIS-Como-configurar-sistema-para-calcular-o-SUFRAMA-> )

CE0\_NFBASE = 'K' - [Valor do desconto da Zona Franca do item] - ([Desconto do PIS]+[Desconto do Cofins]) (Configuração para calculo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253-MP-FIS-Como-configurar-sistema-para-calcular-o-SUFRAMA-> )

CE0\_NFBASE = 'Z' - 0

**Campo Alíquota de calculo (CE0\_NFALIQ)**

**Observação**: As configurações relacionadas aos campos de FECP e relacionados ao ICMS complementar estão disponibilizada ao final desta documentação.

CE0\_NFALIQ = '1' - Alíquota de ICMS da nota fiscal (Necessário utilizar o campo Calc. ICMS = Sim na TES)

CE0\_NFALIQ = '2' - Percentual do Credito Presumido (Campo F4\_CRDPRES) (Configuração para crédito presumido: <https://tdn.totvs.com/pages/viewpage.action?pageId=45220123&preview=%2F45220123%2F45482011%2FFIS_Credito_Presumido_ICMS.pdf> )

CE0\_NFALIQ = '3' - Alíquota do ICMS Solidário da nota fiscal (Necessário calcular ICMS ST)

CE0\_NFALIQ = '4' - Percentual do Estorno de Credito/Debito (Campo F4\_ESTCRED)

CE0\_NFALIQ = '5' - [ Alíquota para calculo do ICMS Complementar] - [Alíquota de ICMS] - [ Alíquota do FECP Complementar quando preenchido ou alíquota do FECP próprio ]

CE0\_NFALIQ = '6' - Informado. Neste caso, preencha a alíquota no campo Vl.Aliquota(CE0\_NFALVA) no próprio cadastro do reflexo.

CE0\_NFALIQ = '7' - Alíquota do FECP Complementar quando preenchido ou alíquota do FECP próprio

CE0\_NFALIQ = '8' - [Alíquota do FECP ST ] + [Alíquota FECP-MG] + [Alíquota FECOP-RN ] + [Alíquota FECP-MT ]

CE0\_NFALIQ = '9' - [Alíquota para calculo do ICMS Complementar ] - [Alíquota interna do estado para calculo do Diferencial de aliquota do Simples Nacional] - [Alíquota FECP]

CE0\_NFALIQ = 'A' - Alíquota de IPI

CE0\_NFALIQ = 'B' - Alíquota do ICMS de transporte Substituição Tributaria (Configuração para calculo: <https://tdn.totvs.com/display/public/PROT/Documento+Fiscal+para+ICMS-ST+de+Transportes+-+MP11+--+116043> )

CE0\_NFALIQ = 'C' - Alíquota FEEF-RJ (Configuração para calculo: <https://tdn.totvs.com/pages/releaseview.action?pageId=271867033> )

CE0\_NFALIQ = 'D' - não disponível

CE0\_NFALIQ = 'E' - Valor ALIQ ICMS EFETIVO (Configuração para calculo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024680071-MP-FIS-Como-gerar-as-tags-do-ICMS-efetivo-> )

CE0\_NFALIQ = 'F' - ([Alíquota de ICMS ] - ([Alíquota FECP ] + [Alíquota FECP-MG] + [Alíquota FECOP-RN ] + [Alíquota FECP-MT ]))

CE0\_NFALIQ = 'G' - Campo D1\_ALQNDES. Este campo é preenchido manualmente na digitação do documento de entrada

CE0\_NFALIQ = 'H' - Conteúdo do campo F7\_ALQANT (Preenchido no cadastro da exceção fiscal - MATA540) OU Conteúdo do campo CFC\_ALQANT (Preenchido no cadastro da UFxUF - FISA080)

CE0\_NFALIQ = 'I' - [ Alíquota para calculo do ICMS Complementar]

CE0\_NFALIQ = 'Z' - 0

**Campo valor do ajuste (CE0\_NFVALO)**

CE0\_NFVALO = '1' - [ Valor do ICMS Normal ] (Necessário utilizar o campo Calc. ICMS = Sim na TES)

CE0\_NFVALO = '2' - [ Valor do ICMS Complementar do item ] - [ Valor do FECP ]

CE0\_NFVALO = '3' - [ Valor da mercadoria ]

CE0\_NFVALO = '4' - [ Valor Antecipação ICMS ] (Configuração para calculo: <https://tdn.totvs.com/pages/releaseview.action?pageId=516199161> )

CE0\_NFVALO = '5' - [ Credito Presumido ] (Configuração para crédito presumido: <https://tdn.totvs.com/pages/viewpage.action?pageId=45220123&preview=%2F45220123%2F45482011%2FFIS_Credito_Presumido_ICMS.pdf> )

CE0\_NFVALO = '6' - [ Valor do ICMS Solidário ] (Necessário calcular ICMS ST)

CE0\_NFVALO = '7' - [ Valor do Estorno de Credito/Debito ] (Conteúdo do campo D2\_ESTCRED/D1\_ESTCRED. Calculo efetuado quando preenchido o campo F4\_ESTCRED)

CE0\_NFVALO = '8'  [ Valor do ICMS diferido ] (Configuração para calculo: <https://tdn.totvs.com/display/PROT/FIS0069_DIFERIMENTO_ICMS> )

CE0\_NFVALO = '9' - Base informada no campo CE0\_NFBASE \* Aliquota informada no campo CE0\_NFALVA. Somente será utilizado quando o campo CE0\_NFALIQ = 6

CE0\_NFVALO = 'A' - [ Valor do FECP ] + [ Valor do FECP-MG ] + [Valor do FECOP-RN ] + [Valor do FECP-MT ]

CE0\_NFVALO = 'B' - [ Valor do FECP ST ] + [ Valor do FECP ST-MG ] + [ Valor do FECOP ST-RN ] + [ Valor do FECP ST-MT ]

CE0\_NFVALO = 'C' - [ Valor do ICMS sobre o frete autônomo ] (Configuração Frete autônomo: <https://tdn.totvs.com/pages/releaseview.action?pageId=322155990> )

CE0\_NFVALO = 'D' - [ DIFAL icms ] (Documentação sobre DIFAL EC87: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018403132-MP-FIS-Diferencial-na-sa%C3%ADda-para-cliente-contribuinte-e-DIFAL-para-n%C3%A3o-contribuinte-?source=search> )

CE0\_NFVALO = 'E' - [ Valor do ICMS Complementar do item ]

CE0\_NFVALO = 'F' - [ Valor FECP DIFAL]

CE0\_NFVALO = 'G' - [ Valor Solidário XML] - [ Valor do ICMS Solidário]

CE0\_NFVALO = 'H' - [ Valor do ICMS Solidário] - [ Valor Antecipação ICMS]

CE0\_NFVALO = 'J' - [ Valor do ICMS Normal ] - [ Credito Presumido ]

CE0\_NFVALO = 'K' - [ Valor do IPI ]

CE0\_NFVALO = 'L' - [ Valor do ICMS de transporte Substituição Tributaria] (Configuração para calculo: <https://tdn.totvs.com/display/public/PROT/Documento+Fiscal+para+ICMS-ST+de+Transportes+-+MP11+--+116043> )

CE0\_NFVALO = 'M' - ( [ Valor original da Base de ICMS ] - [ Valor da Base de ICMS ]) \* [ Alíquota de ICMS ] / 100

CE0\_NFVALO = 'N' - não disponível

CE0\_NFVALO = 'O' - [ ICMS Isento ] (Utilizar L. Fisc. = Isento na TES)

CE0\_NFVALO = 'P' - [ Valor Contabil ]

CE0\_NFVALO = 'Q' - [ ICMS Outros ] (Utilizar L. Fisc. = Outros na TES)

CE0\_NFVALO = 'R' - [ PRODEPE ] (Configuração do calculo: <https://tdn.totvs.com/pages/viewpage.action?pageId=6076389&preview=%2F6076389%2F22708260%2FFIS_PRODEPE_Portaria_2392001_Pernambuco.pdf> )

CE0\_NFVALO = 'S' - [ Valor FEEF-RJ ] (Configuração para calculo: <https://tdn.totvs.com/pages/releaseview.action?pageId=271867033> )

CE0\_NFVALO = 'T' - [ D1\_ICMNDES] - Preenchido manualmente na digitação do documento de entrada

CE0\_NFVALO = 'U' - [ Valor ICMS EFETIVO] (Configuração para calculo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024680071-MP-FIS-Como-gerar-as-tags-do-ICMS-efetivo-> )

CE0\_NFVALO = 'V' - [ Valor do ICMS Solidário] + [ Valor do ICMS Normal ]

CE0\_NFVALO = 'W' - [ D1\_ICMNDES (Preenchido manualmente na digitação do documento de entrada) ] + [ Valor do ICMS Normal ]

CE0\_NFVALO = 'X' - [ Valor do ICMS Normal ] - ( [ Valor da mercadoria ] \* ( [Percentual do Credito Presumido (F4\_CRDPRES))

CE0\_NFVALO = 'Y' - ( [Valor do ICMS Normal ] - ( [Valor do FECP ] + [Valor do FECP-MG ] + [Valor do FECOP-RN ] + [ Valor do FECP-MT ]))

CE0\_NFVALO = 'Z' - [ Valor do ICMS Desonerado Próprio ] (Configuração para calculo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030959773-MP-FIS-Configura%C3%A7%C3%A3o-para-o-c%C3%A1lculo-do-ICMS-Desonerado-Resolu%C3%A7%C3%A3o-SEFAZ-13-2019-RJ>

CE0\_NFVALO = 'AA' - [ Valor do ICMS Desonerado ST ]

CE0\_NFVALO = 'AB' - [ Valor do desconto da Zona Franca do item] (Configuração para calculo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253-MP-FIS-Como-configurar-sistema-para-calcular-o-SUFRAMA-> )

CE0\_NFVALO = 'AC' - [ Valor do desconto da Zona Franca do item] - ( [Desconto do PIS] + [Desconto do Cofins]) (Configuração para calculo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253-MP-FIS-Como-configurar-sistema-para-calcular-o-SUFRAMA-> )

Material de apoio para FECP: <https://tdn.totvs.com/pages/releaseview.action?pageId=287056662>   
Material de apoio para ICMS Complementar - Entrada: <https://tdn.totvs.com/pages/releaseview.action?pageId=61934231>   
Material de apoio para ICMS Complementar - Saída: <https://tdn.totvs.com/pages/releaseview.action?pageId=51249690>
