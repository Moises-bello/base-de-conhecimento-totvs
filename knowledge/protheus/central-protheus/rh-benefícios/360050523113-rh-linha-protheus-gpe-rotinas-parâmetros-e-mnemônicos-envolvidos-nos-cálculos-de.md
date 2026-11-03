---
article_id: 360050523113
category: RH - Benefícios
content_hash: ab610555037c85b8a923766365a0abe4b7ede219f48df078d4c95d54330b7aca
fetched_at: '2026-06-28T22:44:04.794832+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Rotinas, Parâmetros e Mnemônicos envolvidos nos
  cálculos de Benefícios (VT/VR/VA)
type: support-article
updated_at: '2025-09-19T11:44:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050523113-RH-Linha-Protheus-GPE-Rotinas-Par%C3%A2metros-e-Mnem%C3%B4nicos-envolvidos-nos-c%C3%A1lculos-de-Benef%C3%ADcios-VT-VR-VA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32867199996183) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Quais são as Rotinas, Parâmetros e Mnemônicos envolvidos nos cálculos de Benefícios (VR/VA/VT)?  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**As rotinas, parâmetros e mnemônicos utilizados para cálculo dos benefícios são:

**Fontes:**

**- GPEXCBEN** - Cálculo de Benefícios

**- GPEXFORM** - Fórmulas

**- GPEA012** - Cadastro Vale Refeição

**- GPEA013** - Cadastro vale Alimentação

**- GPEA140** - Meios de Transporte

**- GPEA131** - Atualização Benefícios (vínculo do funcionário com tipo de benefício)

**- GPEA133** - Cadastro Benefícios

**- GPFO1BRA** - Atualização Fórmulas

**- GPFO2BRA** - Atualização Fórmulas

**- GPFORBRA** - Atualização Fórmulas

**- GP131CALC** - Chamado do Cálculo de Benefícios

**Parâmetros:**

**- MV\_USACPER** **-** Indica se o cálculo dos benefícios irá utilizar o calendário do período ou a escala do ponto (**.T.** = Período e **.F.** = Escala do Ponto);

**- MV\_TPCALEN** **-** Determina Tipo do Calendário (**1**=Analítico e **2**=Sintético);

**- MV\_CVTUSO** **-** Determina se verifica parâmetro **MV\_CVTPROP** no  cálculo do vale transporte (1 = Sim e 2 = Não)

**- MV\_CVTPROP** **-** Define a base de cálculo para o desconto do Vale Transporte ( Dias Trabalhados = **T,** Dias de Vale Transporte = **P**,  Dias de Saldo trabalhados **S,** e o Salario Integral = **I**)

**-MV\_DIASPER** **-** Determina a quantidade de dias do período para cálculo.  (**1** = Se o divisor será a quantidade de dias do mês do período e **2** = Se o divisor será sempre 30).;

**- MV\_BENEXGS** **-** Define se o cálculo retroativo de benefícios, deve considerar registros do Gestão de Serviços. (**.T.** = Sim e **.F.** = Não);

**- MV\_CALCBEN** **-** Indica se deseja efetuar o cálculo dos vales (VA/VR/VT) no formato novo com utilização da tabela SM7. (**.F.** = Antigo e **.T.** = Novo);

**Mnemônicos:**

**- P\_LDSRHRSP -** Verifica as horas previstas na escala de horário de ponto

**- P\_QTDIAMES -** Quantidade de dias do mês para cálculo

**- P\_NTOTDIAS** - Dias da semana para semanalista

**- P\_SALHBEN -** Considera lançamento para calcular VT para funcionário horista

**- P\_BENPONEV -** Eventos do ponto para desconto de benefícios

**- P\_BENBUSFA -** Quantidade de meses retroativos ao cálculo de benefícios para buscar faltas  
**- P\_NVAFABEN -** Utiliza tabela S153 para calcular benefícios   
**- P\_INTPERAT -** Integração dos roteiros (VT/VR/VA) seja efetuado no período da folha que está aberto  
**- P\_RECALCVT -** Efetuar o recálculo do VT realizado no período anterior

**Saiba Mais**[Manual do Cálculo de Benefícios](https://tdn.totvs.com/pages/viewpage.action?pageId=904043923)  
[RH - Linha Protheus - GPE - Memória de Cálculo de Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043182293-RH-Linha-Protheus-GPE-Mem%C3%B3ria-de-C%C3%A1lculo-de-Benef%C3%ADcios)
