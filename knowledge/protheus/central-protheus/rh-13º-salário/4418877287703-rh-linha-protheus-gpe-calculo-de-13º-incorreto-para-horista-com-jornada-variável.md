---
article_id: 4418877287703
category: RH - 13º salário
content_hash: 227db63982475180b16db0771476faf19860a5965dd891af9bd044b53c44daf6
fetched_at: '2026-06-28T22:44:00.445151+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo de 13º Incorreto para Horista com Jornada
  Variável
type: support-article
updated_at: '2026-06-25T11:37:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418877287703-RH-Linha-Protheus-GPE-Calculo-de-13%C2%BA-Incorreto-para-Horista-com-Jornada-Vari%C3%A1vel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18860684184983) Tempo aproximado para leitura: **00:04:00 min**

**Ocorrência**  
Ao calcular o **13° Segunda parcela** para **Horista com Jornada variável** e conferir o **cálculo com o relatório de Médias - GPER080,** os valores **não batem.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**  
O incidente ocorre normalmente quando o mnemônico **P\_REFMED esta desativado,** e a emissão do relatório de médias é feito com **referência 31/12**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Confira os principais pontos:   
  
Na rotina Funcionários GPEA010 em **Atualizações > Funcionários > Funcionários (GPEA010)** o funcionário deve estar cadastrado como Horista com o campo Jornada Variável - **RA\_HOJORVA = SIM e Cat. Func - RA\_CATFUNC = H**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18860684196503)  
  
  
Na rotina de Verbas GPEA040 em **Atualizações > Definições de Cálculo > Verbas (GPEA040)** as verbas de **Salário Horista - ID 0032** e **DSR Horista - ID 0033**, devem estar configuradas no campo **Grupo de Verba - RV\_GRPVERB com conteúdo** = **0**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18860684210199)

2. Emissão do **GPER080** - Demonstrativo de médias com referência **31/12** em **Relatórios > Lançamentos > Demonstrativo de médias.**  
  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418865464087)  
  
Calculo efetuado Roteiro 132, com o mnemônico **P\_REFMED desativado**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418865542679)  
  
Com esta configuração no mnemônico, o cálculo das médias do roteiro 132 **será feito considerando referência 01/12/2021**, mesmo que nos parâmetros de cálculo esteja referência 31/12, assim, para conferir o cálculo, deve-se **emitir o relatório de médias - GPER080 com referência 01/12/2021 e não 31/12/2021** onde a média será  **dividida por 11 e não por 12.**  
  
Assim, para conferir, emita o **GPER080 com referência 01/12/2021**, utilize a **soma dos valores das verbas do Grupo 0 - Verba 002 (ID 0032) + Verba 013 (ID 0033) = 25.467,50** que **consta no relatório** e **divida por 11 = R$ 2.315,26.** Avaliando o cálculo, temos as **verbas 010** e **254** que ao serem **somadas,** temos exatamente **o valor de 2.315,26.**  
  
3. Caso queira que o cálculo considere a **referência informada nos parâmetros de 31/12/2021**, configure o **mnemônico P\_REFMED com .T. - Ativado**  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418884972567)  
  
Faça a emissão do **Relatório de Médias - GPER080 com referência 31/12/2021**   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418865464087)  
  
Calculo  efetuado Roteiro 132, com o **mnemônico P\_REFMED ativado.** Para ativar o mnemônico acesse a rotina GPEA300 - Mnemônicos em **Atualizações > Definições de Cálculo > Mnemônicos.**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418884937239)  
  
Com esta configuração no mnemônico, o cálculo das médias do roteiro 132 **será feito considerando referência 31/12/2021**, conforme informada nos parâmetros cálculo, assim, para conferir o cálculo, deve-se **emitir o relatório de médias - GPER080 com referência 31/12/2021** onde a média será  **dividida por 12.**  
  
Assim, para conferir, emita o **GPER080 com referência 31/12/2021**, utilize a **soma dos valores das verbas do Grupo 0 - Verba 002 (ID 0032) + Verba 013 (ID 0033) = 25.467,50** que **consta no relatório** e **divida por 12 = R$ 2.122,29.** Avaliando o cálculo, temos as **verbas 010** e **254** que ao serem **somadas,** temos exatamente **o valor de 2.122,29.**  
  
**Saber Mais:**

[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
**Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento:**[**https://www.youtube.com/watch?v=T7b4zMlphTI**](https://www.youtube.com/watch?v=T7b4zMlphTI)
