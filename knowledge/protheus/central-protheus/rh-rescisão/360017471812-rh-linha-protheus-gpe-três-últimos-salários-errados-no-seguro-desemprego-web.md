---
article_id: 360017471812
category: RH - Rescisão
content_hash: 0c2c91f9f0dc4715795711301942ec0e3a06e513a5983e1361e531e86e6e3cea
fetched_at: '2026-06-28T22:43:48.442452+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Três últimos salários errados no Seguro Desemprego
  WEB
type: support-article
updated_at: '2025-09-11T01:06:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017471812-RH-Linha-Protheus-GPE-Tr%C3%AAs-%C3%BAltimos-sal%C3%A1rios-errados-no-Seguro-Desemprego-WEB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34845764299799) Tempo aproximado para leitura:** **00:02:00 min****Ocorrência**Ao gerar o Seguro Desemprego *WEB* (**GPEM090**), os últimos três salários estão sendo gerados errados no arquivo SEGDES.SD.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as Versões.  
  
**Causa**Esse problema pode ocorrer por dois motivos: **1.** Quando no parâmetro de geração do Seguro Desemprego *Web*, nos campos **Verbas do Acumulado** e **Compl. Verbas Acumulado** tem informações de verbas indevidamente.  
  
**2.** Quando no **Acumulado** do funcionário **não tem** a **verba de ID 0318-Salario do Mês** (em casos de funcionários com salário fixo), pois o sistema carrega automaticamente o valor desta verba para o Seguro Desemprego *Web*, então se no acumulado do funcionário com salário fixo não há essa verba com o valor do salário do funcionário, os campos referente aos últimos salários dos funcionários ficarão errados ou em branco.Quando no **Acumulado** do funcionário **não tem** a **verba de ID 0318-Salario do Mês** (em casos de funcionários com salário fixo), pois o sistema carrega automaticamente o valor desta verba para o Seguro Desemprego *Web*, então se no acumulado do funcionário com salário fixo não há essa verba com o valor do salário do funcionário, os campos referente aos últimos salários dos funcionários ficarão errados ou em branco.  
  
**Solução**Os campos abaixo devem ficar em **branco** para funcionários que possuem **salário fixo**, pois o sistema gera o valor do salário da verba com **ID**  **0318** (Salário do mês) e soma com a informação existente nestes campos duplicando o valor.

Estes campos devem ser **utilizados** quando o funcionário **não possui remuneração fixa** ou quando é necessário informar verbas **de remuneração variável (hora extras por exemplo):**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013041731)  
  
  
**Saiba mais**

[RH - Linha Protheus - GPE - No Seguro Desemprego WEB os campos 'Soma dos três Últimos Salários' e 'Últimos Meses trabalhados' ficam em branco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018281132-RH-Linha-Protheus-GPE-No-Seguro-Desemprego-WEB-os-campos-Soma-dos-tr%C3%AAs-%C3%9Altimos-Sal%C3%A1rios-e-%C3%9Altimos-Meses-trabalhados-ficam-em-branco?source=search)

<https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o>
