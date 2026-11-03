---
article_id: 40495614825495
category: Gestão de Transportes (TMS)
content_hash: 4fce3703eefa5bf1e85a61b5f67d7ffe03b6a426c2d109d969618db6956da61e
fetched_at: '2026-06-28T22:45:27.384097+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Campo [viagem.carga.natureza] inválido
type: support-article
updated_at: '2026-05-15T13:53:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40495614825495-Log%C3%ADstica-Linha-Protheus-TMS-Campo-viagem-carga-natureza-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40495614803095) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao integrar o TMS com a Pamcard, ocorre o erro **Campo [viagem.carga.natureza] inválido.**  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**  
A mensagem **Campo [viagem.carga.natureza] inválido** ao integrar com a Pamcard, ocorre se a tag **viagem.carga.natureza** não for enviada ou se o conteúdo da tag for inválido.  
  
**Solução**  
A tag **viagem.carga.natureza** deve ser preenchida com a seguinte regra:

* Se  o **Tipo de carga - DTR\_TIPCRG = 2**, considera a natureza do parâmetro **MV\_PAMNATC.** O conteúdo deste parâmetro deve conter apenas o código da natureza, sem aspas;
* Senão, busca o campo **Tab. Nat. Receita - B1\_TNATREC** do produto do documento transportado - **DTC\_CODPRO**.

Se estes cadastros estiverem conforme a regra citada e ainda assim ocorrer a falha, então, é necessário avaliar os logs da integração com a Pamcard. Para isso, basta habilitar o parâmetro **MV\_TMSXML** para gerar os logs da integração na pasta **/system/.**
