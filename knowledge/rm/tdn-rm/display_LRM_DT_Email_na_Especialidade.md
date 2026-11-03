---
content_hash: c408beef866b5edb041fd4b22286216101660fe3b6fec55953f1e782fd2de779
fetched_at: '2026-06-29T00:08:11.365714+00:00'
page_id: '242389804'
product: rm
source: tdn-rm
title: DT_Email_na_Especialidade
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Email_na_Especialidade
version: 110
---

# E-mail na Especialidade

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Cadastro de Especialidades |  |  | | --- | | **Rotina(s) envolvida(s)** | | Integração com o PEP2 para envio de e-mail na solicitação de parecer para especialidade | |
| **Cadastros Iniciais:** | Especialidade |
| **Requisito (ISSUE):** | SAUHRM01-324 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZESPECIALIDADE |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria consiste na inclusão do e-mail no cadastro de especialidades, para que ele seja utilizado na integração com o Prontuário Eletrônico do Paciente (PEP 2) para o envio de e-mail na solicitação de parecer.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.11 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.12.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

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

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

## Procedimento para Utilização

1. Acesse o menu **Cadastros/ Uso Geral /Especialidade**.
2. Dê um duplo clique na especialidade para editar.
3. Informe o e-mail e salve.
4. No Prontuário **Eletrônico do Paciente** (PEP2), configure o envio de e-mail e faça a solicitação de parecer para a especialidade acima.
5. Verifique se o e-mail foi recebido.

divs
