---
content_hash: a25147e133aaeba7bfe4b344987568a713bc093683d393c9dc6cd1754af3c4c5
fetched_at: '2026-06-29T00:06:17.040537+00:00'
page_id: '212904083'
product: rm
source: tdn-rm
title: TQNSS4_DT_Inclusão_de_Filtro_em_Relatório_de_Folha_de_Produção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212904083
version: 5
---

# Inclusão de Filtro em tela de Folha de Produção

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Faturamento |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento |  |  | | --- | | **Rotina(s) envolvida(s)** | | Folha de Produção | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL/Oracle |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

Criado Filtro que permite ao usuário selecionar a unidade de atendimento para incluir nos filtros de geração do relatório.

## Procedimento para Implantação

 Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.8 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.8.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:  
   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).   
   2. Faça o login, com seu E-mail e Senha.  
   3. Na barra de menu superior, clique em DOWNLOAD.  
   4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   a. Linha: RM  
   b. Versão: RM 12.1.8  
   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

Acesse o menu Faturamento / Repasses / Folha de Produção.

Selecione algum profissional que possua repasses a serem impressos e testar o filtro 'unidade de Atendimento para a geração do relatório.'.

divs
