---
article_id: 360058758834
category: RH - 13º salário
content_hash: 99b9bb2c3623751b199d5fe819e171c9423ee7d364ada457819d8d0be964f0b5
fetched_at: '2026-06-28T22:44:01.653227+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Verba não cadastrada para a fórmula -> S_CALCPERI
type: support-article
updated_at: '2026-06-25T18:46:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058758834-RH-Linha-Protheus-GPE-Verba-n%C3%A3o-cadastrada-para-a-f%C3%B3rmula-S-CALCPERI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18727524788759) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Ao executar algum cálculo no sistema é gerado  a mensagem: Verba não cadastrada para a fórmula -> S\_CALCPERI

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10269356650775)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois no cadastro de verbas não existe algum dos identificadores de cálculo de periculosidade, que são verificados pela fórmula **S\_CALCPERI.**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse: **Atualizações / Definições de Cálculo / Verbas (GPEA040);**  
2. Faça uma busca pelos identificadores de cálculo abaixo:  
  
0036 - Periculosidade  
1290 - Periculosidade 13º Salário   
1300 - Periculosidade Férias Mês  
1440 - Periculosidade 13º Salário Maternidade  
1632 - Periculosidade 13º Salário 1ª parcela  
1643 - Periculosidade 13º Salário Maternidade 1ª Parcela  
1927 - Periculosidade 13º Lic. Adoção 1ª Parcela  
1939 - Periculosidade 13º Lic. Adoção   
  
3. Caso não encontre algum deles, cadastre a verba como **Provento**, com **tipo Valor**, exceto as verbas com Ids **1927** e **1939**, que devem ser incluídas como **Base Provento**.  
Após realizar o cadastro execute novamente o cálculo onde não será mais gerada a mensagem.  
  
**Importante:** Caso tenha o cadastro de verbas (Tabela SRV) **exclusiva,** verifique se há todas as verbas para **todas as filiais.**

**Saiba Mais**[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Sistema não calcula para alguns funcionários 1ª parcela do 13º salario, Pela EndCalc() - S\_ADT13PGT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgyKwHUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzOTEzMTk1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtU2lzdGVtYS1uJUMzJUEzby1jYWxjdWxhLXBhcmEtYWxndW5zLWZ1bmNpb24lQzMlQTFyaW9zLTElQzIlQUEtcGFyY2VsYS1kby0xMyVDMiVCQS1zYWxhcmlvLVBlbGEtRW5kQ2FsYy1TLUFEVDEzUEdUBjsIVDoOc2VhcmNoX2lkSSIpOTA1YmRlMDUtZDQ3ZC00YzAxLWJmNzItMjM4NTM1MzIzMmUzBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIBg1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBTaXN0ZW1hIG7Do28gY2FsY3VsYSBwYXJhIGFsZ3VucyBmdW5jaW9uw6FyaW9zIDHCqiBwYXJjZWxhIGRvIDEzwrogc2FsYXJpbywgUGVsYSBFbmRDYWxjKCkgLSBTX0FEVDEzUEdUBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--0ea4261a1e34c660eba2fc00cba35f222b5fd859)  
[RH - Linha Protheus - GPE - Cálculo de 13º não efetuado - Calculo Finalizado Pela FinalCalc() ou Pela EndCalc() - S\_CAINSAL](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjd2qnUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBwmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDE4Njk3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQyVDMyVBMWxjdWxvLWRlLTEzJUMyJUJBLW4lQzMlQTNvLWVmZXR1YWRvLUNhbGN1bG8tRmluYWxpemFkby1QZWxhLUZpbmFsQ2FsYy1vdS1QZWxhLUVuZENhbGMtUy1DQUlOU0FMBjsIVDoOc2VhcmNoX2lkSSIpNjM0NmRkN2QtNDdhZC00ZmEwLWE3ZTQtODM1NjA4NWVlNzhkBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIBflJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDw6FsY3VsbyBkZSAxM8K6IG7Do28gZWZldHVhZG8gLSBDYWxjdWxvIEZpbmFsaXphZG8gUGVsYSBGaW5hbENhbGMoKSBvdSBQZWxhIEVuZENhbGMoKSAtIFNfQ0FJTlNBTAY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--34a95998f10cea8bfbfa81eb2ab95e73c00206c4)
