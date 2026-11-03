---
content_hash: 88736e254c1005a44fc812bd41831bf6891cf15430c2dabb092333312b6f5c47
fetched_at: '2026-06-29T00:09:23.068580+00:00'
page_id: '422546042'
product: rm
source: tdn-rm
title: Monitor SEFAZ
type: documentation
url: https://tdn.totvs.com/display/LRM/Monitor+SEFAZ
version: 2
---

Este processo é utilizado para informar ao contribuinte se sua SEFAZ está operando normalmente. É aconselhável que ele seja executado sempre imediatamente antes das notas serem enviadas, pois este [web service](http://pt.wikipedia.org/wiki/Web_service) disponibilizado pelo ambiente da NF-e e informa o estado da SEFAZ e sugere a entrada em contingência ou não. Veja abaixo uma mensagem de retorno para uma UF onde o serviço estava fora do ar ao ser consultada:

*"Nota Fiscal Eletrônica - Modelo 55* *Versão da mensagem: 3.10* *Mensagem: 999 Erro na SEFAZ:* *Sugestão: Autorizada operação contingência* *UF Origem: SP"*

Outra mensagem na execução do processo onde o serviço está em operação:

*"Nota Fiscal Eletrônica ao Consumidor Final - Modelo 55* *Versão da mensagem: 3.10* *Mensagem: 107 Serviço em operação* *Status do serviço: SERVICO EM OPERACAO* *UF Origem: DF"*

De qualquer forma o contribuinte ainda pode consultar o status de sua SEFAZ e a orientação do uso do serviço substituto no próprio [Portal da NF-e](http://www.nfe.fazenda.gov.br/portal/principal.aspx).  
Este processo só está disponível para a integração com o TSS. Quando se usa a integração com o TOTVS Colaboração 2.0 o próprio ambiente já fornece esta informação.
