---
content_hash: 8e6c31ac6c21ef03d12bd185d584f6570fb34c247abbecc8fd4b0c80c29e6d9e
fetched_at: '2026-06-29T00:08:06.182364+00:00'
page_id: '236587320'
product: rm
source: tdn-rm
title: DT_Novo_Parâmetro_Controle_Importação_Brasíndice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236587320
version: 118
---

# Novo Parâmetro Controle Importação Brasíndice

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Importação / Atualização Brasindice |  |  | | --- | | **Rotina(s) envolvida(s)** | | Produtos (Anexo: Tabela de Preços) | | Importação / Atualização Brasindice | |
| **Chamados Relacionados** | TUHKMG |
| **Requisito (ISSUE):** | PCREQ-10841 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

 Implementação da preferência por preço PFB/PMC a nível de Item. 

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

1. Acesse o menu **Cadastros/Estoque/Produto**.
2. Clique em **Anexos/Informações TOTVS Saúde/Tabela de Preço**.
3. Selecione em alguns itens o parâmetro **"Priorizar Preço"**para PMC ou PFB.

       2.          Acesse **Utilitários/Rotinas/Importação / Atualização BRASÍNDICE,**importe e atualize os itens do estoque.

divs
