---
content_hash: ff1626a3d1d95f6257b79153db0a05bab8080b8a07e94e23d6e580af12459001
fetched_at: '2026-06-28T21:35:18.234249+00:00'
page_id: '152802071'
product: fluig
source: tdn-fluig
title: Impressão de cópia controlada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=152802071
version: 110
---

# Introdução

---

O recurso de impressão de cópia controlada no TOTVS Fluig Plataforma permite identificar e rastrear as cópias emitidas dos documentos.

É um recurso importante quando ocorre atualização de normas e procedimentos, principalmente de ISO, onde é necessário recolher as cópias impressas antigas e disponibilizar as novas versões para as áreas.

Com o registro de quais áreas possuem os documentos impressos fisicamente, facilita muito essa substituição. Além de evitar não conformidades em auditorias.

# Pré-requisitos

---

São pré-requisitos para a impressão de documentos:

* A configuração de ao menos uma área. Para saber como fazer isso, acesse a documentação sobre [Áreas](http://tdn.totvs.com/x/w4D5DQ);
* A configuração de marca d'água é opcional. Para saber mais, acesse a documentação de [Marca d'água](http://tdn.totvs.com/x/BoH5DQ);

# Tipos de arquivos suportados

---

A plataforma permite a impressão de cópia controlada apenas para arquivos PDF, documentos do Word e planilhas do Excel. Em servidores Linux, arquivos com extensões .doc e .xls podem não funcionar.

A tabela abaixo exibe as extensões suportadas pelo recurso de cópia controlada:

| Extensão | Compatível? | Sistema Operacional do servidor da plataforma |
| --- | --- | --- |
| **.doc** |  | Somente em servidor Windows |
| **.docx** |  | Windows/Linux |
| **.ppt** |  |  |
| **.pptx** |  |  |
| **.xls** |  | Somente em servidor Windows |
| **.xlsx** |  | Windows/Linux |
| **.pdf** |  | Windows/Linux |
| **.txt** |  |  |

Atenção!

Em algumas instalações ocorre o erro: “java.lang.NoClassDefFoundError : null” ao imprimir documentos Microsoft® Office. Para mais detalhes de como solucionar a inconsistência confira a documentação [Configuração de serviços de componentes](http://tdn.totvs.com/x/eiH2Dw).

# Impressão de documentos

---

Os documentos com os tipos de arquivos suportados (listados acima) configurados para utilizar o Visualizador Interno, SEMPRE são impressos como cópia controlada.

Para os demais tipos de arquivos que não são suportados, NÃO é permitida a impressão pela Cópia controlada. É possível apenas a impressão normal do documento e deve ser realizada exclusivamente pela Visualização do Documento, no ícone da Impressora (ver segunda opção abaixo).

## Acionar a impressão

Você pode fazer a impressão de um documento através da navegação ou através da visualização.

Na navegação, selecione o arquivo e acione o botão Mais > Imprimir cópia controlada.

Na visualização do documento há duas opções. Na primeira acione Ações do documento > Imprimir cópia controlada.

Na segunda, acione o ícone da impressora.

Atenção

Para os documentos com os tipos de arquivos NÃO suportados esta é a única forma de impressão pela plataforma. Não sendo registrada como uma cópia controlada.

Para os documentos com os tipos de arquivos suportados, configurados para não utilizar o Visualizador Interno, também será realizada uma impressão normal, sem registro de cópia controlada.

## Realizar a impressão

Após acionar a impressão, você será apresentado à tela de configuração. Configure cada campo conforme a sua necessidade:

1. **Documento protocolo:** escolha um documento protocolo para a impressão. Ele pode conter variáveis de impressão que serão atualizadas quando a impressão for finalizada. Para saber mais acesse o item .
2. **Renderizador de impressão de PDF:** se você não possuir uma impressora instalada e configurada no computador, a plataforma utilizará o renderizador escolhido para gerar um arquivo PDF que normalmente é aberto automaticamente pelo próprio navegador em uma nova aba. Assim você pode salvar o documento e imprimi-lo posteriormente ou apenas mantê-lo. Se a impressão parecer desconfigurada com o renderizador padrão (PDFRenderer), altere para a opção JPedal e tente novamente.
3. **Marca d'água:** Marca d'água que será incluída nas cópias impressas, se desejado. O cadastro da marca d'água é realizado no recurso [Marca d'água](https://tdn.totvs.com/pages/viewpage.action?pageId=234455302) do Painel de controle.   
   Importante: A marca d'água selecionada será aplicada somente nos documentos que não possuem marca definida. Para ver a marca d'água de cada documento, verifique a seção **Documentos selecionados para imprimir cópia controlada**. Caso desejado, para alterar a marca definida, acesse as propriedades do documento.
4. **Área(s) Destino:** são as áreas para as quais a impressão será feita. Esse campo é obrigatório. Cadastre pelo menos uma área. Para saber como fazer isso, acesse a documentação sobre [Áreas](http://tdn.totvs.com/x/w4D5DQ).
5. **Documentos selecionados para imprimir cópia controlada:** Nessa lista são apresentados os documentos que serão impressos, bem como a marca d'água a ser aplicada a cada um deles.
6. **Imprimir cópia controlada:** ao acionar esse botão, a impressão será feita.

# Recursos adicionais

---

A impressão de cópia controlada foi desenvolvida inicialmente com o recurso de *applets*, porém este recurso atualmente está disponível somente para o navegador Internet Explorer. Os navegadores Google Chrome (versão 45 ou superior) e Mozilla Firefox (versão 52 ou superior) não suportam mais a execução dos plugins NPAPI necessários.

Este recurso possibilita identificar qual impressora foi selecionada e também definir o número de cópias emitidas.

Caso você deseje utilizar essas opções é necessário atender os requisitos a seguir:

* Configurar o  no computador do usuário que fará a impressão;
* Utilizar o navegador Internet Explorer. Acesse a [Matriz de Portabilidade](http://tdn.totvs.com/x/_ApbB) para saber qual é a versão homologada;
* Marcar a opção "Habilita applet" em Painel de Controle > Parâmetros. Para saber mais sobre essa tela acesse a documentação sobre [Parâmetros](http://tdn.totvs.com/x/goH5DQ).

  Quando a opção "Habilita applet" está marcada no Painel de Controle > Parâmetros, você NÃO conseguirá fazer a impressão através dos navegadores Firefox ou Chrome. Ao tentar fazer isso, será apresentada a mensagem "Não foi possível carregar applet".

  Nesse caso, você poderá apenas fazer a impressão através do Internet Explorer.

  Se quiser fazer a impressão através dos outros navegadores, desabilite a opção. Lembrando que nesse caso, a informação de qual impressora foi selecionada, não será registrada.

  Importante

  Informamos que o Office 365 não encontra-se no rol de versões homologadas pelo TOTVS Fluig Plataforma.

# Log de cópia controlada

---

O log de cópia controlada é o registro das informações de cada impressão de cópia controlada. Esse registro é importante, pois oferece total controle e rastreabilidade sobre as cópias.

Para saber como consultar esse log acesse a documentação de [Log de cópia controlada](http://tdn.totvs.com/x/-YD5DQ).

# Compatibilidade de impressão com o MS Office

---

Por padrão o TOTVS Fluig Plataforma utiliza o OpenOffice como motor padrão para a impressão de documentos, ou seja, é possível que determinados documentos não sejam impressos exatamente como são visualizados no MS Office.

Para que o MS Office seja o motor padrão de impressão é necessário fazer a [Configuração dos serviços de componentes](http://tdn.totvs.com/x/eiH2Dw). Não é necessário reiniciar a plataforma após a configuração. Basta fazer uma nova impressão.

oculto

**Observação KCS:** Informação duplicada no artigo <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360033839533>.  
Caso seja feita alguma atualização, lembrar de atualizar o artigo!

# Variáveis de impressão e visualização

---

É possível configurar variáveis nos documentos que serão atualizadas durante a visualização ou durante a impressão (quando o documento for utilizado como protocolo). As variáveis podem informar a versão do documento, publicador ou a data de publicação, por exemplo.

## Pré-requisitos

---

Para que as variáveis sejam atualizadas é necessário que a opção *"*Atualiza Propriedades Cópia Controlada?" localizada na aba Informações Gerais das propriedades do documento esteja marcada.

Essa opção pode ser alterada manualmente durante ou após a publicação ou pode estar configurada nas propriedades herdadas da pasta, para que seja marcada automaticamente durante a publicação.

## Configuração de atualização das variáveis

---

Para marcar essa opção manualmente, durante a publicação de documento avançado ou na edição de propriedades após a publicação, acione a aba **Informações Gerais** e marque a opção **Atualiza Propriedades de Cópia Controlada?**.

Para fazer a configuração automática, acione as propriedades da pasta. Acesse a aba **Propriedades Herdadas** e marque a opção **Atualiza propriedades de Cópia Controlada?**.

## Variáveis de visualização

---

As variáveis de visualização são atualizadas sempre que o documento é aberto e visualizado dentro da plataforma. Confira a lista de informações que podem ser adicionadas ao documento:

| Variável | Descrição |
| --- | --- |
| Document.Author | Autor do documento |
| Document.Author.ID | Matricula do autor do documento |
| Document.Author.Name | Nome do autor do documento |
| Document.Active | Documento ativo |
| Document.ID | Código do documento |
| Document.Publisher | Publicador do documento |
| Document.Publisher.ID | Matricula do publicador do documento |
| Document.Publisher.Name | Nome do publicador do documento |
| Document.Version | Versão do documento |
| Document.Revision | Revisão do documento |
| Document.Description | Descrição do documento |
| Document.Comments | Comentários do documento |
| Document.VersionDescription | Descrição da Versão/Revisão |
| Document.Tag | Tags do documento |
| Document.ApprovedOn | Data que o documento foi aprovado |
| Document.CreationDate | Data de criação do documento |
| Document.ExpiresOn | Data de expiração do documento |
| Document.FirstVersionDate | Data da primeira versão |
| Document.LastUpdateDate | Data da última atualização |
| Document.Approvers1,  Document.Approvers2,  Document.ApproversN | Aprovador do nível 1.  O N representa qual aprovador a ser retornado: o 1 retorna o primeiro aprovador, o 2 retorna o segundo e assim sucessivamente, especificamente do nível 1. |
| Document.Level2.Approver1,  Document.Level2.Approver2,  Document.LevelN.ApproverN | Aprovador do nível N.  O N em *Level* representa qual nível deve ser retornado, e o N em *Approver* representa qual aprovador a ser retornado. Por exemplo: Document.Level2.Approver1 retorna o primeiro aprovador do nível 2. |

## Variáveis de impressão

---

As variáveis de impressão são atualizadas somente no documento protocolo quando a impressão é concluída. Essas variáveis não são atualizadas quando o documento é visualizado dentro da plataforma.

Nesse caso, se você tentar visualizar um documento que possui variáveis de impressão, ela será exibida como no exemplo abaixo.

Confira a lista de informações que podem ser adicionadas ao documento:

| Variável | Descrição |
| --- | --- |
| Document.PrintDate | Data da impressão |
| Document.PrintRequester | Requisitante/Solicitante |
| Document.PrintedDocument.AreaResponsible | Responsável pela área |
| Document.PrintedDocument.Description | Descrição do documento |
| Document.PrintedDocument.Comments | Comentários do documento |
| Document.PrintedDocument.VersionDescription | Descrição da Versão/Revisão |
| Document.PrintedDocument.Tag | Tags do documento |
| Document.DocumentNrDocumento | Número do documento |
| Document.PrintedDocument.Version | Versão do documento |
| Document.PrintedDocument.Revision | Revisão do documento |
| Document.DestinationArea | Área |
| Document.PrintedDocument.Publisher | Publicador do documento |
| Document.PrintedDocument.VersionDescription1 | Descrição da versão do documento |
| Document.PrintedDocument.VersionDescription2 | Continuação da descrição da versão do documento |
| Document.PrintedDocument.VersionDescription3 | Continuação da descrição da versão do documento |

Atenção

É padrão do próprio MS Office limitar as propriedades dos documentos em 127 caracteres durante a visualização ou impressão.

## Eventos de documentos

---

Os eventos [onApplyDocumentPrintProperties](http://tdn.totvs.com/display/fluig/Eventos+de+Documentos#EventosdeDocumentos-onApplyDocumentPrintProperties) e [onApplyDocumentProtocolProperties](http://tdn.totvs.com/display/fluig/Eventos+de+Documentos#EventosdeDocumentos-onApplyDocumentProtocolProperties) podem ser utilizados para atualizar ou recuperar as informações das variáveis configuradas nos documentos.

Veja também o exemplo (**interacting-with-copy-controlled-properties**) disponível no repositório do TOTVS Fluig Plataforma clicando **[aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/interacting-with-copy-controlled-properties)**.

## Configurar variáveis

---

### Microsoft Word

Com o documento aberto no Microsoft Word, posicione o cursor no local onde a variável deve ser incluída.

Pressione **CTRL + F9** e preencha o espaço entre as chaves (**{ }**) como no exemplo abaixo:

### Microsoft Excel

falseexcelPasso 1

* Com o documento aberto no Microsoft Excel, clique com o botão direito do mouse sobre **qualquer coluna** conforme a necessidade (1), em seguida acione a opção **Inserir** (2). Para demonstrar esse recurso, utilizaremos a Coluna A:

Passo 2

* Preencha as células da **coluna escolhida** no passo anterior, com um nome que identificará as variáveis que você escolheu. Por exemplo, **Publicador** e **Data**.

Passo 3

* Clique na célula da primeira variável (A2 usada neste exemplo abaixo) e em seguida digite o valor Document.Publisher (ou a variável escolhida) na **Caixa de Nome**;
* Pressione ***enter*** para salvar;
* Faça o mesmo nas demais células, informando na caixa de nome a variável escolhida.

Passo 4

* Clique sobre a célula que deverá ser atualizada com o valor da variável;
* Digite "=" e em seguida clique sobre a célula da variável configurada no passo anterior;
* Pressione ***enter*** para salvar;
* Faça o mesmo com as demais células;
* Salve o documento.

Passo 5

* Clique com o botão direito do mouse sobre a coluna de variáveis que foi criada no passo 1;
* Aciona a opção **Ocultar** para que a coluna não seja exibida;
* Salve o documento.

Passo 6

Confira o passo a passo completo do exemplo que acabamos de fazer:

Atenção!

Lembrando que, a partir do pacote de atualização da release **fluig 1.7.1-220719 -****Crystal Lake****,** em arquivos da ferramenta Excel é possível inserir variáveis em **qualquer coluna ou planilha.**

$("b:contains('oculto')").parent().parent().hide();
]]>
