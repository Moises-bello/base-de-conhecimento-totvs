---
article_id: 4411473232407
category: TAF - REINF
content_hash: eb1bd49130ab7a27c6ea7af7ad4e35d2f6178b661cafbc0124c3b515ff4e04fa
fetched_at: '2026-06-28T22:41:33.513310+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Como Gerar o R-2055
  manualmente no TAF
type: support-article
updated_at: '2023-03-31T17:00:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411473232407-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-Gerar-o-R-2055-manualmente-no-TAF
---

**Dúvida**Quais são os campos necessários para apuração e transmissão do R-2055 no TAF.

**Ambiente**A partir de 12.1.23  
  
**Solução**

**Critérios para gerar o evento R-2055 no TAF.**

**R-2055 - Aquisição Produtor Rural**

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
