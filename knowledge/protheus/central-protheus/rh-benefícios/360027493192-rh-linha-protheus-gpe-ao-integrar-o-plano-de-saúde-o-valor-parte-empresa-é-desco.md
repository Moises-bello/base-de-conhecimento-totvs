---
article_id: 360027493192
category: RH - Benefícios
content_hash: 47e62cf173e6d1b478777d2ab1ef61776128a7d9899e3934ac307bf94ff8c762
fetched_at: '2026-06-28T22:44:03.475600+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Ao integrar o Plano de Saúde, o valor parte empresa
  é descontado do empregado indevidamente
type: support-article
updated_at: '2025-09-12T14:00:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027493192-RH-Linha-Protheus-GPE-Ao-integrar-o-Plano-de-Sa%C3%BAde-o-valor-parte-empresa-%C3%A9-descontado-do-empregado-indevidamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29535889622935) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao integrar o Plano de Saúde, o sistema apresenta os valores de desconto do empregado e da Parte Empresa apenas na verba de desconto, gerando um valor indevido.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

1. Acessar em **Atualizações> Definições de cálculo> Manutenção de tabela (GPEA320)**, Tabela **S016,** verifique se os campos **Vb. Emp. Ass. Med. Tit.** , **Vb. Emp. Ass. Med. Dep.** , **Vb. Emp. Ass. Med. Agr.** estão preenchidos com as verbas de **Base Empresa** e se não são as mesmas que foram informadas na rotina de Planos Ativos: ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29535889630231)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027417932)

Na tabela de Fornecedores S016, devem ser informadas as verbas de **parte empresa** que podem ser **vinculadas a id's** ou **cadastradas sem id's.**

**- 0213 -** Base parte Empresa Assist. Medica**;****- 0725 -** Base parte Empresa Ass. Medica Dependentes;  
**- 0726 -** Base parte Empresa Ass. Medica Agregados.

**2.** Após o ajuste cancele a Integração do Roteiro PLA em **Miscelânea> Cálculos> Integrações (GPEM019):**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29535889632919)**

**3.** Calcule novamente o plano de saúde em **Atualizações> Benefícios> Planos de saúde> Cálculos Plano de Saúde:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29535906170007)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29535889643287)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29535906182039)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29535906190487)**

**6.** Emita o relatório de conferência em **Atualizações> Benefícios> Relatório de cálculo (GPER008).**

**7.** Faça a integração com a folha em **Atualizações> Benefícios> Integração com a folha (GPEM019).**

**Saiba Mais**[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXEfwyNQo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjIzNjA0OTI0Njk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tZGUtc2ElQzMlQkFkZQY7CFQ6DnNlYXJjaF9pZEkiKTM2NGY4ODFiLTJlOTMtNGQwYi05ZTIyLWE3ZTA1ZWE1MGZjZQY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGXJvdGluYSBwbGFub3MgYXRpdm9zBjsIVDoScmVzdWx0c19jb3VudGkCDwE%3D--563db3d7534365debbcb04a5eed8f49023bdb1b8)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXoi9HOgo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBr2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjQ1NDE4Njg0OTUxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tb2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIikzNjRmODgxYi0yZTkzLTRkMGItOWUyMi1hN2UwNWVhNTBmY2UGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhlyb3RpbmEgcGxhbm9zIGF0aXZvcwY7CFQ6EnJlc3VsdHNfY291bnRpAg8B--3afa7c06a73d5c5bab82666b49de5144334986da)
