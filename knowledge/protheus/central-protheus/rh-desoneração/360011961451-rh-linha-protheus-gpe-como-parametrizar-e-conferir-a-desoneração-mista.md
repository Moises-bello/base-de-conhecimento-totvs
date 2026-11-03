---
article_id: 360011961451
category: RH - Desoneração
content_hash: 8ac65fc1a519066cea370c724952753153bb3a93c382c11bdadf100c9f56c2ee
fetched_at: '2026-06-28T22:43:42.263307+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar e conferir a desoneração mista
type: support-article
updated_at: '2023-11-10T20:58:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011961451-RH-Linha-Protheus-GPE-Como-parametrizar-e-conferir-a-desonera%C3%A7%C3%A3o-mista
---

**Dúvida**Como parametrizar e conferir a desoneração mista?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução****1.**Via Configurador, na rotina **Parâmetros**, pelo caminho >**Ambiente** >**Cadastros** >**Parâmetros**, preencha o parâmetro **MV\_DESFOL** com o **ano e mês** de inicio da desoneração: **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18973018101527)**

**2.**No Protheus, na rotina Verbas, pelo caminho >Atualizações >Definições de Cálculo >Verbas, deverá possuir verbas atreladas aos identificadores de cálculo abaixo:  
**ID 0973-INSS Empresa s/ Faturamento** - Base provento - Valor  
**ID 0148-INSS Empresa** - Base provento - Valor  
**ID 0991-Salário Contribuição Anterior a Desoneração (13º Sal.)** - Base provento - Valor (essa verba será calculada apenas na desoneração do 13º salário quando desoneração iniciar no decorrer do ano)  
  
**3.** Na rotina **Manutenção de Tabelas**, pelo caminho > **Atualizações** >**Definições de cálculo** >**Manutenção de Tabelas**, acesse a **Tabela S037** e na coluna **Recolhe S/Fatur.** preencha com **M**: ![](https://totvssuporte.zendesk.com/attachments/token/ivB54HslrEYC34VWRzVAtaxUA/?name=inline-1052698992.png)

**4. Cálculo da folha de pagamento** - Por regra do Sistema, deverá efetuar primeiramente o cálculo da folha e posteriormente rodar a rotina de **Desoneração da folha - GPEM013**.  
  
**5.** Para o cálculo da Desoneração da Folha, o Sistema busca os valores de duas formas:  
- Do Faturamento/Financeiro, para isso a pergunta **Verificar Integração?** deve ficar com uma das opções de **2-Faturamento, 3-Financeiro ou 4-Ambos,** dessa forma, ao executar a rotina de Desoneração da Folha (GPEM013), o Sistema alimenta automaticamente a **Tabela S033**; ou

- Lançando manualmente os valores de faturamento na **Tabela S033** antes da execução da rotina de Desoneração da Folha, a **Tabela S033** fica na rotina **Manutenção Tabelas**, pelo caminho > **Atualizações** > **Definições** **de** **Cálculo** > **Manutenção** **Tabelas**:  
![](https://totvssuporte.zendesk.com/attachments/token/hBo5stsBIh8h9TtQigwgZKpni/?name=inline1678140610.png)  
  
**6.** Calcule a desoneração pela rotina **Desoneração Folha,** pelo caminho >**Miscelânea**>**Cálculos** >**Desoneração Folha.**  
Preencha os parâmetros de acordo com a necessidade de cálculo, lembrando que o Período será preenchido automaticamente após seleção do Processo e Roteiro de acordo com o período em aberto:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013873222)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013873722)

**7.** No cálculo da desoneração, o Sistema gera o log conforme abaixo:  
![](http://tdn.totvs.com/download/attachments/384586004/image2018-7-25_10-49-12.png?version=1&modificationDate=1532526553000&api=v2)  
Resumo:>Tipo da Receita 2 (não desonerada conforme Tabela S033) = 221,903,65   
>Receita Total = 1.055.331,50 (valor base para cálculo receita **tipo 1**) + 221.903,65 (valor base para cálculo receita **tipo 2**) + 840.362,51 (valor das exportações) = 2.117,597,66  
>Receitas de Outras atividades / Receita Bruna Total = 221.903,65 / 2.117.597,66 = 0,10479028  
>Coeficiente de redução = 0,10479028  
>Alíquota Padrão = 20% conforme a tabela S037  
>Coeficiente de redução X Alíquota padrão = 0,10479028 x 20% = 2,095806%  
>Alíquota reduzida = 2,095806%

**IMPORTANTE:** Após o cálculo da desoneração, não é necessário realizar novamente o cálculo da folha para assumir os valores de desoneração, pois esse processo é realizado durante o cálculo da desoneração.

**8.** Acesse o Relatório da Folha de Pagamento, pelo caminho >**Relatórios** >**Periódicos** >**Folha de Pagamento:**  
![](http://tdn.totvs.com/download/attachments/384586004/image2018-7-25_19-20-3.png?version=1&modificationDate=1532557204000&api=v2)  
  
**Contrato** **Determinado:** Verba 781 (ID 0148) = (verba 701 (ID 0013) + verba 703 (ID 0019)) \* % alíquota reduzida informada no log de geração da desoneração = (2845,32 + 1366,00) x 2,095806% = 88,26.  
**Contrato Indeterminado:** Verba 781 (ID 0148) = (verba 701 (ID 0013) + verba 702 (ID 0014) + verba 703 (ID 0019)) \* % alíquota reduzida informada no log de geração da desoneração = (339275,50 + 57099,70 + 11943,88 + 15000,00 x 2,095806% = 8871,97

**Soma dos dois tipos de contratos:**Verba 780 ID 0973= (contrato determinado) 211,73 + (contrato indeterminado) 26171,56 = 26383,29 valor lançado no campo Contribuição Devida da S033.  
**Total Inss Empresa= 8.960,23.**

**OBS**: Para que a verba de ID 0973 (INSS Faturamento) seja apresentada no relatório da folha é necessário que  o parâmetro Impr. Total Filial esteja parametrizado com "**SIM**".  
  
**Saiba mais**  
Para adquirir mais conhecimento acesso o(s) *link*(s) abaixo:  
[RH - Linha Protheus - GPE - Qual o processo completo da Desoneração da Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053866933)  
[RH - Linha Protheus - GPE - Como parametrizar a desoneração pura](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053888253)  
[RH - Linha Protheus - GPE - Como ratear o valor da desoneração entre os funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008542221-RH-Linha-Protheus-GPE-Como-ratear-o-valor-da-desonera%C3%A7%C3%A3o-entre-os-funcion%C3%A1rios)
