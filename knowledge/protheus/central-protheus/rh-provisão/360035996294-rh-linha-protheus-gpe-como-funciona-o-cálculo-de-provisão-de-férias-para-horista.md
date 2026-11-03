---
article_id: 360035996294
category: RH - Provisão
content_hash: b59103042f3c7edb821f37516d3c0ec0b895d1416e887cca1b8cf12b556064b1
fetched_at: '2026-06-28T22:43:55.818918+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o Cálculo de Provisão de Férias para
  Horistas com Jornada Variável
type: support-article
updated_at: '2025-10-24T12:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035996294-RH-Linha-Protheus-GPE-Como-funciona-o-C%C3%A1lculo-de-Provis%C3%A3o-de-F%C3%A9rias-para-Horistas-com-Jornada-Vari%C3%A1vel
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998092903959)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como funciona o Cálculo de Provisão de Férias para Horistas com Jornada Variável?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Alterados os roteiros de Folha de Pagamento, para que ao encontrar funcionário Horista (RA\_CATFUNC = “H”) e com Jornada Variável (RA\_HOJORVA = “1”), faça uma busca nas horas acumuladas de todas verbas que estiverem no grupo 0 campo **Grupo Verba** **(RV\_GRPVER = "0")** e, através dessa média, calcule o salário referência a ser utilizado.

No cálculo da Provisão de Férias, para os funcionários nestas condições, para encontrar o salário referência, será substituída a quantidade de horas mês que está no cadastro de funcionário (RA\_HRSMES), pela média encontrada através da leitura da Tabela de valores acumulados (SRD), com base no Período Aquisitivo do Funcionário.

**Exemplo:**Funcionário foi admitido em 10/01/2018, tem como salário R$ 10,00 por hora.

Em cada um dos meses do Período Aquisitivo realizou, uma quantidade de horas diferente, conforme abaixo:

01/2018 = 150 horas e 20 horas de DSR = 170  
02/2018 = 180 horas e 22 horas de DSR = 202  
03/2018 = 227 horas e 25 horas de DSR = 252  
04/2018 = 220 horas e 20 horas de DSR = 240  
05/2018 = 227 horas e 20 horas de DSR = 247  
06/2018 = 180 horas e 20 horas de DSR = 200  
07/2018 = 250 horas e 20 horas de DSR = 270  
08/2018 = 150 horas e 20 horas de DSR = 170  
09/2018 = 200 horas e 20 horas de DSR = 220  
10/2018 = 220 horas e 20 horas de DSR = 240  
11/2018 = 220 horas e 20 horas de DSR = 240  
12/2018 = 100 horas e 20 horas de DSR = 120

Total das Horas : 2.571 / 12 = 214,25 Média de Horas.

Memória de cálculo: A média de Horas Trabalhada e DSR do período é de 214,25, este valor multiplicamos pelo salário hora atual 10,00.

Então o salário Referência para o cálculo das Provisões de Férias Vencidas será de **2.142,50**.

O valor utilizado como Base para cálculo das Provisões de Férias Vencidas e Proporcionais é apresentado no Relatório de Médias do Funcionário. Observe os Totais do Grupo 0.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047055474)

Importante : Caso o funcionário seja Horista (RA\_CATFUNC = "H") e o novo campo Jor.Variavel (RA\_HOJORVA) tenha o conteúdo 1-Sim, mas no cadastro de verbas nenhuma verba esteja no GRUPO 0 (RV\_GRPVER = "0") A média salarial não será calculada.

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

<https://tdn.totvs.com/display/public/PROT/TVMEN0_DT_Horistas_com_Jornada_Variavel>
