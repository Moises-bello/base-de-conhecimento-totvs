---
article_id: 31576586397079
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: bb27afe832b191c0943d3a1e06ea3ae4e092f7a5ebdb8479e07542d91065f211
fetched_at: '2026-06-28T22:37:24.161755+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Schedule - Agendamento
  Medições de Contratos
type: support-article
updated_at: '2025-04-22T12:21:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31576586397079-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Schedule-Agendamento-Medi%C3%A7%C3%B5es-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31576602962199) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**  
Como configurar Agendamento Medições de Contratos?  
  
**Ambiente**  
Esta funcionalidade estará disponível a partir da versão **12.1.2410**  
  
**Solução**

1. Ao executar acessar a rotina **Manutenção de Contratos ( CNTA300 )** acesse em Outras Ações / Schedules / Agendamentos Medições

![](https://tdn.totvs.com/download/thumbnails/864331498/image-2024-8-23_8-57-19.png?version=1&modificationDate=1724414296440&api=v2)

A visualização dos eventos executados desta rotina serão exibidos

![](https://tdn.totvs.com/download/attachments/864331498/image-2024-8-23_8-57-34.png?version=1&modificationDate=1724414309533&api=v2)

Nesta tela também será possível realizar a criação de uma agendamento recorrente ( clicando no botão **NOVO )**, conforme demonstrado abaixo:

Execução Única, em data/hora pre-deteminada:

![](https://tdn.totvs.com/download/attachments/864331498/image-2024-8-9_15-21-40.png?version=1&modificationDate=1724410568570&api=v2)

Execução Diária:

![](https://tdn.totvs.com/download/attachments/864331498/image-2024-8-9_15-27-5.png?version=1&modificationDate=1724410568767&api=v2)

Execução Semanal:

![](https://tdn.totvs.com/download/attachments/864331498/image-2024-8-9_15-29-4.png?version=1&modificationDate=1724410568703&api=v2)

Execução Mensal:

![](https://tdn.totvs.com/download/attachments/864331498/image-2024-8-9_15-29-50.png?version=1&modificationDate=1724410568887&api=v2)

Parametrização adicional:

![](https://tdn.totvs.com/download/attachments/864331498/image-2024-8-9_15-30-37.png?version=1&modificationDate=1724410568827&api=v2)

Após informado os dados, confirme a gravação.

![](https://tdn.totvs.com/download/attachments/864331498/image-2024-8-23_8-57-53.png?version=1&modificationDate=1724414328677&api=v2)

![](https://tdn.totvs.com/download/attachments/864331498/image-2024-8-9_15-34-42.png?version=1&modificationDate=1724410568950&api=v2)

## 2. Demais informações

Importante

Para realizar manutenções no agendamento criado, a principio só poderá ser feito através do configurador, na rotina Ambiente \ Schedule \ Schedule.

Importante

Esta funcionalidade estará disponível a partir da versão 12.1.2410

Importante

Para o **funcionamento**deste **recurso**, se faz necessário a configuração do **Smart Schedule**em seu ambiente conforme a documentação: [Schedule Protheus](https://tdn.totvs.com/display/public/framework/Schedule+Protheus)

**3. Cadastro do tipo de Contrato automático**

No cadastro de Tipo de Contrato Configure o  Campo Med Automática**(CN1\_MEDAUT)** = Sim.

Exemplos.

**Cadastro Tipo de Contrato.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31576602963479)

**Cadastro Tipo de Planilha**

No Cadastro de Tipo de Planilha Configure o campo Medição Automática**(CNL\_MEDAUT)** = Sim

ou Conforme Contrato caso no cadatro de Tipo de Contrato o campo Medição automática **(CN1\_MEDAUT)** esteja igual a Sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31576602963735)

Inclua o Contrato utilzando o Tipo de Contrato e Tipo de Planilha configurados como Medição automática, após a Inclusão do Cronograma Financeiro será preenchido o campo Dt.prevista de Medição**(CNF\_PRUMED)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31576602963863)

Para geração automática das Medições via SCHEDULE será verificado o parâmetro MV\_ATUGCT = **20240722**  e o campo Dt. prevista de Med**(CNF\_PRUMED)** do cronograma financeiro com a mesma Data do parâmetro **MV\_ATUGCT** para processamento das Medições**.**

Exemplo de Medição Incluída e Encerrada Automaticamente Via Schedule.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31576602963991)**

***Saiba Mais:***

[DT Smart Schedule GCT - Agendamento Medições de Contratos](https://tdn.totvs.com/pages/viewpage.action?pageId=864331498)

[CNTA260 - Medição Automática no módulo de Gestão de Contrato via JOB e através de execução de rotina do menu](http://tdn.totvs.com/pages/releaseview.action?pageId=268578950)

[MP - SIGAGCT - Como fazer para as Medições Automáticas ( CNTA260 ) serem geradas pela Rotina Nova Medição (CNTA121) ? - MV\_CT26021](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034124234-MP-SIGAGCT-Medi%C3%A7%C3%B5es-autom%C3%A1ticas-geradas-n%C3%A3o-podem-ser-visualizadas-na-rotina-CNTA121-%C3%A9-apresentado-o-Help-Op%C3%A7%C3%A3o-indispon%C3%ADvel-para-medi%C3%A7%C3%B5es-realizadas-com-a-rotina-de-medi%C3%A7%C3%A3o-padr%C3%A3o-)

[MP - SIGAGCT - Quais os Pontos de Entrada da Rotina de Medição Automática - CNTA260 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008103842-MP-SIGAGCT-Quais-os-Pontos-de-Entrada-da-Rotina-de-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-CNTA260-?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
