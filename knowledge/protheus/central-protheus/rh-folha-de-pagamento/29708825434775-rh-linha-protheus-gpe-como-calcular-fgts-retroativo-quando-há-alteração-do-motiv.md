---
article_id: 29708825434775
category: RH - Folha de Pagamento
content_hash: b5fb51b08ae73620e592cd21e29f5afcb78852e907c574c1476fecdcb4b31ef7
fetched_at: '2026-06-28T22:44:12.261382+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular FGTS retroativo quando há alteração
  do Motivo do afastamento
type: support-article
updated_at: '2025-09-01T17:57:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29708825434775-RH-Linha-Protheus-GPE-Como-calcular-FGTS-retroativo-quando-h%C3%A1-altera%C3%A7%C3%A3o-do-Motivo-do-afastamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29708825419159) Tempo aproximado para leitura: **00:03:00min** **Dúvida**Ao alterar o tipo de ausência de auxílio doença para acidente de trabalho, se o afastamento iniciou-se em mês anterior ao período de cálculo da folha, faz-se necessário gerar recolhimento de FGTS retroativo, conforme deliberação do manual do e-Social e [entendimento da consultoria tributária.](https://tdn.totvs.com.br/pages/releaseview.action?pageId=861547446)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**Foi criado o novo identificador de cálculo 1966 - Base FGTS Acidente de Trabalho Mês Anterior, que deverá ser incluída em uma verba de Base Provento, sem incidências e configurada para lançamento diário (RV\_LCTODIA = 'S').

Ao efetuar a alteração do afastamento de doença para acidente de trabalho, no momento que a ausência é integrada com o TAF, o campo R8\_DATALT do afastamento é gravado com a data base da alteração.

Ao efetuar o cálculo da folha, se for encontrado afastamento cujo campo R8\_DATALT coincida com o período de cálculo e que tenha iniciado em período anterior, o sistema pegará todos os dias de afastamento referentes aos períodos anteriores e irá gerar a base de FGTS sobre acidente de trabalho de períodos anteriores na verba com identificador de cálculo 1966.

Os valores gerados na verba 1966 por sua vez serão somados a base de FGTS do mês para que seja gerado o recolhimento total, conforme exemplo:

Cadastro da verba

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34611883778967)

Data do Inicio do afastamento - 01/05/2024

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29709302942487)

Data da alteração do Motivo do afastamento- Auxilio Doença para Acidente do Trabalho em 24/10/2024

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29709302944663)

Funcionário com salário de R$3.660,00, no cálculo de Outubro, o sistema irá gerar a verba 1966 referente a 15 dias de Maio (os 15 primeiros dias já foram recolhidos por parte da empresa) e os valores referente a Junho / Julho/ Agosto e Setembro, o sistema demonstra na mesma verba mas de forma separada para uma melhor conferência, conforme exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29709812098199)  
15 dias de Maio (Retroativo)  
30 dias Junho (Retroativo)  
30 dias Julho (Retroativo)  
30 dias Agosto (Retroativo)  
30 dias Setembro (Retroativo)  
30 dias Outubro (Mensal)  
Totalizando uma **base de FGTS de 20.130,00 \* 8% = 1.610,40**

<https://tdn.totvs.com/pages/releaseview.action?pageId=880081335>

**Saiba Mais**

<https://www.youtube.com/watch?v=T7b4zMlphTI>  
[RH - Linha Protheus - GPE - ID 1883 Base FGTS 13º salario acidente do trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417996909079-RH-Linha-Protheus-GPE-ID-1883-Base-FGTS-13%C2%BA-salario-acidente-do-trabalho)  
[RH - Linha Protheus - GPE - Como criar verbas para atender ao Parecer SEI Nº 16120/2020/ME](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007487421-RH-Linha-Protheus-GPE-Como-criar-verbas-para-atender-ao-Parecer-SEI-N%C2%BA-16120-2020-ME)  
[RH - Linha Protheus - GPE - Como deve ser o cadastro do afastamento por doença para o calculo de adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006694841-RH-Linha-Protheus-GPE-Como-deve-ser-o-cadastro-do-afastamento-por-doen%C3%A7a-para-o-calculo-de-adicionais)  
[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
