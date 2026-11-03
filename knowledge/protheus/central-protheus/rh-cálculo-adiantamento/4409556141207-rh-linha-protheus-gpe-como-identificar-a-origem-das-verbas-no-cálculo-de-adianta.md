---
article_id: 4409556141207
category: RH - Cálculo Adiantamento
content_hash: 2da3839428614121af08fb1f0010fcd6ac9460e1d3c5f79dafed4f58d9dc51f3
fetched_at: '2026-06-28T22:43:14.271361+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: 'RH - Linha Protheus - GPE - Como identificar a origem das verbas no cálculo
  de Adiantamento '
type: support-article
updated_at: '2025-04-15T12:26:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409556141207-RH-Linha-Protheus-GPE-Como-identificar-a-origem-das-verbas-no-c%C3%A1lculo-de-Adiantamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como identificar a origem das verbas no cálculo de Adiantamento   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**

A origem de uma verba depende muito do processo que o usuário realizou no Sistema.  
  
Quando o adiantamento é calculado **automaticamente** pelo Sistema, o qual observa o campo **salário** (RA\_SALARIO) e **percentual de adiantamento** (RA\_PERCADT) no cadastro do funcionário, sua origem é **A - Adiantamento**.  
Ela só aparece após o fechamento do roteiro **ADI** e carregada para **RGB**.  
ele   
![](https://totvssuporte.zendesk.com/attachments/token/s3sdMnfLFuunXxSp4HWHwxvrC/?name=inline1464417552.png)​  
  
Após o cálculo da **folha,** ela ainda permanece com a mesma origem.  
  
![](https://totvssuporte.zendesk.com/attachments/token/yh3MzGHt7k6bqBZ7qpW0VWDwx/?name=inline1606082080.png)​  
  
Contudo, se por algum motivo ela for **lançada** pelo usuário (geralmente para um ajuste de valor), ela fica com origem **I - Informada**, tanto na **RGB** quanto na **SRC** após **recalcular** **a folha**.  
  
![](https://totvssuporte.zendesk.com/attachments/token/Mzx3DjiD0Vl26cvyJqr8nCmw0/?name=inline1074086505.png)​  
​  
![](https://totvssuporte.zendesk.com/attachments/token/1CDJ42s6zS8zrmYbNVdUI9N3r/?name=inline1987417423.png)​  
  
Quando as verbas são **geradas** por outras rotinas, como **Lançamentos Fixos** e L**ançamentos Futuros,** sua origem aparece como **G - Gerada**.  
  
![](https://totvssuporte.zendesk.com/attachments/token/w3v4pwcsXZhKv8FHwoD6I5RDO/?name=inline-365037558.png)

Estes dados podem ser facilmente visualizados em **Atualizações > Lançamentos > Por Funcionário.**

**Para Saber Mais**

[RH - Linha Protheus - GPE - Adiantamento Salarial - Configurações e Conceitos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052166714-RH-Linha-Protheus-GPE-Adiantamento-Salarial-Configura%C3%A7%C3%B5es-e-Conceitos?source=search)

[RH - Linha Protheus - GPE - Verba de pensão alimentícia sobre adiantamento salarial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058874533-RH-Linha-Protheus-GPE-Verba-de-pens%C3%A3o-aliment%C3%ADcia-sobre-adiantamento-salarial?source=search)

[RH - Linha Protheus - GPE - Como conferir o desconto de IR no adiantamento para o tipo de regime de pagamento caixa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024797174-RH-Linha-Protheus-GPE-Como-conferir-o-desconto-de-IR-no-adiantamento-para-o-tipo-de-regime-de-pagamento-caixa?source=search)

[RH - Linha Protheus - GPE - Como identificar a origem das verbas gravadas no cálculo da folha e períodos abertos de fechados (tabelas SRC e SRD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016689031-RH-Linha-Protheus-GPE-Como-identificar-a-origem-das-verbas-gravadas-no-c%C3%A1lculo-da-folha-e-per%C3%ADodos-abertos-de-fechados-tabelas-SRC-e-SRD-?source=search)

[RH - Linha Protheus - GPE - Cálculo de Adiantamento não apresenta verbas de líquido para geração de arquivo CNAB e Relatório de Líquidos (GPER020)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051486074-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Adiantamento-n%C3%A3o-apresenta-verbas-de-l%C3%ADquido-para-gera%C3%A7%C3%A3o-de-arquivo-CNAB-e-Relat%C3%B3rio-de-L%C3%ADquidos-GPER020-?source=search)
