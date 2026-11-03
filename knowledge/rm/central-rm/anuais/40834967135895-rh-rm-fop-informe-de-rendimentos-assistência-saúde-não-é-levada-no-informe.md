---
article_id: 40834967135895
category: Anuais
content_hash: 1efa7eac16ec793eb2fd4c7a8cb6c8949fa2834528f6621663a1b18d2612837c
fetched_at: '2026-06-28T22:46:50.930607+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP - Informe de Rendimentos -  Assistência saúde não é levada no
  informe
type: support-article
updated_at: '2026-05-29T20:50:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40834967135895-RH-RM-FOP-Informe-de-Rendimentos-Assist%C3%AAncia-sa%C3%BAde-n%C3%A3o-%C3%A9-levada-no-informe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40834967104919) Tempo aproximado para leitura: **00:04:40 min**  
  
**Dúvida**  
Na geração do Informe de Rendimentos dependentes de funcionários não estão aparecendo no relatório de Informe de rendimentos no campo 7 - Informações Complementares.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**  
O incidente ocorre pois existe divergência de informações entre o registro da ficha financeira e o Histórico de assistência saúde. Para a situação em questão, inicialmente é necessário identificar quais dependentes do funcionário em questão não está sendo apresentado. Conforme exemplificado no material de apoio (print):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40834983256215)

* No exemplo o funcionário possui dois dependentes de Assistência Médica. O Dependente Nº1 e o Nº4 com incidência em assistência Médica marcado.

Cadastro da operadora de Assistência Saúde

* Acessar aba Esocial | Operadora Saúde | Cadastro Operadora de Saúde:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40834967112087)

  Dentro do cadastro da operadora Saúde informar os eventos da operadora:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40834983260567)

Para que o dependente seja levado corretamente no Informe de Rendimentos é necessário que o evento de assistência saúde tenha  o código de calculo 14, e que o lançamento da verba ocorra no envelope do funcionário e o registro no histórico de assistência saúde definido por dependentes.

Conferencia do lançamento da verba:

* Acessar Ficha financeira e verificar o lançamento da verba:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40834983261335)

* Acessar Anexos do funcionário | Histórico de assistência saúde e conferir se os lançamentos estão demonstrados por dependentes conforme valor lançado no envelope:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40834967115671)

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40834983262871)

Conferencia das informações para geração no informe de rendimentos:

* Acessar Anuais | DIRF INFORME DE RENDIMENTOS | DIRF/INFORME DE RENDIMENTOS | Parâmetros específicos da coligada | Incluir caso não esteja a operadora de assistência saúde e seus respectivos eventos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40834983264535)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40834983265303)

Salvar o parâmetro para no momento da geração ser levado corretamente, orientamos a utilização do LOG DA DIRF para realizar as conferencias das informações da ficha financeira e do histórico de assistência saúde:

[RH - RM - FOP - Como gerar o Log da DIRF conferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38575728647447-RH-RM-FOP-Como-gerar-o-Log-da-DIRF-confer%C3%AAncia)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40834967118871)

Geração do Informe de Rendimentos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40834967119767)

**Observação:** Para que o campo Informações complementares **Total** seja preenchido é necessário que os eventos estejam dentro dos parâmetros específicos da coligada | na aba do campo 7 - Campos complementares:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40835559468439)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40835525489303)

Saiba mais: [RH - RM - FOP - Parametrização do Plano de Saúde para gravação no histórico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009552422-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-do-Plano-de-Sa%C3%BAde-para-grava%C3%A7%C3%A3o-no-hist%C3%B3rico)
