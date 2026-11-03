---
article_id: 360020113451
category: RH - Férias
content_hash: 60d910a049751111449df6094ac1b3026b710acdf62384b4912250b1c2136cf3
fetched_at: '2026-06-28T22:43:58.176106+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como não calcular férias em dobro quando o colaborador
  tem afastamento dentro do período concessivo
type: support-article
updated_at: '2026-02-03T20:23:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020113451-RH-Linha-Protheus-GPE-Como-n%C3%A3o-calcular-f%C3%A9rias-em-dobro-quando-o-colaborador-tem-afastamento-dentro-do-per%C3%ADodo-concessivo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26837297555095) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**  
Afastamento no Período Concessivo - Férias em Dobro - **MV\_SUSPCON**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
O sistema possui o parâmetro **MV\_SUSPCON**, que permite suspender ou não a contagem do período concessivo durante o afastamento.  
Existem casos em que o empregado se afasta por **motivo de doença ou acidente de trabalho**, durante o período concessivo, havendo a possibilidade do empregador não ter tempo hábil para pré-avisar o empregado sobre o gozo de suas férias.  
Tal ocorrência pode resultar em dúvida se os dias que ultrapassem a data limite para concessão das férias devem ser pagas em dobro. Em alguns casos o empregador entende que o período concessivo mantém-se inalterado, ou seja, deve haver o pagamento em dobro, enquanto para outros, sua contagem deve ser suspensa durante o afastamento (independente se ocorreu no inicio ou fim do período concessivo).  
Para que o Sistema atenda as diferentes posições mencionadas acima, o novo parâmetro deve ser configurado com as seguintes opções:  
  
**MV\_SUSPCON:**  
Caso configure com conteúdo .T. (conteúdo padrão), vazio ou o parâmetro não exista, o período concessivo permanece suspenso pelo tempo que durar o afastamento por doença ou acidente de trabalho. Nessa situação, o período concessivo se prolonga conforme os dias afastados. Somente os dias de férias posteriores ao fim do novo período serão pagos em dobro.  
  
Caso configure o parâmetro com conteúdo .F., a contagem do período concessivo mantém-se inalterada, ocorrendo o pagamento em dobro dos dias de férias que ultrapassarem a data limite para o período concessivo.  
  
Exemplo:  
Período concessivo: 08/03/11 a 07/03/12  
Período de gozo: 01/03/12 a 20/03/12  
Empregado com afastamento durante o período concessivo: Tipo ‘P’ de 01/12/11 a 18/01/12

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015817172)

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015817252)

Exemplo 1 de parametrização - MV\_SUSPCON= .T.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26837280500247)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26837280502551)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26837297564567)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26837297573143)

Exemplo 2 de parametrização = MV\_SUSPCON= .F.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26837297575959)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26837297591063)

**Observações:**  
  
**-**O parâmetro **MV\_SUSPCON** somente se aplica à apuração dos dias de férias para pagamento em dobro.  
Em nenhuma situação este parâmetro influencia na alteração do período concessivo ou aquisitivo.

-Foi criado o mnemônico **P\_SUSPMAT** caso a empregada tenha afastamento por licença maternidade durante o período concessivo, será suspenso e estendido por prazo idêntico ao do afastamento. O uso do mnemônico **P\_SUSPMAT**deve ser em conjunto do parâmetro **MV\_SUSPCON**, ou seja, para suspender os dias da licença maternidade no período concessivo o **MV\_SUSPCON**também deverá estar ativo.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Quando o Funcionário tem direito a Férias em dobro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018129572-RH-Linha-Protheus-GPE-Quando-o-Funcion%C3%A1rio-tem-direito-a-F%C3%A9rias-em-dobro)  
[RH - Linha Protheus - GPE - Como parametrizar Workflow para notificação automática de Férias em dobro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034157334-RH-Linha-Protheus-GPE-Como-parametrizar-Workflow-para-notifica%C3%A7%C3%A3o-autom%C3%A1tica-de-F%C3%A9rias-em-dobro)  
[RH - Linha Protheus - GPE - Cálculo de Férias em Dobro para funcionária Afastada por Licença Maternidade no Período Concessivo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024729993-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-F%C3%A9rias-em-Dobro-para-funcion%C3%A1ria-Afastada-por-Licen%C3%A7a-Maternidade-no-Per%C3%ADodo-Concessivo)
