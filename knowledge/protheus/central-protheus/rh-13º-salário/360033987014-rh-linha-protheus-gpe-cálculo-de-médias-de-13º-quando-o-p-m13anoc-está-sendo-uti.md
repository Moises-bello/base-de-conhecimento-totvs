---
article_id: 360033987014
category: RH - 13º salário
content_hash: 1cb5205bddd09ce9b5c5d1ddbddb754fa6830191e222f86f5095ee1dfb564a02
fetched_at: '2026-06-28T22:44:00.466605+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Médias de 13º quando o P_M13ANOC está
  sendo utilizado
type: support-article
updated_at: '2026-06-26T19:16:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033987014-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-M%C3%A9dias-de-13%C2%BA-quando-o-P-M13ANOC-est%C3%A1-sendo-utilizado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18739937764631) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Como funciona o cálculo de médias de 13º Salário, quando o **P\_M13ANOC (antigo MV\_M13ANOC)** está sendo utilizado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O mnemônico P\_M13ANOC (antigo MV\_M13ANOC) define se a composição de médias de 13º salário irá considerar apenas os **meses do ano corrente ou também do ano anterior.**

Preenchimento do mnemônico P\_M13ANOC   
**Atualizações/ Definições de Cálculo/ Mnemônicos:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18739931727639)

Com **"1" - Sim** , segue a configuração tradicional, média de décimo terceiro salário deve considerar **somente as verbas no ano corrente.**  
Com **"2" - Não**,a rotina verificará a quantidade de meses indicada no cadastro da verba ou no cadastro do sindicato sem levar em conta se está buscando a verba no ano anterior à data de referência.

**Exemplo:**

* **P\_M13ANOC com "1"**Foram considerados apenas o **ano corrente,** ou seja, de **01/2025 a 12/2025.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34494967516311)

* **P\_M13ANOC com "2"**  
  No cadastro das verbas, o campo "Media 13º" está informado 12 (últimos 12 meses), portanto foi considerado o período de **12/2024** a **11/2025.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34494967519511)  
  
  
Para **Rescisão,** configurando o mnemônico **P\_M13ANOC****com o conteúdo "2" - Não**, obtém-se os seguintes resultados:

**Quantidade de meses para média, definido no Cadastro de Sindicatos.**  
Se houver uma rescisão no mês de fevereiro/2025, e se forem definidos os três últimos meses para média (campo "Meses Méd. 1º", na pasta "Médias"), o sistema localiza as verbas para média nos meses de Novembro/2024, Dezembro/2024 e Janeiro/2025.

**Quantidade de meses para média, definido no Cadastro de Verbas.**Se houver uma rescisão no mês de fevereiro/2025, e se forem definidos os seis últimos meses para média numa determinada verba (campo "Médias 13º", na pasta "Médias"), o sistema localiza as verbas para médias dos meses de Agosto/2024, Setembro/2024, Outubro/2024, Novembro/2024, Dezembro/2024 e Janeiro/2025.  
  
**Obs:** Este mnemônico/parâmetro só terá efeito quando o mnemônico **P\_MEDDIREN** ou parâmetro **MV\_MEDDIRE** estiver como "**N**".

**Saiba Mais**  
[RH - Linha Protheus - GPE - Parâmetros e Mnemônicos utilizados para o cálculo de Média](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7011337477015-RH-Linha-Protheus-GPE-Par%C3%A2metros-e-Mnem%C3%B4nicos-utilizados-para-o-c%C3%A1lculo-de-M%C3%A9dia)  
[RH - Linha Protheus - GPE - Como funciona o calculo de médias de 13º na provisão quando o MV\_M13ANOC esta sendo utilizado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX5dqiAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDkzNjg3MDAzMTEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZnVuY2lvbmEtby1jYWxjdWxvLWRlLW0lQzMlQTlkaWFzLWRlLTEzJUMyJUJBLW5hLXByb3ZpcyVDMyVBM28tcXVhbmRvLW8tTVYtTTEzQU5PQy1lc3RhLXNlbmRvLXV0aWxpemFkbwY7CFQ6DnNlYXJjaF9pZEkiKTE5NjNiMjkzLTcyY2YtNGIwYS05MzRlLTQ5MmYyNTU4MmY5MAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD01WX00xM0FOT0MGOwhUOhJyZXN1bHRzX2NvdW50aQIkBQ%3D%3D--db95d0d7e0b1b31ce7f18de933920cb749259806)
