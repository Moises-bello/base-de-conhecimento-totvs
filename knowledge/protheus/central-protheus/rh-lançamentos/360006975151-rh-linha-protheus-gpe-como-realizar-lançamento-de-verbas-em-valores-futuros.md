---
article_id: 360006975151
category: RH - Lançamentos
content_hash: 05974469bfd4babf62e5de1556bf3219102c5894a2534dff8140d50e3fd35574
fetched_at: '2026-06-28T22:43:31.243593+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar lançamento de verbas em Valores Futuros
type: support-article
updated_at: '2025-07-23T18:08:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006975151-RH-Linha-Protheus-GPE-Como-realizar-lan%C3%A7amento-de-verbas-em-Valores-Futuros
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26241831185303)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como efetuar o lançamento de verbas em Valores Futuros?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Será demonstrado abaixo a funcionalidade da rotina de**GPEA110**disponível em **Atualizações > Lançamentos > Valores Futuros**, porém, será utilizado como **exemplo** a verba de **empréstimo** que será lançada **automaticamente** após o cálculo da Folha.

**1 .** Acesse a rotina **GPEA110 - Atualizações > Lançamentos > Valores Futuros,** selecione o funcionário em questão e clique na opção **incluir.****Observação:**

* **Antes** de gerar o cálculo da folha e preencha os parâmetros de **valores futuros,** verifique se a verba que será utilizada para o **desconto,** está devidamente criada.

* Nesta rotina você tem a possibilidade de utilizar o campo **Nr. Parcelas**, para dividir o valor informar no campo**Vlr. Principal**, por exemplo:

Informando **Vlr Principal** 1.000,00 e no campo **Nr. Parcelas 10**, automaticamente o sistema trará como resultado 100,00 no campo **Vr. Parcela,**sem que seja informada uma linha para cada parcela.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26241831188759)  
  
A data do Próximo vencimento é preenchida automaticamente pelo Sistema de acordo com o período aberto da folha em **Atualizações > Definições de Cálculo > Períodos**.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26241831191063)

Caso o desconto tenha de ser realizado em **período posterior**, este campo pode ser **editado.**  
  
O campo Data do Movimento refere-se a data em que está sendo feita inclusão do registro.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26241840413463)  
  
  
Para que possamos **direcionar o desconto da parcela**, seja em **folha de pagamento** ou nas **férias**, existe o campo **Reg.Desconto** que irá tratar a regra de desconto. Quando selecionado **férias,** o sistema fará o desconto da parcela nas férias do funcionário, e os **próximos** serão realizados corretamente na **folha.**  
Caso queira que o desconto ocorra **sempre** na **folha** de pagamento, selecione **Folha** ou deixe em branco. Assim quando o funcionário estiver de férias, o sistema fará o desconto da parcela diretamente na **folha** de pagamento e não nas férias.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26241840416151)

2 . Após parametrizar os lançamentos futuros, será necessário acessar a rotina **GPEM020**disponível em **Miscelânea > Cálculos > Folha**, executar o processamento de cálculo da folha e na sequência analisar o seu resultado através da rotina **Lançamentos por Funcionário** em **Atualizações > Lançamentos > Por Funcionário.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26241840425367)**

**Observação:**Após o fechamento do período da folha, o Sistema atualizará a rotina de **Valores Futuros** com a **quantidade de parcelas pagas, restantes, data do próximo vencimento** (de acordo com o período aberto no cadastro de períodos) e **saldo em** **aberto.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26241840427159)**  
  
**Saiba Mais**

[RH - Linha Protheus - GPE - Como controlar as movimentações de Lançamentos Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiQShDSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwNjU2ODU5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb250cm9sYXItYXMtbW92aW1lbnRhJUMzJUE3JUMzJUI1ZXMtZGUtTGFuJUMzJUE3YW1lbnRvcy1WYWxvcmVzLUZ1dHVyb3MGOwhUOg5zZWFyY2hfaWRJIikyMmEwZGQ2OC1lY2IxLTQxNjUtOTg4ZS0wNjY4OTdkZWNlMTYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJImJSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjb250cm9sYXIgYXMgbW92aW1lbnRhw6fDtWVzIGRlIExhbsOnYW1lbnRvcyBWYWxvcmVzIEZ1dHVyb3MGOwhUOhJyZXN1bHRzX2NvdW50aQLrAw%3D%3D--5c52fb5b61f4abd4062bc2af40c38fc84b1bedac)

[RH - Linha Protheus - GPE - Como suspender valores lançados na rotina de Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj877fSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzU1NTQ1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1zdXNwZW5kZXItdmFsb3Jlcy1sYW4lQzMlQTdhZG9zLW5hLXJvdGluYS1kZS1WYWxvcmVzLUZ1dHVyb3MGOwhUOg5zZWFyY2hfaWRJIikyMmEwZGQ2OC1lY2IxLTQxNjUtOTg4ZS0wNjY4OTdkZWNlMTYGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJImJSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjb250cm9sYXIgYXMgbW92aW1lbnRhw6fDtWVzIGRlIExhbsOnYW1lbnRvcyBWYWxvcmVzIEZ1dHVyb3MGOwhUOhJyZXN1bHRzX2NvdW50aQLrAw%3D%3D--d0cea1364dc47f0488c1f9f46c8bb5e5f292877d)

[RH - Linha Protheus - GPE - Relatório Valores Futuros em planilha (GPER570)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgpBd7UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzYwNTY3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUmVsYXQlQzMlQjNyaW8tVmFsb3Jlcy1GdXR1cm9zLWVtLXBsYW5pbGhhLUdQRVI1NzAGOwhUOg5zZWFyY2hfaWRJIik1ZDUyMjNkNy0wMmJjLTQxY2YtODNhNC1kMDcwNzc4NzQ1ZDQGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhR2YWxvcmVzIGZ1dHVyb3MGOwhUOhJyZXN1bHRzX2NvdW50aQI7BA%3D%3D--4b27245a85ed8d99cae6c192bb3941d90bca491d)

[RH - Linha Protheus - GPE - Como visualizar as verbas integradas para folha com a pergunta Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXELvJhQw6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEzNzY4NzU0NjYzNDQ3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLXZpc3VhbGl6YXItYXMtdmVyYmFzLWludGVncmFkYXMtcGFyYS1mb2xoYS1jb20tYS1wZXJndW50YS1WYWxvcmVzLUZ1dHVyb3MGOwhUOg5zZWFyY2hfaWRJIik1ZDUyMjNkNy0wMmJjLTQxY2YtODNhNC1kMDcwNzc4NzQ1ZDQGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhR2YWxvcmVzIGZ1dHVyb3MGOwhUOhJyZXN1bHRzX2NvdW50aQI7BA%3D%3D--93070b4169ffffa249dec21b9e02ae378a29fbe4)

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
