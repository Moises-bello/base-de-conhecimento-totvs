---
article_id: 4412920416023
category: NFe - Nota Fiscal Eletrônica
content_hash: 250d02132a6283499894c55550f156a1626efde13ce3c1faf66819e607166f39
fetched_at: '2026-06-28T22:40:05.279386+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 745 Rejeição: O
  tipo de transportador não ser informado quando não estiver informado proprietário
  do veículo de tração'
type: support-article
updated_at: '2025-06-18T14:23:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412920416023-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-745-Rejei%C3%A7%C3%A3o-O-tipo-de-transportador-n%C3%A3o-ser-informado-quando-n%C3%A3o-estiver-informado-propriet%C3%A1rio-do-ve%C3%ADculo-de-tra%C3%A7%C3%A3o
---

**Dúvida**Como corrigir a rejeição 745 : O tipo de transportador não ser informado quando não estiver informado proprietário do veículo de tração ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1. Caso o veiculo seja de terceiro ou agregado deve preencher o campo **Frota DA3\_FROVEI = 2 ou 3 Preencher o campo Proprietário DA3\_CODFOR com o código do fornecedor.**

![744_primeiro.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32895964652439)

 2. Caso **tptransp seja TAC** deve preencher o campo **A2\_TIPO como físico**  deve informar o **CPF deste fornecedor no cadastro.**

3. Caso o veiculo seja frota **própria deve preencher Frota "DA3\_FROVEI = 1" e o campo Proprietário DA3\_CODFOR** deixe **em branco.**

![725_rejei__o_2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32895954642967)

4. Após isso, **exclua o MDFe e gere novamente.**

* ***Importante:*** O ambiente deve estar atualizado com os pacotes do link abaixo:

*[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Manifesto de Carga Nota técnica 2021.002](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402644962967)*

* **Validação da Sefaz:**

![745_rejeicao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4412920277911)
