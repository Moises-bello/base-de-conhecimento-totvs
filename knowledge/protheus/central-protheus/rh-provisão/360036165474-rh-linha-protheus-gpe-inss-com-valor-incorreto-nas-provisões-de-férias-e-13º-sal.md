---
article_id: 360036165474
category: RH - Provisão
content_hash: 62ad77a5508dd25069f25bab49d6b9b14aa9d811a96c91dff135d3d386291570
fetched_at: '2026-06-28T22:43:55.931871+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - INSS com valor incorreto nas Provisões de Férias
  e 13º Salário
type: support-article
updated_at: '2025-10-24T12:04:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036165474-RH-Linha-Protheus-GPE-INSS-com-valor-incorreto-nas-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998747671831)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**O que Analisar quando o Cálculo do INSS está incorreto nas Provisões de Férias e 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para compor o percentual de INSS nas provisões, são considerados os valores informados na tabela S037 e S038.   
Se ao calcular as Provisões de Férias e 13º Salário o valor de INSS estiver incorreto, realize os seguintes passos para identificar o percentual INSS utilizado no cálculo das provisões:  
  
1. Acesse: Atualizações / Definições de Cálculo / Manutenção de Tabelas / Selecione a Tabela S037 e verifique o preenchimento dos campos **%Empresa**, **%Acid.Trab**;  
  
2. Acesse: Atualizações / Definições de Cálculo / Manutenção de Tabelas / Selecione a Tabela S038 e verifique o preenchimento do campo **%Terceiros**.   
Caso a empresa recolha INSS referente à Outras Entidades (SESC, SENAI, SENAC...), os campos destacados abaixo também serão considerados na composição do percentual de INSS nas provisões:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048202653)  
  
3. Verifique se o cálculo do INSS das Provisões de Férias e 13º Salário de um funcionário como exemplo, está coerente com o resultado da soma entre os percentuais das tabelas S037 e S038.  
Observação: A linha a ser considerada para conferência dos valores de INSS é a linha "Atual" do Relatório de Provisão.  
  
4. Caso o valor do INSS não bata com o percentual localizado, acesse: Atualizações / Cadastros / Centro de Custos, e verifique se no Cadastro Centro de Custo do funcionário, os campos destacados abaixo estão preenchidos:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047315214)

Se os campos estiverem preenchidos, o sistema desconsidera os percentuais informados nas tabelas S037 e S038, e considera os percentuais informados no cadastro do Centro de Custo.  
  
5. Caso o valor do INSS ainda esteja incorreto com o percentual localizado, acesse: Atualizações / Funcionários / Funcionários, e verifique se no Cadastro do Funcionário, o campo **%Acid.Trab.** (RA\_PERCSAT) está preenchido:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047315294)  
  
Se o campo estiver preenchido, o sistema desconsidera os percentuais informados nas tabelas S037 e S038, e considera o percentual informado no cadastro do Funcionário.  
  
Vale lembrar que o percentual de INSS na provisão, deve ser o mesmo percentual utilizado no cálculo da Folha de Pagamento, para que não haja divergências entre o relatório de provisão e a contabilização.

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035904253-MP-GPE-Como-conferir-o-c%C3%A1lculo-do-INSS-na-Provis%C3%A3o-com-Percentuais-de-INCRA-SESI-SENAI-SENAC-SEBRAE-SENAR-SECONC-SEST-SENAT-ou-SESCOOP>
