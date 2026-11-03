---
article_id: 360060756613
category: RH - Provisão
content_hash: d5fdd479ae881a3adbb3987e1482b7dd2f2f587f1f98c0130f44d9a9b651544c
fetched_at: '2026-06-28T22:43:55.762520+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Conferir o INSS nas Provisões de Férias e
  13º Salário quando há Alteração dos Percentuais de Encargos de Empresa
type: support-article
updated_at: '2025-10-24T12:52:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060756613-RH-Linha-Protheus-GPE-Como-Conferir-o-INSS-nas-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio-quando-h%C3%A1-Altera%C3%A7%C3%A3o-dos-Percentuais-de-Encargos-de-Empresa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998096093079)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como Conferir o INSS nas Provisões de Férias e 13º Salário quando há Alteração dos Percentuais de Encargos de Empresa?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O percentual de Cálculo de INSS nas **Provisões**, são considerados de acordo com as informações contidas nas tabelas de Encargos de Empresa.  
Quando há alteração do percentual de INSS Patronal, realize os seguintes passos para identificar o percentual INSS utilizado no cálculo das Provisões:  
1. Acesse: Atualizações / Definições de Cálculo / **Manutenção de Tabelas** (**GPEA320**) e Visualize as Tabelas **S037** e **S038** e some os percentuais de INSS Patronal;  
Na tabela S037, serão considerados os campos "**% Empresa**" e "**%Acid. Trab.**", e na tabela S038, o campo "**% Terceiros**", como destacado no exemplo abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000494162)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101591653)

Considerando este exemplo, o Percentual de INSS Patronal será de 26,80%.

2. Acesse: Relatórios / Provisões / **Provisão de Férias** (**GPER070**) e preencha os parâmetros para emissão do Relatório de Provisão de Férias do Período em que deseja fazer a conferência dos valores de INSS.  
A Conferência deve ser realizada considerando a Linha "**Atual**" do relatório e não a linha "**No Mês**", tendo em vista que o cálculo de provisão é realizado considerando o valor Acumulado do funcionário, e não o valor Mensal.  
No exemplo abaixo, a conferência deve ser realizada da seguinte forma: Total das Férias x 26,80% = INSS:

23.014,82 x 26,80% = **6.167,97**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000494442)  
3. Acesse: Relatórios / Provisões / **Provisão 13º Salário** (**GPER090**) e preencha os parâmetros para emissão do Relatório de Provisão de 13º Salário do Período em que deseja fazer a conferência dos valores de INSS e realize as conferências considerando as mesmas orientações do passo 2.  
Total 13o Salário x 26,80% = INSS:

10.068,99 x 26,80% =**2.698,48**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101592213)

Observação: Tanto para os relatórios de Provisão de Férias quanto para os relatórios de Provisão de 13º Salário, a linha "**No Mês**" representa a diferença entre o valor de provisão Atual, e o valor de provisão calculado no mês Anterior, por este motivo a conferência não deve ser realizada considerando os valores desta linha.

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
