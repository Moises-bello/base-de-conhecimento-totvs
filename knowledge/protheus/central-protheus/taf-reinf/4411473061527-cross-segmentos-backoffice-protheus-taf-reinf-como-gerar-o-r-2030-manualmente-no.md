---
article_id: 4411473061527
category: TAF - REINF
content_hash: ac0a20f4d514f0e94a3f75cf42a483b60af1730fa03ce8b2c9c0fd092ee5723e
fetched_at: '2026-06-28T22:41:33.685551+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como Gerar o R-2030 manualmente
  no TAF
type: support-article
updated_at: '2023-03-31T17:12:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411473061527-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-Gerar-o-R-2030-manualmente-no-TAF
---

**Dúvida**Quais são os campos necessários para apuração e transmissão do R-2030 no TAF.

**Ambiente**A partir de 12.1.23  
  
**Solução**

**Critérios para gerar o evento R-2030 no TAF.**

**R-2030 - Recursos Recebidos por Associação Desportiva**

* Documentos Fiscais
  + Capa do documento
    - Dt Emissão (C20\_DTDOC): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão do Documento Fiscal;
    - Oper. (C20\_INDOPE): Para que o Documento Fiscal seja considerado, seu Tipo de Operação deverá corresponder a uma Emissão (Saída);
  + Produtos/Serviços
    - Tipo Repasse (C30\_TPREPA): Apenas Itens de Documentos Fiscais cujo campo Tipo Repasse esteja preenchido serão consideradas;
    - Tipo Serviço (C30\_IDTSER): Para que o Item do Documento Fiscal seja considerado, o Tipo Serviço deverá possuir conteúdo válido, que corresponda a um código da tabela C8C - Serviço Sujeito à Retenção de Contribuição Previdenciária;
  + Tributos do Item
    - Tributo (C35\_CODTRI): Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código 13-Previdência serão considerados.
  + Faturas
    - Capa da Fatura
      * Natureza (LEM\_NATTIT): Apenas serão consideradas Faturas com Natureza = 1 - A Receber;
      * Dt Emissão (LEM\_DTEMIS): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão da fatura;
      * Doc Original (LEM\_DOCORI): Apenas Faturas que não possuam vínculo com documento fiscal serão consideradas, ou seja, apenas Faturas com o campo Doc. Original em branco.
    - Tipo de Serviço
      * Tipo Repasse (T5M\_TPREPA): Apenas faturas cujo campo Tipo Repasse esteja preenchido serão consideradas;
      * Vl Base INSS (T5M\_BSINSS): Para que a fatura seja considerada, ela deve possuir o campo Vl Base INSS com conteúdo maior do que zero.
      * Apur. Ret. (T5M\_VLREAP): Para que a fatura seja considerada, ela deve possuir o campo Vlr da retenção de contribuição previdenciária maior do que zero.
      * Valor Bruto (T5M\_VLBRUT): Para que a fatura seja considerada, ela deve possuir o campo Valor Bruto maior que zero.
    - Participantes
      * CNPJ (C1H\_CNPJ): Apenas Faturas/Documentos Fiscais cujo Participante possua CNPJ preenchido serão consideradas.
    - **Importante**
    - Conforme parecer da consultoria tributária, é possível realizar a apuração do R-2030 e R-2040 pela data de baixa das faturas.

* Foi criado o parâmetro [MV\_TAFRECD](https://tdn.totvs.com/pages/releaseview.action?pageId=619383177)que define se a apuração desses eventos será pela data da emissão da fatura e nota fiscal ou pela data da(s) baixa(s) das fatura(s).
