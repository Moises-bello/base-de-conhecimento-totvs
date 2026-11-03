---
content_hash: ea1441b3f910d2a60153ded22b4c64f27be11ec1b29e391df2d0bea35dd664f6
fetched_at: '2026-06-29T00:09:37.245120+00:00'
page_id: '425459580'
product: rm
source: tdn-rm
title: TOTVS Integração -  Novidades das Versões Anteriores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459580
version: 6
---

**Novidades das Versões Anteriores**

---

****Versão 11.80.0****

**11.80.0** - Integração ECM - Certificado Digital  
   
A partir dessa versão além de efetuar o upload de documentos e inserí-lo em um fluxo de aprovação, a integração da Linha RM x ECM permite a certificação do arquivo. Essa funcionalidade prioriza a autenticidade e integridade do documento.  
    
**11.80.0** - TOTVS Business Analytics - Novos Indicadores  
   
Foi disponibilizado para o módulo de RH indicadores de desempenho para avaliação e acompanhamento dos responsáveis e da alta gerência nas organizações.  
    
**11.80.0** - Linha RM x Microsoft Dynamics CRM

A partir desta versão a integração é realizada com base nos Conceitos do TBC. Novos cadastros e processos são integrados, como por exemplo os cadastros de Empreendimento, Unidade e Sub-Unidade, e o processo de Venda.

**Versão 11.50.0**

**11.50.0** - Web Method Lançamento Financeiro.  
    
 O WebService do TBC (Totvs Business Conector) irá proporcionar aos clientes o uso de um Web Method para realizar lançamentos financeiros. O Web Service será preenchido um DataServer do TBC, onde os dados serão pré-validados e entregue ao financeiro no formato esperado. O módulo financeiro não sofrerá alteração para esta integração.  
     
 **11.50.0** - Web Method Movimentos.  
    
 O WebService do TBC (Totvs Business Conector) irá proporcionar aos clientes o uso de um Web Method para realizar inclusão, alteração e exclusão de movimentos. O Web Service será preenchido um DataServer do TBC, onde os dados serão pré-validados e entregue no formato esperado. O módulo de Gestão Estoque, Compras e Faturamento não sofrerá alteração para esta integração.  
     
 **11.50.0** - Realizar agendamento/execução de múltiplos conceitos.  
    
 A TOTVS disponibiliza para seus clientes a possibilidade de realizar o agendamento múltiplo de conceitos, bem como a execução múltipla dos mesmos. O agendamento é configurado através do processo "Processar Conceito", na visão Conceito. Após a parametrização, os conceitos estarão agendados e serão executados conforme configurado.   
     
 **11.50.0** - Lookup CRM.  
    
 A operação Lookup CRM recebe um valor e retorna de acordo com as parametrizações realizadas outro valor. Funciona da mesma forma que a operação Lookup, exceto que os dados são buscados na base CRM.  
     
 **11.50.0** - HCTransformação   
    
 O recurso Transformação é destinado à inclusão de mensagens de transformação (XSLT) utilizadas nas integrações dos produtos de origens diferentes (Ex.: BackOffice Protheus x Totvs Obras e Projetos). O objetivo é padronizar as integrações com os produtos TOTVS, fazendo com que os mesmos trabalhem com uma mensagem XML únicos evitando, desta forma, o processo de transformação de mensagens.   
     
 **11.50.0** - Nova pagina dos Web Services.  
    
 Está disponibilizada uma nova PageIndex para os Web Services, tanto para os que estão hospedados via Host quanto para os hospedados via IIS. Confira esta novidade!  
     
 11.50.0 - Histórico de Pedido.  
    
 Na integração TOTVS Obras e Projetos x BackOffice Protheus, ao gerar um pedido no TOP é possível que este seja do tipo Histórico. Este permite o registro manual no RM dos movimentos de compra que eventualmente foram criados no Protheus antes da integração ser habilitada, ou seja, serão apenas para consulta (histórico) e para compor corretamente o custo do projeto.  
     
 **11.50.0** -  Rateio de Centro de Custo na geração de S.A.  
    
 Disponibilizada na integração TOTVS Obras e Projetos x BackOffice a possibilidade de realizar o rateio de centro de custo durante a geração de uma Solicitação de Armazém no TOP. Os dados são automaticamente sincronizados ao Protheus.  
    
 **11.50.0** - Geração de Solicitação de Compras em Pedidos.  
    
 Na integração TOTVS Obras e Projetos x BackOffice Protheus, ao gerar um pedido no TOP é possível que este seja do tipo Solicitação de Compra. Desta forma será diretamente gerada no Protheus uma solicitação de compra.  
    
 **11.50.0** - Integração TOTVS Business Analytics.  
    
 A TOTVS disponibiliza para seus clientes a integração TOTVS Business Analytics com aplicativos BI (Business Intelligence). Esta integração irá proporcionar a comunicação com outros aplicativos BI de outras linhas TOTVS e também com linhas terceiras de uma maneira padrão. Fazendo uso do conceito de Stage Area, todos os BackOffices da TOTVS utilizarão o mesmo formato. Com este padrão adotado o BI poderá recuperar todos os dados do BackOffice de forma padrão, ou seja, esta comunicação não mudará conforme o BackOffice TOTVS utilizado. Confira esta novidade!

