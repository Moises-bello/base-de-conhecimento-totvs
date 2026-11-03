---
article_id: 360052131333
category: RH - Benefícios
content_hash: 8e7bd6b55b79de3c835b4ca671fa4314a78b8b8d5a77750a7bb5b7587794d194
fetched_at: '2026-06-28T22:44:04.716866+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - MV_CVTPROP igual a P para Horistas
type: support-article
updated_at: '2025-09-25T11:26:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052131333-RH-Linha-Protheus-GPE-MV-CVTPROP-igual-a-P-para-Horistas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32471902094103) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Parâmetro MV\_CVTPROP igual a P para Horistas  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Sistema está calculando incorretamente o custo funcionário no cálculo de Vale Transporte quando o parâmetro MV\_CVTPROP possui conteúdo igual a  'P' (Proporcional) para funcionários Horistas.

O valor do salário base do funcionário não está sendo dividido por 31 nos meses com 31 dias.

O parâmetro MV\_DIASPER está configurado como 2=30 Dias.  
 **Solução**O tratamento para o uso de 31 dias no caso de funcionários da categoria Horista mesmo que utilizando o parâmetro MV\_DIASPER igual a 2 (ou seja, divisão por 30 dias) é o de cadastramento de um Processo/Período a parte para os funcionários da categoria Horista de forma que o campo 'Dias de Cálculo' (mesmo que carregado com 30, seja editado para 31).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11651801276183)

Possuindo essa configuração como premissa, foi realizado ajuste no cálculo do custo funcionário no cálculo do Vale Transporte.

**Exemplo - Horista com uso de MV\_DIASPER igual a 2 (por 30 dias)**

Parâmetros:  
MV\_DIASPER igual a 2  
MV\_CVTUSO igual a 1  
MV\_CVTPROP igual a P  
  
Cadastros:  
Período Julho/2019 = 31 Dias de Cálculo e Dias de Período  
Dias Trabalhados = 23  
Dias DSR = 4  
Dias Úteis VTR = 23  
Salário Hora = 10  
Salário Base Horista => 10 x 227.30 => 2273.30

Cálculo:  
Dias Proporcionais Informados => 26  
Custo Funcionário => ((Salário Base Horista/Dias de Cálculo) \* Dias Proporcionais Informados) \* 6%  
Custo Funcionário => ((2273.30/31) \* 26) \* 6%  
Custo Funcionário => 114.39

Dias Proporcionais Informados => 0  
Custo Funcionário => ((Salário Base Horista/Dias de Cálculo) \* Dias Úteis VTR) \* 6%  
Custo Funcionário => ((2273.30/31) \* 23) \* 6%  
Custo Funcionário => 101.20

**Importante:** Esse ajuste anula a correção efetuada na issue abaixo.  
[6653810 DRHPAG-28650 DT Cálculo Vale Transporte - MV\_CVTPROP = "P"](https://tdn.totvs.com/pages/viewpage.action?pageId=513418641)

**Saiba Mais**[RH - Linha Protheus - GPE - Como utilizar parâmetro MV\_CVTPROP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014665512-RH-Linha-Protheus-GPE-Como-utilizar-par%C3%A2metro-MV-CVTPROP)  
[RH - Linha Protheus - GPE - Desconto de Vale Transporte com parâmetro MV\_CVTPROP = P](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057345093-RH-Linha-Protheus-GPE-Desconto-de-Vale-Transporte-com-par%C3%A2metro-MV-CVTPROP-P)  
[RH - Linha Protheus - GPE - Desconto de Vale Transporte com parâmetro MV\_CVTPROP = T](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057771853-RH-Linha-Protheus-GPE-Desconto-de-Vale-Transporte-com-par%C3%A2metro-MV-CVTPROP-T)  
[RH - Linha Protheus - GPE - Desconto de Vale Transporte com o parâmetro MV\_CVTPROP = S](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016194312-RH-Linha-Protheus-GPE-Desconto-de-Vale-Transporte-com-o-par%C3%A2metro-MV-CVTPROP-S)
