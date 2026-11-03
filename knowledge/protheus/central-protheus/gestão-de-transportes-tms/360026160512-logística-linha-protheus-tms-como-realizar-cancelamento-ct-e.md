---
article_id: 360026160512
category: Gestão de Transportes (TMS)
content_hash: 3c1b99d8330a2e958374a5e236ff6064ceada23adb76a2c615e98c28a19d48c0
fetched_at: '2026-06-28T22:45:27.493855+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como realizar cancelamento CT-e
type: support-article
updated_at: '2025-03-28T18:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026160512-Log%C3%ADstica-Linha-Protheus-TMS-Como-realizar-cancelamento-CT-e
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22541287069463)**Tempo aproximado para leitura: **00:03:40 min****Dúvida**Como realizar o cancelamento do **CT-e - Conhecimento de Transporte Eletrônico** no **TOTVS Logística TMS**?  
  
 **Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para efetuar o cancelamento **CT-e** será necessário**Estornar o Cálculo do Frete e transmitir o Cancelamento.**Estornar Cálculo do Frete: acessar **Atualizações/Recebimento/Entrada Documentos de Clientes**. Selecionar o **lote/documento** que deseja estornar e em **Outras Ações/Calculo Frete/Estornar**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025627632)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025643591)

Marcar o **CT-e** e clicar em **Confirmar**.  
  
Será apresentada a mensagem **TMSA20042** informativa, pois a transmissão do cancelamento para **SEFAZ - Secretaria de Estado da Fazenda** será realizada nos próximos passos. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025643731)

**Transmitir o Cancelamento**: acessar **Atualizações/Recebimento/Entrada Documentos de Clientes**. Selecionar o **lote/documento** que deseja estornar e em **Outras Ações/Calculo Frete/CT-e:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025628432)

Será apresentada a tela de **Parâmetros**, preencher os dados condizentes com o **CT-e** em questão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025628552)

No **Monitor de** **CT-e**, clicar em **Monitor** e informar o **CT-e** que será cancelado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025628632)

Na tela abaixo **não** deverá selecionar nenhum **CT-e** e clicar em**Transmitir**.  
  
Será apresentada a mensagem de alerta **Não existem documentos marcados para transmitir! Transmite documentos cancelados?**Confirme clicando em **Sim**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025644951)

Acessar o monitor do **CT-e** novamente, constará o retorno da **SEFAZ** como **015-Cancelamento Autorizado**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025645231)

 O lote do **CT-e** cancelado ficará disponível para calcular novamente se desejar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025629712)

**Como realizar o cancelamento extemporâneo?**  
O cancelamento extemporâneo consiste em realizar o cancelamento do CT-e quando este procedimento for realizado fora do prazo estipulado.  
  
Para a realização do cancelamento extemporâneo, deve ocorrer inicialmente a comunicação ao órgão responsável, **Sistema Integrado de Administração da Receita Estadual - SIARE**. O pedido de cancelamento extemporâneo de CT-e será prestado mediante o pagamento da **Taxa de Serviços Estaduais - TSE**, que pode ter um valor específico por documento, calculado com base na legislação vigente do estado em que a operação estiver sendo realizada.   
Após, as chaves dos documentos que devem ser cancelados já terem sido informadas e mediante a concessão de autorização de uso pelo **SIARE**, poderá ser dado seguimento a transmissão do cancelamento extemporâneo via sistema.   
  
Parâmetros que podem interferir no **Cancelamento**:

* **MV\_CTECAN** **-** Habilita validação da exclusão do CT-e. Só permite cancelar após autorização da SEFAZ.
* **MV\_CTEEXC** **-** Prazo em dias para cancelamento do CT-e após ser autorizado.
* **MV\_CTEEXCH** **-** Prazo em horas para cancelamento CT-e após ser autorizado.
* **MV\_CANCEXT -** Define a quantidade de dias para transmissão do Cancelamento Extemporâneo. Este parâmetro deve estar configurado com o valor de 30 dias ou superior.
* **MV\_ESPECIE** - Se a série do CT-e não estiver contida neste parâmetro, teremos o campo **F3\_ESPECIE** em branco, e desta forma, o cancelamento não será transmitido. O campo **F3\_ESPECIE** deve obrigatoriamente conter a palavra **CTE**.
* **MV\_HVERAO** - Se na transmissão do cancelamento retornar a rejeição 637 - A data do evento não pode ser menor que a data de autorização, então deve-se validar os parâmetros de fuso horário exclusivos por filial.

**Saiba mais**Parâmetros de fuso horário: [Logística - Linha Protheus - TMS - Mudança no horário de verão CT-e, MDF-e e CC-e.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018563352-Log%C3%ADstica-Linha-Protheus-TMS-Mudan%C3%A7a-no-hor%C3%A1rio-de-ver%C3%A3o-CT-e-MDF-e-e-CC-e?source=search)  
Cancelamento de CT-e com evento de Carta de Correção vinculado: [Logística - Linha Protheus - TMS - Cancelamento de CT-e quando existir evento de Carta de Correção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025397891-Log%C3%ADstica-Linha-Protheus-TMS-Cancelamento-de-CT-e-quando-existir-evento-de-Carta-de-Corre%C3%A7%C3%A3o)Mais informações poderão ser acessadas no *link*: [Documentos de Transporte Estornados](https://tdn.totvs.com/pages/viewpage.action?pageId=514724397)
