---
article_id: 4413304874647
category: RH - Definições de Cálculo
content_hash: 079af55c116b765e65c23068bf3fcd8d24ecfcbcc00f40477ca512be71a25059
fetched_at: '2026-06-28T22:43:22.230317+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE -  Criação do ID 1879 para dedução do salário família
  calculado na rescisão original
type: support-article
updated_at: '2026-06-26T16:39:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413304874647-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-do-ID-1879-para-dedu%C3%A7%C3%A3o-do-sal%C3%A1rio-fam%C3%ADlia-calculado-na-rescis%C3%A3o-original
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34420294060823) Tempo aproximado para leitura: 00:01:00 min** **Dúvida**Criação do ID 1879 para dedução do salário família calculado na rescisão original.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Erro: Caso na rescisão original tenha sido calculado salário família e na rescisão complementar no mesmo mês não seja mais calculado devido o salário reajustado ultrapassar o salário limite para geração do benefício, apesar dos valores calculados na rescisão estarem corretos, a base de cálculo do e-Social fica incorreta pois não é efetuado a dedução do salário família gerado na rescisão original.  
  
**Ajuste** para o cálculo de rescisão complementar no mesmo mês da original no caso em que na rescisão original havia sido efetuado pagamento de salário família e na complementar não há mais o direito ao benefício devido reajuste salarial, para que o valor do salário família pago na rescisão original seja gerado na verba do **ID 1879**.  
  
**Observação**Sugere-se que a verba vinculada ao **ID de cálculo 1879** deve ser cadastrada com o **tipo Base Desconto** e **deve possuir as mesmas incidências de e-Social da verba do ID 0034.****Mas**, caso haja entendimento que o valor de salário família pago anteriormente na rescisão original, apesar de ser devido naquele momento, deve ser descontado do funcionário, uma vez que com o salário novo não há mais direito ao benefício, então a verba deverá ser cadastrada como Desconto.

**Saiba Mais**  
Mantenha o sistema atualizado para que os novos identificadores fiquem disponíveis para cadastro: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao_continua>
