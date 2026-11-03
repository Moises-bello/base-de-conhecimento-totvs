---
article_id: 360024800734
category: Gestão de Transportes (TMS)
content_hash: 8c1c331a7b0e3e94a4f8caccfb2c2f7ae8bde046f8a4b0c62bf59b666790df99
fetched_at: '2026-06-28T22:45:27.311097+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cadastros básicos para emissão de documento
type: support-article
updated_at: '2025-06-06T17:20:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024800734-Log%C3%ADstica-Linha-Protheus-TMS-Cadastros-b%C3%A1sicos-para-emiss%C3%A3o-de-documento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23157230939159)***Tempo aproximado para leitura: **00:06:30 min****Dúvida**Quais os cadastros principais relacionados a emissão de um documento no **TOTVS Logística TMS**?  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Os cadastros principais relacionados a emissão de um documento no **TOTVS Logística TMS**são:

1. **MV\_INTTMS -** Identifica se o **TOTVS Logística TMS** está integrado aos outros módulos. Deve ser o primeiro parâmetro a ser habilitado para utilizar o **TOTVS Logística TMS**;
2. Acessar o menu **Atualizações/Logística/Estrutura de regiões - TMSA120**.Cadastrar a estrutura de regiões utilizando o *wizard* com o botão direito do *mouse*.
3. **MV\_CDRORI -** Define o código da região de origem da filial. Após definir a **E****strutura de região**, cada filial deve possuir este parâmetro definido com o código da região referente ao seu município;
4. Cadastrar condição de pagamento. Acessar menu **Atualizações/Cadastros/Condições de pagamento - MATA360**;
5. Cadastrar clientes. Acessar menu **Atualizações/Cadastros/Clientes - MATA030/CRMA980**;
6. **MV\_CLIGEN** - Define o código do **Cliente/Loja** que serão utilizados nos **Contratos Genéricos** no módulo **TOTVS Logística TMS**. Deve ser definido com o **código** e **loja** do cliente genérico. Este parâmetro deve ser cadastrado como compartilhado entre as filiais. Para preencher o **MV\_CLIGEN**, é necessário que cadastre um cliente na rotina **Clientes - MATA030/CRMA980**. Este cliente genérico permite que as configurações comerciais sejam tratadas de forma mais abrangente, evitando assim uma demanda de cadastros comerciais para clientes que possuirão o mesmo comportamento **Comercial/Fiscal**;
7. **MV\_ESTADO** - Sigla do estado de onde a filial emissora do **CT-e** esta localizada. Para efeito de cálculo de **ICMS - Impostos Sobre Circulação de Mercadoria e Serviços**, este parâmetro deve ser exclusivo por filial;
8. Acessar o menu **Atualizações/Logística/Complemento de Regiões - TMSA380**. Efetuar o cadastro das regiões;
9. Cadastro de produtos.Acessar o menu **Atualizações/Cadastros/Produtos - MATA010**:
   1. **Produto de transporte:** é o produto indicado na **DANFE - Documento Auxiliar da Nota Fiscal Eletrônica** a ser transportada. Podendo ser cadastrado um único produto indicando somente o tipo da mercadoria como **Auto peças, eletrônicos, alimentos e etc**;
   2. **Produto de Cálculo.** Este produto é utilizado para a escrituração do documento que será emitido no **TOTVS Logística TMS**. Necessário cadastrar uma para cálculo do **ICMS**  e outro para o **ISS - Imposto Sobre Serviços**. Se necessário, verifique a documentação [Logística - Linha Protheus - TMS - Cadastro de produto de cálculo;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025656472-Log%C3%ADstica-Linha-Protheus-TMS-Cadastro-de-produto-de-c%C3%A1lculo)
   3. **MV\_PROGEN -** Define o código do produto que sera utilizado para obtenção de tabelas de frete ou seguro quando não for encontrado o código do produto solicitado.
   4. Cadastrar classificação **ONU - Organização das Nações Unidas:** Utilizado para transporte de produtos perigosos. **Atualizações/Cadastros/Classificações ONU - TMSA021**.
