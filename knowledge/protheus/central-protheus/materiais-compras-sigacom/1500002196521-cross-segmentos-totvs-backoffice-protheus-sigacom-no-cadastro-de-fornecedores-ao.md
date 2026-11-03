---
article_id: 1500002196521
category: Materiais - Compras (SIGACOM)
content_hash: 7e7d84318276486a4b13f7016aafce6bc7694dac7262bc7dfed77a4f70faf60b
fetched_at: '2026-06-28T22:41:21.919015+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - No cadastro de Fornecedores,
  ao mudar o Tipo "A2_TIPO" para F=Fisico, a Máscara do campo "A2_CGC" não muda para
  CPF
type: support-article
updated_at: '2023-01-23T10:42:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002196521-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-No-cadastro-de-Fornecedores-ao-mudar-o-Tipo-A2-TIPO-para-F-Fisico-a-M%C3%A1scara-do-campo-A2-CGC-n%C3%A3o-muda-para-CPF
---

**Dúvida**Porque a máscara do campo **A2\_CGC** continua como CNPJ sendo que o campo **A2\_TIPO** é **F=Físico** no cadastro de ***Fornecedores (MATA020)*** ?

**Ambiente**  
Protheus – Compras – A partir da versão 11.80

**Solução**A máscara do campo não é alterada pois existe uma validação especifica para fornecedores de São Paulo e Minas Gerais:

**Validação:**

*PICPES(IIf((M->A2\_INDRUR <> "0" .And. M->A2\_EST $ "SP|MG" .And. M->A2\_TIPO == "F"), "J", M->A2\_TIPO )*  
  
Ou seja, para fornecedores de São Paulo ou Minas Gerais utilizarem máscara de **CPF (A2\_CGC)**, é necessário que o campo "**Tipo" (A2\_TIPO)** seja **IGUAL**  a **"F-Fisico"** e **também** o campo **"Ind. Prod. Rur."** **(A2\_INDRUR)** **seja igual** **"0 - Não é prod. Rural"**

***Saiba Mais :°***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
