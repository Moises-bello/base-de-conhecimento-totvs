---
content_hash: 021f94a1966b95e9464b28abcb83a9db64b1d792ba4ac37a71fe0265410e7504
fetched_at: '2026-06-29T00:08:12.245774+00:00'
page_id: '243641271'
product: rm
source: tdn-rm
title: DT_Lançamento_Automático_Exames_APAC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243641271
version: 109
---

# Lançamento Automático de Exames na APAC

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Registro de Atendimentos Externos | |
| **Requisito (ISSUE):** | RHRM01-53 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle®/ SQL Server® |
| **Tabelas Utilizadas:** | SZPARAMSUS |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado o Lançamento Automático de Exames na APAC.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.12 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.12.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.12

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse**Opções/ Parâmetros/Parâmetros SUS**.
2. Marque a opção **Executa Lançamentos de APAC na geração dos pedidos de exames?**.
3. Na aba **Procedimentos Relacionados** vincule um procedimento.
4. Acesse **Cadastros/Unidade de Diagnóstico/Exames e Serviços**.
5. Vincule o Procedimento SUS ao exame/serviço.
6. Acesse **Atendimento/Pronto Atendimento/Ambulatório/Registro de Atendimentos Externos**.
7. Inclua exames solicitados.
8. Verifique o lançamento dos procedimentos relacionados na APAC

divs
