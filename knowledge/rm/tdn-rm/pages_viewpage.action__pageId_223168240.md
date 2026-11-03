---
content_hash: a0ed95d82cbc271803dd8b0c31d75bb2cb8c03b0431e38a4ceafaebca7620e38
fetched_at: '2026-06-29T00:06:21.307273+00:00'
page_id: '223168240'
product: rm
source: tdn-rm
title: TTRSGB_DT_Integração_PEP2_RM_AGFA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223168240
version: 2
---

# Integração PEP2/RM/AGFA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Saúde |
| **Módulo:** | Totvs Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Unidade de Atendimento. | |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Sistema(s) Operacional(is):** | Windows. |
| **Versões/Release:** | 12.1.8. |

## Descrição

   Alterada rotina de integração entre PEP2/RM/AGFA, em que ao ser configurado, os aprazamentos liberados sejam integrados com o **Totvs Gestão Hospitalar** e com o **Sistema de Diagnóstico por Imagem (AGFA)**.

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

1. Em **Totvs Gestão Hospitalar**, acesse o menu **Cadastros \ Unidades de Atendimento.**
2. Selecione a unidade que será configurada.
3. Na aba **Identificação**, informe o valor "**Sem integração**" para o campo "**Diagnóstico por Imagem - Setores**":
4. Acesse o **PEP 2** e realize o login na unidade que foi configurada:
5. Acesse o prontuário de algum paciente com aprazamentos pendentes e selecione a aba "**Planejamento Terapêutico**":
6. Clique em "**Liberar Aprazamento**" e a integração com o **Totvs Gestão Hospitalar** é iniciada e a configuração **RM/AGFA** é verificada. Caso esteja ativa e configurada, a integração é chamada\*:
7. Caso a integração com o **Totvs Gestão Hospitalar** seja realizada com sucesso, a aprazamento será liberado:  
     
   **Observação:** A integração completa (PEP2/RM/AGFA) só pode ser simulada com testes controlados, em conjunto com a equipe da AGFA.

divs
