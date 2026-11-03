---
content_hash: 5da993bbd86be1f5953469200d7282cfcefe53299e04184531e606410bb09617
fetched_at: '2026-06-29T00:08:14.692694+00:00'
page_id: '244713134'
product: rm
source: tdn-rm
title: DT_Registro_de_Atendimento_Externo_Cópia_Campos_do_Endereço_Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244713134
version: 112
---

# Registro de Atendimento Externo - Cópia dos Campos do Endereço do Paciente

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Atendimentos Externos | |
| **Requisito (ISSUE):** | SAUHRM01-395 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria na tela de Registro de Atendimentos Externo, inserido menu com opções para copiar e colar o endereço de um paciente para outro atendimento.

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

## Procedimento para Utilização

**Exemplo:**

1. Acesse o menu **Atendimento / Pronto Atendimento/Ambulatório / Registro de atendimentos externos**.
2. Preencha os dados referentes ao paciente e clique com o botão direito do mouse.
3. Será exibido um menu com a opção de copiar o endereço do cadastro atual. Campos copiados em memória:  
   * + CEP.
     + Tipo Logradouro.
     + Logradouro.
     + Número.
     + Complemento.
     + Bairro.
     + Tipo de Bairro.
     + UF.
     + Cidade.
4. Acesse outro registro de atendimento, ou crie um novo.
5. Clique com o botão direito do mouse e selecione a opção de **Colar Endereço**. Os valores do endereço copiado anteriormente serão colados no novo registro:

divs
