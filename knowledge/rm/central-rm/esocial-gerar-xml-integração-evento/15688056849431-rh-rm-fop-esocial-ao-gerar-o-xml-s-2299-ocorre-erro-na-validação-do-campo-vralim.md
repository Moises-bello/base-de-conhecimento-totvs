---
article_id: 15688056849431
category: eSocial - Gerar XML/ Integração Evento
content_hash: a47362b666b4cfcdeec77bda9d4a7c83be8959330428c8d23804060ae3711040
fetched_at: '2026-06-28T22:47:11.953755+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao gerar o XML S-2299 ocorre erro na validação do
  campo ''vrAlim'': Valor deve ser maior que zero'
type: support-article
updated_at: '2024-12-30T15:44:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15688056849431-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-2299-ocorre-erro-na-valida%C3%A7%C3%A3o-do-campo-vrAlim-Valor-deve-ser-maior-que-zero
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15688042836119) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o XML de desligamento S-2299, para casos que há dependentes cadastrados, ocorre **erro na validação do campo 'vrAlim': Valor deve ser maior que zero.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15687015572631)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse erro ocorre pois para o trabalhador em questão há dependentes cadastrados com incidência em pensão. De acordo com o leiaute, se for informado pensão alimentícia igual a 2 ou 3 é necessário que o valor da pensão seja maior que 0.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15687136592279)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Identifique se o dependente do trabalhador possui **Incidência em Pensão**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15687534373655)

2. Caso possua, identifique a necessidade do envio ou não do valor da pensão alimentícia.

2.1. Caso seja necessário o envio, acesse o **Cadastro da Pensão Alimentícia - Anexo - Movimentação da Pensão de Dependentes**, crie uma movimentação e informe os dados necessários;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15687877708951)

2.2. Caso não seja necessário o envio das informações da pensão, informe em **Dados da Pensão a Data Fim do Desconto.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15687951684503)

**Saiba mais**  
Para mais informações, acesse:

[RH - RM - FOP - Cadastro de dependentes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4570859149847-RH-RM-FOP-Cadastro-de-dependentes)
