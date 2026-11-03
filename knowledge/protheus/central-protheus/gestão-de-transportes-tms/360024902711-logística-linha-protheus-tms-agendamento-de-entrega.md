---
article_id: 360024902711
category: Gestão de Transportes (TMS)
content_hash: 8f667ec65d9c692532ea27e8dcc4b038200f330e197cd81e82400d288f5ab774
fetched_at: '2026-06-28T22:45:27.230002+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Agendamento de Entrega
type: support-article
updated_at: '2024-02-26T12:51:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024902711-Log%C3%ADstica-Linha-Protheus-TMS-Agendamento-de-Entrega
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:05:30 min****Dúvida**Como utilizar o **Agendamento de Entrega** no **TOTVS Logística TMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Essa funcionalidade permitir a utilização do **Agendamento de Entregas**, agilizando o processo de distribuição de carga e fornecer ao usuário uma visão detalhada do trabalho a ser executado, dentro de cada prioridade de distribuição definida pelo transportador.   
  
**Procedimento para Utilização****Em Atualizações / Comercial / Componentes Frete - TMSA030**, incluir um novo componente e no campo **Calc.Sobre**, selecione a opção **15 – Cliente Destinatário**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023242232/mceclip0.png)

**Em Atualizações / Comercial / Configuração Tabela de Frete  - TMSA130**, inclua ou altere uma configuração de tabela de frete e adicione o **Componente de Frete**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023280231/mceclip1.png)

**Em Atualizações / Comercial / Componente de Frete por Destinatário - TMSA013**, inclua um novo Componente de Frete. No campo **Agendamento de Entrega** será preenchido, com as opções:

* **Sim -** Será possível incluir agendamentos de entregas para este destinatário.
* **Não -** Destinatário não é participante do agendamento de entrega
* **Obrigatório -** Sempre deverá ser gerado um agendamento de entrega para este destinatário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023280271/mceclip2.png)

Para efeito de cobrança de agendamentos, **caso os mesmos não sejam cobrados, não é necessário cadastrar esta tabela**. Somente o componente onde será informado que existe agendamento de entrega, conforme item anterior.  
  
Nesse exemplo vamos cadastrar a tabela para realizar a cobrança do cliente CLI001.  
  
**Em Atualizações / Comercial / Tabela de Frete por Destinatário - TMSA012**, inclua uma nova tabela de frete por destinatário e informe a Tabela de Frete, Cliente Destinatário e o Valor.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023280391/mceclip3.png)

**Em Atualizações / Cadastros / Prioridade de Entrega - TMSA015**, inclua uma nova prioridade de entrega

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023242672/mceclip4.png)

**Em Atualizações / Recebimento / Entrada Dc.cliente - TMSA050**, incluir uma nova nota para um Destinatário que seja participante do Agendamento de Entrega, assim os campos pertinentes aos dados do agendamento de entrega, tais como **Tipo Agend., Data Agend., Período, Hr. Ini. Agend, Hr. Fim. Agend e Motivo**, serão habilitados para edição

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023242712/mceclip5.png)

Todas as notas fiscais vinculadas a cotação poderão ser agendadas desde que para a mesma data e período, gerando assim um único agendamento de entrega para todas as notas fiscais. Caso o digitador tente informar uma data de agendamento de entrega diferente entre as notas fiscais, será apresentado uma mensagem de *Help*.  
  
Caso tenhamos várias notas digitadas com datas de agendamento diferentes e sem cotação de frete, teremos um documento por nota.  
  
Caso o cliente destinatário esteja configurado com a **opção Agd. Entrega = Obrigatório** e na entrada do documento do cliente não seja informado a data e hora, será criado automaticamente para o documento um agendamento de entrega com o *status* **Aguardando Agendamento**. Em seguida, se necessário poderá realizar alterações através do monitor.  
  
Para o agendamento de entrega ser criado automaticamente, é necessário que o Pergunte "Gera Agendamento?" esteja como **Sim** no **F12** da rotina **Cálculo de Frete - TMSA200**.

![](https://totvssuporte.zendesk.com/attachments/token/SZRvAv0dNZDI1Wdo0BAZhCEtq/?name=image.png)

**Em Atualizações / Transporte / Monitor Agendamento - TMSA018**: Interface para monitoramento dos agendamentos, com o devido posicionamento de cada agendamento e *status*.  
  
Na abertura do **Monitor de Agendamento** será apresentado a tela de **Parâmetros** abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023280791/mceclip6.png)

No monitor de agendamento o usuário terá acesso a **inclusão, cancelamento, monitoramento e reagendamento dos documentos**, onde serão informados, responsabilidade pela ocorrência, prioridade, cliente, transportador.  
  
O agendamento não será criado de forma automática. Após a inclusão do documento através da rotina **Entrada Dc.cliente e informar os dados referente ao agendamento,** será necessário realizar a inclusão do agendamento de entrega para documento de forma manual.  
  
**Em Atualizações / Transporte / Monitor Agendamento / Visualização:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023280831/mceclip7.png)

**Em Atualizações / Transporte / Manutenção de Documento - TMSA500**, visualizamos o documento gerado com o componente **TAG**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023242852/mceclip8.png)

Na aba **Agendamento de Entrega**, será possível consultar as informações do agendamento de entrega diretamente pelo documento de frete.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023281031/mceclip9.png)

**Em Atualizações / Viagens / Rodoviário Entrega / Viagens Modelo 2 - TMSA144:** São apresentados os dados do Agendamento de Entrega para os documentos que possuam agendamentos de entrega. Também são apresentados avisos de alertas ao tentar colocar um documento com agendamento de entrega com data diferente do agendamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023242972/mceclip10.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023243012/mceclip11.png)

Após realizar a entrega do documento, **ao apontar uma ocorrência do tipo Encerra Processo**, o *status* do agendamento de entrega do documento, é atualizado para **Realizado** ou **Realizado com Atraso.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023281211/mceclip12.png)

A opção **Reagendamento** deve ser utilizada quando por algum motivo for determinado que este documento deve ser entregue em uma nova data. Assim o transportador pode realizar o reagendamento da entrega e o Sistema gravar um histórico de todos os reagendamentos que forem realizados.  
  
A opção **Cancelar** permite realizar o cancelamento de um agendamento de entrega, deixando o documento livre para ser colocado em um novo agendamento.  
  
Exemplo do relatório gerado em **Relatórios / Agendamento de Entrega / Agendamento de Entrega - TMSR630:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14113981879703)
