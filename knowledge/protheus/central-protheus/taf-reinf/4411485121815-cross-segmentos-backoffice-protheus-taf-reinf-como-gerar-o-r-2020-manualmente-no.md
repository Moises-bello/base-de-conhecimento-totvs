---
article_id: 4411485121815
category: TAF - REINF
content_hash: 226b3f8c8d6faf34c872758c130d7d26e457402bfb7864f02adc73d4e0c8ec9f
fetched_at: '2026-06-28T22:41:33.681181+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como Gerar o R-2020 manualmente
  no TAF
type: support-article
updated_at: '2024-07-12T14:16:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411485121815-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-Gerar-o-R-2020-manualmente-no-TAF
---

**Dúvida**Quais são os campos necessários para apuração e transmissão do R-2020 no TAF.

**Ambiente**A partir de 12.1.23  
  
**Solução**

**Critérios para gerar o evento R-2020 no TAF.**

**R-2020 - Retenção Contribuição Previdenciária - Serviços Prestados**

* Documentos Fiscais
  + Capa do documento
    - Dt Emissão (C20\_DTDOC): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão do Documento Fiscal;
    - Oper. (C20\_INDOPE): Para que o Documento Fiscal seja considerado, seu Tipo de Operação deverá corresponder a uma Emissão (Saída);
  + Produtos/Serviços
    - Tipo Repasse (C30\_TPREPA): Apenas Itens de Documentos Fiscais cujo campo Tipo Repasse esteja em branco serão considerados;
    - Tipo Serviço (C30\_IDTSER): Para que o Item do Documento Fiscal seja considerado, o Tipo Serviço deverá possuir conteúdo válido, que corresponda a um código da tabela C8C - Serviço Sujeito à Retenção de Contribuição Previdenciária;
  + Tributos do Item
    - Tributo (C35\_CODTRI): Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código 13-Previdência serão considerados.

* Participantes
  + Assoc Despor (C1H\_INDDES): Apenas Faturas/Documentos Fiscais cujo Participante não corresponda à uma Associação Desportiva serão consideradas;
  + CNPJ (C1H\_CNPJ): Apenas Faturas/Documentos Fiscais cujo Participante possua CNPJ preenchido serão consideradas

* + - * Faturas -> **Somente considerar essa opção para lançamento de fatura avulsa**.
        + Capa da Fatura
          - Natureza (LEM\_NATTIT): Apenas serão consideradas Faturas com Natureza = 1 - A Receber;
          - Dt Emissão (LEM\_DTEMIS): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão da fatura;
          - Doc Original (LEM\_DOCORI): Apenas Faturas que não possuam vínculo com documento fiscal serão consideradas, ou seja, apenas Faturas com o campo Doc. Original em branco.
        + Tipo de Serviço
          - Tipo Serviço (T5M\_IDTSER): Para que a fatura seja considerada, o Tipo Serviço deverá possuir conteúdo válido, que corresponda a um código da tabela C8C - Serviço Sujeito à Retenção de Contribuição Previdenciária;
          - Tipo Repasse (T5M\_TPREPA): Apenas faturas cujo campo Tipo Repasse esteja em branco serão consideradas;
          - Vl Base INSS (T5M\_BSINSS): Para que a fatura seja considerada, ela deve possuir o campo Vl Base INSS com conteúdo maior do que zero.

* + - * + Participantes
          - Assoc Despor (C1H\_INDDES): Apenas Faturas/Documentos Fiscais cujo Participante não corresponda à uma Associação Desportiva serão consideradas;
          - CNPJ (C1H\_CNPJ): Apenas Faturas/Documentos Fiscais cujo Participante possua CNPJ preenchido serão consideradas.
