---
content_hash: 243a3b3e0a2f3900cd46c3a1095873177425e5299ae867374205017de56bbd86
fetched_at: '2026-06-29T00:05:47.088988+00:00'
page_id: '1005899558'
product: rm
source: tdn-rm
title: DT - Folha Analítica - Desconsiderar Histórico de Função Futuro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1005899558
version: 7
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Folha Analítica - Desconsiderar Histórico de Função Futuro |
| País: | Brasil |
| Issue: | [DRHROTRM-4024](https://jiraproducao.totvs.com.br/browse/DRHROTRM-4024 "View this issue") |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir dos patches:

* 12.1.2502.223
* 12.1.2506.171
* 12.1.2510.104 e superiores

## **03. SITUAÇÃO/REQUISITO**

Garantir que, durante a geração da Folha Analítica Mensal, não seja considerado o histórico de função com data futura, assegurando que a função apresentada no relatório corresponda corretamente aomês e ano da competência gerada.

## **04. SOLUÇÃO**

Foi ajustada a descrição do parâmetro "**Considerar histórico de situação de funcionário ao gerar Folha Analítica na competência atual**" para "**Considerar dados do histórico de funcionário ao gerar Folha Analítica na competência atual**". Esse parâmetro está localizado no menu Configurações | Folha de Pagamento | Folha Normal | Geral 1/2.

* Com o parâmetro marcado  
  Ao gerar a Folha Analítica para a competência atual, o relatório utilizará os dados registrados nos **Históricos de Seção, Histórico de Situação e Histórico de Função** do funcionário.
* Com o parâmetro desmarcado  
  Ao gerar a Folha Analítica para a competência atual, o relatório considerará os dados atuais do cadastro do funcionário (tabela **PFUNC**), utilizando as informações dos campos de **Seção**, **Situação** e **Função** exibidas na tela de funcionários.
* Para geração retroativa (competências anteriores)  
  Independente do parâmetro estar marcado ou desmarcado, o relatório sempre utilizará os dados conforme os **Históricos de Seção, Históricos de Situação e Histórico de Função** do funcionário.

### **Exemplo**

* Competência atual: **11/2024**
* Funcionário teve alteração de **seção, função e situação** para a competência **12/2024**
* Na geração da Folha Analítica para **11/2024**, será considerado o **histórico de seção** vigente para esse mês, ignorando alterações posteriores (12/2024).

Menu Administração de Pessoal | Funcionários | Anexos | Histórico de Seção

Menu Administração de Pessoal | Funcionários | Anexos | Histórico de Função

Menu Administração de Pessoal | Funcionários | Anexos | Histórico de Situação

Com o parâmetro **"Considerar dados do histórico de funcionário ao gerar Folha Analítica na competência atual"** desmarcado, a folha analítica foi gerada, utilizando os dados conforme o cadastro atual do funcionário.

Com o parâmetro **"Considerar dados do histórico de funcionário ao gerar Folha Analítica na competência atual"** marcado, a folha analítica foi gerada corretamente, considerando o histórico do funcionário conforme o período da competência.

## **05. DEMAIS INFORMAÇÕES**

* [Folha Analítica](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719339)
* [Parametrizador | Folha de Pagamento | Folha Normal - Geral 1/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719263)
