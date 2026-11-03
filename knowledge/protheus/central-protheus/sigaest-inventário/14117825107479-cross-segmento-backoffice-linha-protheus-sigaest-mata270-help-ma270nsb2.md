---
article_id: 14117825107479
category: SIGAEST - INVENTÁRIO
content_hash: b6a3ccf4a3da5f884c412e005ff11fea5d6c4cf7cba005ee320082458296f863
fetched_at: '2026-06-28T22:38:50.337851+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA270 - HELP MA270NSB2
type: support-article
updated_at: '2026-01-26T15:03:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14117825107479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA270-HELP-MA270NSB2
---

Na rotina Digitação do Inventário (MATA270) do TOTVS Protheus, para evitar o erro HELP MA270NSB2 ao incluir um registro, deve-se pressionar F12 na tela de inclusão e alterar o parâmetro "Valida existência do produto" para "Não". Alternativamente, incluir um saldo inicial zerado na rotina Saldos Iniciais (MATA220) no armazém correspondente também resolve o problema.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37937798227735) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Na rotina **Digitação do Inventário (MATA270)** ao tentar incluir um registro apresenta o **HELP MA270NSB2,** como proceder para continuar a Digitação?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14118045658647)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**  
Para **não** exibir o **HELP MA270NSB2**, voltar a tela de inclusão da Digitação do Inventário e pressionar a tecla F12, em seguida altere o *parâmetro F12* **'Valida existência do produto'** para **'Não'**, veja exemplo no print abaixo.

Também é possível, incluir um **Saldo inicial zerado** na rotina de **Saldos Iniciais (MATA220)** no Armazém que esta tentando inventariar, após essa inclusão, não apresentará o Help novamente.

![](https://totvssuporte.zendesk.com/attachments/token/bJUYEHOL7gBo0wtywabYC8Bip/?name=image.png)

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre INVENTÁRIOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)

[SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)