**Versão 11.40.0**

**11.40.0** - A integração Top x BackOffice Protheus foi alterado para poder gravar logs que utilizam procedures na tabela HcFilaIntegracao.  
    
 Implementado o recurso de gravação de logs na tabela HCFilaIntegracao, este recurso tem como objetivo a melhor identificação dos valores passados pelo processo de integração.  
     
 **11.40.0 -** Alteração no Configurador.  
    
 Foi retirado a opção "Marcar Todas", visando proporcionar segurança aos usuários.  
     
 **11.40.0** - Atualização nos parâmetros relativos ao ByYou ESB.  
    
 Atualização referente aos parâmetros ByYou ESB das integração Rm x SigaLoja Protheus e Totvs Educacional x Web Ensino x Ams, foram adicionados os parâmetros do ByYou ESB nas integrações e retirado da opção Configurações Gerais.  
     
 **11.40.0** - Atualização sobre o processo de controle de acesso nas visões Configurar e Parâmetros.  
    
 Implementado o controle de acesso nas visões Configurar e Parâmetros.  
     
 **11.40.0** - Cadastro de arquivos Xml.  
    
 Cadastro de arquivos Xml, referente a Nota Fiscal de serviço eletrônica.

Cadastro de arquivos Xml, referente ao Conhecimento de transporte.  
     
 **11.40.0** - Exibir listagem de Web Services do Conector via browser.  
    
 Foi disponibilizado a listagem de de Web Service do Conector via browser.  
     
 **11.40.0** - Integração de movimentos com os recursos de arquivos fiscais eletrônicos.

Importação de arquivos XML  
    
 Disponibilizado nesta versão a importação de arquivos XML que contempla a manipulação de arquivos Xml´s do tipo Notas Fiscais Eletrônicas (NF-e), Conhecimento de Transporte Eletrônico (CT-e), ou Notas Fiscais de Serviços (NFS-e). Atendendo a esta melhoria, estão disponíveis os seguintes processos: - Cadastro de XML O cadastro tem o objetivo de armazenar o arquivo XML no banco de dados, sendo utilizado para manutenção e controle dos processos executados sobre o arquivo. - Inclusão de Movimento com base em uma NF-e Validada pela SEFAZ É possível realizar a inclusão de um movimento utilizando um arquivo XML referente a uma NF-e, que tenha sido validado pela SEFAZ. A inclusão do movimento pode ser ocorrer de várias maneiras: Inclusão Direta ou Manual,Faturamento (Pedido de Venda) e Cópia por Referencia. Cancelamento/Exclusão de Faturamento e Exclusão de Movimento são alguns processos que também podem ser realizados através desta rotina.  
    
    
 **11.40.0** - Melhorias na visão de Conceito.  
    
 Foi disponibilizado melhorias para a visão de Conceito, são elas:

* Criado novos parametros para o Conceito. (Parâmetro: Sistema, Coligada do Contexto).
* Permitir definir conceitos de somente leitura (Realizar update na tabela HCConceito, campo ReadOnly).
* Filtro para Action de Conceito.

**11.40.0** - Outras atualizações.

* Atualização no contexto de sincronismo de projeto/obra/etapa/tarefa com o BackOffice Protheus.
* Atualização referente a informação do Codigo e Nome do Sistema na tela de Conceito.
* Atualizações no processo de geração de pedidos, quando o modulo Totvs Obras e Projetos está integrado com o BackOffice Protheus.
* Atualizações realizadas na integração Totvs Obras e Projetos x BackOffice Protheus.
* Atualizações referente a montagem e processamento de Conceitos na plataforma Oracle.
* Atualizações referente a visão de Conceito.
* Atualizações referente ao processo de adiantamento a receber e a pagar, processo que envolve a integração entre Totvs Obras e Projetos x BackOffice Protheus.
* Atualizações referente ao processo de calculo da curva S.
* Atualizações referente ao processo de geração de Pedido quando a aplicação está integrada com o BackOffice Protheus.
* Atualizações referente ao processo de geração de pedido.
* Disponibilizado atualizações referente ao processo de geração de Pedido.
* Foi disponibilizado atualizações referente a tela de Conceito, quando se utiliza Xml x Data Server.
* Realizado ajustes na visão "Configurar" referente ao a integração Totvs Obras e Projetos x BackOffice Protheus.
* Realizado alterações no processo de sincronismo de Moeda/Cotação, referente a Integração - Totvs Obras e Projetos x BackOffice Protheus.
* Realizado atualizações no processo de inclusão de arquivo Xml.
* Realizado atualizações no processo de sincronização de Projetos/Obra/Etapa/Tarefa referente a integração entre Totvs Obras e Projetos x BackOffice Protheus.
* Validação adicionada a tela de Conceito quando se trabalha na conexão de Origem com Arquivo Xml.

