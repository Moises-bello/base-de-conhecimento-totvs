---
article_id: 4411473193367
category: TAF - REINF
content_hash: 88df016c4c6191f29a8516a8d821fd384cfed6c5444a38ccc684a8df81ce98a2
fetched_at: '2026-06-28T22:41:33.508746+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Como Gerar o R-2050
  manualmente no TAF
type: support-article
updated_at: '2023-03-31T17:00:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411473193367-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-Gerar-o-R-2050-manualmente-no-TAF
---

**Dúvida**Quais são os campos necessários para apuração e transmissão do R-2050 no TAF.

**Ambiente**A partir de 12.1.23  
  
**Solução**

**Critérios para gerar o evento R-2050 no TAF.**

##### R-2050 - Comercialização da Produção por Produtor Rural PJ/Agroindústria

* Documentos Fiscais
  + Capa do documento
    - Dt Emissão (C20\_DTDOC): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão do Documento Fiscal;
    - Oper. (C20\_INDOPE): Para que o Documento Fiscal seja considerado, seu Tipo de Operação deverá corresponder a uma Emissão (Saída);
  + Produtos/Serviços
    - Tipo Serviço (C30\_IDTSER): Apenas Itens de Documentos Fiscais cujo campo Tipo Serviço esteja em branco serão considerados;
    - Cód. Serviço (C30\_SRVMUN): Apenas Itens de Documentos Fiscais cujo campo Cód. Serviço esteja em branco serão considerados;
    - Tipo Repasse (C30\_TPREPA): Apenas Itens de Documentos Fiscais cujo campo Tipo Repasse esteja em branco serão considerados;
    - CFOP (C30\_CFOP): Onde o ID tem que pertencer a registro válido da tabela C0Y – Cadastro de CFOP
    - Para informar a conta contábil na nota fiscal preencha o campo (C30\_CODCTA) - Conta Contábil
  + Tributos do Item
    - Tributo (C35\_CODTRI): Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda aos códigos 000013-Previdência, 000024-GILRAT ou 000025-SENAR serão considerados.
  + Participantes
    - Tipo Pessoa (C1H\_PPES ): Apenas Documentos Fiscais cujo Participante seja Pessoa Jurídica serão considerados;
    - PAA? (C1H\_PAA)  - Comercialização da Produção para Entidade do Programa de Aquisição de Alimentos - PAA;

**OBS:** Este campo é considerado para escrituração da TAG **indCom**

**Lógica:**Se Ind. Isencao ( C30\_INDISE ) *igual a*1 **indCom** *recebe* 7

                                        Se PAA? (C1H\_PAA) *igual a* 1 **indCom** *recebe* 8

                                        Se PAA? (C1H\_PAA) *diferente de* 1 *e*  CFOP de exportação direta (iniciado com 7) *ou* CFOP 5501, 5502, 6501 *ou* 6502 **indCom** *recebe* 9

                                        Se PAA? (C1H\_PAA) *diferente de* 1 *e*  CFOP não for de exportação indireta (iniciado com 5 ou 6 ) **indCom** *recebe* 1
