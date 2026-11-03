---
content_hash: 85cc10793f54f71f624bf8ab669026ee3b14079057d36a26d115e8012410519b
fetched_at: '2026-06-29T00:08:40.790143+00:00'
page_id: '286504703'
product: rm
source: tdn-rm
title: DT Seleção de Sinais Vitais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286504703
version: 111
---

# Seleção de Sinais Vitais: Integração - Prontuário Eletrônico do Paciente

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Itens de Enfermagem | Cadastro de sinais vitais | |
| **Requisito****:** | SAUHRM02-1324 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria na integração entre TOTVS Gestão Hospitalar e Prontuário Eletrônico do Paciente, possibilita filtro de Sinais Vitais cadastrados pela Unidade de Atendimento selecionada.

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

## Procedimento para Utilização

**Exemplo:**

1. Acesse **Cadastros/Cuidados com o Paciente/Prescrição Médica/Itens de Enfermagem**.
2. Cadastre um item do tipo **Sinais Vitais**.
3. Na aba **Unidade de Atendimento**, selecione as unidades nas quais o item ficará disponível.
4. No **Prontuário Eletrônico do Paciente**, em **Registros de Enfermagem**, caso seja selecionada a mesma unidade de atendimento na qual os itens foram cadastrados, eles serão apresentados na listagem.
5. Na aleta **Prescrição Médica/Painel Rotinas**, **Cuidados, Monitorizações e Sinais Vitais**, os itens que são apresentados, são os cadastrados para aquela unidade de atendimento. Os que tem o checkbox “**Padrão**” marcado no cadastro do **TOTVS Gestão Hospitalar**, já são selecionados no **Prontuário Eletrônico do Paciente**.

No cadastro dos itens de enfermagem, é necessário informar pelo menos uma unidade de medida, clicando em **Anexos/Unidades**.

divs
