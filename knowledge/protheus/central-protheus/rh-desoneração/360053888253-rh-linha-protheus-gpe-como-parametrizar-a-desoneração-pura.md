---
article_id: 360053888253
category: RH - Desoneração
content_hash: 26e2a9067f18e1f9fc17572fba93af5f4ea03653ab1ccd5eed8f1926cbf4dd1e
fetched_at: '2026-06-28T22:43:42.193211+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar a desoneração pura
type: support-article
updated_at: '2023-11-10T20:57:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053888253-RH-Linha-Protheus-GPE-Como-parametrizar-a-desonera%C3%A7%C3%A3o-pura
---

**Dúvida**Como parametrizar a Desoneração pura da Folha de Pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal - Todas as versões  
  
**Solução****1.** Via Configurador, na rotina **Parâmetros**, pelo caminho > **Ambiente** > **Cadastros** > **Parâmetros**, preencha o parâmetro **MV\_DESFOL** com o ano e mês de inicio da desoneração:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012456102)  
  
**2.** Na rotina **Manutenção de Tabelas**, pelo caminho > **Atualização** > **Definições de Cálculo** > **Manutenção Tabela**, na **Tabela S037**, deixe a coluna **Recolhe S/ Fatur**. com **S**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089050253)

**3.**Na rotina **Verbas**, pelo caminho > **Atualizações** > **Definições de Cálculo** > **Verbas**, deve ser cadastrada uma verba como Base Provento relacionada ao **ID 0973** - **INSS sobre Faturamento**, nesta verba que será apresentada no resumo da folha o valor desonerado:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012456302)  
  
  
**4. Cálculo da folha de pagamento** - Por regra do Sistema, deverá efetuar primeiramente o cálculo da folha e posteriormente rodar a rotina de **Desoneração da folha - GPEM013**.  
  
**5.**Para o cálculo da Desoneração da Folha, o Sistema busca os valores de duas formas: Do Faturamento/Financeiro, onde ao executar a rotina de Desoneração da Folha (GPEM013), o Sistema alimenta automaticamente a **Tabela S033**, ou lançando manualmente os valores de faturamento na Tabela S033 antes da execução da rotina de Desoneração da Folha.  
A **Tabela S033** fica na rotina Manutenção Tabelas, pelo caminho > **Atualizações** > **Definições** **de** **Cálculo** > **Manutenção** **Tabelas**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087903314)  
  
**6.** Execute a rotina Desoneração Folha - GPEM013, preencha os parâmetros de acordo com a necessidade de cálculo, lembrando que o Período será preenchido automaticamente após seleção do Processo e Roteiro de acordo com o período em aberto:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18972196048023)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18972179011991)

**7.** No final do cálculo da Desoneração, o Sistema gerará o log com o percentual desonerado:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089052353)  
  
**8.** Após a geração da Desoneração da Folha, não é necessário executar novamente o cálculo da folha para assumir os valores da desoneração, pois na execução da Desoneração esse processo já é realizado. Verifique no Resumo da folha impressa através do Relatório da Folha de pagamento (GPER040 OU GPER106) os valores de desoneração:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089055233)  
  
**OBS.:** Por se tratar de Desoneração Pura, o sistema substituirá os 20% da parte patronal pela DARF de desoneração, e consequentemente a verba com Id 0148 - INSS Parte Empresa não será apresentado no cálculo da folha.

Para que a verba de ID 0973 (INSS Faturamento) seja apresentada no relatório da folha é necessário que  o parâmetro Impr. Total Filial esteja parametrizado com "**SIM**".  
  
  
**Saiba mais**  
Para adquirir mais conhecimento acesso o(s) *link*(s) abaixo:  
[MP - GPE - Desoneração Orientação campo a campo da tabela S033.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046988434-MP-GPE-Desonera%C3%A7%C3%A3o-Orienta%C3%A7%C3%A3o-campo-a-campo-da-tabela-S033-)
