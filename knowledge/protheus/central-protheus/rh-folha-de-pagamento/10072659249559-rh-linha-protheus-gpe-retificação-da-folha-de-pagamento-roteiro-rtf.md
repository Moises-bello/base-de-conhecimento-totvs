---
article_id: 10072659249559
category: RH - Folha de Pagamento
content_hash: eb0bd37b37cf02e5b7b86dcef0e393095312e5acc348b417779d638a688df6b2
fetched_at: '2026-06-28T22:44:16.295882+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Retificação da folha de Pagamento - Roteiro RTF
type: support-article
updated_at: '2026-04-06T17:01:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10072659249559-RH-Linha-Protheus-GPE-Retifica%C3%A7%C3%A3o-da-folha-de-Pagamento-Roteiro-RTF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23230559192471) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como realizar cálculo de retificação da folha de pagamento como IR, INSS, FGTS e outros valores?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**  
  
O roteiro **"RTF"** tem como objetivo promover a **correção** de Folhas de Pagamento já encerradas, no que se refere a **incluir** verbas que não foram pagas na época correta.

A execução do roteiro prevê o cálculo de verbas vinculadas a ID´s específicos e **diferença** de **INSS,** mediante o **lançamento da diferença** por parte do usuário.

Cálculos realizados pelo roteiro:

* Verba **informada** pelo usuário
* Recálculo do **INSS** - segurado
* Recálculo do **FGTS**
* INSS - **Parte** da **empresa** (Terceiros, SAT, Patronal, etc)
* Cálculo do **Líquido** a ser gerado na folha corrente
* Base de Cálculo do **IRRF;**

O valor a receber pelo funcionário deverá transitar pela folha em **aberto,** para que a retenção de **IRRF** seja feita corretamente **no mês** que será **paga** a **diferença,** pois para fins de Imposto de Renda sempre devemos considerar a data do **fato gerador.**Desta forma, o valor recolhido entrará como referência do mês **calculado,** e não com referência ao mês que estão retificando.

Para que seja feito corretamente a retififcação, siga os seguintes passos:  
  
1) Crie **verbas** com os **identificadores** de calculo **1658, 1659** e **1660** conforme instruções abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10069711971735)

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467839964311)

2) Adicione períodos referente as competências que serão retificadas com número de **pagamento 02.** Pode ser um ou mais períodos (neste caso será feita retificação de março até dezembro de 2024).  
  
No exemplo, temos dois períodos de pagamento referente a cada mês que será retificado de 2024: um com número de pagamento **01** que permanece com status **Fechado** e com os roteiros que estavam cadastrados na época que foram calculados, e outro com número de pagamento **02** que estará em status **Aberto** e apenas com o roteiro **RTF** cadastrado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467846497303)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467846498327)

A **data de pagamento** do roteiro **RTF deve ser** a **data de pagamento da folha aberta,** que neste caso é **01/2025,** sendo seu pagamento em **05/02/2025.**  
  
***![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467846499095)***  
  
**Lembrando*****:*** O roteiro RTF **somente** deverá ser cadastrado quando houver necessidade de calcular a retificação de um período que já foi **fechado.**

3) Para calcular cada mês do roteiro RTF, deve ser lançada a verba que quer retificar e informar a data de referência dentro do mês da retificado. No exemplo demonstrado, foi feito lançamento da verba 210 de Horas Extra 100% .  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467839968919)  
  
Verba lançada:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467839970199)  
  
4) Consulta de Calculado do roteiro RTF:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467839971607)  
  
5) Depois dos períodos com **RTF calculados** e **integrados** na folha atual, **todos** os registros serão levados para **RGB** através dos id's de cálculo **1659** e **1660.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467839974935)

No cálculo da **folha** do **mês atual aberto** (01/2025), os valores do RTF são **demonstrados** também.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467839975447)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467839976343)

Memória de cálculo do Imposto de Renda:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467839977111)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467846507159)

**Diferença de INSS**  
A **base** de **cálculo** considera as verbas que foram **pagas** na **folha** que já foi **fechada** e estes são **recalculados** quando a verba **lançada** no **RTF** possui estas **incidências.** No exemplo acima foi recalculado **Imposto de Renda,** mas o **INSS** e **FGTS** não, pois ela **não** tinha incidência para eles.  
  
Para recálculo do **INSS,** o Sistema usa a seguinte fórmula:  
Base de INSS folha fechada + verbas com sim para INSS lançadas no RTF = Base INSS folha aberta.  
Com este valor, é aplicada a tabela progressiva do ano corrente referente ao período aberto e deduzido o valor de INSS já recolhido na folha fechada.  
  
**Observações**  
 Verifique no recibo de pagamento que o líquido do roteiro **RTF** ficará zerado, pois foi gerado a verba de ID **1658** com o mesmo valor do líquido.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31467839978647)

Após cálculo da folha, o fechamento do roteiro **RTF** poderá ser realizado através da rotina de Cálculos por Roteiros (GPEM020) ou Cálculos Múltiplos (GPEM020A).

**Saiba mais:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=567744061>

[RH - Linha Protheus - GPE - Ao calcular roteiro RTF o cálculo é finalizado na fórmula S\_VLDPDRTF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19368148908439-RH-Linha-Protheus-GPE-Ao-calcular-roteiro-RTF-o-c%C3%A1lculo-%C3%A9-finalizado-na-f%C3%B3rmula-S-VLDPDRTF?source=search)

[RH - Linha Protheus - GPE - Cálculo de dissídio para roteiro RTF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14327779138455-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-diss%C3%ADdio-para-roteiro-RTF?source=search)
