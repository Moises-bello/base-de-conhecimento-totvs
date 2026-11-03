---
article_id: 13321877361943
category: RH - 13º salário
content_hash: feb8d5c822e5521ea8981b158cdc4eb515cb43ad7faf3853020610757cf6ee20
fetched_at: '2026-06-28T22:44:00.616027+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como é feito pagamento de antecipação de 13º salário
  no cálculo de férias fracionadas em mais de um período
type: support-article
updated_at: '2025-07-23T12:18:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13321877361943-RH-Linha-Protheus-GPE-Como-%C3%A9-feito-pagamento-de-antecipa%C3%A7%C3%A3o-de-13%C2%BA-sal%C3%A1rio-no-c%C3%A1lculo-de-f%C3%A9rias-fracionadas-em-mais-de-um-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33657817538455) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como é feito pagamento de **antecipação de 13º salário no cálculo de férias fracionadas em mais de um período de gozo?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A verba com id de cálculo **0022** - antecipação de 13º - é gerada **apenas** no **1º cálculo** de férias.  
  
Quando a empresa opta por deixar os períodos de férias já **programados** no **Controle de Dias de Direito** ou a informação de antecipação de 13º venha do **App Meu RH**, o **percentual** fica gravado para cálculo:  
   
![](https://totvssuporte.zendesk.com/attachments/token/OyXdiMERrCijv9Nna59ENstnj/?name=image.png)  
   
 Quando processado cálculo, tanto pela rotina de cálculo de férias quanto férias coletivas/ programadas, a verba de antecipação é **gerada** **no 1º cálculo de férias**:  
   
![](https://totvssuporte.zendesk.com/attachments/token/kED7TknwOt66JFMEEPReTnr0m/?name=image.png)  
   
Porém no **segundo cálculo** ela **não** volta a ser apresentada:  
   
![](https://totvssuporte.zendesk.com/attachments/token/fnyfyGilnhDmr2q9feDaaKXhC/?name=image.png)  
   
O que pode causar estranheza é que, ao **entrar** na rotina de cálculo de férias, o Sistema **traz** o campo de **percentual** preenchido com **50** na segunda férias, mas ele não gera a verba de pagamento de 13º.  
   
![](https://totvssuporte.zendesk.com/attachments/token/o1OMN3dht32CYI3q6g3Le8Srw/?name=image.png)  
   
Isso ocorre porque o **cabeçalho** das férias traz as informações preenchidas no **controle de dias de direito** do funcionário, mas a verba **não é calculada duas vezes** pois já foi feito pagamento antes.  
  
O Sistema checa o histórico do funcionário antes. Tendo o id 0022 no acumulado dele (SRD), ele não calcula de novo.  
 

**Para Saber Mais**

[RH - Linha Protheus - GPE - Como é calculado a antecipação de 13º nas férias quando há licença maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409135226519-RH-Linha-Protheus-GPE-Como-%C3%A9-calculado-a-antecipa%C3%A7%C3%A3o-de-13%C2%BA-nas-f%C3%A9rias-quando-h%C3%A1-licen%C3%A7a-maternidade?source=search)

[RH - Linha Protheus - GPE - Como imprimir recibo de antecipação de 13º nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057728993-RH-Linha-Protheus-GPE-Como-imprimir-recibo-de-antecipa%C3%A7%C3%A3o-de-13%C2%BA-nas-f%C3%A9rias?source=search)

[RH - Linha Protheus - GPE - Como antecipar o 13º nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006362581-RH-Linha-Protheus-GPE-Como-antecipar-o-13%C2%BA-nas-f%C3%A9rias?source=search)
