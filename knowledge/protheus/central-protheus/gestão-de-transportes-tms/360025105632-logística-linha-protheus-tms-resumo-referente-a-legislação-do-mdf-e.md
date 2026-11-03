---
article_id: 360025105632
category: Gestão de Transportes (TMS)
content_hash: c0c776206cc296998a8a40f806615e59b5870bc4b045ae14246142f174f6880a
fetched_at: '2026-06-28T22:45:33.349218+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: 'Logística - Linha Protheus - TMS - Resumo referente a legislação do MDF-e '
type: support-article
updated_at: '2022-04-27T11:44:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025105632-Log%C3%ADstica-Linha-Protheus-TMS-Resumo-referente-a-legisla%C3%A7%C3%A3o-do-MDF-e
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:08:00 min**  
  
**Dúvida**  
O que é **MDF-e - Manifesto Eletrônico de Documentos Fiscais** ?  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
O **MDF-e** modelo **58** é o documento fiscal eletrônico que substituiu o **Manifesto de Carga**, modelo **25.** É o documento emitido e armazenado eletronicamente, de existência apenas digital para vincular os documentos fiscais utilizados na operação e/ou prestação, à unidade de carga utilizada no transporte, cuja validade jurídica é garantida pela assinatura digital do emitente e a autorização do uso pela administração tributária da unidade federada do contribuinte **SEFAZ - Secretaria de Estado da Fazenda.**Sua emissão cabe a empresas prestadoras de serviço de transporte para prestações com mais de um conhecimento de transporte ou pelas demais empresas nas operações, cujo transporte seja realizado em veículos próprios, arrendados ou mediante contratação de transportador autônomo de cargas, com mais de uma nota fiscal.  
  
Empresas com transporte próprio ou empresas que contratam autônomo, onde essas empresas efetuam o transporte com veículo próprio ou autônomo até o destinatário final da carga. Quando essas empresas efetuam o transporte, mesmo com veículo próprio ou autônomo, até a transportadora que efetuará o processo de entrega final, não são obrigadas a efetuar a emissão do **Manifesto**.  
  
A emissão do **MDF-e** cabe somente a operações com **CT-e - Conhecimento de Transporte eletrônico**, não existindo **MDF-e** para transportes **Municipais**, **Nota Fiscal de Serviço de Transporte**, uma vez em que a competência do **MDF-e**, modelo **58**, cabe ao estado **CT-e**.  
  
Atualmente somente a **SEFAZ** do Rio Grande do Sul encontra-se operando com o processo **MDF-e**, onde todos os **MDF-e** gerados de qualquer **Federação** são direcionados a essa **SEFAZ**. O projeto prevê que todas as **UF - Unidade Federação** estejam operando no processamento de seus **MDF-e**, mas sem uma data prevista para o início.  
  
**Importante**Sua geração deve ser feita por **UF** de **Destino da Carga** e tem caráter obrigatório somente para processos de **Carga Fracionada**, onde nesses processos os dados do veículo do referido transporte constará no **MDF-e**. Já para as operações de **Carga Lotação**, não é necessária a geração e emissão do **MDF-e** e os dados do veículo do referido transporte constam no respectivo **CT-e**.

