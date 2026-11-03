---
content_hash: 1967240ad4dee1e70ed69d1e7035c64b90c744ecb9af545e31ce58f1cf423d94
fetched_at: '2026-06-29T00:08:06.306299+00:00'
page_id: '236590999'
product: rm
source: tdn-rm
title: DT_Resultado_de_Exames_com_Prontuário_Eletrônico_do_Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236590999
version: 117
---

# Resultado de Exames com Prontuário Eletrônico do Paciente (PEP 2.0)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Resultado de Exames integrado com o PEP 2.0 |  |  | | --- | | **Rotina(s) envolvida(s)** | | Pedido de exames, preenchimento do resultado do exame | |
| **Requisito (ISSUE):** | PCREQ-9366 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementação disponibiliza os resultados de exames do TOTVS Gestão Hospitalar dentro da aleta Resultados de Exames do PEP 2.0. Todos os resultados visualizados no sistema serão exibidos no Prontuário Eletrônico do Paciente (PEP 2.0).

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

Para esta funcionalidade é necessário a configuração do TBC (TOTVS BusinessConnect).

1. O arquivo **wsResultadosOnline.asmx** deve estar na pasta raiz do TBC.
2. O arquivo **web.config** deve conter o seguinte trecho:  

   <location path="wsResultadosOnline.asmx">  
    <system.web>  
     <webServices>   
       <soapExtensionImporterTypes>  
          <add type="Microsoft.Web.Services3.Description.WseExtensionImporter, Microsoft.Web.Services3, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35"/>  
       </soapExtensionImporterTypes>  
       <soapServerProtocolFactory type="Microsoft.Web.Services3.WseProtocolFactory, Microsoft.Web.Services3, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35"/>  
       <protocols>  
          <add name="HttpGet"/>  
          <add name="HttpPost"/>  
       </protocols>  
     </webServices>  
    </system.web>  
    </location>
3. No menu **Opções/Parâmetros/Parâmetros Gerais**, acesse a página **Integração**, subpágina **PEP 2.0** e preencha o endereço do TBC

## Procedimento para Utilização

1. Acesse o Prontuário Eletrônico do Paciente, selecione uma unidade de atendimento e clique em um paciente.
2. Selecione a aleta **Resultado de Exames**.
3. Serão exibidos todos os exames solicitados ao paciente.
4. Para os exames que possuem data do laudo, é possível clicar no ícone da coluna "Link", para baixar o resultado.
5. Ao clicar no link, a tela abaixo será exibida para abrir ou salvar o resultado
6. Clique em **Abrir** e o resultado será exibido.
7. Caso utilize a planilha de exames, os mesmos serão exibidos como sendo os primeiros exames.
8. Para as integrações com outros sistema laboratoriais em que o resultado é enviado para o TOTVS Gestão Hospitalar,o resultado também será exibido nesta funcionalidade.

divs
