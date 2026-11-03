---
article_id: 360012989932
category: Folha Mensal
content_hash: 4b6cd06ca049a30d7d58c0576d989bf5b69950158c902d335ec6cc75527d0a8c
fetched_at: '2026-06-28T22:47:00.293575+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Existem férias cadastradas que não estão Calculadas/Lançadas/Finalizadas
type: support-article
updated_at: '2025-01-22T18:27:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012989932-RH-RM-FOP-Existem-f%C3%A9rias-cadastradas-que-n%C3%A3o-est%C3%A3o-Calculadas-Lan%C3%A7adas-Finalizadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29425035134871)Tempo aproximado para leitura**: 00:02:50 min**  
  
**Ocorrência**  
Ao efetuar a liberação de competência em: **Folha Mensal| Liberação de Competência**, o sistema apresenta o seguinte erro:**Existem férias cadastradas que não estão calculadas/lançadas/finalizadas dentro da competência para o(s) funcionário(s) 'chapa xxx'. Favor acertar a situação da(s) mesma(s) antes de efetuar a liberação da competência.****Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
O erro é apresentado quando as férias do funcionário não foram lançadas/finalizadas. Outra possibilidade para causar o erro é realizar o processo de forma indevida, alterando algum dado manualmente, como por exemplo: Situação das férias, situação do funcionário, incluído histórico de situação manualmente, e entre outros.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:1. Identifique a chapa do funcionário que apresentou o erro na descrição do erro e acesse:**Administração de Pessoal | Funcionários.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29425047993239)**  
2. No ícone **Férias** verifique se os botões**Lançar** e **Finalizar** estão desabilitados. Caso estejam habilitados basta efetuar o lançamento e a finalização. Caso o botão de Finalizar esteja desabilitado, prossiga com os passos seguintes. **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418197735447)**3. Acesse: **Cadastro do funcionário | aba Situação** e altere a situação para **F- Férias**. **![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418197753111)**4. Altere a situação das férias para **Pagas** em **Período aquisitivo | Período de gozo | Situação das férias.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009014252)**5. Acesse o cadastro do funcionário em **Administração de Pessoal | Funcionários | Aba históricos | Histórico de situação** e ajuste os históricos que possivelmente estarão inconsistentes. O último histórico deverá ser**F- Férias** com a data de início das férias, como no exemplo abaixo: **![Sem_t_tulo7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009021351)**6. Efetue a finalização das férias. Acesse: **Administração de Pessoal | Funcionários | Férias | Finalizar**. Neste momento será criado um novo histórico de situação para o funcionário **A - Ativo** e as férias ficarão com status Finalizadas.  
 **![](https://centraldeatendimento.totvs.com/hc/article_attachments/29425035138071)  
  
Importante**A finalização das férias acontece apenas na competência que o período de férias termina. Ou seja, em caso de férias partidas, a finalização deverá acontecer somente na próxima competência. Deste modo, o sistema não apresentará a mensagem de erro. Apenas se a férias não estiver sido Lançadas. Além disso, os passos acima poderão ser executados apenas se os eventos de férias já estiverem lançados no envelope.
