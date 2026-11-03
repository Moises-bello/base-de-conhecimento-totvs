---
article_id: 25196624458903
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 917b18f03a0ccbcbdc934b68600be882007a4622dc5a11678ccef2748cd29230
fetched_at: '2026-06-28T22:37:23.864922+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Medição Automática
  via Schedule
type: support-article
updated_at: '2025-11-11T20:37:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25196624458903-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-via-Schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25196624421783) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Como configurar a Medição Automática via Schedule?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Gestão de Contratos - Todas as versões.

**Solução**

Assistam nosso vídeo no link - [SIGAGCT - Medição Automática por Schedule](https://www.youtube.com/watch?v=_CVBTeKdBqM)

Segue passo a passo abaixo:

**1.** No Configurador do Sistema em Ambiente >Schedule> Smartch Scheduler Iniciado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25196627972759)

**2.** Agendamentos >Novo para Inclusão do Schedule conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32402765771415)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25196624427927)

-Após Criar o Novo Agendamento , o mesmo ficará Habilitado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25196627977623)

**3.** Configure os parâmetros abaixo no Configurador do Sistema.

Exemplo.

MV\_ATUGCT - **20240722**  Data logada no sistema

MV\_MEDDIAS - **0** (Para que possa executar todos os dias as Medições automaticamente processando o campo Data prevista de Medição do cronograma Financeiro do Contrato com a mesma data do Parâmetro MV\_ATUGCT.)

MV\_MEDPEND = **1**

**4.** No cadastro de Tipo de Contrato Configure o  Campo Med Automática**(CN1\_MEDAUT)** = Sim.

Exemplos.

**Cadastro Tipo de Contrato.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25196624429975)

**Cadastro Tipo de Planilha**

No Cadastro de Tipo de Planilha Configure o campo Medição Automática**(CNL\_MEDAUT)** = Sim

ou Conforme Contrato caso no cadatro de Tipo de Contrato o campo Medição automática **(CN1\_MEDAUT)** esteja igual a Sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25196627979415)

**5.** Inclua o Contrato utilizando o Tipo de Contrato e Tipo de Planilha configurados como Medição automática, após a Inclusão do Cronograma Financeiro será preenchido o campo Dt.prevista de Medição**(CNF\_PRUMED)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25196627987607)

**6.** Para geração automática das Medições via SCHEDULE será verificado o parâmetro MV\_ATUGCT = **20240722**  e o campo Dt. prevista de Med**(CNF\_PRUMED)** do cronograma financeiro com a mesma Data do parâmetro **MV\_ATUGCT** para processamento das Medições**.**

**7.** Exemplo de Medição Incluída e Encerrada Automaticamente Via Schedule.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25196624434711)**

Para o funcionamento deste recurso, se faz necessário a configuração do Smart Schedule em seu ambiente conforme a documentação: [Schedule Protheus](https://tdn.totvs.com/display/public/framework/Schedule+Protheus)

**Obs:**

No processo de rotina automática, não há disponível parâmetros para que pedidos gerados na medição automática já sejam gerados liberados ou com informações adicionais.

Dessa forma para complemento de informações na geração de pedidos de vendas ou compras no processo de medição, pode-se avaliar a possibilidade através de customização com os pontos de entradas disponíveis abaixo, a se avaliar o que se adequa conforme a necessidade existente:

[- Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os Pontos de Entrada da Rotina de Medição Automática - CNTA260 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008103842-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-Pontos-de-Entrada-da-Rotina-de-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-CNTA260)

[- Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o)

***Saiba Mais:***

[CNTA260 - Medição Automática no módulo de Gestão de Contrato via JOB e através de execução de rotina do menu](http://tdn.totvs.com/pages/releaseview.action?pageId=268578950)

[MP - SIGAGCT - Como fazer para as Medições Automáticas ( CNTA260 ) serem geradas pela Rotina Nova Medição (CNTA121) ? - MV\_CT26021](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034124234-MP-SIGAGCT-Medi%C3%A7%C3%B5es-autom%C3%A1ticas-geradas-n%C3%A3o-podem-ser-visualizadas-na-rotina-CNTA121-%C3%A9-apresentado-o-Help-Op%C3%A7%C3%A3o-indispon%C3%ADvel-para-medi%C3%A7%C3%B5es-realizadas-com-a-rotina-de-medi%C3%A7%C3%A3o-padr%C3%A3o-)

[MP - SIGAGCT - Quais os Pontos de Entrada da Rotina de Medição Automática - CNTA260 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008103842-MP-SIGAGCT-Quais-os-Pontos-de-Entrada-da-Rotina-de-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-CNTA260-?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