**11.40.0** - Outras atualizações:  
  
 Atualização nos scripts das integrações.  
  
 **11.40.0** - Processo que permita incluir um movimento de entrada, referente a NF-e, através da importação de um arquivo XML, validado junto a SEFAZ.  
  
 O processo de cadastro e envio de movimento de entrada referente a NF-e visa integrar a solução NeoGrid, que irá validar a autenticidade de uma NF-e junto a SEFAZ do estado origem, com base no arquivo XML. Ela irá garantir que o documento recebido é o mesmo emitido pelo fornecedor e armazenado na SEFAZ.  
  
 **11.40.0** - Recurso de Testar Url do Web Service do Protheus na integração Totvs Obras e Projetos x BackOffice Protheus.  
  
 Foi adicionado o recurso de Testar Url do Web Service do Protheus na integração Totvs Obras e Projetos x BackOffice Protheus.  
  
 **11.40.0** - Sincronizar usuários do Corpore RM ao GED (TOTVS By You ECM)  
  
 A partir da versão 11.40, é possível sincronizar usuários do Corpore RM ao GED - TOTVS By You ECM. O processo "Sincronizar usuários do Corpore RM ao GED" disponível no segmento Serviços Globais permite exportar o usuário do Corpore RM para o GED promovendo maior agilidade nos procedimentos.  
  
 **11.40.0** - WebServices no RM Conector sendo hospedado no RM.Host.  
  
 Foi disponibilizado na versão 11.40 o recurso que visa a hospedagem dos Web Services do Conector no Rm.host, para isto deve-se instalar Certificado e configurar os seguintes arquivos Rm.host.Config e Rm.exe.Config conforme abaixo: RM.Host.exe.config <appSettings> <add key="WcfProtocol" value="ALL" /> <add key="CERTIFICATEFINDVALUE" value="localhost" /> <add key="CERTIFICATESTORELOCATION" value="LocalMachine" /> <add key="CERTIFICATESTORENAME" value="TrustedPeople" /> <add key="CERTIFICATEFINDTYPE" value="FindBySubjectName" /> </appSettings> RM.exe.config <appSettings>  
 <add key="WcfProtocol" value="TCP" /> </appSettings> Sobre a configuração dos certificados isto pode variar de ambiente, a configuração acima é somente um exemplo.   
  
**Versão 11.20.0**  
  
 **11.20.0** – Atualização do Controle de opções na tela de Conceito   
  
 Anteriormente ao entrar na tela de Conceito, a aplicação exibia o tipo Web Service na aba Conexão Origem, a partir dessa versão foi feito um controle na aba Conexão Origem evitando conexões sobre o Tipo Web Service.       
  
 **11.20.0** - Configuração do arquivo TotvsAppServer.ini, para integração TOP x BackOffice Protheus  
  
 Foi realizado alteração no arquivo TotvsAppServer.ini, para realizar o retorno quando a integração ocorrer via Web Service. A partir de agora o arquivo deve ser alterado para contemplar corretamente a integração, conforme abaixo: Realizar a seguinte alteração no arquivo TotvsAppServer.ini: - NameSpace - <http://www.totvs.com.br/rm/>  
  
 **11.20.0** - Integração com GED  
  
 Implementado os anexos de "Integração com GED" no cadastro de professor e em documentos solicitados do aluno no RM Classis Net.       
  
 **11.20.0** - Integração da Linha RM ao ECM (GED)  
  
 A integração da Linha RM ao GED permite o relacionamento entre um registro em qualquer tela cadastro do RM e um (ou vários) documento(s) que será postado no GED. Assim, os documentos incluídos a partir de qualquer aplicativo da linha RM podem ser visualizados, alterados ou excluídos diretamente através do sistema sem a necessidade de login no ECM. Além disso, o TOTVS Business Connect (TBC) também permite a sincronização de usuários do RM para o GED.       
  
 **11.20.0** - Permissão para actions mais intuitiva  
  
 A partir dessa versão a concessão de permissão para as actions Importar, Exportar e Gereniar Conceito torna-se mais intuitiva. Na versão 11.0 a permissão para as actions era concedida através do seguinte caminho: Segmento Serviços Globais | aba Segurança | botão Perfil | sistema Integração. A partir da versão 11.20 a configuração de segurança poderá ser realizada através do seguinte caminho: Na aba Segurança | Botão Perfil | escolher sistema e habilitar a partir de Gestão as seguranças específicas.
