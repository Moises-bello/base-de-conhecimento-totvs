---
article_id: 27049321105687
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: fcb4e80580af8fde2ae97525256bd82ce2501fbab983f61f1e99392d941722eb
fetched_at: '2026-06-28T22:37:49.246211+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Portal do Cliente -
  Download do Boleto não está disponível
type: support-article
updated_at: '2025-06-06T20:54:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27049321105687-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Portal-do-Cliente-Download-do-Boleto-n%C3%A3o-est%C3%A1-dispon%C3%ADvel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27049292560407) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No Portal do Cliente ao tentar realizar a baixa do boleto, apresenta a mensagem

**Download do Boleto não está disponível. Favor entrar em Contato**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27049321082903)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir do release 12.1.2310

**Causa**Este cenário ocorre, devido ao boleto não ter sido gerado pela **API - FINA713** - [Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)  
O boleto gerado, foi criado por meio de customização RDMAKE, ou não foi gerado boleto para este titulo.

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Boletos no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018348051-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Boletos-no-Protheus)  
  
**Solução**Para ativar as opções, existem 3 maneiras.

1º Realize a transmissão do título e utilize a comunicação bancária via **API pelo job FINA713.**

[Webinar Totvs l MP - SIGAFIN - FINA713 - Comunicação bancária](https://www.youtube.com/watch?v=fzc6PCRSFAw)

2º  Via implementação de pontos de entrada, onde o PE deve chamar sua customização de boletos  
[NGFBXBOL -> Permite o download do boleto em PDF dos boletos personalizados, habilitando opção Baixar boleto.](https://tdn.totvs.com/pages/releaseview.action?pageId=692920438)

3º  O cenário pode estar ocorrendo por conta da falta do **arquivo printer.exe**, desta maneira é necessário que o arquivo esteja na pasta do **appserver** aonde roda o **REST** do **Portal do Cliente.**

[TOTVS Printer](https://tdn.totvs.com/display/tec/TOTVS+Printer)

**Importante**

As opções serão desabilitadas quando o **título** estiver **totalmente baixado**, ou seja, com **saldo igual a zero**.

**Saiba mais**  
[Portal do Cliente](https://tdn.totvs.com/display/public/PROT/Portal+do+Cliente)[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Copiar linha digitável, Enviar Boleto por e-mail e Baixar Boleto no Portal do Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11822256827031)
