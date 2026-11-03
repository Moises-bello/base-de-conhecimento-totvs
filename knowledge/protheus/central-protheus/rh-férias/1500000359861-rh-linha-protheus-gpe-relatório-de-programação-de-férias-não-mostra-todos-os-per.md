---
article_id: 1500000359861
category: RH - Férias
content_hash: 050ee3d03cbe1fe36abec81a0bd6d0c976a78fb740db16332b73e9464cfa1337
fetched_at: '2026-06-28T22:43:59.204025+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de Programação de Férias não mostra todos
  os períodos e dias proporcionais em aberto do funcionário
type: support-article
updated_at: '2025-05-12T11:27:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000359861-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Programa%C3%A7%C3%A3o-de-F%C3%A9rias-n%C3%A3o-mostra-todos-os-per%C3%ADodos-e-dias-proporcionais-em-aberto-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32036602333591) Tempo aproximado para leitura: **00:02:00 min**  
**Ocorrência**Feita emissão do GER400 - Relatório de Programação de Férias - Sistema não apresentou todos os período aquisitivos abertos e seus respectivos dias ainda não gozados pelo funcionário.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Isso acontece devido ao intervalo do período informado nos campos **Pergunta 09 : Programadas de ?** e **Programadas ate ?**. Quando o funcionário já teve alguma programação de férias antes e esta não está dentro deste período informado, o Sistema não demonstra o saldo de dias restante para ele.  
  
**Solução**Para que o relatório demonstre este **período aquisitivo anterior,** é necessário informar período que **abrange todas** as **programações** dele.

**Exemplo**  
Funcionário tem **período aquisitivo** de 05/02/2019 até 04/02/2020 aberto, sendo que em **15/06/2020** teve uma **programação** de férias de 15/06/2020 até 28/06/2020 sendo 14 dias de férias e 10 dias de abono pecuniário.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101500693)

Nesta situação é necessário informar na **Pergunta 09 : Programadas de ?** uma data anterior a esta programação, assim o Sistema irá demonstrar os dias restantes deste período aquisitivo.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000401462)  
  
**Saiba Mais**[RH - Linha Protheus - GPE - Relatório de Programação de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036866153-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Programa%C3%A7%C3%A3o-de-F%C3%A9rias)  
[RH - Linha Protheus - GPE - Relação Programação de Férias em planilha (GPER400)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053560653-RH-Linha-Protheus-GPE-Rela%C3%A7%C3%A3o-Programa%C3%A7%C3%A3o-de-F%C3%A9rias-em-planilha-GPER400)  
[RH - Linha Protheus - GPE - Como gerar o relatório de programação férias com o quantidades de avos proporcional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052426913-RH-Linha-Protheus-GPE-Como-gerar-o-relat%C3%B3rio-de-programa%C3%A7%C3%A3o-f%C3%A9rias-com-o-quantidades-de-avos-proporcional)
