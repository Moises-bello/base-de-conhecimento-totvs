---
content_hash: 4b9df4b9018ebdb7008d17f3b5487fcfcabe60d35ca8dcbc5c0206404dbafebf
fetched_at: '2026-06-29T00:06:13.430733+00:00'
page_id: '208341347'
product: rm
source: tdn-rm
title: DT_Possibilita_Seleção_Mais_de_100_Atendimentos_na_Geração_de_Remessas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208341347
version: 4
---

# Permitir Seleção de Mais de 100 Atendimentos na Tela de Geração de Remessas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Faturamento |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento |  |  | | --- | | **Rotina(s) envolvida(s)** | | Faturamento Para Convênios | | Geração de Guia TISS | |
| **Requisito (ISSUE):** | [PCREQ-7611](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-7611 "PCREQ-7611") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle/MSSQL |
| **Tabelas Utilizadas:** | SZFATURACONVENIO |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

   Melhoria possibilita a seleção de mais de 100 contas em um mesmo processo de geração de faturamento para Convênios.

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

1. Acesse o menu “Faturamento / Faturamento Para Convênios”.
2. Selecione uma remessa em aberto ou criar uma nova (o convênio deve ter mais de 100 contas para serem geradas).
3. Avance mais uma tela e clique em Executar.
4. Aguarde a conclusão do processo. Na tela de finalização, o sistema irá informar as remessas que foram geradas.
5. Acesse a pasta onde os arquivos XML estão configurados para serem salvos e verificar o conteúdo dos que foram gerados neste processamento. O correto é 1 XML para cada remessa.
6. O processamento das remessas recém criadas também deve ser feito normalmente.

divs
