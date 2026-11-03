---
content_hash: 12a2391a580f73e02ee92f6ae28e55845894ae37b49d77d6bf427e7525631e24
fetched_at: '2026-06-29T00:06:00.170063+00:00'
page_id: '194512786'
product: rm
source: tdn-rm
title: ER_PCREQ-5424_Recuperação_de_dados_no_dia_D_do_Censo_do_ensino_básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=194512786
version: 14
---

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Totvs Gestão Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | R\_EDU011 | **IRM1** | PCREQ-5423 |
| **Requisito1** | PCREQ-5424 | **Subtarefa1** | PDR\_EDU\_EDU011-484 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | (x  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Recuperação de dados com base em uma data de corte informada pelo MEC, visando o envio de informações pertinentes ao Censo escolar

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Especificação de produto :  $/RM/Documentos/Edu-Educacional/Especificações/Matrícula/ Especificação - Matrícula.docx | [Alteração] | “Matrícula e Avaliação”->“Matrículas” (Matrícula no período letivo) | - |
| Especificação de produto :  $/RM/Documentos/Edu-Educacional/Especificações/Matrícula/ Especificação – Situação de Matrícula.docx | [Alteração] | “Matrícula e Avaliação”->“Matrículas” (acessar o processo “Alterar situação de matrícula”**)** | - |

A geração dos dados do Educacenso a serem enviados ao MEC, precisa sofrer uma reformulação, permitindo o cliente obter uma “fotografia” dos seus dados em distintas linhas do tempo. Evitando assim, que a volaticidade dos dados ao longo do tempo, mascare a real situação da época requerida. Sendo assim, devemos fazer as seguintes alterações:

1)  Para tal deverá ser criado um checkbox denominado “Preenche data de encerramento da matrícula para efeitos do Censo” na aba “Status no período letivo” do cadastro de “Situação de matrícula” situado no menu  “Currículo e Oferta” do Totvs Educacional.

2)  O campo a ser preenchido será criado na base de dados, na tabela SMATRICPL e será chamado de DTMATRICULAENCERRA, do tipo datetime, poderá ser nulo, caso preenchido não poderá ser menor que a data de matrícula. Este campo poderá ser preenchido em distintos momentos, sendo eles:

 2.1) No ato da alteração da situação de matrícula, somente para as situações de matrículas que estiverem com o checkbox acima citado marcado

 2.2) Manualmente na própria tela de matrícula no período letivo situada no menu “Matrícula e Avaliação”->“Matrículas” (Matrícula no período letivo), a permissão desta edição manual deverá ser configurada em “Sistemas Globais”->”Segurança”->”Perfis”(sistema: Educacional), edita-se o perfil, clica-se com o o botão direito do mouse e escolha o seguinte menu: “outras informações”->”Parâmetros educacionais” Item “Permitir alterar a data de encerramento da matricula para efeitos do Censo”.

 2.3) Ou por meio do novo  processo anexado à visão “matricula  no período letivo” denomimando “Altera datas de matrícula para efeitos do Censo”, que deverá ser criado, sendo necessária a permissão para a funcionalidade. (deverá ser exigido o motivo da alteração para avançar no processo,a data de matrícula não poderá ser vazia caso o seu checkbox estiver marcado (vide protótipo de tela), entretanto, a data de encerramento de matrícula poderá ter seu conteúdo vazio, caso o checkbox esteja marcado, entendendo assim que o objetivo seja limpar o mesmo.)

3) Independente da forma como este campo será preenchido, deverá ser gerado o log desta alteração, e apresentado no anexo “Histórico de alteração de matrícula período letivo”. Sendo assim será necessário a criação da coluna DTMATRICULAENCERRA e DTMATRICULAENCERRAANT na tabela SLOGPLETIVO. 

4) Deverá ser parametrizado no sistema, os códigos das consultas SQL a serem usadas pelos "registros" do Educacenso (ver pdf do Educacenso), 00, 10, 20, 30, 40, 50, 51, 60, 70 e 80.

5) Será criado no menu “Atividades acadêmicas-> Assistentes”, um processo denomiando “Arquivamento e recuperação de dados do Educacenso”, neste será possível  obter os dados do Censo, visualizá-los e alterá-los para que seja gerada a “fotografia”  do dia “D” (data de corte informado pelo MEC). Esta “fotografia” será um arquivo no formato XML sendo salvo na base de dados, que poderá ser consultado, alterado, e recuperado futuramente para geração dos dados a serem enviados ao MEC.

5.1) Para tal, deverá ter nesta nova tela, um campo de data denominado "Data de corte", que será usado como referência para filtrar os dados.  A data de corte deverá estar compreendida entre a “data de matrícula” e a “data de encerramento de matrícula para efeitos do Educacenso”, sendo que esta última poderá ser nula. Segue a cláusula que será acrescida às consultas do banco de dados, visando buscar os alunos e suas respetivas turmas, esta sentença deverá estar presente nos filtros dos registros 60, 70 e 80, pois diz respeito ao aluno. Esta lógica se aplica da seguinte forma:

          (:DATACORTE >= SMATRICPL.DTMATRICULA AND :DATACORTE <= SMATRICPL. DTMATRICULAENCERRA) OR (:DATACORTE >= SMATRICPL.DTMATRICULA  AND SMATRICPL. DTMATRICULAENCERRA  IS NULL)

Ao lado desta data deverá ter um botão "Gerar arquivo base", que irá executar as consultas SQL parametrizdas e gerar os dados no formato XML, salvando-os automaticamente em tabelas físicas no banco.

