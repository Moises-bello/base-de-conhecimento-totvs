---
content_hash: 8b315817d7e67a7bfb71dd8d73c2cb5997f75bdb46bf3c4ff91fcb4cda64db30
fetched_at: '2026-06-29T00:08:41.313163+00:00'
page_id: '286720034'
product: rm
source: tdn-rm
title: DT Código de Barras da Pulseira do Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286720034
version: 105
---

# PEP X RM: Dados do código de barras da pulseira / 5 certos na checagem - Revisão CHECKS Linha RM

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Integração com Prontuário Eletrônico do Paciente |  |  | | --- | | **Rotina(s) envolvida(s)** | | Planejamento Terapêutico - Checagem (Prontuário Eletrônico do Paciente) | |
| **Parâmetro(s):** | Parâmetros Gerais, aba Registro e Controle IV:   * Dados do Código de Barra * Tipo de Código de Barra * Caractere Separador |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | SAUHRM02-1191 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada alteração na rotina de integração com Prontuário Eletrônico do Paciente para enviar os dados do código de barras da pulseira do paciente.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realize a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.18 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.18.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.18

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Menu Parâmetros/Parâmetros Gerais**, aba **Registro e Controle IV**, insira os valores dos parâmetros **Dados do Código de Barras**, **Tipo de Código de Barras**, **Caractere Separador**, conforme imagem abaixo:

## Procedimento para Utilização

**Geração do código de barras da pulseira:**

Após serem definidos os parâmetros para geração do código de barras, durante a integração com o Prontuário Eletrônico do Paciente, este valor é enviado para que possa ser feita a identificação do paciente através da leitura da pulseira na checagem do mesmo.

A imagem mostra um exemplo de código de barras no formato EAN13, gerado utilizando o código do paciente. 

Dentro do Prontuário Eletrônico do Paciente, na tela de Planejamento Terapêutico, ao efetuar a leitura do código de barras no campo "Paciente (Leitura da Pulseira)", será feita a comparação com o valor do código de barras enviado através da integração com o TOTVS Gestão Hospitalar.

Caso os valores sejam iguais, aparecerá a mensagem de pulseira validada com sucesso, conforme mostra a imagem.

divs
