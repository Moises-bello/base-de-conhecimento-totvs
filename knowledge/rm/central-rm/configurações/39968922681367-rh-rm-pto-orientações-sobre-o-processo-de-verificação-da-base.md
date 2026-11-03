---
article_id: 39968922681367
category: Configurações
content_hash: 90da9cd23b6be3a753fbf5bf5358b103116b74850b46902a845b4bbff7a9be79
fetched_at: '2026-06-28T22:46:29.834270+00:00'
product: rm
section_id: 1500000835121
source: central-rm
title: RH - RM - PTO - Orientações sobre o processo de Verificação da Base
type: support-article
updated_at: '2026-04-29T11:51:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39968922681367-RH-RM-PTO-Orienta%C3%A7%C3%B5es-sobre-o-processo-de-Verifica%C3%A7%C3%A3o-da-Base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39968922641687) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como funciona o processo de Verificação da Base no módulo de Automação de Ponto e quais os critérios para a identificação de inconsistências.  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1  
  
**Solução**  
O processo de Verificação da Base identifica inconsistências em dois níveis: Erros, que impossibilitam a execução de processos ou geram dados incorretos, e Avisos, que indicam pontos de atenção sem necessariamente bloquear o sistema. A verificação abrange históricos de funcionários, integridade de horários, interseção de períodos e compatibilidade de parâmetros.

**Passos**

Abaixo, os itens detalhados que são validados durante o processo:

**1. Cadastro de Funcionários**

* **Histórico de Horários:** Verifica se existem funcionários com histórico nulo, o que gera Erro por impedir o cálculo.
* **Exceção para Professores:** Caso o funcionário seja professor e utilize o horário do Classis, o erro não é gerado.
* **Histórico de Seções:** Valida se a seção atual do funcionário consta em seu histórico de seções, gerando Erro em caso de ausência.

**2. Cadastro de Horários**

* **Interseção de Intervalos:** Verifica se há sobreposição entre intervalos de descanso, compensados, trabalho ou ausência planejada, gerando Aviso.
* **Horário Rígido:** Não permite intervalos com tempo planejado, limites de compensação de extras/atrasos ou intervalos não compensáveis, gerando Aviso.
* **Horário Flexível/Semi-flexível:** Valida interseções entre tempo planejado e trabalhado, além de proibir intervalos não compensáveis, gerando Aviso.
* **Compatibilidade de Tipo:** Valida se o tipo definido no cadastro do funcionário condiz com o tipo do horário associado, gerando Aviso em caso de divergência.

**3. Períodos**

* **Interseção Mensal, Quinzenal e Semanal:** Valida se as datas de início e fim dos períodos se sobrepõem a outros períodos cadastrados, gerando Erro por tornar o recálculo inconsistente.

**4. Parâmetros de Sindicato e Funcionário**

* **Distribuição de Extras:** Verifica se a parametrização de distribuição diária é coincidente entre o funcionário e o sindicato, gerando Erro.
* **Banco de Horas:** Gera Erro e impede o recálculo se o banco de horas for diário enquanto a distribuição de extras no sindicato for por período.

**5. Registros sem Vínculo**

* **Horários e Sindicatos:** Se parametrizado, o sistema identifica cadastros que não possuem funcionários associados para auxiliar na limpeza da base, gerando Aviso.

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39985708606999)

**Saiba mais**

[**Verificação da Base**](https://tdn.totvs.com/pages/releaseview.action?pageId=452719238)
