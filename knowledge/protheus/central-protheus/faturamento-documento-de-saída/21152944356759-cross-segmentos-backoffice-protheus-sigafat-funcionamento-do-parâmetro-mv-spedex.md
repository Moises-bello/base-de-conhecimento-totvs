---
article_id: 21152944356759
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: c251ebaadae82006cc676ca0e4968c7ac27ae215f10299c9ee425c89c0d4d9e4
fetched_at: '2026-06-28T22:38:44.039978+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Funcionamento do parâmetro
  MV_SPEDEXC no Faturamento
type: support-article
updated_at: '2024-09-07T14:20:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21152944356759-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-SPEDEXC-no-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21152986360471) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Qual o funcionamento do parâmetro MV\_SPEDEXC no Faturamento?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

O parâmetro define se o documento de saída pode ser excluído, com base na configuração de horas especificada

**OBERSVAÇÃO:** O comportamento do MV\_SPEDEXC não é avaliado mesmo, quando há o FATJOBNFE (MV\_CANCNFE = .T.)

Contudo, esse parâmetro só é considerado se as seguintes premissas estiverem preenchidas:

* Campo "Espécie do Documento (F2\_ESPECIE)" da nota fiscal de saída preenchida com "SPED" ou RPS;
* Campo "Data de Autorização (F2\_DAUTNFE)" da nota fiscal de saída preenchido a data;
* Campo "Flag de Imp. (F2\_FIMP)" da nota fiscal de saída preenchido com "T", "S" ou "N";

Com os campos da NF acima preenchidos, o sistema verifica:

Se "F2\_DAUTNFE (Data de auto) - Database" for maior que um dia e for horário de verão (parâmetros "MV\_HVERAOI" e "MV\_HVERAOF") o sistema verifica isso:

* Dias = Data atual - F2\_DAUTNFE (Data de auto)
* Horas = Fuso horário da UF "Estado (M0\_ESTENT)" do sistema - F2\_HAUTNFE (Hora de auto)

**RETORNO**: Horas + (Dias \* Horas)

Se não, o sistema verifica isso:

* Dias = Data atual - "F2\_DAUTNFE (Data de auto)"
* Horas = Hora atual - "F2\_HAUTNFE (Hora de auto)"

**RETORNO**: Horas + (Dias \* 24)

Se o **RETORNO** foi maior que o conteúdo do parâmetro MV\_SPEDEXC (**RETORNO** > MV\_SPEDEXC) a mensagem ocorre:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21153709313815)

Ou seja, para permitir a exclusão ou forçar a exclusão, deve estar de acordo o parâmetro MV\_SPEDEXC, a data/hora de transmissão (F2\_DAUTNFE e F2\_HAUTNFE) ou a data/hora do sistema no momento deve estar no intervalo permitido do prazo de exclusão.

**Dúvidas nos campos "F2\_DAUTNFE (Data de auto)", "F2\_HAUTNFE (Hora de auto)", "F2\_FIMP (Flag de Imp.)"  ou parâmetro "MV\_CANCEXT", contate a Equipe Protheus SPED.**

Conceito de porque MV\_SPEDEXC não é avaliado mesmo, quando há o FATJOBNFE (MV\_CANCNFE = .T.):

* Quando (MV\_CANCNFE = .T.) a SEFAZ irá validar se pode excluir a nota ou não. A própria SEFAZ autorizará ou não a partir do prazo ou outros fatores que impedem a exclusão (nota delegada etc).
* Quando (MV\_CANCNFE = .F.), o parâmetro (MV\_SPEDEXC) é validado e considerado, considerando o tempo informado no parâmetro.

**Saiba mais:**

****[FAT0191 - Job para exclusão documento de saída (MATA521) - FATJOBNFE](https://tdn.totvs.com/x/tr44E)****
