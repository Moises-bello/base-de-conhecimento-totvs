---
article_id: 360052314713
category: RH - Férias
content_hash: 0778f0e7fac8c2342f89b0977e166ce33455095613ee702e64a1980065681dfd
fetched_at: '2026-06-28T22:43:58.306551+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Memória de cálculo das férias
type: support-article
updated_at: '2025-09-24T11:37:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052314713-RH-Linha-Protheus-GPE-Mem%C3%B3ria-de-c%C3%A1lculo-das-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32378227096727) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como imprimir relatório de memória de cálculo das férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para impressão do Relatório, realize os seguintes passos:  
  
1. Acesse: **SIGAGPE > Atualizações > Definições de Cálculo > Mnemônicos** e altere o Mnemônico **P\_LMEMCALC** para **.T.** para que possa ser recriadas as fórmulas com o Log ativado.  
**Toda vez** que este mnemônico for alterado as fórmulas serão recriadas.

![](https://tdn.totvs.com/download/attachments/330831446/image2019-8-12_9-21-0.png?version=1&modificationDate=1565612460647&api=v2)

2. **Execute o Cálculo** das férias normalmente   
  
3. Após o cálculo o Log estará disponível para consulta na rotina de **Cálculo de Férias (Miscelanea/ Cálculos/ Férias - GPEM030).**Selecione o funcionário deseja no *browser* da rotina de clique em **Outras Ações/ Consultar Memória de Cálculo.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32378259246487)

**Consulta da Memória de Cálculo:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32378227099543)

4. Para impressão do **Relatório de Memória de Cálculo**, selecione a opção Relatório Memória de Cálculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32378227104023)

Configure os parâmetros para selecionar o cálculo que deseja imprimir

* **Processo:**Selecione o Processo de cálculo que deseja imprimir
* **Roteiro:**Selecione o Roteiro de cálculo que deseja imprimir
* **Período:**Através da Consulta Padrão (F3), selecione o Período, Nr. Pagamento, Data e Hora de Geração do cálculo que deseja imprimir. Os registros listados são filtrados pelo Processo e Roteiro informados nas perguntas anteriores. Os registros estão ordenados por Data e Hora de Geração em ordem decrescente, do mais novo ao mais antigo.
* **Filial:**Pergunta do tipo *range*. Informe a(s) filial(ais) que deseja imprimir ou mantenha em branco para imprimir todas as filiais do cálculo selecionado.
* **Matrícula:**Pergunta do tipo *range*. Informe a(s) matricula(s) que deseja imprimir ou mantenha em branco para imprimir todas as matrículas do cálculo selecionado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32378259249047)

**Relatório de Memória de Cálculo:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32378259250583)

**Atenção**O mnemônico **P\_LMEMCALC** deve ser desativado após sua utilização para conferência do cálculo, pois estando habilitado durante o processamento normal das rotinas que geram memória de cálculo, acarretará a **perda de performance** do ambiente.

Saiba Mais  
[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)  
[RH - Linha Protheus - GPE - Como visualizar cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057823253-RH-Linha-Protheus-GPE-Como-visualizar-c%C3%A1lculo-de-f%C3%A9rias)  
[RH - Linha Protheus - GPE - Como cancelar cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050830934-RH-Linha-Protheus-GPE-Como-cancelar-c%C3%A1lculo-de-f%C3%A9rias)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de Médias para Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726351592855-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-M%C3%A9dias-para-F%C3%A9rias)
