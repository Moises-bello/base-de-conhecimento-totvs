---
article_id: 360027399631
category: Gestão de Transportes (TMS)
content_hash: 8dcef1d38caf9af0413de77ec758bb82059759f76b82f377843b6de7effbac31
fetched_at: '2026-06-28T22:45:29.218296+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Frete Informado para Frete a Receber
type: support-article
updated_at: '2025-09-09T19:13:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027399631-Log%C3%ADstica-Linha-Protheus-TMS-Frete-Informado-para-Frete-a-Receber
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25185675337751)**Tempo aproximado para leitura: **00:02:20 min****Dúvida**Como configurar o **Frete Informado**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Utilizando a opção **Frete** **Informado**, o valor do frete a receber será definido sempre no momento da digitação do documento, pela opção **Outras Ações / Frete Inf.** na inclusão do documento na rotina **TMSA050 - Entrada de Documentos de Clientes**.  
  
Configurar os parâmetros:

* **MV\_TMSVINF = .T. -** Permite informar o valor do Frete informado na digitação da Nota Fiscal do cliente - **TMSA050**.
* **MV\_COTVFEC = .F. -**  Permite informar o valor do Frete informado no Painel de Agendamento - **TMSAF76**.

Efetuar os seguintes cadastros:  
  
**1. Contrato Cliente**1.1. Acesse **Atualizações / Comercial / Contrato Cliente - TECA250;**1.2. Na aba **TMS**, o campo **Seleção de Serviços** informe a opção de **1 - Digitado**, para uso do frete informado.  
  
**2.** **Cadastro de Componentes**2.1. Acesse **Atualizações / Comercial / Componentes - TMSA030:**  
2.2. Defina o componente com um comportamento que seja afetado no processo de digitação da **NF-e - Nota Fiscal eletrônica** na rotina **Entrada de Documentos de Clientes** **- TMSA050**, como **Peso**, **Valor** ou **Volume**. Para isto deve utilizar o campo **Calc. Sobre - DT3\_TIPFAI** com uma destas opções **01 - Peso Mercadoria**, **02 - Valor Mercadoria** ou **03 - Qtde. Volumes**. **3. Configuração Tabela de Frete**3.1. Acesse **Atualizações / Comercial / Config tab Frete - TMSA130.**3.2. Defina uma tabela de frete com o componente que foi criado;  
  
**4. Tabela de Frete**  
4.1. Acesse **Atualizações / Comercial / Tabela de frete - TMSA010.**4.2. Inclua uma tabela de frete com Origem e Destino, faixa até **999.999.999,9999**e valor 100,00;  
  
**5. Serviço x Tarefa**5.1. Acesse **Atualizações / Serviços / Serviço x Tarefa - DLGA070.**5.2 Altere o Serviço de negociação informando um percentual de desconto nos campos **1º.%Desc.Cot, 2º.%Desc.Cot, 3º.%Desc.Cot**e **4º.%Desc.Cot**Se os valores utilizados no **Frete Informado** não forem acatados no **Preview** ou **Calculo do Frete**, então, Acesse **Atualizações / Comercial / Perfil do Cliente - TMSA480,** e ajuste o campo **Recalcula frete na cotação - DUO\_RECFRE** para **2 - Não.**
