---
article_id: 360015195412
category: RH - Folha de Pagamento
content_hash: 8931851719f088019ab0b21c6cfa952dab71ffd577779188fae02af7d7314af7
fetched_at: '2026-06-28T22:44:13.250977+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir o cálculo de funcionário horista
type: support-article
updated_at: '2025-05-12T16:39:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015195412-RH-Linha-Protheus-GPE-Como-conferir-o-c%C3%A1lculo-de-funcion%C3%A1rio-horista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26265148450583) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como analisar o cálculo de funcionário horista?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.25  
  
**Solução**Para conferir o cálculo de Folha de Pagamento de um funcionário da categoria **HORISTA** devemos nos atentar com as seguintes informações:

1. Configuração do Parâmetro MV\_DIASPER;  
Para o exemplo abaixo utilizamos igual a 2, ou seja, divisor sempre por 30.

2. Dados do funcionário;  
Salário dia => R$ 111,11

![](http://tdn.totvs.com/download/attachments/225214846/Img3.jpg?version=1&modificationDate=1456397453000&api=v2)  
  
3. Dados do Período que estamos trabalhando.  
Para o período abaixo temos 26 DIAS ÚTEIS e 5 DIAS DE DSR.

Perceba que ao utilizarmos o parâmetro MV\_DIASPER como '2', o campo 'Dias de Cálculo' (RCF\_DCALCM) se torna editável e inicializado com 30.

![](http://tdn.totvs.com/download/attachments/225214846/Img1.jpg?version=1&modificationDate=1456397449000&api=v2)

![](http://tdn.totvs.com/download/attachments/225214846/Img2.jpg?version=1&modificationDate=1456397451000&api=v2)  
  
Após a conferência dessas informações e da execução do cálculo, vamos agora conferir como fora realizado o cálculo:  
![](http://tdn.totvs.com/download/attachments/225214846/Img4.jpg?version=1&modificationDate=1456397455000&api=v2)

Horas Normais => 26 DIAS ÚTEIS \* 6 horas por dia => 156hrs  
Horas DSR => 5 DIAS DSR \* 6 horas por dia => 30hrs  
Salário Hora => R$ 111,11  
Salário Dia => 6 horas por dia \* 111,11 => R$ 666,66  
Salário Mês => 666,66\*30 dias mensais => R$ 19.999,80

Salário Horista => **156**\*111,11=> **R$ 17.333,16**DSR Horista => **30**\*111,11=> **R$ 3333,33**  
  
**Observação:**  
Para o sistema Protheus, não são mais considerados os campos 'Hrs Normais'(R6\_HRNOMA) e 'Hrs Desc.'(R6\_HRDESC) para o cálculo do Horista, permanecendo no cadastro apenas para fins de utilizações no processos de integrações entre marcas.  
  
**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[RH - Linha Protheus - GPE - Como é o cálculo da rescisão para funcionário horista com jornada variável](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7503224755351-RH-Linha-Protheus-GPE-Como-%C3%A9-o-c%C3%A1lculo-da-rescis%C3%A3o-para-funcion%C3%A1rio-horista-com-jornada-vari%C3%A1vel?source=search)

[RH - Linha Protheus - GPE - Cálculo incorreto de folha para funcionários horistas com afastamento sequencial por doença](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018687372-RH-Linha-Protheus-GPE-C%C3%A1lculo-incorreto-de-folha-para-funcion%C3%A1rios-horistas-com-afastamento-sequencial-por-doen%C3%A7a-?source=search)

[RH - Linha Protheus - GPE - Como considerar 30 dias para o cálculo de adiantamento do funcionário horista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014440672-RH-Linha-Protheus-GPE-Como-considerar-30-dias-para-o-c%C3%A1lculo-de-adiantamento-do-funcion%C3%A1rio-horista?source=search)

[RH - Linha Protheus - GPE - Como é realizado o calculo de salário família proporcional admissão para funcionários horista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060367133-RH-Linha-Protheus-GPE-Como-%C3%A9-realizado-o-calculo-de-sal%C3%A1rio-fam%C3%ADlia-proporcional-admiss%C3%A3o-para-funcion%C3%A1rios-horista?source=search)

[RH - Linha Protheus - GPE - Como configuração calculo Menor Aprendiz Horista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034214354-RH-Linha-Protheus-GPE-Como-configura%C3%A7%C3%A3o-calculo-Menor-Aprendiz-Horista?source=search)
