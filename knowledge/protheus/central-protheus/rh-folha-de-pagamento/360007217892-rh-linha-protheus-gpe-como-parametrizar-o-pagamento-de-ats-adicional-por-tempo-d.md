---
article_id: 360007217892
category: RH - Folha de Pagamento
content_hash: eeca3e7b9964f4eede60c931810c8b58e93c7a406bba7ab79d66a4be12bafb7a
fetched_at: '2026-06-28T22:44:14.663401+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como Parametrizar o Pagamento de ATS (Adicional
  por Tempo de Serviço) na versão 12
type: support-article
updated_at: '2025-04-23T17:19:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007217892-RH-Linha-Protheus-GPE-Como-Parametrizar-o-Pagamento-de-ATS-Adicional-por-Tempo-de-Servi%C3%A7o-na-vers%C3%A3o-12
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25992553835159) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como parametrizar o Pagamento de ATS - Adicional por Tempo de Serviço na Release 12 do Protheus?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para a configuração do cálculo do adicional por tempo de serviço execute os passos abaixo:  
**1.** Verifique os campos sindicato, data de admissão e adicionais em **Atualizações > Funcionário > Funcionários (GPEA010)**:**![](http://tdn.totvs.com/download/attachments/266968082/image2016-10-3%2016%3A41%3A25.png?version=1&modificationDate=1475524521000&api=v2)**Informar no cadastro do funcionário o tipo de adicional que será calculado. O tipo **N - Funcionário não recebe adicional** vem marcado, portanto deve ser desmarcado para que o calculo seja realizado. **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097965234)**

**2.** Verifique a configuração do **sindicato** em **Atualizações > Cadastros > Sindicatos (GPEA340)** na **Aba Adic. Tempo Serv.:**  
  
Para **alterações no cadastro do sindicato**, deve-se sempre *logar* no sistema com **a data que deseja fazer a alteração**. Exemplo: O sindicato alterou o valor do triênio dia 01/10 porém esse valor saiu em atraso e será necessário calcular o dissidio retroativo com data 01/08. Nesse cenário, devemos *logar* no sistema com data 01/08 para que o sistema grave que a alteração é a partir dessa data e assim calcular os valores retroativos no cálculo do dissidio.

 - O tempo de serviço do funcionário é calculado a partir da sua data de admissão ou a partir da data base do adicional.

 - O valor a ser pago do adicional por tempo de serviço será determinado entre 1 para anuênio, 2 para biênio, 3 para triênio, 4 para quadriênio e 5 para quinquênio que poderá ser parametrizado para ser pago como um valor fixo ou um percentual sobre a base de cálculo que o cliente montar.

Esta rotina permite montar a regra de cálculo que será utilizada.

![](https://tdn.totvs.com/download/attachments/266968082/image2016-10-3%2016%3A48%3A10.png?version=1&modificationDate=1475524521000&api=v2)

![](https://tdn.totvs.com/download/attachments/266968082/image2016-10-3%2016%3A48%3A28.png?version=1&modificationDate=1475524521000&api=v2)

**3.** Verifique o cadastro de verbas em **Atualizações > Cadastros > Verbas (GPEA040)**:

Nesta rotina o cliente deverá cadastrar uma verba de provento que corresponda ao pagamento do adicional por tempo de serviço, porém para cada tipo de adicional existe um Identificador de cálculo específico. 

![](https://tdn.totvs.com/download/attachments/266968082/image2016-10-3%2016%3A37%3A49.png?version=1&modificationDate=1475524521000&api=v2)

Para o cálculo do adicional por tempo de serviço sobre verbas, devemos informar ao sistema quais verbas entrarão para cálculo dos adicionais, através do campo Adic.T.Serv. Com conteúdo SIM, a verba em questão entrará para base de cálculo.  
  
Exemplo: quando configurado Salario + Verbas o sistema utilizará o valor da verba de Hora Extra para compor o valor base de cálculo do ATS.  
Então no cadastro de verbas, informamos quais verbas farão base de cálculo para o adicional.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045666334)  
  
**4.** Execute o cálculo de folha de pagamento em **Miscelânea > Cálculos > Por Roteiro (GPEM020)**:  
  
![](http://tdn.totvs.com/download/attachments/266968082/image2016-10-3%2016%3A52%3A51.png?version=1&modificationDate=1475524521000&api=v2)

**5.** Consulte o cálculo em **Consultas > Calculo > Por funcionário (GPEA090)**:  
  
![](http://tdn.totvs.com/download/attachments/266968082/image2016-10-3%2016%3A54%3A8.png?version=1&modificationDate=1475524521000&api=v2)  
  
**Saiba Mais**

[RH - Linha Protheus - GPE - Como parametrizar o sistema para que o cálculo do Adicional por Tempo de Serviço (ATS) seja sobre salário base mais verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwht9Pc%2BXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB5Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDAwMjM2NjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tcGFyYW1ldHJpemFyLW8tc2lzdGVtYS1wYXJhLXF1ZS1vLWMlQzMlQTFsY3Vsby1kby1BZGljaW9uYWwtcG9yLVRlbXBvLWRlLVNlcnZpJUMzJUE3by1BVFMtc2VqYS1zb2JyZS1zYWwlQzMlQTFyaW8tYmFzZS1tYWlzLXZlcmJhcwY7CFQ6DnNlYXJjaF9pZEkiKWQ3MWFhNTc5LTY0ZWQtNDNjMy05MjliLTViODgzYjZkZmEzMAY7CEY6CXJhbmtpDToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiJlJIIC0gTElOSEEgUFJPVEhFVVMgIC0gR1BFICAtIEFUUwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--30c9051e5e93de645f0834ad90da03b8128da71a)  
[RH - Linha Protheus - GPE - Como o sistema efetua o cálculo do adicional por tempo de serviço (ATS) sobre as verbas indenizatórias quando a base de cálculo é salário + verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi%2B1nk%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSICCQFodHRwczovL2NlbnRyYWxkZWF0ZW5kaW1lbnRvLnRvdHZzLmNvbS9oYy9wdC1ici9hcnRpY2xlcy8xNTAwMDA4NTM1NzQyLVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLW8tc2lzdGVtYS1lZmV0dWEtby1jJUMzJUExbGN1bG8tZG8tYWRpY2lvbmFsLXBvci10ZW1wby1kZS1zZXJ2aSVDMyVBN28tQVRTLXNvYnJlLWFzLXZlcmJhcy1pbmRlbml6YXQlQzMlQjNyaWFzLXF1YW5kby1hLWJhc2UtZGUtYyVDMyVBMWxjdWxvLSVDMyVBOS1zYWwlQzMlQTFyaW8tdmVyYmFzBjsIVDoOc2VhcmNoX2lkSSIpZDcxYWE1NzktNjRlZC00M2MzLTkyOWItNWI4ODNiNmRmYTMwBjsIRjoJcmFua2kOOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSImUkggLSBMSU5IQSBQUk9USEVVUyAgLSBHUEUgIC0gQVRTBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--d1bf646ad8b21ba7f19fafcb5cbb19858d68f2d7)  
[RH - Linha Protheus - GPE - Como utilizar a carência do Adicional de Tempo de Serviço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050439654-RH-Linha-Protheus-GPE-Como-utilizar-a-car%C3%AAncia-do-Adicional-de-Tempo-de-Servi%C3%A7o?source=search)
