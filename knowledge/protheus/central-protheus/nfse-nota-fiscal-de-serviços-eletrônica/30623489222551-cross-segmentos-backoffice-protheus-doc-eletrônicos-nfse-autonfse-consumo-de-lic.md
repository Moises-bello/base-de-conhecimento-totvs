---
article_id: 30623489222551
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: b06634ff1794a2cb7875009d723d530151115216acbab41ac1028068b778c1ad
fetched_at: '2026-06-28T22:39:56.297517+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - AUTONFSE
  (Consumo de Licenças)
type: support-article
updated_at: '2025-05-21T12:01:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30623489222551-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-AUTONFSE-Consumo-de-Licen%C3%A7as
---

**Dúvida**Como funciona o consumo de licenças no AUTONFSE?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões.  
  
**Solução**O uso de Schedule no TOTVS Protheus consome licença no momento da execução da rotina agendada, se esta tiver a necessidade de abertura da empresa.

A configuração do Schedule do AutoNfse envolve a criação de agentes para processar as notas fiscais de serviços eletrônicas (NFSe) que consequentemente fazem abertura da empresa e necessitam de licenças para tal atividade.

O uso de qual licença irá depender do plano contratado por cada cliente e configuração de License Server.

Podendo ser uma licença nomeada, simultânea, corporativa entre outras.

No caso de licenças nomeadas cada execução irá consumir a licença do módulo configurado no agendamento neste caso a do Faturamento.

Quando configuramos rotinas agendadas no TOTVS Protheus, o consumo de licenças ocorre apenas durante a execução dessas rotinas. Portanto, é crucial entender que quanto mais processos você paralelizar, mais licenças serão utilizadas simultaneamente.

Vamos detalhar como isso funciona:

**Execução Paralela e Consumo de Licenças:**

1. **Rotinas Agendadas e Licenças**:

   * Cada rotina agendada que está em execução consome uma licença caso a rotina agendada tenha a necessidade de abertura da empresa. Isso significa que se você tiver várias rotinas agendadas sendo executadas ao mesmo tempo, cada uma delas estará consumindo uma licença.
2. **Paralelização dos Processos**:

   * Quando você paraleliza processos, ou seja, executa várias rotinas ao mesmo tempo, o consumo de licenças aumenta proporcionalmente. Por exemplo, se você agendar três processos de transmissão de NFS-e para serem executados simultaneamente, cada um desses processos consumirá uma licença, resultando em três licenças em uso ao mesmo tempo.
3. **Exemplo Prático**:

   * Imagine que sua empresa tem três filiais e você agendou três tipos de serviços para cada filial: Transmissão de NFS-e, Monitoramento de NFS-e, e Cancelamento de NFS-e.
   * Se todos esses serviços forem agendados para rodar em paralelo em todas as filiais, o consumo de licenças será elevado.
   * Para cada filial, temos três serviços: Transmissão (1 licença), Monitoramento (1 licença), e Cancelamento (1 licença). Se todas as três rotinas rodarem simultaneamente em cada uma das três filiais, isso resulta em 9 licenças consumidas ao mesmo tempo.
4. **Impacto no Sistema**:

   * A execução paralela de várias rotinas pode ser vantajosa para concluir tarefas rapidamente, mas é importante garantir que você tenha licenças suficientes para suportar essa carga paralela.
   * A falta de planejamento pode levar à escassez de licenças, impactando outros usuários e processos que também dependem do sistema.

### Considerações para Maximizar Eficiência:

* **Planejamento de Agendamentos**: Analise cuidadosamente quais rotinas precisam ser paralelizadas e quais podem ser agendadas em horários diferentes para otimizar o uso das licenças.
* **Monitoramento de Licenças**: Utilize as ferramentas de monitoramento do Protheus para acompanhar em tempo real o consumo de licenças e ajustar os agendamentos conforme necessário.
* **Ajuste de Prioridades**: Priorize processos críticos para serem executados em horários de pico e distribua tarefas menos urgentes para períodos de menor uso.

### Conclusão:

Paralelizar processos no TOTVS Protheus pode melhorar a eficiência operacional, mas também aumenta o consumo de licenças. Um planejamento cuidadoso e um monitoramento constante são essenciais para garantir que sua empresa utilize os recursos de forma otimizada, evitando a falta de licenças para outros usuários e processos importantes.

**Importante o número de threads configuradas no agendamento dos serviços do AutoNfse não afeta no consumo de licenças.**

Para mais informações sobre o funcionamento de cada tipo de licença regras de consumo e formas de configuração consultar o Guia de Gestão de Licenças:

[Guia Gestão de Licenças TOTVS](https://tdn.totvs.com/pages/viewpage.action?pageId=184779108)
