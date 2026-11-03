---
content_hash: 5d5a9274c497503989161033de1cb4dd00b248e2fe8bae419ea123277958abe0
fetched_at: '2026-06-29T00:09:23.061686+00:00'
page_id: '422546040'
product: rm
source: tdn-rm
title: Monitor SEFAZ NFC-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Monitor+SEFAZ+NFC-e
version: 2
---

Este processo é utilizado para informar ao contribuinte se sua SEFAZ está operando normalmente. É aconselhável que ele seja executado sempre imediatamente antes das notas serem enviadas, pois este [web service](https://pt.wikipedia.org/wiki/Web_service) disponibilizado pelo ambiente da NFC-e informa o estado da SEFAZ e sugere a entrada em contingência ou não.

Veja abaixo uma mensagem de retorno para uma UF onde o serviço estava fora do ar ao ser consultada.  
*"Nota Fiscal Eletrônica - Modelo 55 Versão da mensagem: 3.10 Mensagem: 999 Erro na SEFAZ: Sugestão: Autorizada operação contingência UF Origem: DF"*

Outra mensagem na execução do processo onde o serviço está em operação:  
*"Nota Fiscal Eletrônica ao Consumidor Final - Modelo 65 Versão da mensagem: 3.10 Mensagem: 107 Serviço em operação Status do serviço: SERVICO EM OPERACAO UF Origem: DF"*

De qualquer forma o contribuinte ainda pode consultar o status de sua SEFAZ e a orientação do uso do serviço substituto no próprio [Portal da NF-e](http://www.nfe.fazenda.gov.br/portal/principal.aspx).  
Este processo só está disponível para a integração com o TSS.
