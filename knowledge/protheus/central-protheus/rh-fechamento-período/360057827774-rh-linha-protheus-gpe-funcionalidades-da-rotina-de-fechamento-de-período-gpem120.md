---
article_id: 360057827774
category: RH - Fechamento Período
content_hash: 3f2fd6c47aa04db28b6c8c9701a2b788d48152043edde2c46192f8bf5529cfe3
fetched_at: '2026-06-28T22:43:24.458644+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidades da rotina de Fechamento de Período
  - GPEM120
type: support-article
updated_at: '2024-06-24T12:44:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057827774-RH-Linha-Protheus-GPE-Funcionalidades-da-rotina-de-Fechamento-de-Per%C3%ADodo-GPEM120
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22323370544023) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Funcionalidades do fechamento GPEM120  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2210

**Solução**A rotina de Fechamento é responsável pela **geração** **dos dados** do arquivo de **movimento acumulado** dos roteiros de cálculo, **atualizando** os dados a fim de preparar o processamento da Folha de Pagamento do mês seguinte, baseado nos dados do mês calculado.

* **Lançamentos Por Funcionário:**  
  Prepara o arquivo de Lançamentos Por Funcionário para o mês seguinte (RGB).
* **Cadastro de Funcionários:**  
  Atualiza o Cadastro de Funcionário, em função dos dependentes que ultrapassaram o limite de idade para salário família e Imposto de Renda, Situação, Contribuição Sindical, alteração de Nome/Endereço entre outros campos.
* **Lançamentos Futuros:**  
  Baixa as parcelas pagas do arquivo de Lançamentos Futuros (SRK).
* **Acumulados:**  
  Grava os lançamentos do mês no arquivo de Acumulados (SRD).
* **Férias:**  
  Atualiza a data base de férias dos funcionários que estiveram de férias durante o mês.  
  A cada fechamento mensal são adicionados avos de direito no COntrole de Dias de Direito e criados novos períodos de férias, não sendo necessário cadastrá-los manualmente.
* **Afastamento:**  
  Promove a troca dos períodos de férias dos funcionários que estão retornando de afastamento durante o mês, dos que ficaram afastados por mais de 6 meses e que perderam o período aquisitivo de férias.
* **Histórico de Benefícios:**  
  Atualiza o arquivo de Histórico de Benefícios (RG2) e de Outros Benefícios (RIR).
* **Histórico de Cálculo PLR:**Atualiza o arquivo de Histórico de Cálculo PLR (RG4).
* **Valores e Modificações Salariais:**  
  Atualiza os arquivos de Histórico Valores Salariais (SR3) e Histórico de Modificações Salariais (SR7) quando houver aumento salarial.
* **Cadastro de Períodos**  
  Atualiza os roteiros do período fechado para não selecionado e faz a abertura do período posterior da folha e demais roteiros previamente cadastrados (RFQ e RCH).  
  Grava o código e nome do usuário que efetuou o fechamento do roteiro (RCH)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14012252462743)

* Data de Fechamento (RCH\_DTFECH): Data em que fora realizado o fechamento.
* Período Selecionado (RCH\_PERSEL): Atualiza para **2-Não**, informando que o roteiro para este período não está mais ativo. Atualizando com **1-Sim** o roteiro cadastrado no período subsequente.
* *Status* (RCH\_STATUS): Informa que o roteiro em questão foi fechado.
* *Status* (RFQ\_STATUS): Atualiza para **2-Fechado**’ na ocasião em que todos os roteiros cadastrados para aquele período forem fechados.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Fechamento mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027259971?source=search)

[RH - Linha Protheus - GPE - Melhoria de performance no fechamento mensal com MV\_CALCTHD ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050884333?source=search)

[RH - Linha Protheus - GPE - Implementação de GRID no Fechamento de Período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19124711142679?source=search)

[RH - Linha Protheus - GPE - Implementação do Multi Thread no fechamento da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034908554?source=search)

[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