10. Cadastrar complemento de produto - aba **TMS**. Quando o produto for perigoso é necessário informar o número de **ONU** para envio no **XML - Extensible Markup Language** do **CT-e - Conhecimento de Transporte Eletrônico**. Este cadastro pode ser efetuado somente para o produto de transporte, não tendo necessidade de fazer para o produto de cálculo;
11. Cadastrar configurações de documento:
    1. Cadastrar **TES - Tipos de Entrada e Saída**. Acessar menu **Atualizações/Cadastros/TES - MATA080:**  
       1. **MV\_TESDD -** Indica **TES** predeterminado para geração de movimentos de materiais **devolvidos** à terceiros. Necessário cadastrar a **TES** de saída - **981** - indicada no parâmetro. Este **TES** não precisa calcular impostos;
       2. **MV\_TESDR -**Indica **TES** predeterminado para geração de movimentos de materiais **remetidos** de terceiros. Necessário cadastrar a **TES** de entrada - **481** -  indicada no parâmetro. Este **TES** não precisa calcular impostos;
       3. **TES de saída -**Cadastrar **TES** de saída que será utilizado no cálculo dos impostos.
    2. Cadastrar uma série para ser utilizada no **CT-e** na **SX5**. Se necessário, verifique a documentação [Logística - Linha Protheus - TMS - Série CT-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10112735030295-Log%C3%ADstica-Linha-Protheus-TMS-S%C3%A9rie-CT-e);
    3. Cadastrar **Configuração de documentos.** Indicar **Docto. Transp, Série** indicado no tópico 10 item 2 e **Cod. Produto**com o produto de cálculo indicado no tópico 8 item 2. Acessar menu  **Atualizações/Documentos e regras/****Config. documentos - TMSA150**;
    4. Cadastrar **Regra de Tributação** indicando a **TES** que será utilizada para calcular os impostos. Acessar menu **Atualizações/Documentos e regras/Regras Tributação - TMSA410**;
    5. Cadastrar **Regra de Tributação Por cliente**. Indicando no cadastro o **Cliente genérico, Docto. transp** e **Regra trib.**Acessar menu **Atualizações/Documentos e regras/Regras Por cliente - TMSA600**.
12. Serviços: 
    1. Carregamento:
       1. **Tarefa**. Acessar menu **Atualizações/Serviços/Tarefas x atividades - DLGA080.**Indicar **Cod. tarefa=004** e **Cod. atividad=048**;
       2. **Serviço Entrega operacional**. Acessar menu **Atualizações/Serviços/Serviços x tarefas - DLGA070.** Indicar o conteúdo dos campos conforme exemplo.   
          **Cod. Servico= 002  
          Serv. Transp.= 3  
          Tipo Transp.= 1  
          Categ. servic= 2  
          Cod. Tarefa= 004**
       3. **Serviço transferência operacional**. Este deve ser cadastrado somente quando a transportadora possuir processo de transferência de mercadoria entre as suas filiais.  Acessar menu **Atualizações/Serviços/Serviços x tarefas - DLGA070**. Indicar o conteúdo dos campos conforme exemplo.   
          **Cod. Servico= 014  
          Serv. Transp.= 2  
          Tipo Transp.= 1  
          Categ. servic= 2  
          Cod. Tarefa= 004**
    2. Negociação:
       1. São os serviços que serão indicados no contrato do cliente. Caso as opções de **Cód. Serviço**não atendam as necessidade. Novos códigos podem ser cadastrados por meio do módulo **SIGACFG-Configurador**nas tabelas genéricas **SX5**tabela **L4**.
       2. **Negociação de entrega**. Acessar menu **Atualizações/Serviços/Serviços x tarefas - DLGA070**. Indicar o conteúdo dos campos conforme exemplo.  
          **Cod. Servico= 013  
          Serv. Transp.= 3  
          Tipo Transp.= 1  
          Categ. servic= 1  
          Docto. transp= 2  
          Serv. Operac.= 002  
          Cod. Tarefa= 004**
       3. **Negociação de Transferência**.  Este deve ser cadastrado somente quando a transportadora possuir processo de transferência de mercadoria entre as suas filiais.  Acessar menu **Atualizações/Serviços/Serviços x tarefas - DLGA070**. Indicar o conteúdo dos campos conforme exemplo.   
          **Cod. Servico= 018  
          Serv. Transp.= 2  
          Tipo Transp.= 1  
          Categ. servic= 1  
          Docto. transp= 2  
          Serv. Operac.= 014  
          Cod. Tarefa= 004**
    3. **MV\_SVCENT -** Código do serviço para carregamento de entrega do módulo **TOTVS Logística TMS**. Indicar **002**;
13. Comercial.
    1. **MV\_TMSCFEC -** Indica se as funcionalidades de carga fechada estão ativas. Ativar parâmetro;
    2. **MV\_CONTHIS -** Controla alteração da Tabela/Ajuste de Frete;
    3. **MV\_CALNORI** - Define se o Sistema irá verificar os níveis superiores da região de origem no cálculo do frete. Caso o cliente queira subir a estrutura de regiões para origem da tabela. No configurador, utilizar o programa **Bases de Dados - CFGX031** que fica no caminho **Protheus/Configurador/Base de Dados/Dicionario**.
    4. **Cadastrar componentes de frete.** Acessar menu **Atualizações/Comercial/Componentes Frete - TMSA030**. Defina o componente de acordo com sua regra comercial preenchendo os campos obrigatórios;
    5. **Cadastrar configuração da tabela de frete**. Acessar menu **At****ualizações/Comercial/Config.tab. Frete - TMSA130**. Criar a composição da tabela de frete;
    6. **Cadastrar Tabela de frete**. Acessar menu **Atualizações/Comercial/Tab. de Frete - TMSA010**. Indicar faixas e valores de acordo com as regiões atendidas pela transportadora;
    7. **Cadastrar negociação**. Acessar menu **Atualizações/Comercial/Negociações Cliente - TMSAF70**;
    8. **Cadastrar contrato do cliente**. Acessar menu **Atualizações/Comercial/Contrato cliente - TECA250**. Efetue o cadastro com o **Cliente genérico** preenchendo os campos obrigatórios;
    9. **Cadastrar perfil do cliente**. Acessar menu **Atualizações/Comercial/Perfil do Cliente - TMSA480**.Efetue o cadastro com o **Cliente genérico** preenchendo os campos obrigatórios;
