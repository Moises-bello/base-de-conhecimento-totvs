---
content_hash: ef70d12ba6af833a12e8a75499443b7e8b085457241b83e413c3fd69b2c2f91c
fetched_at: '2026-06-29T00:08:05.863135+00:00'
page_id: '235601202'
product: rm
source: tdn-rm
title: DT_API_do_Formulário_Dinâmico_Busca_de_Informações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235601202
version: 119
---

# API do Formulário Dinâmico - Busca de Informações

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Integração TOTVS Gestão Hospitalar e Formulários Dinâmicos (Prontuário Eletrônico do Paciente) |  |  | | --- | | **Rotina(s) envolvida(s)** | | Registro de Alta | |
| **Requisito (ISSUE):** | [PCREQ-10902](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10902 "PCREQ-10902") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL®, Oracle® |
| **Tabelas Utilizadas:** | SZCAMPOSFORMDINAMICO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação tem como objetivo a integração entre o TOTVS Gestão Hospitalar (RM Saúde) e a API da aplicação de Formulários Dinâmicos, utilizada pelo Prontuário Eletrônico do Paciente.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.11 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.11.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.11

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o **IIS** e busque, no diretório do **TOTVS.PEP.WEB**, através do web.config.
2. No web.config, pegue o endereço da aplicação de formulário dinâmico (key **ApplicationDynamicForms**).
3. Teste a **URL** no browser, na mesma máquina onde está rodando o **RM**. A aplicação de **Formulários Dinâmicos** abrirá.
4. Acesse **Opções / Parâmetros / Parâmetros Gerais / Aba "Integração" / Sub-aba “Outros”**. Preencha o campo **URL Form. Dinâmico** com o valor que está no **web.config.**
5. Na aplicação de **Formulários Dinâmicos**, procure pelo Formulário desejado e busque o ID correspondente na URL de acesso.
6. Exemplo: **<http://vrmsaude.poa01.local/TOTVS.FormBuilder.Web/FormExecution/New/a6137e4e-5f53-439f-ae7d-dc97ebb7b0e8>**, onde o ID é **a6137e4e-5f53-439f-ae7d-dc97ebb7b0e8.**
7. Realize o insert na tabela "**SZCAMPOSFORMDINAMICO**", com as informações obrigatórias, conforme exemplo:  
     
   INSERT INTO SZCAMPOSFORMDINAMICO  
   (CODCOLIGADA, IDCAMPO, TABELARM, COLUNARM, IDFORMDINAMICO, CAMPOFORMDINAMICO, UTILIZAATTENTIONID, RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY, RECMODIFIEDON)  
   VALUES  
   (2, 1, 'SZATENDIMENTO', 'CODCID',     'a6137e4e-5f53-439f-ae7d-dc97ebb7b0e8', 'CID\_PRINCIPAL', 'F','implantacao', GETDATE(), 'implantacao', GETDATE())

## Procedimento para Utilização

1. Preencha o campo referente ao metadado **CID\_PRINCIPAL**, ou como estiver configurado no formulário desejado, para o paciente que terá alta.
2. Acesse o registro de alta e busque pelo mesmo paciente. O valor correspondente será listado no campo CID(Alta), assim que o paciente for encontrado.

   Importante

   O cadastro e configuração do formulário dinâmico fica a critério do cliente, portanto o mesmo pode ou não conter o campo **patientId** na composição do filtro.   
   Caso o campo esteja no filtro, o campo **UTILIZAATTENTIONID** deverá estar setado como ‘T’.   
   As informações sobre a integração, uma vez inseridas no banco de dados, podem ser alteradas através do menu **Cadastros/Registro e Controle/Correlação com Form. Dinâmico**.

divs
