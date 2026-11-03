---
content_hash: 038595deb1e8c31424d677dcebf006ad664d857d48a9fafd85ea814d96ecfff0
fetched_at: '2026-06-29T00:06:18.325184+00:00'
page_id: '215483649'
product: rm
source: tdn-rm
title: TTKXC5_DT_Informar_Quantidade_Item_de_Débito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=215483649
version: 3
---

# Permitir Informar a Quantidade Default do Item de Débito

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Unidade de Diagnóstico |
| **Rotina:** | |  | | --- | | **Rotina** | | Pedidos de Exames |  |  | | --- | | **Rotina(s) envolvida(s)** | | Cadastros de Exames e Serviços | |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | MSSQL/ORACLE. |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

   Implementada rotina que permite o lançamento de mais de um item de débito, em uma mesma solicitação de exame.

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

1. - Acesse o menu “Cadastros / Unidades de diagnóstico / Exames e Serviços” e selecione o exame desejado.
2. Clique em “Anexos / Item de Débito” e inclua os itens de débito desejados, com a respectiva quantidade default, para cada um deles:.
3. Acesse o menu “Unidades Diagnóstico / Pedidos de Exames Pacientes Internos”.
4. Inclua um novo pedido e selecionar um paciente internado.
5. Clique em “Incluir”.
6. Selecione os dados obrigatórios e clicar em “Grava”.
7. Na aba “Exames Solicitados” clique em “Inclui”.
8. Selecione o exame e clique em “Grava”.
9. Clique em “Lançamento em conta” e verifique se o item foi lançado com a quantidade e o valor corretos.
10. Acesse o prontuário eletrônico do Paciente (Menu “Prontuario” da tela principal) e clique na aba “Avaliações Complementares”.
11. Clique em “Solicitação de Exames” e selecione Especialidade, Padrão terapêutico e o Exame e clique em “Confirma”.
12. Acesse o menu de “Elaboração de contas(ctrl+l)” e selecione a conta do paciente;
13. Na aba “Diagnose/Terapia”, verifique se o item foi lançado com quantidade e valor corretos.

divs
