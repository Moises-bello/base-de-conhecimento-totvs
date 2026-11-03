---
article_id: 4411473345303
category: TAF - REINF
content_hash: e40cdd33634af7a33bdc4b8bc481aac60527474d14f06e7961aae252e293030a
fetched_at: '2026-06-28T22:41:33.519525+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Como Gerar o R-2055
  participante optante pela folha de pagamento manualmente no TAF
type: support-article
updated_at: '2023-09-05T20:48:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411473345303-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-Gerar-o-R-2055-participante-optante-pela-folha-de-pagamento-manualmente-no-TAF
---

**Dúvida**

Quais são os campos necessários para apuração e transmissão do R-2055 no TAF, Participante optante pela folha de pagamento.

**Ambiente**A partir de 12.1.23  
  
**Solução**

No cadastro do Participante o campo (C1H\_INDCP) ID RURAL deverá ser preenchido a opção folha de pagamento.

Importante destacar a importância do preenchimento no campo do fornecedor (tabela C1H) C1H\_INDCP (Ind. Rural) a opção 2 - Sobre a Folha de Pagamento, desta forma será gerado no XML o preenchimento da TAG  IndOpcCP= "S" corretamente no Reinf:

**R-2055 - Aquisição Produtor Rural**

A apuração do evento R-2055 é feita através da rotina TAFAPR2055 e aglutina as informações de Documentos Fiscais que atendam os seguintes critérios:

* Documentos Fiscais
  + Capa do documento
    - Dt Emissão (C20\_DTDOC): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão do Documento Fiscal;
    - Oper. (C20\_INDOPE): Para que o Documento Fiscal seja considerado, seu Tipo de Operação deverá corresponder a uma Emissão (Entrada);
  + Produtos/Serviços
    - Tipo Serviço (C30\_IDTSER): Apenas Itens de Documentos Fiscais cujo campo Tipo Serviço esteja em branco serão considerados;
    - Cód. Serviço (C30\_SRVMUN): Apenas Itens de Documentos Fiscais cujo campo Cód. Serviço esteja em branco serão considerados;
    - Tipo Repasse (C30\_TPREPA): Apenas Itens de Documentos Fiscais cujo campo Tipo Repasse esteja em branco serão considerados;
    - CFOP (C30\_CFOP): Onde o ID tem que pertencer a registro válido da tabela C0Y – Cadastro de CFOP;
  + Tributos do Item
    - Tributo (C35\_CODTRI): Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda aos códigos 000013-Previdência, 000024-GILRAT ou 000025-SENAR serão considerados.
  + Participantes
    - Tipo Pessoa (C1H\_PPES): Apenas Documentos Fiscais cujo Participante seja Pessoa Física;
    - Atividade (C1H\_RAMO): preenchido com a opção 4 - Produtor Rural;

**OBS:** Este campo é considerado para escrituração da TAG **indAquis**

**Lógica:**Se CNPJ ( C1H\_CNPJ) estiver preenchido e o CPF (C1H\_CPF) estiver em branco

                                             Se PAA? (C1E\_PAA) igual a 1 e Ind. Isenção ( C30\_INDISE ) diferente de 1 **indAquis**recebe 3

                                             Se PAA? (C1E\_PAA) igual a 1 e Ind. Isenção ( C30\_INDISE ) igual a 1 **indAquis**recebe 6

                                             Se PAA? (C1E\_PAA) diferente de 1 **indAquis**recebe 3

                                       Se CPF (C1H\_CPF) estiver preenchido.

                                            Se PAA? (C1E\_PAA) igual a 1 e Ind. Isenção (C30\_INDISE) diferente de 1 **indAquis**recebe 2

                                            Se PAA? (C1E\_PAA) igual a 1 e Ind. Isenção ( C30\_INDISE ) igual a 1 **indAquis**recebe 5

                                            Se PAA? (C1E\_PAA) diferente de 1 e Ind. Isenção ( C30\_INDISE ) diferente de 1 **indAquis**recebe 1

                                            Se PAA? (C1E\_PAA) diferente de 1 e Ind. Isenção ( C30\_INDISE ) igual a 1 **indAquis**recebe 4

                                           Se o Id. CFOP (C30\_CFOP) igual*a*1501 ou 2501  **indAquis**recebe 7

Trecho Manual da REINF 1.5

1. Informação do grupo “{detAquis} – Detalhamento das aquisições de produção rural” e o recolhimento ao SENAR. *1. Caso o produtor rural tenha optado pela tributação da contribuição previdenciária**sobre a folha de pagamento, todos os campos do grupo “{detAquis} – Detalhamento das* *aquisições de produção rural” deverão ser informados com os valores correspondentes.* 2.2. É devida a retenção e o recolhimento da contribuição ao SENAR mesmo no caso em que o produtor rural pessoa física tenha optado pela contribuição previdenciária sobre a folha de pagamento. Neste caso a operacionalização do recolhimento da contribuição ao SENAR será realizada conforme a seguir: O adquirente, obrigado ao preenchimento do evento R-2055 deverá informar: *- o campo {indOpcCP} com “S” (sim);*
2. o campo {vlrBruto} com o valor bruto da comercialização da produção rural;
3. o campo {vlrCPDescPR} com valor zero;
4. o campo {vlrRatDescPR} com valor zero; e *- o campo {vlrSenarDesc} com o valor real a ser recolhido.*
