---
article_id: 115010342148
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: bfb602f90283545b327675970df5b0dab9090353abff76f7437ce0f9080769f4
fetched_at: '2026-06-28T22:39:51.408300+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Rejeição de Transmissão
  - XML sem DI
type: support-article
updated_at: '2021-08-19T12:23:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010342148-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Rejei%C3%A7%C3%A3o-de-Transmiss%C3%A3o-XML-sem-DI
---

**Dúvida**

Como corrigir a Rejeição de Transmissão - XML sem DI?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.

**Solução**

Sequencia 001 – Geração da Nota Fiscal Complementar de IPI e ICMS no SIGACOM:

1. No módulo de Compras (SIGACOM) acesse Atualizações/Movimento/Doc.Entrada.
2. No Browser das notas fiscais, clique no botão Incluir
3. O sistema irá exibir a tela de inclusão de Documento de Entrada do módulo SIGACOM para que possa ser inclusa a Nota Fiscal Complementar de IPI e ICMS.
   1. Observe as importantes premissas para inclusão desta Nota de forma que a mesma possa relacionar nos dados de envio à SEFAZ os dados da DI do processo ao qual a mesta será vinculada:
4. Na capa da Nota:

   a)       No campo “Tipo da Nota” deverá ser informado o valor “Compl. ICMS”

   b)       No campo “Form. Prop.” deverá ser informado com o valor “Sim”

   c)       No campo “Fornecedor” deverá ser informado o fornecedor do processo de desembaraço (mesmo fornecedor relacionado nas Notas Fiscais de Entrada gerada para este processo de desembaraço)

   Nos itens da Nota:

   d)       No campo “Produto” deve ser informado sempre um produto que esteja no processo de desembaraço para o qual há nota fiscal de entrada gerada

   e)       Para cada produto, será necessário clicar no botão “Ações relacionadas > Origem” e associar o item da Nota Fiscal de Entrada do processo de desembaraço referente, afim que de que o sistema preencha automaticamente os campos “Docto. Orig.”, “Serie Orig.” e “It.Doc Orig” associando o item da Nota Fiscal Complementar de ICMS ao item da Nota Fiscal de Entrada do Processo de desembaraço.

   f)       É obrigatório também informar os campos “Vlr.Unitario”, “Vlr.Total”, “Tp.Oper”, “Tipo Entrada” e “Cod. Fiscal”.

   g)       Ao final da informação dos dados uma tela semelhante à tela a seguir será exibida:
5. Clique no botão Confirmar. Será exigida uma numeração de Nota para a inclusão.  
   ADMIN
6. Clique no botão OK para finalizar

Sequencia 002 – Transmissão da Nota para SEFAZ

1. No módulo de Faturamento (SIGAFAT) acesse Atualizações/Nf-e e NF-s/Nf-e Sefaz.

       a)Transmissão, selecione 1-NF-e.

       b)Tipo de Nfe - 2 -Entrada.

       c) Filtra? 2 -Sem filtro

       d)Serie da nota fiscal e selecione - OK

2. Selecione Outras Ações - Transmissão, informe o número da Nota Fiscal e selecione Avançar e a Nota Fiscal será transmitida.

**Saiba mais**

[Nota Fiscal Complementar de IPI e ICMS](https://tdn.totvs.com/display/public/PROT/Nota+Fiscal+Complementar+de+IPI+e+ICMS)
