---
article_id: 19638124257303
category: TAF - REINF
content_hash: b467350340fea9d9fc84c7049341ded8ff476aed0d2885a9e660d450a763cb1f
fetched_at: '2026-06-28T22:41:34.707548+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Lentidão Painel Reinf
type: support-article
updated_at: '2023-12-12T19:41:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19638124257303-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Lentid%C3%A3o-Painel-Reinf
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19638111908375) Tempo aproximado para leitura: 00:05:00 min****Ocorrência**

Ao acessar o painel Reinf, ocorre uma lentidão no relatório de conferências ou no monitor de eventos.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19638095786647)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATAF - Todas as versões  
  
**Causa**Esse problema ocorre por diversos fatores como:

* Falta de atualização no ambiente TAF
* Utilização simultânea de duas configurações, MPP - Porta Multiprotocolo e *REST.*
* Configuração incorreta da chave ***Maxstringsize***

**Solução**

**Passo 1-** Para resolver essa questão, verifique se o ambiente está utilizando duas configurações simultaneamente, ou seja, se está empregando a Porta Multiprotocolo e o *REST* ao mesmo tempo. Acesse o arquivo appserver.ini para verificar a configuração utilizada. Após esse passo, acesse a tabela **SX6** e confira se os parâmetros **MV\_BACKEND** e **MV\_GCTPURL** estão preenchidos.

É fundamental ressaltar que o *REST* e a  MPP são configurações distintas para acessar o **Painel Reinf**. Recomendamos  não utilizar ambas as configurações simultaneamente, pois isso pode acarretar problemas no **Painel Reinf**.

Nossa sugestão é utilizar a configuração Porta Multiprotocolo, que é a configuração mais atualizada do **Painel Reinf,** e excluir o conteúdo dos parâmetros informados anteriormente.

**Passo 2**-  Acesse o appserver.ini  localize a chave ***Maxstringsize*** e verifique se está no formato padrão conforme o exemplo abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19638108010135)

**Passo 3-** Após efetuar todas as correções mencionadas anteriormente, certifique-se de que o seu ambiente está atualizado de acordo com os últimos pacotes do TAF disponíveis no link abaixo:

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Atualização Completa Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-Reinf?source=search)
