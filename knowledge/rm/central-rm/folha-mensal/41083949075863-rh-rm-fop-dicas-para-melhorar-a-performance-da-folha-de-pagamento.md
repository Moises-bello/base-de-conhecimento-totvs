---
article_id: 41083949075863
category: Folha Mensal
content_hash: 98caae42f0ce1d6f810352b61374576e36450d95bd94b09fdbf92a42c3ba654c
fetched_at: '2026-06-28T22:46:57.888638+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP- Dicas para melhorar a performance da Folha de Pagamento
type: support-article
updated_at: '2026-06-09T19:44:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41083949075863-RH-RM-FOP-Dicas-para-melhorar-a-performance-da-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41083933590807) Tempo aproximado para leitura: **00:10:35 min**  
  
**Ocorrência**  
Caso no Totvs Folha de Pagamento, ao efetuar rotina Lançamento do grupo de eventos, recálculo da folha e enfrentar problemas de lentidão, como identificar a **causa da baixa performance** e quais são as melhores práticas para **melhorar a performance**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Totvs Folha de Pagamento - A partir do release 12.1.2510  
  
**Causa**  
A lentidão no RM TOTVS Folha de Pagamento pode ser causada por diversos fatores, incluindo configurações do ambiente, um grande número de acessos simultâneos, locks em tabelas do banco, desempenho da infraestrutura atual, fórmulas de evento no movimento e fórmulas visuais, entre outros fatores.  
  
**Solução**  
Criamos a documentação abaixo, que detalha as principais configurações recomendadas para melhorar a performance de Lançamento do Grupo de eventos e recálculo da folha. Recomendamos que você leia atentamente toda a documentação preparada. Se, após seguir essas orientações, o problema persistir, continue consultando o restante deste KCS para mais informações e soluções adicionais.

**Melhore o desempenho do processamento em até 70% utilizando o recurso de fracionamento de JOBs.**

