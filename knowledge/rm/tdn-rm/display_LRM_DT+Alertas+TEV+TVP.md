---
content_hash: 8ac34788fc18c99adaaeb29e952a85a8e3ddf2841a23f86d1ab94c03e072e55a
fetched_at: '2026-06-29T00:08:38.488190+00:00'
page_id: '285656938'
product: rm
source: tdn-rm
title: DT Alertas TEV TVP
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Alertas+TEV+TVP
version: 102
---

# Parametrização de Alertas no Prontuário Eletrônico de Acordo com o Preenchimento do TEV (TVP)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Prontuário Eletrônico/ Prescrição Médica |  |  | | --- | | **Rotina(s) envolvida(s)** | | Prontuário Eletrônico / Anamnese/Exame Físico / Profilaxia TVP | |
| **Parâmetro(s):** | Parâmetros / Parâmetros Gerais, aba Prontuário Eletrônico, sub-aba Alertas TEV |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1207 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZPARAM |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criada parametrização de alertas para serem exibidas no Prontuário Eletrônico, aba Prescrição Médica, de acordo com a classificação de risco do TEV (TVP).

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

1. Acesse **Opções / Parâmetros / Parâmetros Gerais,** aba **Prontuário Eletrônico**.
2. Acesse a sub-aba **Alertas TEV**.
3. Nesta nova sessão é possível parametrizar mensagens que aparecerão caso o campo **Exibir Mensagem**esteja marcado, ou não, e houver classificação de risco da Profilaxia TVP (Baixa, Média ou Alta).
4. As mensagens terão uma limitação de 255 caracteres e é possível definir em que momento as mensagens deverão ser exibidas: 1 – Ao Selecionar a aba Prescrição Médica no Prontuário Eletrônico; 2 – Ao clicar no botão para uma nova prescrição para o paciente.
5. As mensagens serão exibidas conforme a Profilaxia TVP definida em **Prontuário Eletrônico / aba Anamnese/Exame Físico**, botão **Profilaxia TVP*.***
6. Se o paciente tem uma Profilaxia TVP realizada e deseja-se fazer uma prescrição médica a mensagem será exibida conforme a parametrização explicada anteriormente.

divs
