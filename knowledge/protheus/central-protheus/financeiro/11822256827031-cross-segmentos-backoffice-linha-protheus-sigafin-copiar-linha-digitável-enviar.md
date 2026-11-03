---
article_id: 11822256827031
category: Financeiro
content_hash: de83a6f4d1d36f75c2c547cf8a22a16cde85471bffd9cb33164f7ac811816253
fetched_at: '2026-06-28T22:38:02.888346+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Copiar linha digitável,
  Enviar Boleto por e-mail e Baixar Boleto no Portal do Cliente
type: support-article
updated_at: '2024-02-09T14:12:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11822256827031-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Copiar-linha-digit%C3%A1vel-Enviar-Boleto-por-e-mail-e-Baixar-Boleto-no-Portal-do-Cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21240252413719) Tempo aproximado para leitura: **00:06:00 min****Dúvida**Como Copiar linha digitável, Enviar Boleto por e-mail e Baixar Boleto no Portal do Cliente?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da Release 12.1.33  
  
  
**Solução**

No **Portal do Cliente** existem 3 opções abaixo:

* Copiar linha digitável
* Enviar Boleto por e-mail
* Baixar Boleto

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11822167717655)

Quando criamos o título, sem utilizar comunicação bancária via API pelo job **FINA713**, o mesmo irá apresentar no portal, porém ficará bloqueado as opções.

Para ativar as opções, exitem 2 maneiras.

1º Opção: Realizar a transmissão do título utilizando a comunicação bancária via API pelo job **FINA713.**

2º Opção: Via implementação de pontos de entrada

[NGFBXBOL](https://tdn.totvs.com/pages/viewpage.action?pageId=619130482) -> Permite o download do boleto em PDF dos boletos personalizados, habilitando opção **Baixar boleto.**

[NGFEMBOL](https://tdn.totvs.com/pages/viewpage.action?pageId=692917157) -> Permite o envio de e-mail com boletos personalizados, habilitando a opção **Enviar boleto por e-mail.**

**Importante:** As opções estarão desabilitadas caso o título esteja totalmente baixado, ou seja, seu saldo é igual à 0.

**Saiba mais:**  
[Portal do Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=718992131#tabs-relatorios_downloads)