5.2) Com respeito a salvar o arquivo xml, ao gerar os dados do Censo, este será salvo em duas tabelas distintas, sendo elas : SCENSOXMLBASE e SCENSOXMLMANUTENCAO, um novo registro ocorrerá toda vez que o usuário optar por gerar os dados do Censo, obtendo assim uma fotografia em tempos distintos, este primeira versão será chamada de "Base".

5.3) Estes arquivos xml irão aparecer em um treeview na tela “Arquivamento e recuperação de dados do Censo Escolar” situado à esquerda na tela. Ao posicionar em algum nodo de arquivos manutenção do treeview e clicar no botão a ser criado "Ler arquivo XML", serão abertas à direita do treeview, várias abas com suas respectivas grades de dados, pertinentes aos assuntos agrupados do Censo.

5.4) Caso o usuário simplestemente altere os dados já gerados, ele poderá salvar estes por meio do botão a ser criado "Salvar nova versão XML", o sistema irá apenas criar uma nova versão em XML, gerando um novo registro somente na tabela SCENSOXMLMANUTENCAO, porém referenciando por meio de chave estrangeira a tabela SCENSOXMLBASE para sabermos de onde os dados foram originados.

5.5) O usuário poderá criar várias versões XML, porém deverá ter um botão "XML oficial", onde será sinalizado o XML oficial a ser usado pelo gerador de saídas que gerará o arquivo final a ser enviado para o MEC.

5.6) O usuário poderá excluir qualquer versão XML de "Manutenção", porém a versão "Base" não poderá.

5.7) Pelo fato dos campos “data de matrícula” e “data de encerramento da matrícula para efeitos do Educacenso” na matrícula do período letivo, poderem serem alterados mediante permissão, podem ocorrer casos em o usuário altere a natureza dos cadastros, possibilitando que algum aluno tenha mais de uma turma nos dados referente ao registro 80. Para estes casos, deverá ser criado o botão “Considerar último registro de matrícula”, que permitirá somente a permanência da última matricula feita pelo sistema. Esta verificação será feita pelo o campo físico da tabela SMATRICPL.RECCREATEDON.

5.8)Deverá ser criado o botão “Remover item”, este irá excluir uma ou várias linhas marcadas pelo checkbox, caso o usuário exclua algum item do registro 30, todos os filhos serão excluídos, ou seja, os itens dos registros 40, 50 e 51. Assim ocorre também para o registro 60 e seus filhos, 70 e 80.

6) Será criado no gerador de saídas o layout do Censo, resultando em arquivo txt com os dados a serem enviados para o MEC. Este layout irá obter os dados baseando-se na “fotografia” do dia “D”, ou seja, no arquivo XML gerado conforme especificado em todo o item anterior. Como poderão existir vários registros em ambas tabelas (SCENSOXMLBASE e SCENSOXMLMANUTENCAO), o sistema irá recuperar os dados somente do arquivo identificado como oficial, conforme citado no item 5.5.

Segue a estrutura física das tabelas dos arquivos XML:

**SCENSOXMLBASE**

CREATE TABLE [dbo].[SCENSOXMLBASE](  
 [CODCOLIGADA] [dbo].[DCODCOLIGADA] NOT NULL,  
 [CODFILIAL] [smallint] NULL,  
 [ANOBASE] [varchar](4) NOT NULL,  
 [IDARQUIVOXMLBASE] [int] NOT NULL,  
 [ARQUIVOXMLBASE] [dbo].[MEMO] NOT NULL,  
 [RECCREATEDBY] [varchar](50) NULL,  
 [RECCREATEDON] [datetime] NULL,  
 [RECMODIFIEDBY] [varchar](50) NULL,  
 [RECMODIFIEDON] [datetime] NULL,  
 [NOMEARQEXTERNO] [varchar](40) NOT NULL,  
 CONSTRAINT [PKSCENSOXMLBASE] PRIMARY KEY CLUSTERED   
(  
 [CODCOLIGADA] ASC,  
 [IDARQUIVOXMLBASE] ASC )

**SCENSOXMLMANUTENCAO**

CREATE TABLE [dbo].[SCENSOXMLMANUTENCAO](  
 [CODCOLIGADA] [dbo].[DCODCOLIGADA] NOT NULL,  
 [CODFILIAL] [smallint] NULL,  
 [IDARQUIVOXMLBASE] [int] NOT NULL,  
 [IDARQUIVOXMLMANUTENCAO] [int] NOT NULL,  
 [ARQUIVOXMLMANUTENCAO] [dbo].[MEMO] NOT NULL,  
 [RECCREATEDBY] [varchar](50) NULL,  
 [RECCREATEDON] [datetime] NULL,  
 [RECMODIFIEDBY] [varchar](50) NULL,  
 [RECMODIFIEDON] [datetime] NULL,  
 [OFICIAL] [varchar](1) NULL,  
 [NOMEARQEXTERNO] [varchar](40) NULL,  
 CONSTRAINT [PKSCENSOXMLMANUTENCAO] PRIMARY KEY CLUSTERED   
(  
 [CODCOLIGADA] ASC,  
 [IDARQUIVOXMLBASE] ASC,  
 [IDARQUIVOXMLMANUTENCAO] ASC

### Opcional

## Protótipo de Tela

**Protótipo 01 - Status**

**Protótipo 02 - Parametros Educacionais**

****Protótipo 03 - Cadastro da matrícula no período letivo****

********Protótipo 04 - Log de alteração da data de encerramento para efeitos do Educacenso********

****************Protótipo 05 - Processo de alteração das datas para efeitos do Educacenso****************

************************************************Protótipo 06 - Parametrização das consultas SQL************************************************

********************************Protótipo 07 - Tela Arquivamente e recuperação dos dados do Educacenso********************************

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
