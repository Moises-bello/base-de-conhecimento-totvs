---
article_id: 360034429593
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 0e558d85eed642f2165ad9c40d9a79c4aea672210f8d34bc8c2e7848e0532231
fetched_at: '2026-06-28T22:39:36.827601+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Incluir despesas
  acessórias, seguro e frete na base de cálculo do PIS/COFINS.
type: support-article
updated_at: '2021-06-29T12:24:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034429593-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Incluir-despesas-acess%C3%B3rias-seguro-e-frete-na-base-de-c%C3%A1lculo-do-PIS-COFINS
---

**Dúvida** Tratamento para as despesas acessórias, seguro e frete serem incluídos na base dos impostos **PIS/COFINS.**  
**Ambiente**  
Protheus – Sigafis – A partir da versão 12.1.17

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Abra o parâmetro MV\_FRTBASE pelo configurador;  
2. Altere para  :

* **T:** Soma as despesas acessórias (seguro, frete e etc) na Base de PIS e COFINS.
* **F:** Desconsidera as despesas acessórias (seguro, frete e etc) da base de PIS e COFINS.

* A validação do parâmetro ocorre em conjunto com o preenchimento dos campos**Desp Ac Cof** (F4\_DESPCOF) e **Desp Ac Pis** (F4\_DESPPIS), localizados no cadastro de TES

3. Configure o TES ;

4. Alterando os campos Desp Ac Pis (F4\_DESPPIS), Desp Ac Cof (F4\_DESPCOF) para :

* **Sim:**Indica que o valor das despesas acessórias (seguro, frete e etc) será agregado na base de PIS/COFINS**.**
* **Não:**Indica que o valor das despesas acessórias (seguro, frete e etc) não será agregado na base de PIS/COFINS**.**

**Obs: O Parâmetro MV\_FRTBASE será usado para operações de Entrada e Saída.**
