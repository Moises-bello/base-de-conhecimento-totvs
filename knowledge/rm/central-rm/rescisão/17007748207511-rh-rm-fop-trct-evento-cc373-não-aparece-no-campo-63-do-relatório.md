---
article_id: 17007748207511
category: Rescisão
content_hash: da56fd34f6291cefe2831ccdbcb701ef63906625e0f2d07ded062290965f58c0
fetched_at: '2026-06-28T22:46:54.194220+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: Evento cc373 não aparece no campo 63 do relatório '
type: support-article
updated_at: '2025-02-12T18:06:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17007748207511-RH-RM-FOP-TRCT-Evento-cc373-n%C3%A3o-aparece-no-campo-63-do-relat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17007761939863) Tempo aproximado para leitura: **00:01:51 min****Ocorrência**Ao informar a rubrica do evento de código de cálculo 373 no campo 63 do TRCT, o evento 13º Rescisão Licença Maternidade Provento não é impresso no relatório.  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Causa**Isso ocorre pois de acordo com o layout do TRCT, o campo 63  é reservado para o valor de 13° Salário Proporcional, ou seja, evento de Código de cálculo 48. Veja abaixo: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17007061197591)  
  
**Solução**Para solucionar, deve-se discriminar os valores de cada evento em seu devido campo. Segue orientações:

1. Informe a rubrica do evento de Código de Cálculo 373 no campo 95. O campo 95 é destinado para outras verbas de provento, ou seja, caso já tenha uma rubrica informada no campo 95, **é permitido a inclusão de mais de uma rubrica** caso necessário.

Verifique o exemplo a seguir: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17007356608919)

Funcionamento do campo 95: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17007604026519)  
  
2. Caso queira, para o evento de Código de Cálculo 48, você poderá preencher um código de rubrica no cadastro do evento e vincular a rubrica no campo 63 do relatório.

3. Desta forma será descriminado o valor de 13° salário proporcional no campo 63 e o valor de 13° Rescisão Licença Maternidade Provento no campo 95. 

**Saiba Mais:**

[RH - RM - FOP - TRCT: parametrização do código de rubricas em eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003040531-RH-RM-FOP-TRCT-parametriza%C3%A7%C3%A3o-do-c%C3%B3digo-de-rubricas-em-eventos)

[RH - RM - FOP - Parametrização Folha de Pagamento - Emissão TRCT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411690878103-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-Folha-de-Pagamento-Emiss%C3%A3o-TRCT)