[RH - RM - FOP - Habilitar Fracionamento de Jobs](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9912971569559-RH-RM-FOP-Habilitar-Fracionamento-de-Jobs)  
[TOTVS Folha de Pagamento - Fracionamento de Jobs](https://tdn.totvs.com.br/display/public/LRM/TOTVS+Folha+de+Pagamento+-+Fracionamento+de+Jobs)  
[Segurança de Jobs Fracionáveis](https://tdn.totvs.com/pages/releaseview.action?pageId=547231277)

**Os principais objetivos do fracionamento de jobs incluem:**

1. **Otimização de Recursos**: Dividir tarefas grandes em partes menores ajuda a otimizar o uso de recursos computacionais (como CPU, memória e armazenamento), evitando sobrecarga do sistema e garantindo um desempenho mais equilibrado;
2. **Maior Controle e Monitoramento**: Processos fracionados permitem um controle mais eficiente sobre cada parte do job, facilitando a identificação de falhas ou gargalos e permitindo ações corretivas mais rápidas;
3. **Melhoria na Performance**: Ao dividir tarefas em porções menores, elas podem ser executadas de forma mais ágil e eficiente, com maior paralelismo, o que contribui para reduzir o tempo total de execução;
4. **Minimizar Impactos no Sistema**: Fracionar jobs pode minimizar o impacto em sistemas e usuários, evitando travamentos ou lentidão em tarefas críticas, especialmente em sistemas de produção;
5. **Facilidade de Recuperação**: Caso algo dê errado durante a execução de um job, é mais fácil retomar ou corrigir o processo em uma parte específica sem ter que reiniciar a execução completa;
6. **Escalabilidade**: Quando processos são divididos, é possível distribui-los em múltiplos servidores ou instâncias, permitindo que o sistema lide com uma quantidade maior de dados ou tarefas sem sobrecarregar um único recurso.  
     
   **Veja abaixo algumas dicas que podem melhorar a performance do Lançamento do grupo de eventos:**

* Dica 1: Acesse: **Configurações | Parametrizador | Folha Normal | Geral 1/2** e marque o parâmetro: **Lança Grupo de eventos sem recalcular envelope**

  Este parâmetro serve para ganho de performance que ao lançar o grupo de eventos não seja necessário acionar o recálculo automático do sistema. Sendo assim, quando terminar todos os lançamentos incluindo o grupo de eventos será necessário um recálculo geral para ficar com o movimento coerente com os cálculos necessários.

  Com este parâmetro marcado, ao realizar o lançamento de Grupos de Eventos (em Folha Mensal | Lançamentos | Grupo de Eventos) o envelope do funcionário **não será recalculado no momento do lançamento**.
* Dica 2: Fracionar o processo de Jobs conforme a documentação: [RH - RM - FOP - Habilitar Fracionamento de Jobs](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9912971569559-RH-RM-FOP-Habilitar-Fracionamento-de-Jobs).   
    
  ⚠️ **Esse mesmo processo pode ser utilizado na execução do recálculo da folha.**
* Dica 3:  Para rastrear o evento cuja fórmula está gerando impacto negativo no desempenho do processo de Lançamento do Grupo de Eventos, utilize a consulta SELECT abaixo:  
    
  **select CODIGO, ULTALTDATA, INDSELECAO from GFORMULA**

  **where CODCOLIGADA='XX'**

  **order by ULTALTDATA desc**

  **Observação: Em 'XX' informar o código da coligada.**
* Dica 4: Para validar se existe alguma Fórmula Visual ou Trigger impactando no processo, execute o processo abaixo:  
   [RH - RM - FOP - Desabilitar triggers e fórmulas visuais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415329649943-RH-RM-FOP-Desabilitar-triggers-e-f%C3%B3rmulas-visuais)  
    
  **Importante:** Execute o processo primeiramente em ambiente de Homologação.

No link de Segurança de Jobs Fracionáveis é possível fracionar o processo de Lançamento do grupo de eventos ou Recálculo do envelope. Basta seguir a documentação e adicionar a classe de job.   
  
 Veja as orientações na documentação:  [Segurança de Jobs Fracionáveis](https://tdn.totvs.com/pages/releaseview.action?pageId=547231277)  
  
A Classe de job para o lançamento do grupo de eventos é a **FopCalcularFolhaProcess**, e a do processo de execução do recálculo é a **FopRecalcularFolhaProc.**  
  
Se precisar de acompanhamento para análise da performance e otimização das fórmulas customizadas, temos nosso time de consultoria técnica que poderá apoiá-lo na análise. Se optar por este caminho basta retornar no ticket manifestando este interesse que direcionamos o atendimento para que o time lhe informe os procedimentos e valores.

1. Caso a lentidão ocorra em processos específicos, ou seja, somente no módulo de folha de pagamento, avalie se no gerenciamento de jobs, há jobs de recálculo da folha ou lançamento do grupo de eventos. Jobs de diferentes processos do módulo de Folha de Pagamento executando simultaneamente podem causar locks no banco, ou mesmo lentidão nos processos.  
     
   Agendamentos de jobs executando simultaneamente, também podem causar lentidão.  
     
   Para identificar jobs agendados, segue documentação:  
   [Framework - Linha RM - Frame - Identificar job agendado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014009212-Framework-Linha-RM-Frame-Identificar-job-agendado)  
     
   Se identificar vários jobs agendados, sem necessidade, podendo causar lentidão, segue documentação para desabilitá-los:  
   [Framework - Linha RM - Frame - Como desabilitar job agendado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003038712-Framework-Linha-RM-Frame-Como-desabilitar-job-agendado)
2. Se a lentidão estiver de forma generalizada, ou seja, em qualquer processo, qualquer módulo, sugerimos verificar a documentação abaixo:  
   [Framework - Framework RM - BD - Orientações Gerais para Otimização de Performance](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027943052-Framework-Framework-RM-BD-Orienta%C3%A7%C3%B5es-Gerais-para-Otimiza%C3%A7%C3%A3o-de-Performance)

**Importante**  
Se houver necessidade de investigação mais aprofundada em seu ambiente, temos nosso serviço TIS. O Infraestrutura de Sistemas é o serviço especializado de análise, sustentação e evolução da infraestrutura que suporta os sistemas de gestão da TOTVS.  
Para maiores detalhes, segue link [**TIS**](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-servico-infraestrutura-de-sistemas/)

**Saiba mais**  
Para avaliar locks no banco, segue documentação para base SQL:  
[Framework - Framework RM - BD - Como verificar Deadlock no SQL Server](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003068212-Framework-Framework-RM-BD-Como-verificar-Deadlock-no-SQL-Server)  
  
Como apoio, para auxiliar no monitoramento do ambiente, segue documentação sobre o Sentinela:  
[Framework - Framework RM - BD - Sentinela RM Ferramenta de Monitoramento de Ambientes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007212312--Framework-Framework-RM-BD-Sentinela-RM-Ferramenta-de-Monitoramento-de-Ambientes)  
  
Para fracionar outras rotinas do módulo de folha de pagamento, veja as documentações abaixo:  
[RH - RM - FOP - Fracionamento de Jobs - Cálculo do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27594180464663-RH-RM-FOP-Fracionamento-de-Jobs-C%C3%A1lculo-do-13-Sal%C3%A1rio)  
[RH - RM - FOP - Fracionamento de Jobs - Atualiza Campo Desconto Simplificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29396880696599-RH-RM-FOP-Fracionamento-de-Jobs-Atualiza-Campo-Desconto-Simplificado)  
[RH - RM - FOP - Crédito do Trabalhador - Fracionamento de Jobs](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33529867205143-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Fracionamento-de-Jobs)  
  
Confira também, como melhorar o desempenho de outros Produtos do RH:  
[RH - RM - PTO- Dicas para melhorar a performance do Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/41002575739287-RH-RM-PTO-Dicas-para-melhorar-a-performance-do-Automa%C3%A7%C3%A3o-de-Ponto)  
[RH - RM - Meu RH- Dicas para melhorar a performance do Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441139391767-RH-RM-Meu-RH-Dicas-para-melhorar-a-performance-do-Meu-RH)
