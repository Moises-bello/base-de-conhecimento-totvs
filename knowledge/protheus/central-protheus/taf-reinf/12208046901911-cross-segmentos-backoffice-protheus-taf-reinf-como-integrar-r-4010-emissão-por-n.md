---
article_id: 12208046901911
category: TAF - REINF
content_hash: 88d1f5f60bf71652fa10934f9567ef2c94f975e25e0a46692af6927aa343de25
fetched_at: '2026-06-28T22:41:33.761828+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como integrar R-4010
  (Emissão) por nota manualmente no TAF.
type: support-article
updated_at: '2023-03-31T16:58:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12208046901911-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-integrar-R-4010-Emiss%C3%A3o-por-nota-manualmente-no-TAF
---

**Dúvida**Como gerar o evento R-4010 manualmente no TAF.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12.   
  
**Solução**

**Para que os documentos fiscais de entrada (TAFA062),  sejam considerados no evento R-4010 → Pagamentos/créditos a beneficiário pessoa física o imposto calculado na nota fiscal deve ser o IR na emissão (ID TAF = 000012 - IR Emissão).**  
  
 Atualizações -> Movimentos REINF -> documento de entrada(TAFA062E) -> Incluir.

**Capa do documento.**

Dt Emissão (C20\_DTDOC): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão do Documento Fiscal;

![R4010_doc_entrada.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12207206319639)  
Tp. Oper. (C20\_INDOPE): Para que o Documento Fiscal seja considerado, seu Tipo de Operação deverá corresponder a uma Aquisição (Entrada);

![R4010_doc_entrada_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12207328197271)

**Produtos/Serviços.**

Natureza de Rendimento (C30\_CNATRE): Para que o item do documento seja considerado, a Natureza de Rendimento deverá possuir conteúdo válido que corresponda a um código da tabela V3O - Naturezas de Rendimento.

![R4010_do_entrada_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12207312018327)

**Tributos do Item.**

C.Tributo (C35\_CODTRI): Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código 12-IR emissão

![R4010_doc_de_entrada_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12207451094551)

**Participantes.**

* + Tipo Pessoa (C1H\_PPES ):

![R4010_doc_de_entrada_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12207563127191)

* + Para Beneficiários residentes no Brasil (C1H\_CODPAI=000001) Faturas/Documentos Fiscais/Pagamentos cujo Participante seja Pessoa Física serão consideradas;

![R4010_doc_entrada_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12207641653271)

* + Tipo Pessoa (C1H\_PPES ): Para participantes residentes no exterior (C1H\_CODPAI <> 000001) Também serão considerados os Participantes que estejam com a opção = "3 - Outros" no campo Tipo Pessoa. Neste cenário é necessário preencher o campo Tipo Pessoa Exterior (C1H\_PEEXE) como 1 - Pessoa Física;
* ![R4010_doc_entrada_6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12207847152279)
* + - CPF (C1H\_CPF): Para beneficiários residentes no Brasil (C1H\_CODPAI=000001) apenas Faturas/Documentos Fiscais/Pagamentos cujo Participante possua CPF preenchido serão consideradas.

![R4010_doc_entrada_7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12207907647895)
