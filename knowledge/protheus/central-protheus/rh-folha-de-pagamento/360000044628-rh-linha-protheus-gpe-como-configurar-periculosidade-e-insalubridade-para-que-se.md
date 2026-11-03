---
article_id: 360000044628
category: RH - Folha de Pagamento
content_hash: 7f25c7a88eabcab3123d9129cffb85a82b4cd13829397a495523c25bb5967298
fetched_at: '2026-06-28T22:44:13.344949+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar periculosidade e insalubridade
  para que sejam calculadas pelas horas informadas e não pelas horas do cadastro do
  funcionário
type: support-article
updated_at: '2025-04-23T17:27:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000044628-RH-Linha-Protheus-GPE-Como-configurar-periculosidade-e-insalubridade-para-que-sejam-calculadas-pelas-horas-informadas-e-n%C3%A3o-pelas-horas-do-cadastro-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25992481195287) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como configurar periculosidade e insalubridade para que sejam calculadas pelas horas informadas e não pelas horas do cadastro do funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Na versão 12, a configuração da periculosidade e insalubridade pode ser feita sobre salário ou sobre salário mais verbas.  
A forma como está configurado o mnemônico **P\_SALHDSR** influenciará nos valores calculados.  
Por este motivo, abaixo foram descritos dois cenários, um que mostra como ficará os valores, usando o mnemônico com **.T.** e outro com .F.  
 **1º cenário**  
Periculosidade e/ou insalubridade base salário ou salário verbas com a utilização do mnemônico **P\_SALHDSR**como**.T.**

Cadastro do funcionário com **sim** para periculosidade e/ou insalubridade, quantidade de horas será preenchida automaticamente baseando-se nas horas mensais, não será permitido alterar.  
  
Obs.: para que o cálculo seja executado para o mnemônico com .T., é necessário que o parâmetro MV\_DIASPER esteja com conteúdo 1 ou no cadastro de períodos, aba Cadastro Calendário, estiver com o campo Dias Cálculo com a quantidade de dias do mês.  
![](http://tdn.totvs.com/download/attachments/307848953/image2017-10-24_10-0-17.png?version=1&modificationDate=1508848453000&api=v2)  
  
Cadastro de sindicato aba adicionais preenchido com a Base de Cálculo = salário e percentual  
![](http://tdn.totvs.com/download/attachments/307848953/image2017-10-24_10-5-53.png?version=1&modificationDate=1508848453000&api=v2)  
  
Com a utilização do mnemônico  **P\_SALHDSR**como**.T.** será considerada na verba com Identificador para Cálculo **(ID) 0318** a soma das verbas horas normais (**id 0032**) e horas DSR (**id 0033**) com isso o valor de periculosidade será calculado pelas horas informadas e não pelas horas que estão no cadastro do funcionário.  
  
No cálculo, o sistema somou as verbas horas normais (**Identificador para Cálculo 0032**) e horas DSR (**Identificador para Cálculo 0033**) para realizar o mesmo.  
![](http://tdn.totvs.com/download/attachments/307848953/image2017-10-24_10-8-40.png?version=1&modificationDate=1508848453000&api=v2)  
  
**2º cenário**Cadastro de funcionário e sindicato da mesma forma do primeiro cenário.  
  
Periculosidade e/ou insalubridade base salário ou salário verbas com a utilização do mnemônico **P\_SALHDSR**como**.F.**

**![](http://tdn.totvs.com/download/attachments/307848953/image2017-10-24_10-10-13.png?version=1&modificationDate=1508848453000&api=v2)**  
  
Observe que o cálculo com a utilização do mnemônico  **P\_SALHDSR** como **.F.**será considerada na verba com Identificador para Cálculo 0318 as horas que estão no cadastro do funcionário, desta forma o cálculo da periculosidade será baseada no salário cadastral e não nas horas informadas.  
**![](http://tdn.totvs.com/download/attachments/307848953/image2017-10-24_10-29-51.png?version=1&modificationDate=1508848453000&api=v2)**  
- As verbas com Identificadores para cálculo **0032** e **0033** não deverão estar com **SIM** para periculosidade pois o sistema considera a verba com id p/ cálculo **0318** para cálculo da periculosidade sobre salário.

**Saiba mais**

[RH - Linha Protheus - GPE - Pagamento da Periculosidade Integral no mês da Admissão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018668311-RH-Linha-Protheus-GPE-Pagamento-da-Periculosidade-Integral-no-m%C3%AAs-da-Admiss%C3%A3o?source=search)  
[RH - Linha Protheus - GPE - Como configurar o cálculo da insalubridade sobre salário mínimo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052920234-RH-Linha-Protheus-GPE-Como-configurar-o-c%C3%A1lculo-da-insalubridade-sobre-sal%C3%A1rio-m%C3%ADnimo?source=search)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
