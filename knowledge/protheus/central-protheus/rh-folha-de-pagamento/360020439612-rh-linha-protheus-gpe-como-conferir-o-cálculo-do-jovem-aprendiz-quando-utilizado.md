---
article_id: 360020439612
category: RH - Folha de Pagamento
content_hash: 214f51a71651f44a8cd355a281c1bb8a6751d3bf231330c7523f11fa1b940228
fetched_at: '2026-06-28T22:44:17.103400+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir o cálculo do jovem aprendiz quando
  utilizado o parâmetro MV_MAPREND = .T.
type: support-article
updated_at: '2025-10-01T12:52:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020439612-RH-Linha-Protheus-GPE-Como-conferir-o-c%C3%A1lculo-do-jovem-aprendiz-quando-utilizado-o-par%C3%A2metro-MV-MAPREND-T
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26165661318935) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como conferir o calculo do jovem aprendiz quando utilizado o parâmetro MV\_MAPREND = .T.?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Certifique-se que seu parâmetro **MV\_MAPREND = .T.**  
Para realizar a conferência acesso **Configurador (SIGACFG)** no caminho: **Ambiente > Cadastro > Parâmetro**, localize o parâmetro e salve conforme modelo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020900551)

Cadastro do Período: certifique que está configurado pelos dias do mês:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19128320916631)

Cadastro de funcionário: certifique que está configurado como Horista (Categoria Funcionário) e se as Horas Mês, Horas Semanais e Horas Dias estão cadastradas corretamente:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19128320924951)  
  
Orientação do cálculo conforme a Nota Técnica n° 52 :  
  
![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016675252)

Siglas utilizadas para entendimento das informações:  
**SA**= SALARIO HORA  
**X** = SALARIO MÊS  
**HS** = HORAS SEMANAIS (Quantidade de horas mensais no cadastro do funcionário / 5)  
**QS** = QUANTIDADE DE SEMANAS (de acordo com a tabela acima)  
**DS** = DIAS DA SEMANA  
   
**Qual a formula? (valor bruto a ser pago ao jovem Aprendiz)**  
X = SA X HS X QS X DS / 6  
X = R$6,25 X 40 X 4,428517 (mês de dezembro) X 7 / 6 = 1.291,65  
X = R$1.291,67

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19128345835927)

**Calculo da proporcionalização entre Salario horista e DSR:**  
X = RA\_SALARIO \* HS \* QS   
X = 6,25 \* 40 \* 4,428517  
X = 1.107,14 (SALARIO HORISTA ID 0032)

DSR = SALARIO HORISTA / 6

DSR = 1.107,14 / 6

DSR = 184,52 (ID 0035)

**Saiba Mais**

<https://tdn.totvs.com/pages/releaseview.action?pageId=476747392>

[RH - Linha Protheus - GPE - Como configuração calculo Menor Aprendiz Horista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034214354-RH-Linha-Protheus-GPE-Como-configura%C3%A7%C3%A3o-calculo-Menor-Aprendiz-Horista?source=search)

[RH - Linha Protheus - GPE - Como realizar o cálculo do DSR de horistas conforme a tabela de Horário Padrão do módulo SIGAPON](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018862371-RH-Linha-Protheus-GPE-Como-realizar-o-c%C3%A1lculo-do-DSR-de-horistas-conforme-a-tabela-de-Hor%C3%A1rio-Padr%C3%A3o-do-m%C3%B3dulo-SIGAPON?source=search)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
