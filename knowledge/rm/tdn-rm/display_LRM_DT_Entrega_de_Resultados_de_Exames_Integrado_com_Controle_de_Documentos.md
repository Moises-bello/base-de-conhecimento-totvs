---
content_hash: 6d51811de8690304a528989659614cccc6cef6bae6002fca51ea3bfcc4f68860
fetched_at: '2026-06-29T00:08:19.414104+00:00'
page_id: '267785399'
product: rm
source: tdn-rm
title: DT_Entrega_de_Resultados_de_Exames_Integrado_com_Controle_de_Documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Entrega_de_Resultados_de_Exames_Integrado_com_Controle_de_Documentos
version: 108
---

# Entrega de Resultados de Exames Integrado com Controle de Documentos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de pedidos de Exames | | Controle de Documentos | |
| **Parâmetro(s):** | * Utiliza Status Liberado Recepção - Depois da impressão do resultado * Gera Controle de Documento na Entrega de Exame |
| **Requisito (ISSUE):** | SAUHRM02-66 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a integração entre entrega de exames e Controle de Documentos. A melhoria possibilita a gestão da movimentação dos documentos entre setores via sistema, sem a necessidade de controles paralelos.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.14 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.14.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.14

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE ACESSO**

1. Acesse o menu**Cadastros / Segurança / Perfil.**
2. Configure o acesso a funcionalidade Entrega Exame.

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Opções/Parâmetros/Parâmetros Gerais**.
2. Na aba **Unidade Diagnóstico II**, marque o parâmetro **Utiliza Status Liberado Recepção****Depois da impressão do resultado** eo parâmetro  **Gera Controle de Documento na Entrega de Exame.**

## Procedimento para Utilização

**Exemplo:**

1. Acesse o menu **Unidade de Diagnóstico / Controle de Pedidos de Exames**.
2. Ao liberar o exame, o sistema irá gerar o controle de documento.
3. Para acessar o controle de documento, utilize o ícone indicado na imagem.
4. Para enviar ao setor de entrega dos exames, acesse **Processos** e **Gerar malote**.
5. Informe  o usuário a quem se destina o malote e a justificativa de envio.
6. Ao receber fisicamente o documento, é necessário a confirmação via sistema.
7. Ao efetuar a entrega, utilize **Processos/ Entregar Exames.**
8. Caso ocorra a necessidade de estornar as informações de entrega, utilize **Processos/ Estorno.**

divs
