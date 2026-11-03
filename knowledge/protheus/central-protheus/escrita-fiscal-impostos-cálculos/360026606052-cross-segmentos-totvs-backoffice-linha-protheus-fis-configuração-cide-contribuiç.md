---
article_id: 360026606052
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 747b90177afc825abb05e68832a4e96eda643497bb78eafc8d4c1f800b83c5dc
fetched_at: '2026-06-28T22:39:30.689057+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configuração CIDE
  – Contribuição de Intervenção no Domínio Econômico
type: support-article
updated_at: '2024-05-07T18:22:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026606052-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-CIDE-Contribui%C3%A7%C3%A3o-de-Interven%C3%A7%C3%A3o-no-Dom%C3%ADnio-Econ%C3%B4mico
---

**Dúvida**

Como configurar cálculo do CIDE?

**Ambiente**

Protheus – Fiscal – A partir da versão 12.1.17  
  
**Solução:**

**Procedimento para Configuração**

1. Acesse o **Cadastro de Fornecedores**(MATA020), inclua ou altere no cadastro de um Fornecedor. Na pasta **Outros**, o campo **Recolhe CIDE**deve ser preenchido com **Sim**, que corresponde à aplicabilidade do CIDE.  
2. Acesse o **Cadastro de Naturezas**(FINA010), inclua ou altere um cadastro de Naturezas definindo:

* O campo **ED\_CALCCID**como **SIM**.

* O campo **ED\_BASECID**deve ser definido caso exista Base de Cálculo para o Imposto

* O campo **ED\_PERCCIDE**também deve ser definido, pois se refere ao percentual a ser utilizado no cálculo.

3. Acesse o **Cadastro de Fornecedores**(MATA020), e defina a natureza cadastrada/alterada no cadastro do fornecedor.

**Procedimento para Utilização**

1. Acesse a rotina de **Documentos de Entrada***(*MATA103*)*, e efetue uma compra com o Fornecedor configurado anteriormente. É necessário que a TES utilizada esteja configurada para Gerar Duplicatas (F4\_DUPLIC). Ao salvar a Nota Fiscal, será gerado um título no Contas a Pagar referente à Compra e outro Título referente ao Valor do CIDE e vai possuir o Tipo CIDE.

Boletim técnico:

<https://tdn.totvs.com/pages/viewpage.action?pageId=642623799>
