---
article_id: 1500008869502
category: RH - Provisão
content_hash: 45628917e5aaa9500700de32a952432f788457f58d70592bbc737899ccbf257b
fetched_at: '2026-06-28T22:43:56.806956+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Qual alíquota utilizada no calculo do INSS na Provisão
  de 13º Salário quando a empresa possui desoneração Mista
type: support-article
updated_at: '2025-10-24T13:00:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008869502-RH-Linha-Protheus-GPE-Qual-al%C3%ADquota-utilizada-no-calculo-do-INSS-na-Provis%C3%A3o-de-13%C2%BA-Sal%C3%A1rio-quando-a-empresa-possui-desonera%C3%A7%C3%A3o-Mista
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32997913665559) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Qual alíquota utilizada no calculo do INSS na Provisão de 13º Salário quando a empresa possui desoneração Mista?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  GPE Gestão de Pessoal – Todas as versões.  
  
**Solução**As empresas com desoneração mista tem a alíquota formada por:  
**% Alíquota reduzida + % Terceiros (S038) + % Acid. Trab. (S037)**No caso da **Provisão do Décimo Terceiro Salário**, é necessário executar o Cálculo da Desoneração do 13º Salário, para identificar o Percentual de Desoneração utilizado, este será diferente da Folha de Pagamento, uma vez que no 13º é apurado todos os valores da **Tabela S033 - Faturamento Mensal** do ano processado.  
Veja o exemplo abaixo:  
  
**1.** Tabela S033 - Faturamento Mensal (acesse **Atualizações** -> **Definições** **de** **Cálculo** -> **Manutenção** **de** **Tabelas**): período a ser calculado, destacado:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013644861)  
 **2.** Tabela S037 - Encargos Empresa (acesse **Atualizações** -> **Definições** **de** **Cálculo** -> **Manutenção** **de** **Tabelas**): desta tabela é anotado o percentual do Acid. Trab. que neste exemplo é 0,5000:  
**![](https://tdn.totvs.com/download/attachments/614377490/image2021-4-26_14-9-3.png?version=1&modificationDate=1619460524443&api=v2)****3.** Tabela S038 - Outras Entidades (acesse **Atualizações** -> **Definições** **de** **Cálculo** -> **Manutenção** **de** **Tabelas**): desta tabela é retirado o percentual de Terceiros,  5,8000:  
**![](https://tdn.totvs.com/download/attachments/614377490/image2021-4-26_14-9-31.png?version=1&modificationDate=1619460524370&api=v2)****4. Provisões** **de** **Férias**/**13º** **Salário** **- GPEA070** (acesse **Miscelânea** -> **Provisões** -> **Provisões** **de** **Férias**/**13º** **Salário**): o intuito é identificar como foi efetuado o cálculo da verba de INSS Provisão 13º Salário   
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013644961)  
  
Até o passo 4, já foi possível identificar os percentuais de Acid. Trab. e Terceiros  
**% Alíquota reduzida + % Terceiros (S038) + % Acid. Trab. (S037)**  
Alíquota reduzida + 5,80000 + 0,5000  
  
**5.** Para descobrir o Percentual da Alíquota Reduzida é necessário executar a Desoneração do 13º Salário.  
Habilite o Roteiro 132, pode ser no período de Dezembro do ano vigente, em seguida execute o cálculo pela rotina **Desoneração Folha - GPEM013** (acesse **Miscelânea** -> **Cálculos** -> **Desoneração Folha**)  
Log da rotina demonstrando a alíquota reduzida:  
*​![](https://totvssuporte.zendesk.com/attachments/token/18KKL0FWtayAyvsNEFttXzpo2/?name=inline-573717673.png)***% Alíquota reduzida + % Terceiros (S038) + % Acid. Trab. (S037)**3,098592 + 5,80000 + 0,5000 = **9,398592**Total da Provisão de 13º Salário = 1.815,27 x 9,398592 % = **170,60**O mesmo cálculo pode ser realizado para a conferencia da Provisão no mês, apresentada no Relatório da Provisão.  
  
**Saiba Mais:**  
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
