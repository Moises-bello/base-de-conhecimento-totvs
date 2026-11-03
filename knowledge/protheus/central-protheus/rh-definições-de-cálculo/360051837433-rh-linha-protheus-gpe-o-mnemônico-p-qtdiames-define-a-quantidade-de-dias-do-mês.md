---
article_id: 360051837433
category: RH - Definições de Cálculo
content_hash: beea73ce60c9cb6a75e68a7741385e0852daeeef268fa494169165ceb8b54e3f
fetched_at: '2026-06-28T22:43:22.577342+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - O mnemônico P_QTDIAMES define a quantidade de dias
  do mês para cálculo
type: support-article
updated_at: '2023-02-17T19:37:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051837433-RH-Linha-Protheus-GPE-O-mnem%C3%B4nico-P-QTDIAMES-define-a-quantidade-de-dias-do-m%C3%AAs-para-c%C3%A1lculo
---

**Dúvida**O mnemônico P\_QTDIAMES define a quantidade de dias do mês para cálculo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Ocorre sua utilização nos seguintes cálculos:  
  
**Relatório de médias:**O sistema utiliza os dias para efetuar o cálculo do salário/hora para funcionários com pagamento mensal (RA\_SALARIO / (P\_QTDIAMES X RA\_HRSDIA)). O valor do salário hora será utilizado para a apresentação dos valores das verbas de horas,

**Cálculo de benefícios:**Verificar mais detalhes no link:  
<https://tdn.totvs.com/display/public/PROT/GPE021BEN_Calculo_VT_MV_CVTPROP_S>.

**Cálculo de rescisão:**O sistema utiliza os dias para efetuar o cálculo dos valores de férias vencidas, férias proporcionais, férias sobre aviso e férias em dobro ( [Base] / (P\_QTDIAMES X [Dias de férias]) ).

**Cálculo de pensão alimentícia:**O sistema utiliza os dias para efetuar a proporcionalização do valor da pensão conforme os dias trabalhados no período ( [Dias trabalhadors] / (P\_QTDIAMES ).

**Cálculo de salário família:**O sistema utiliza os dias para efetuar a proporcionalização do valor do salário família conforme os dias trabalhados no período, quando o parâmetro MV\_SALFD está configurado com N ( [Base] / (P\_QTDIAMES X [Dias trabalhados]) ).  
  
**Saiba Mais**As informações foram retiradas do *link*: <https://tdn.totvs.com/pages/releaseview.action?pageId=555278890>
