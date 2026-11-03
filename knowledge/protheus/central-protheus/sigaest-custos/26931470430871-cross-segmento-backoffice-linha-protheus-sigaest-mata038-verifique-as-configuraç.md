---
article_id: 26931470430871
category: SIGAEST - CUSTOS
content_hash: 0fdfe62c92b58bccefa22d08b1fa63adca4a972f58b1b6eaafef7ef7994caf06
fetched_at: '2026-06-28T22:39:02.031961+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Verifique
  as configurações do calendário contábil
type: support-article
updated_at: '2026-06-25T14:17:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26931470430871-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Verifique-as-configura%C3%A7%C3%B5es-do-calend%C3%A1rio-cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26931470391575) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Durante o processo de fechamento ou reabertura do periodo, ocorre o HELP **Verifique as configurações do calendário contábil**, como ajustar para efetuar o fechamento ou reabertura do periodo?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33.  
  
**Solução**  
Antes de tudo, voce tem licença para uso do modulo SIGACTB? caso não tenha, siga esse boletim:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Sem licença ao modulo SIGACTB como fechar o estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/41297339022359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Sem-licen%C3%A7a-ao-modulo-SIGACTB-como-fechar-o-estoque)

O Help informado durante a etapa de fechamento ou reabertura, indica a necessidade de avaliação dos "processos" dentro do calendario contabil, algum processo como por exemplo EST esta com o periodo bloqueado ou fechado, e ele precisa constar como "Aberto" para contabilizar ou efetuar a reabertura do periodo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26931475865879)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26931475875607)

Precisa validar o calendario contabil, algum periodo letivo esta com bloqueio nos processos, para efetuar a reabertura ou fechamento, voce precisa deixar o periodo do processo em aberto:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26931475877911)

Após abrir o periodo, basta refazer o processo novamente de fechamento ou reabertura, não há necessidade de sair da rotina.

**A filial em questão é nova e esse foi o primeiro fechamento de estoque:**

Se voce acabou de efetuar o fechamento da filial, onde ela não tem periodos anteriores, e esse fechamento foi efetuado com contabilização. quando voce tentar efetuar a reabertura do periodo, o HELP também vai ser apresentado, porque o sistema não tem referencia de um "Calendario contabil Historico anterior", a data Histórica se da no calendario existente sistemico de 1997/01/01, então caso voce esteja nessa situação, basta criar um calendario desse periodo para referencia da reabertura do periodo que acabou de ser encerrado.

**OBS:** A Reabertura de do PERIODO, **não efetiva nenhuma tratativa na contabilidade,** então não altera nada na contabilidade, apenas é exigido a validação do calendario pois, quando se faz a reabertura, normalmente é para efetuar novas movimentações no periodo, então fica a critério se você quer "Efetuar uma nova contabilização" dos movimentos ou não, para o fechamento do mesmo posteriormente.

**Duvidas sobre o calendario contabil, consulte a Faq do time Contabil:**

[Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA010 - Calendário contábil bloqueado ou fechado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006722952-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA010-Calend%C3%A1rio-cont%C3%A1bil-bloqueado-ou-fechado)

**Saiba mais**:

[*Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)
