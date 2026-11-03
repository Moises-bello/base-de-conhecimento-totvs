---
article_id: 360052344573
category: RH - Definições de Cálculo
content_hash: a2204a1f03c6856a29148bde1fe12550fd0810d8a747e66f7187d052bc3d3449
fetched_at: '2026-06-28T22:43:22.594015+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Verba não Cadastrada para Formula -> S_CALACONF
  - Cálculo Adicional Cargo de Confiança
type: support-article
updated_at: '2024-02-20T17:24:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052344573-RH-Linha-Protheus-GPE-Verba-n%C3%A3o-Cadastrada-para-Formula-S-CALACONF-C%C3%A1lculo-Adicional-Cargo-de-Confian%C3%A7a
---

**Dúvida**Ao calcular a folha é apresentado um Log com a mensagem: **"Verba não Cadastrada para Formula -> S\_CALACONF - Cálculo Adicional Cargo Confiança  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081569934)****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução:**A mensagem é apresentada quando o sistema está validando que deverá ser efetuado um cálculo de adicional de confiança para alguma matricula, porém não contem a verba com Id 0984 cadastrada em seu cadastro de verbas  
  
1) Acesse **Atualizações-> Definições de Cálculo -> Verbas** e consulte se já existe verba cadastrada.  
  
2) Em caso negativo, efetue o cadastro de uma verba e configure os campos:

**Tipo Cod**. (RV\_TIPOCOD): 1 - Provento;

**Tipo Verba** (RV\_TIPO): V (Valor);

**Percentual** (RV\_PERC): Informe 100;

**Id.p/Cálculo** (RV\_CODFOL): Informe o código 0984 - Adicional para Cargo de Confiança.  
  
3) Após esse cadastro, refaça o cálculo da folha de pagamento.
