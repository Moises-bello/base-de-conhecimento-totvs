---
article_id: 4411485224983
category: TAF - REINF
content_hash: 6fa108e7e7d087165ca754aa89079628dba65efd66ed45b40714be62096adf94
fetched_at: '2026-06-28T22:41:33.689962+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como Gerar o R-2040 manualmente
  no TAF
type: support-article
updated_at: '2024-02-22T11:21:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411485224983-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-Gerar-o-R-2040-manualmente-no-TAF
---

**Dúvida**Quais são os campos necessários para apuração e transmissão do R-2040 no TAF.

**Ambiente**A partir de 12.1.23  
  
**Solução**

**Critérios para gerar o evento R-2040 no TAF.**

**R-2040 - Recursos Repassados para Associação Desportiva**

* Documentos Fiscais
  + Capa do documento
    - Dt Emissão (C20\_DTDOC): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão do Documento Fiscal;
    - Oper. (C20\_INDOPE): Para que o Documento Fiscal seja considerado, seu Tipo de Operação deverá corresponder a uma Entrada;
  + Produtos/Serviços
    - Tipo Repasse (C30\_TPREPA): Apenas Itens de Documentos Fiscais cujo campo Tipo Repasse esteja preenchido serão consideradas;
    - Tipo Serviço (C30\_IDTSER): Para que o Item do Documento Fiscal seja considerado, o Tipo Serviço deverá possuir conteúdo válido, que corresponda a um código da tabela C8C - Serviço Sujeito à Retenção de Contribuição Previdenciária;
  + Tributos do Item
    - Tributo (C35\_CODTRI): Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código 13-Previdência serão considerados.

Em caso de lançamento por Fatura

  Capa da Fatura

* Natureza (LEM\_NATTIT): Apenas serão consideradas Faturas com Natureza = 0 - A Pagar;
* Dt Emissão (LEM\_DTEMIS): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão da fatura;
* Doc Original (LEM\_DOCORI): Apenas Faturas que não possuam vínculo com documento fiscal serão consideradas, ou seja, apenas Faturas com o campo Doc. Original em branco.

* + Tipo de Serviço
    - Tipo Repasse (T5M\_TPREPA): Apenas faturas cujo campo Tipo Repasse esteja preenchido serão consideradas;
    - Vl Base INSS (T5M\_BSINSS): Para que a fatura seja considerada, ela deve possuir o campo Vl Base INSS com conteúdo maior do que zero.
    - Apur. Ret. (T5M\_VLREAP): Para que a fatura seja considerada, ela deve possuir o campo Vlr da retenção de contribuição previdenciária maior do que zero.
    - Valor Bruto (T5M\_VLBRUT): Para que a fatura seja considerada, ela deve possuir o campo Valor Bruto maior que zero.
  + Participantes
    - Assoc Despor (C1H\_INDDES): Apenas Faturas/Documentos Fiscais cujo Participante correspondam à uma Associação Desportiva serão consideradas;
    - CNPJ (C1H\_CNPJ): Apenas Faturas/Documentos Fiscais cujo Participante possua CNPJ preenchido serão consideradas.

**Importante**

Conforme parecer da consultoria tributária, é possível realizar a apuração do R-2030 e R-2040 pela data de baixa das faturas.

Foi criado o parâmetro [MV\_TAFRECD](https://tdn.totvs.com/pages/releaseview.action?pageId=619383177) que define se a apuração desses eventos será pela data da emissão da fatura e nota fiscal ou pela data da(s) baixa(s) das fatura(s).
