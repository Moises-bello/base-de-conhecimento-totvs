---
content_hash: 5e2027d62f953ac92a21c9686e30014cff5e2abe688a8a0de636d1fd1c1acb2b
fetched_at: '2026-06-29T00:08:32.426799+00:00'
page_id: '273985849'
product: rm
source: tdn-rm
title: DT Parâmetros de Integração com Carestream por Unidade de atendimento e Modalidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273985849
version: 13
---

# Parâmetros de Integração com Carestream por Unidade de atendimento e Modalidade

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Parâmetros de Integração com Carestream por Unidade de atendimento e Modalidade | SauParamCarestreamModalidadeAction |  |  | | --- | | **Rotina(s) envolvida(s)** | | Pedido de Exames para paciente Interno | | Avaliações complementares (Prontuário) | |
| **Cadastros Iniciais:** | Cadastro de Exames, Cadastros de Unidades de Atendimento |
| **Parâmetro(s):** | Parametrização da estação de trabalho para habilitar o botão de visualização das imagens |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | SAUHRM02-333 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZPARAMCARESTREAMMODALIDADE |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A melhoria consiste em permitir a parametrização da integração com Carestream por Unidade de atendimento e Modalidade do exame de imagem. O usuário poderá possuir endereços de sistema PACS para cada Unidade de atendimento/Modalidade. Deste modo, pode possuir fornecedores de PACS para cada modalidade de exames e que sigam o padrão Carestream para recebimento dos pedidos e envio dos laudos.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.17 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.17.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.17

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Cadastros / Unidades de Diagnóstico / Parâmetros Carestream por Unidade de Atendimento e Modalidade**.
2. Realize os cadastros necessários para cada unidade de atendimento e modalidade do exame. Se informado o tipo **Diretório**, informe a pasta onde os pedidos serão gravados.  
   Ao selecionar o tipo de integração como Diretório, deve-se informar a pasta onde serão gravados os xmls gerados para que o sistema de PACS leia e importe o pedido. O diretório que será utilizado para a importação dos laudos deve ser informado nos parâmetros gerais da integração com a Carestream.
3. Instruções de uso para preencher a URL. Posicione o mouse sobre o agrupamento **Visualização das imagens** e aparecerão as instruções para o preenchimento da URL.  
   As palavras reservadas devem ser maiúsculas e entre chaves {}. O sistema substituirá as variáveis encontradas pelos valores correspondentes conforme itens abaixo.  
   Palavras reservadas:

   {USER\_NAME} = Campo usuário  
   {PASSWORD} = Campo senha  
   {ACCESSION\_NUMBER} = Número gerado pelo sistema  
   {PATIENT\_ID} = Código do paciente  
   {SERVER\_NAME} = AETitle
4. Parametrização dos exames para utilizar modalidades diferentes. Acesse **Cadastros / Unidades de Diagnósticos / Exames e Serviços**.
5. Acesse o pedido de exames e realize pedidos para as unidades de cada exame parametrizado. Ao salvar os exames, o sistema verifica a parametrização e se encontrar parâmetros específicos para a unidade de atendimento e modalidade do exame solicitado, ele utilizará desses parâmetros para gerar o arquivo xml. Caso contrário, o sistema assumirá os parâmetros gerais da integração.
6. Visualização da imagem. Para deixar o botão **Filme** visível, é necessário habilitar o parâmetro **Utiliza PACS** no menu **Opções / Parâmetros / Parâmetros por Estação de Trabalho**.
7. Ao clicar no botão acima, a URL é chamada para visualizar a imagem do exame.
