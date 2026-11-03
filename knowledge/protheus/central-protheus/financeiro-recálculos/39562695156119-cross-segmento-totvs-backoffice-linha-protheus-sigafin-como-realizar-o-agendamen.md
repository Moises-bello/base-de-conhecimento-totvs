---
article_id: 39562695156119
category: Financeiro - Recálculos
content_hash: 61e6484d01934c9357eb46e5c0e7722b07c2e4bea73a040233dfa0d5da05ecdd
fetched_at: '2026-06-28T22:38:20.185871+00:00'
product: protheus
section_id: 1500001550362
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Como realizar
  o agendamento da rotina FINA410 via Schedule
type: support-article
updated_at: '2026-04-07T13:53:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39562695156119-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Como-realizar-o-agendamento-da-rotina-FINA410-via-Schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
Como realizar o agendamento da rotina de Refaz Saldos Cliente/Fornecedor (FINA410) para execução em segundo plano, via Schedule no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2410  
  
**Solução**  
  
A partir da release 12.1.2410, a rotina FINA410 (Refaz Saldos Cliente/Fornecedor) foi atualizada para permitir a execução via Schedule (JOB). Essa funcionalidade visa otimizar o processamento de grandes volumes de dados, permitindo que a tarefa seja executada em segundo plano sem travar a interface do usuário ou de forma programada em horários de menor impacto no banco de dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39562717559831)

Para utilizar o recurso, é necessário que o serviço de Schedule do Protheus esteja devidamente configurado e ativo no ambiente.

**Passos**

1. No módulo **Financeiro (SIGAFIN)**, acesse **Atualizações > Miscelânea > Refaz Saldos Cli/For (FINA410)**.
2. Na tela de parâmetros da rotina, preencha as perguntas conforme a necessidade do reprocessamento.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39562695148183)
3. Na guia "Informações", clique no botão **Agendar**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39562695148951)
4. O sistema abrirá a interface de **Agendamento**, onde deverão ser informados os detalhes do agendamento:

   * **Data e Hora** para o início do processamento.
   * **Empresa/Filial** em que o processo será executado, e usuário responsavel.  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39562717562135)
5. Após configurar os detalhes do agendamento, confirme a operação.
6. O JOB será registrado automaticamente no **Schedule Protheus** e poderá ser monitorado através da rotina de **Agendamentos** no módulo **Configurador (SIGACFG)**.
7. Caso deseje iniciar o processamento imediatamente em segundo plano, utilize a opção **Executar em segundo plano** disponível no monitor de agendamentos.

**Importante:** Confira se o processo usa agentes padrão e se estão ativos para garantir o agendamento.
