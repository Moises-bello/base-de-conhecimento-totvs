---
article_id: 360014665512
category: RH - Benefícios
content_hash: 5bc4b36f717afc3fd123c775d360f5b84ea8f30b97074d8422d65589e3647598
fetched_at: '2026-06-28T22:44:03.877476+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como utilizar parâmetro MV_CVTPROP para cálculo
  proporcional de Vale Transporte
type: support-article
updated_at: '2026-04-28T12:52:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014665512-RH-Linha-Protheus-GPE-Como-utilizar-par%C3%A2metro-MV-CVTPROP-para-c%C3%A1lculo-proporcional-de-Vale-Transporte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15620929819543) Tempo aproximado para leitura: **00:02:00min**

**Dúvida**  
Como utilizar parâmetro MV\_CVTPROP para cálculo proporcional de desconto de vale transporte?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Para que o sistema considere o parâmetro **MV\_CVTPROP**, é preciso primeiramente, alterar via configurado o parâmetro  **MV\_CVTUSO=1**.  
  
1. Acesse o modulo Configurador.

2. Acesse a rotina em **Ambientes > Cadastros > Parâmetros**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10835591493911)  
  
3. Clique no sinal de **+** em seguido em **Parâmetros**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10835601781271)

4. Clique na **Lupa** e pesquise o parâmetro **MV\_CVTUSO**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10835597703191)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10835649161495)

5. Selecione o parâmetro **MV\_CVTUSO** e clique em **Alterar**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10835654685975)

6. Ajuste o parâmetro **MV\_CVTUSO =1** para verificar o parâmetro **MV\_CVTPROP** no cálculo de Vale Transporte![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10835922552855)

7. Após ajustar o parâmetro **MV\_CVTUSO** pesquise o parâmetro **MV\_CVTPROP**  
**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10837788202135)**

8. Clique em **Alterar** e realize a configuração do parâmetro conforme a necessidade. 

O parâmetro MV\_CVTPROP com a descrição "Dias a ser considerado no cálculo do desconto do Vale Transporte", quando o funcionário tiver dias proporcionais de vales a receber pode ser configurado de quatro maneiras diferentes:

1. Para cálculo **proporcional aos dias trabalhados**, deve-se utilizar conteúdo igual a **T**;  
2. Para cálculo **proporcional aos dias de vale transporte,** deve-se utilizar conteúdo igual a **P**;  
3. Para cálculo **sobre o salário integral,**deve-se utilizar conteúdo igual a**I**.  
4. Para cálculo **sobre o saldo de dias**, deve-se utilizar conteúdo igual a **S.**

Exemplos:  
**Parâmetro definido como "I"**, o desconto será feito sobre o salário integral  
Salário = R$ 1.000,00 Base para Desconto.      

**Parâmetro for definido como "P"**, o desconto será feito sobre os dias informados ou calculados no Campo R0\_DIASPRO (Dias Proporcionais de V. transporte).  
Salário 1.000,00  
**R0\_DIASPRO** (Dias Proporcionais) = 22 e Dias úteis de Vale Transportes = 30  
Base Para Desconto = Salário / 30 dias, ou dias do Período x 22

**Parâmetro for definido como "T"**, o cálculo será feito sobre os dias trabalhados (dias trabalhados e DSR, campo Nº Dias DSR "RCF\_DIADSR" e Nº Dias Trab "RCFDIATRA").  
Salário = 1000,00  
Dias Trabalhados = 25 e  Dias úteis de VT = 30  
Base Para Desconto = Salário / 30 dias, ou dias do Período x 25

**Parâmetro for definido como "S",** o cálculo será feito sobre o dias de saldo do mês da seguinte forma: Salário mês / dias do período \* Dias Saldo Mês  
O exemplo de cálculo encontra-se na documentação: [RH - Linha Protheus - GPE - Cálculo de Vale Transporte com parâmetro MV\_CVTPROP com S](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016194312-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Vale-Transporte-com-par%C3%A2metro-MV-CVTPROP-com-S?source=search)

**Observações:**  
Dias úteis de VT são os dias do **Cadastro de Calendário**, que estão com Sim para Vale Transporte.  
Para meios de transporte com o preenchimento de **dias fixos**, **não** é possível **abater, faltas, férias e afastamentos**.

**Saiba Mais:**  
[RH - Linha Protheus - GPE - MV\_CVTPROP igual a P para Horistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052131333-RH-Linha-Protheus-GPE-MV-CVTPROP-igual-a-P-para-Horistas?source=search)  
[RH - Linha Protheus - GPE - Como calcular percentual de desconto de Vale transporte inferior a 6% para todos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059488853-RH-Linha-Protheus-GPE-Como-calcular-percentual-de-desconto-de-Vale-transporte-inferior-a-6-para-todos-funcion%C3%A1rios?source=search)
