---
article_id: 360013117832
category: Rescisão
content_hash: d231dff65ded7f2b00325c2081bc6e9df5e7c8a7ab2fb310d93ba814ecb187d2
fetched_at: '2026-06-28T22:46:55.421071+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão Complementar: Evento de CC 96 não cadastrado ou inativo
  na coligada'
type: support-article
updated_at: '2025-01-22T18:45:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013117832-RH-RM-FOP-Rescis%C3%A3o-Complementar-Evento-de-CC-96-n%C3%A3o-cadastrado-ou-inativo-na-coligada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao processar uma rescisão complementar o sistema apresenta o seguinte erro: **Evento de CC 96 não cadastrado ou inativo na coligada 'X'**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente pode ocorre devido a três motivos diferentes:  
1. Apenas um evento cadastrado com o Código de Cálculo 96;  
2. Dois eventos cadastrados com o Código de Cálculo 96, mas um deles está inativo;  
3. Dois eventos cadastrados com o Código de Cálculo 96, mas com incidência em INSS Folha iguais.  
  
**Solução**Para que o erro não seja apresentado durante o processo de cálculo da Rescisão Complementar é necessário que efetue o cadastro dos eventos com o código de cálculo 96 sendo que um terá incidência em INSS e o outro não terá incidência em INSS. A parametrização dos dois eventos deverá ser igual, com a exceção do nome e código do evento e da incidência em INSS Folha.  
  
Em primeiro plano, acesse **Administração de Pessoal | Eventos | Eventos** para cadastrar ou alterar os eventos com Código de Cálculo 96. Segue abaixo imagem com a parametrização exemplo de dois eventos sendo que um deles **com** incidência em INSS e o outro **sem** incidência.

* Evento 0116 com código de cálculo 96 e incidência em **INSS Folha** **marcada.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009200331/mceclip2.png)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009162372/mceclip1.png)

* Evento 0246 com código de cálculo 96 e incidência em **INSS Folha** **desmarcada.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009162492/mceclip3.png)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009162332/mceclip0.png)
