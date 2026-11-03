---
article_id: 4411472910871
category: TAF - REINF
content_hash: 67c1c831f3189721ce445d54cba0e706d0843e2cb187b803464f436e345b91b1
fetched_at: '2026-06-28T22:41:33.675344+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como Gerar o R-2010 manualmente
  no TAF
type: support-article
updated_at: '2024-06-21T15:00:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411472910871-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-Gerar-o-R-2010-manualmente-no-TAF
---

**Dúvida**Quais são os campos necessários para apuração e transmissão do R-2010 no TAF.

**Ambiente**A partir de 12.1.23  
  
**Solução**

**Critérios para gerar o evento R-2010 no TAF.**

**R-2010 - Retenção Contribuição Previdenciária - Serviços Tomados**

* Documentos Fiscais
  + Capa do documento
    - Dt Emissão (C20\_DTDOC): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão do Documento Fiscal;
    - Oper. (C20\_INDOPE): Para que o Documento Fiscal seja considerado, seu Tipo de Operação deverá corresponder a uma Aquisição (Entrada);
  + Produtos/Serviços
    - Tipo Repasse (C30\_TPREPA): Apenas Itens de Documentos Fiscais cujo campo Tipo Repasse esteja em branco serão considerados;
    - Tipo Serviço (C30\_IDTSER): Para que o Item do Documento Fiscal seja considerado, o Tipo Serviço deverá possuir conteúdo válido, que corresponda a um código da tabela C8C - Serviço Sujeito à Retenção de Contribuição Previdenciária;
  + Tributos do Item
    - Tributo (C35\_CODTRI): Apenas documentos que possuam Tributos do Item cujo código de Tributo corresponda ao código 13-Previdência serão considerados.

* Participantes
  + Assoc Despor (C1H\_INDDES): Apenas Faturas/Documentos Fiscais cujo Participante não corresponda à uma Associação Desportiva serão consideradas;
  + CNPJ (C1H\_CNPJ): Apenas Faturas/Documentos Fiscais cujo Participante possua CNPJ preenchido serão consideradas.

**Importante:** Deve ser lançado somente um tipo de documento, caso a geração do evento seja por nota não deve ser lançada fatura.

* + Faturas
    - Capa da Fatura
      * Natureza (LEM\_NATTIT): Apenas serão consideradas Faturas com Natureza = 0 - A Pagar;
      * Dt Emissão (LEM\_DTEMIS): O mês/ano selecionado para apuração deve corresponder ao mês/ano da data de emissão da fatura;
      * Doc Original (LEM\_DOCORI): Apenas Faturas que não possuam vínculo com documento fiscal serão consideradas, ou seja, apenas Faturas com o campo Doc. Original em branco serão consideradas pela apuração.
    - Tipo de Serviço
      * Tipo Serviço (T5M\_IDTSER): Para que a fatura seja considerada, o Tipo Serviço deverá possuir conteúdo válido, que corresponda a um código da tabela C8C - Serviço Sujeito à Retenção de Contribuição Previdenciária;
      * Tipo Repasse (T5M\_TPREPA): Apenas faturas cujo campo Tipo Repasse esteja em branco serão consideradas;
      * Vl Base INSS (T5M\_BSINSS): Para que a fatura seja considerada, ela deve possuir o campo Vl Base INSS com conteúdo maior do que zero.

* + - * + - Participantes
            * Assoc Despor (C1H\_INDDES): Apenas Faturas/Documentos Fiscais cujo Participante não corresponda à uma Associação Desportiva serão consideradas;
            * CNPJ (C1H\_CNPJ): Apenas Faturas/Documentos Fiscais cujo Participante possua CNPJ preenchido serão consideradas.
