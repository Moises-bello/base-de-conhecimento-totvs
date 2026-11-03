---
article_id: 40564916333719
category: Folha Mensal
content_hash: 0cd19cdfc185ee37e7649cb5faf18a6c245a316de12d9e7b7ef0013a43d19a1c
fetched_at: '2026-06-28T22:46:57.900681+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: Desconsiderar histórico de função futuro'
type: support-article
updated_at: '2026-06-18T18:29:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40564916333719-RH-RM-FOP-Folha-Anal%C3%ADtica-Desconsiderar-hist%C3%B3rico-de-fun%C3%A7%C3%A3o-futuro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40564916270487) Tempo aproximado para leitura: **00:03:29min**  
  
**Dúvida**  
Como garantir que, durante a geração da Folha Analítica Mensal, não seja considerado o histórico de função com data futura, assegurando que a função apresentada no relatório corresponda corretamente aomês e ano da competência gerada?  
  
**Ambiente**  
 TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

* 12.1.2502.223
* 12.1.2506.171
* 12.1.2510.104 e superiores

**Solução**  
Foi ajustada a descrição do parâmetro "Considerar histórico de situação de funcionário ao gerar Folha Analítica na competência atual" para **"Considerar dados do histórico de funcionário ao gerar Folha Analítica na competência atual"**. Esse parâmetro está localizado no menu **Configurações | Folha de Pagamento | Folha Normal | Geral 1/2.**

* Com o parâmetro marcado:  
  Ao gerar a Folha Analítica para a competência atual, o relatório utilizará os dados registrados nos Históricos de Seção, Histórico de Situação e Histórico de Função do funcionário.
* Com o parâmetro desmarcado:  
  Ao gerar a Folha Analítica para a competência atual, o relatório considerará os dados atuais do cadastro do funcionário (tabela PFUNC), utilizando as informações dos campos de Seção, Situação e Função exibidas na tela de funcionários.
* Para geração retroativa (competências anteriores):  
  Independente do parâmetro estar marcado ou desmarcado, o relatório sempre utilizará os dados conforme os Históricos de Seção, Históricos de Situação e Histórico de Função do funcionário.

Exemplo:

* Competência atual: 11/2024
* Funcionário teve alteração de seção, função e situação para a competência 12/2024
* Na geração da Folha Analítica para 11/2024, será considerado o histórico de seção vigente para esse mês, ignorando alterações posteriores (12/2024).

Menu **Administração de Pessoal | Funcionários | Anexos | Histórico de Seção:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40564916276247)

Menu **Administração de Pessoal | Funcionários | Anexos | Histórico de Função:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40564916280855)

Menu **Administração de Pessoal | Funcionários | Anexos | Histórico de Situação:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40564916281751)

Com o parâmetro **"Considerar dados do histórico de funcionário ao gerar Folha Analítica na competência atual"** desmarcado, a folha analítica foi gerada, utilizando os dados conforme o cadastro atual do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40564916286103)

Com o parâmetro **"Considerar dados do histórico de funcionário ao gerar Folha Analítica na competência atual"** marcado, a folha analítica foi gerada corretamente, considerando o histórico do funcionário conforme o período da competência.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40564916291607)

**Saiba Mais:**

[RH - RM - FOP - Folha Analítica: cadastro e parametrização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416042752151-RH-RM-FOP-Folha-Anal%C3%ADtica-cadastro-e-parametriza%C3%A7%C3%A3o?source=search)
