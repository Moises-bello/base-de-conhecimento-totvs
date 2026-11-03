---
article_id: 115010342088
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: d462adcb1844704633b279ee996cb7ac52b24ca494bab6a51b1ea7964f32a9c2
fetched_at: '2026-06-28T22:39:51.005787+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Como gerar uma
  NF de Complementar de ICMS para uma Despesa de Acessória
type: support-article
updated_at: '2021-08-19T12:33:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010342088-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-gerar-uma-NF-de-Complementar-de-ICMS-para-uma-Despesa-de-Acess%C3%B3ria
---

**Dúvida**Como gerar uma Nota Fiscal Complementar de ICMS para uma Despesa Acessória?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.

**Solução**

Quando a despesa for**complemento de ICMS,** cadastrar da seguinte forma:

1. Acesse SIGAEIC - Atualizações - Financeiro - Cadastro de despesas - selecione incluir

- Campo YB\_BASECUSS - Base de custo = SIM

- Campo YB\_BASEIMP - Base de imposto = NÃO

- Campo YB\_BASEICM - Base de ICMS = SIM

- Campo YB\_ICMS\_XX na NFT = SIM e informar o UF na aba ICMS UF para o estado do Importador.

Existe um parâmetro que define se será calculado ICMS na nota complementar, o mesmo deve estar habilitado: MV\_ICMSNFC.

Para gerar a nota complementar, realizar o seguinte procedimento:

2. Acessar SIGAEIC na rotina Desembaraço -> Manutenção -> Posicionar no processo a ser gerada a nota complementar, clicar em ações relacionadas -> Despesa, informar a despesa base de custo e confirmar.

3. Acessar SIGAEIC na rotina de Desembaraço -> Recebimento de Importação, posicionar no processo -> Clicar em ações relacionadas -> Complementar.

**Classificação do Documento de Entrada**

No módulo de Compras (SIGACOM) acesse Atualizações/Movimento/Doc.Entrada.

1. Selecione a nota fiscal.
2. No Browser das notas fiscais, clique no botão classificar.
3. É obrigatório também informar os campos “Tipo Entrada” e “Cod. Fiscal”.
4. Clique no botão OK para finalizar.

**Transmissão da Nota para SEFAZ**

No módulo de Faturamento (SIGAFAT) acesse Atualizações/Nf-e e NF-s/Nf-e Sefaz.

       a) Transmissão, selecione 1-NF-e.

       b) Tipo de Nfe - 2 -Entrada.

       c) Filtra? 2 -Sem filtro

       d) Serie da nota fiscal e selecione - OK

2. Selecione Outras Ações - Transmissão, informe o número da Nota Fiscal e selecione Avançar e a Nota Fiscal será transmitida.
