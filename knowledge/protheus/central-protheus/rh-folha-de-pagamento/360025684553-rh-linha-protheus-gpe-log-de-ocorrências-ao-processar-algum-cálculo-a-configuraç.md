---
article_id: 360025684553
category: RH - Folha de Pagamento
content_hash: b6287211975d75ebbfb3b069ad304414f37b4291ddf06d2f6016bd56639c9951
fetched_at: '2026-06-28T22:44:15.048678+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Log de Ocorrências ao processar algum Cálculo -
  A Configuração dos Períodos está Incorreta, ou não existem dados válidos no Período
  que está sendo Calculado
type: support-article
updated_at: '2025-05-12T16:38:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025684553-RH-Linha-Protheus-GPE-Log-de-Ocorr%C3%AAncias-ao-processar-algum-C%C3%A1lculo-A-Configura%C3%A7%C3%A3o-dos-Per%C3%ADodos-est%C3%A1-Incorreta-ou-n%C3%A3o-existem-dados-v%C3%A1lidos-no-Per%C3%ADodo-que-est%C3%A1-sendo-Calculado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26273606765847) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**O que analisar quando é exibido o Log de Ocorrências - A Configuração dos Períodos está Incorreta, ou não existem dados válidos no Período que está sendo Calculado?  
  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039666934)**

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse **Atualizações** > **Definições de Cálculo** > **Períodos** e verifique se a data fim corresponde realmente ao último dia do mês. Em meses que tem 31 dias a data fim deve ser obrigatoriamente 31/XX/XXXX   
2. Acesse **Atualizações** > **Definições de Cálculo** > **Períodos** e verifique se existe o próximo Período e Roteiro em questão já cadastrado, caso não tenha, inclua;  
3. Acesse **Atualizações** > **Definições de Cálculo** > **Períodos** > Aba **Calendário** e verifique se os campos **Horas DSR** e **Dias DSR** estão preenchidos;  
4. Acesse **Atualizações** > **Ponto Eletrônico** > **Turno de Trabalho** e verifique se os campos **Id.Acre.Not** (R6\_IDACREN), **Aut.He.Fer** (R6\_AUTOHEF) e **Mc.Imp.JC.** (R6\_MCIMPJC) estão preenchidos;  
5. Acesse **Atualizações** > **Funcionários** > **Funcionários** e verifique na aba Funcionais, se os campos **Hrs. Mensais** (RA\_HRSMES), **Hrs. Semanais** (RA\_HRSEMAN) e **Horas Dia** (RA\_HRSDIA) estão preenchidos.  
6. Após fazer os ajustes, faça o cálculo novamente.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
