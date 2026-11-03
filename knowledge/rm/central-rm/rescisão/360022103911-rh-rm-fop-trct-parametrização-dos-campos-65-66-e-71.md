---
article_id: 360022103911
category: Rescisão
content_hash: b37ee1be558932b604ad042c2853cb168fde04f62df509e34ca29c5e31acb632
fetched_at: '2026-06-28T22:46:55.346498+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: Parametrização dos campos 65, 66 e 71'
type: support-article
updated_at: '2026-06-26T14:09:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022103911-RH-RM-FOP-TRCT-Parametriza%C3%A7%C3%A3o-dos-campos-65-66-e-71
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:06:40 min****Dúvida**Como devo parametrizar o sistema para preenchimento dos campos 65, 66 e 71 do TRCT?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os passos abaixo:  
  
Primeiramente é necessário a criação de eventos do tipo **base de cálculo** que possuam códigos de cálculo específicos, e que irão detalhar os valores de **Avos de Férias Indenizadas sobre Aviso**, **Férias Proporcionais** e **Férias Vencidas.** Estes eventos poderão ter as rubricas associadas para terem seus respectivos valores impressos nos campos **71, 65 e 66**.  
  
1. Acesse: **Administração de Pessoal | Eventos | Eventos.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8867569261335/mceclip0.png)**2. Crie o evento com o código de cálculo 329:  
  
**Código de calculo 329 - FÉRIAS INDENIZADAS SOBRE AVISO PREVIO**  
Deve ser do tipo Base de cálculo e do tipo Valor, sem incidência.  
Associar uma rubrica neste evento.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8867618274199/mceclip3.png)  
  
O evento é calculado e lançado automaticamente na rescisão para atender exclusivamente o **campo 71** do TRCT. O valor deste código de cálculo é exatamente o valor correspondente aos avos que foram acrescentadas nos eventos **Férias Indenizadas - código de cálculo 24**, **Férias Proporcionais - código de cálculo 25** e médias devido ao aviso indenizado.  
  
3. Crie o evento com o código de cálculo 330:  
  
**Código de calculo 330 – FÉRIAS PROPORCIONAIS SEM AVISO PRÉVIO INDENIZADO**  
Deve ser do tipo Base de cálculo e do tipo Valor, sem incidência.  
Associar uma rubrica neste evento.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8867625018903/mceclip2.png)  
  
Este é calculado e lançado automaticamente na rescisão para atender exclusivamente o **campo 65** do TRCT. O valor deste código de cálculo é exatamente o valor correspondente aos avos das Férias Proporcionais e médias sem considerar a projeção dos dias do aviso prévio indenizado. Não é valor do **código de cálculo 25-Férias Proporcionais** lançado na rescisão.  
  
4. Crie o evento com o código de cálculo 331:  
  
**Código de calculo 331 – FÉRIAS VENCIDAS SEM AVISO PRÉVIO INDENIZADO**  
Deve ser do tipo Base de cálculo e do tipo Valor, sem incidência.  
Associar uma rubrica neste evento  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8867620426391/mceclip4.png)  
  
Este é calculado e lançado automaticamente na rescisão para atender exclusivamente o **campo 66** do TRCT. O valor deste código de cálculo é exatamente o valor correspondente os avos das Férias Vencidas e médias sem considerar a projeção dos dias do aviso indenizado. Não é exatamente o valor do evento com **código de cálculo 24-Férias Indenizada**.  
  
5. Calcular a rescisão e os eventos criados serão lançados no movimento.  
  
6. Na geração do TRCT, informe as rubricas que foram associadas aos eventos em cada um dos campos 65, 66 e 71 de acordo com a orientação acima.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8867683455383/mceclip5.png)  
  
**Saiba mais**  
Para mais informações, [CLIQUE AQUI](http://tdn.totvs.com/pages/viewpage.action?pageId=36309636).