* Para a **SEFAZ**, a determinação de **Fracionado** é o simples fato de existir mais de um **CT-e** em uma carga/veículo. Mesmo nos casos em que houver mais de um **CT-e** e todos esses sendo de um mesmo **Pagador de Frete**, **Origem** e **Destino** será caracterizado perante a **SEFAZ** como sendo um transporte **Fracionado** e não de **Lotação**.
* O **MDF-e** deverá ser encerrado após o final do percurso descrito no documento e sempre que haja transbordo, redespacho, subcontratação ou substituição do veículo, do motorista, de contêiner, bem como na hipótese de retenção imprevista de parte da carga transportada, através do registro deste evento conforme disposto no **Manual de Orientação do Contribuinte -** **MDF-e**.
* A emissão e encerramento do **MDF-e** deve ser feita pela **Filial** de início da operação, sendo essa operação executada no final do percurso. Depois de gerado, havendo a necessidade de efetuar a troca de um dos recursos do manifesto, **Veículo** ou **Motorista**, exemplo veículo quebrado, o **MDF-e** deve ser encerrado e gerado um novo, com a troca dos recursos.
* Não há o conceito de **Inutilização** de número de **MDF-e** como é existente no processo **CT-e**, devendo sempre um **MDF-e** ser gerado e encerrado. Sua numeração deverá constar sequencialmente na **SEFAZ** e devendo possuir numeração sequenciada de 1 a 999.999.999 por estabelecimento ou por série, devendo ser reiniciada quando atingido esse limite. O contribuinte poderá adotar séries distintas por emissão de **MDF-e**, vedada a utilização de subsérie. O **Fisco** poderá restringir a quantidade de série ou o uso de séries.
* O cancelamento de um **MDF-e** tem o prazo de 24 horas determinado pela **SEFAZ**.
* Caso a carga transportada seja destinada a mais de uma unidade federada, o transportador deverá emitir tantos **MDF-e** distintos quantas forem as unidades federadas de descarregamento, agregando por **MDF-e**, os documentos destinados a cada uma delas.
* A **SEFAZ** determina que enquanto houver **MDF-e** pendente de encerramento não ocorrerá a autorização de um novo **MDF-e** para a mesma **UF** **de Carregamento**, **UF** **de Destino** e para o mesmo veículo.
* Nos casos de **subcontratação**, o **MDF-e** deverá ser emitido exclusivamente pelo transportador responsável pelo gerenciamento deste serviço, assim entendido aquele que detenha as informações do veículo, da carga e sua documentação, do motorista e da logística do transporte.
* Atualmente a **SEFAZ** não impede a abertura e o encerramento de um **MDF-e** quando o veículo ou motorista em questão contiver **MDF-e** em aberto de outra transportadora, impedindo somente quando o **MDF-e** em questão é da mesma transportadora. Há um plano por parte da **SEFAZ** de vir a bloquear tais ações mesmo quando o referido **MDF-e** for de outra **Transportadora**.
* O **MDF-e** tem a finalidade de agilizar o **Registro em Lote** de documentos fiscais em trânsito e identificar a unidade de carga utilizada e as demais características do transporte. Entende-se como **Registro em Lote** a possibilidade de através da **Chave do** **MDF-e** obter-se as chaves de todos os documentos de transporte vinculados a ele **CT-e** e **NFe - Nota Fiscal Eletrônica**.
* O peso indicado no **MDF-e** como também a classificação dos produtos contidos serão utilizados para validações nas passagens de barreira e pesagens.
* Fazendo uma descrição simplificada do **MDF-e**, podemos dizer que o arquivo eletrônico conterá: **Dados do Veículo da Carga; Dados do Condutor; Previsão de Itinerário; Valor e Peso da Carga; Documentos Fiscais Transportados**;
* E seu transporte só poderá iniciar após sua devida autorização por parte da **SEFAZ**.
* Referente ao **conflito** de prazos de cancelamento existente entre **CT-e**, que é de 7 dias e o do **MDF-e**, que é de 24 horas. Na visão da **SEFAZ**, um **CT-e** pode vir a ser cancelado até que o mesmo não entre em processo de transporte ou trânsito, ou seja, a partir do momento que estiver em trânsito, respetivamente constar em um **MDF-e**, esse prazo perde a validade.
* Existem os apontamentos de **EVENTOS** ao **MDF-e**, que pode ser o fato de encerrar ou cancelar um determinado **MDF-e**, como também eventos apontados pelas barreiras, como o simples fato da passagem de trânsito do veículo pela mesma. O emitente poderá gerar somente os eventos de **Cancelamento** e **Encerramento**.
* Algumas transportadoras vêm se deparando com a seguinte rejeição ao tentar efetuar o cancelamento de um determinado **MDF-e**: Rejeição do **MDF-e** código **219 - circulação** do **MDF-e** verificada. Essa rejeição é apresentada quando tenta-se efetuar o cancelamento de um determinado **MDF-e** que já contenha evento de passagem por alguma barreira.
* Havendo **CT-e** em **contingência**, o **MDF-e** deverá ser gerado em **contingência** também se não, não será autorizado pela **SEFAZ**.
* Para acompanhar o transporte das mercadorias deverá ser impresso, em papel, um documento auxiliar do **MDF-e** de acordo com o *layout* definido no manual: **DAMDFE - Documento Auxiliar de Manifesto Eletrônico de Documentos Fiscais**. Impressão do **DAMDFE**: Havendo a necessidade e interesse por parte do emitente do **MDF-e**, poderá acrescentar campos no *layout* do **DAMDFE**, desde que sejam colocados abaixo do *layout* padrão. Ainda poderá utilizar até 50% do verso de qualquer folha do **DAMDFE** para continuação desses dados ou observações. O restante do verso deverá ser deixado sem nenhum tipo de impressão. Sempre que o verso do **DAMDFE** for utilizado, a informação que **continua no verso**, deverá constar no anverso, ao final do quadro **Observação**.
