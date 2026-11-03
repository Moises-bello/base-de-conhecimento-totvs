---
article_id: 4412880451095
category: MDFe - Manifesto de Carga
content_hash: 25d0afbb315a38d68f639b1e3b97ebb5b67af31531518d9e672bdba9bc7e28ba
fetched_at: '2026-06-28T22:40:08.254522+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - 744 Rejeição:
  O tipo de transportador deve ser ETC ou CTE quando informado CNPJ do proprietário
  do veículo de tração'
type: support-article
updated_at: '2025-06-17T17:53:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412880451095-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-744-Rejei%C3%A7%C3%A3o-O-tipo-de-transportador-deve-ser-ETC-ou-CTE-quando-informado-CNPJ-do-propriet%C3%A1rio-do-ve%C3%ADculo-de-tra%C3%A7%C3%A3o
---

**Dúvida**Como corrigir a Rejeição 744 : O tipo de transportador deve ser ETC ou CTE quando informado CNPJ do proprietário do veículo de tração ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

Se modal rodoviário e informado ***CNPJ do proprietário do veículo de tração:***   
A informação do tipo de transportador ***(tpTransp) deverá ser preenchida com ETC (1) ou CTC (3).***

 1. Realize atualização da patch e do **RDMAKE do MDFSEFAZ do link abaixo:**

*[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)*

2. Realize alteração abaixo no **cadastro do Veiculo e fornecedor:**ETC - Empresa de Transporte de Cargas  
Os campos que diferem para o sistema o tipo de transportadora, neste caso para um ETC, são:  
Frota **(DA3\_FROVEI): 2 Terceiro ou 3 - Agregado**  
Proprietário **(DA3\_CODFOR): Fornecedor do tipo pessoa física - Tipo (A2\_TIPO): J - Jurídico**

**![744_primeiro.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412880291351)**

3. Proprietário do veiculo **(Fornecedores - SA2)** como pessoa jurídica: **Tipo (A2\_TIPO): J - Jurídico**

**![744_2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412898893463)**

**Ou**

4. CTC- Cooperativa de Transporte de Cargas  
Os campos que diferem para o sistema o tipo de transportadora, neste caso para um CTC, são:  
**Frota (DA3\_FROVEI): 2 - Terceiro ou 3 - Agregado**

![744_primeiro.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412880291351)

5. Proprietário **(DA3\_CODFOR): Fornecedor do tipo pessoa física - Tipo (A2\_TIPO): X - Outros**

Proprietário do veiculo **(Fornecedores - SA2) como pessoa jurídica: Tipo (A2\_TIPO): X - Outros**

![744_3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412880424599)

6. Após isso, **exclua o MDFe e gere novamente.**

* **Validação da Sefaz:**

**![744_rejei__o.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4412879862551)**
