---
article_id: 360000284088
category: SIGAEST - PROCESSAMENTOS
content_hash: c022b2ef1d353e7a9599df05a4992cdb95cb86ca353953551a4bec68734e08a4
fetched_at: '2026-06-28T22:39:04.989643+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Não foi possível realizar
  a subida da thread
type: support-article
updated_at: '2026-06-17T21:52:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000284088-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-N%C3%A3o-foi-poss%C3%ADvel-realizar-a-subida-da-thread
---

Ao executar rotinas como Saldo Atual e Recalculo do Custo Médio, pode aparecer a mensagem "Não foi possível realizar a subida da thread". Para resolver, verifique se o parâmetro MV\_CUSTEXC está como "Compartilhado", confira o error.log com TRACESTACK=1 ativado, ajuste o parâmetro MV\_M330THR para 1 no Configurador, e monitore mensagens no dbAccess. Em casos de deadlock, consulte um DBA para análise detalhada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40910083502743) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Ao executar rotinas de processamento (Ex. Saldo Atual, Virada de Saldos, Recálculo do Custo Médio, etc.), é exibida a mensagem "**Não foi possível realizar a subida da thread**". Como proceder nessas situações?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Thread é um pequeno programa que trabalha como um subsistema, sendo uma forma de um processo se autodividir em duas ou mais tarefas. É o termo em inglês para Linha ou Encadeamento de Execução. Para analisar este tipo de incidente, é necessário executar as orientações abaixo:

**Passos**

1. **Através do módulo Configurador (SIGACFG)**, verifique se o conteúdo do parâmetro [**MV\_CUSTEXC**](https://tdn.totvs.com/x/X9pc)está configurado como Compartilhado.
2. Abra o arquivo error.log e verifique se houve algum incidente no processamento da rotina. **Importante:** Antes de executar a rotina, habilite a chave[**TRACESTACK**](https://tdn.totvs.com/x/jopc)**=1** no seu arquivo appserver.ini.
3. **Abra o módulo Configurador (SIGACFG)** e altere a quantidade de threads a serem executadas de forma simultânea através do parâmetro correspondente. Exemplo: Altere o parâmetro [MV\_M330THR](https://tdn.totvs.com/x/EONc) para a quantidade igual a 1 (no caso de erro na rotina MATA330).

   **Nota:** Algumas rotinas de processamento têm seu próprio parâmetro de threads. Para consultar, pressione **Shift+F6 logado na rotina, vá em parâmetros e identifique se existe**. Caso não tenha o parâmetro em sua base de dados.
4. Abra o dbAccess Monitor de seu ambiente e execute os procedimentos abaixo:

* Clique na aba Mensagem e aperte o botão Limpar.
* Execute a rotina em questão com o erro apresentado e deixe a mensagem "Não foi possível realizar a subida da thread" ser exibida na tela.
* Retorne ao dbAccess Monitor e verifique na aba Mensagem a existência de algum texto de não-conformidade gerado pela rotina.

5. Para que o suporte possa avaliar a questão, na abertura do ticket anexe os arquivos console.log do appserver, arquivos de logs gerados do dbAccess e ID da central de diagnóstico.

* [Como enviar dados pela Central de Diagnóstico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)

### **Sobre problemas relacionados a deadlock:**

Exemplo: *Error : 1205 (40001) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]*  
*A transação (ID do processo 918) entrou em deadlock em bloquear recursos com outro processo e foi escolhida como a vítima do deadlock. Execute a transação novamente.*

**deadlock** é frequentemente confundido com bloqueio normal. Quando uma transação solicita um bloqueio em um recurso bloqueado por outra transação, a transação solicitante espera até que o bloqueio seja liberado. Por padrão, **as transações do SQL Server não têm um tempo limite, a menos que** `LOCK_TIMEOUT` tenha sido definido.

* Para identificar com precisão quais queries estão envolvidos no deadlock, é sugerido a atuação de um **analista DBA**. Dessa forma ele consegue, diretamente no banco de dados, verificar qual query manteve os registros bloqueados e qual tentou acessá-los sem sucesso.  
     
  Sendo assim, reforçamos a importância de direcionar esse cenário ao seu time de infraestrutura. Caso seja necessário um apoio mais aprofundado, contamos com áreas especializadas em infraestrutura, cujo atendimento é 100% faturado, mediante orçamento. Havendo interesse, podera ser aberto um ticket ao time **HUB Plataformas** através de uma solicitação à parte.
* Vale ressaltar que cada banco tem um tempo de espera para o deadlock e é possivel aumentar o tempo limite de espera, a seguir uma documentação auxiliar (externa Microsoft), que pode ser util e apoio para o analista DBA  
  <https://learn.microsoft.com/pt-br/sql/relational-databases/sql-server-deadlocks-guide?view=sql-server-ver17>

**Saiba mais**

[*FAQs - Estoque e Custos*](https://tdn.totvs.com/display/public/PROT/FAQs+-+Estoque+e+Custos)

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)
