---
content_hash: ff0020f5fe58abe5231e7a9fdfd8b312102ea6384253442ab678f5daca4f8a4c
fetched_at: '2026-06-29T00:06:29.274512+00:00'
page_id: '234457169'
product: rm
source: tdn-rm
title: TRMFAJ_DT_Intervalos_na_Classificação_de_Risco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=234457169
version: 120
---

# Intervalos na Classificação de Risco

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Totvs Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Painel de Classificação de Riscos |  |  | | --- | | **Rotina(s) envolvida(s)** | | Registro de Atendimentos Externos | |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | MSSQL, Oracle. |
| **Tabelas Utilizadas:** | SZINTERVALOCLASSIFICACAO. |
| **Sistema(s) Operacional(is):** | Windows. |

## Descrição

   Esta implementação tem como objetivo possibilitar a inclusão de intervalos de atendimento, durante um plantão cadastrado no Painel de Classificação de Riscos.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.10 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.10.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.10

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu “Opções -> Parâmetros -> Parâmetros Gerais”, aba “Classificação de Risco”;
2. Configure conforme a imagem:
3. Acesse o menu “Cadastros -> Uso Geral -> Unidades de Atendimento”;
4. Selecione a unidade de atendimento desejada e acesse a aba “Outros Dados”;
5. Marque a opção “Realiza Classificação de Risco” e informe o Período de Triagem, conforme imagem:
6. Acesse o menu “Atendimento -> Pronto Atendimento/Ambulatório -> Painel de Classificação de Riscos”;
7. Acesse a aba Plantão.
8. Clique no ícone ;
9. Selecione a data atual e hora de início e fim para o plantão, bem como os outros dados obrigatórios:
10. Na parte inferior do painel, ainda na aba Plantão, inclua as especialidades atendidas pelo plantão cadastrado:

## Procedimento para Utilização

1. Acesse o menu “Cadastros -> Uso Geral -> Unidades de Atendimento”;
2. Clique sobre o registro da unidade de atendimento que deseja parametrizar e acesse o menu “Anexos > Intervalos na Classificação de Riscos”;
3. Inclua um novo intervalo que contemple o horário em que o primeiro atendimento de testes será inserido:
4. Acesse o menu “Atendimento -> Pronto Atendimento/Ambulatório -> Registro de Atendimentos Externos”
5. Registrar um novo atendimento externo:
6. Acesse o menu “Atendimento -> Pronto Atendimento/Ambulatório -> Painel de Classificação de Riscos”;
7. Verifique a aba “Atendimento Médico”. Conforme parametrizado, o registro deverá estar nesta aba, pois o atendimento foi registrado dentro de um período de intervalo:
8. Acesse novamente o Cadastro da Unidade de Atendimento e exclua o intervalo cadastrado anteriormente;
9. Inclua um novo atendimento externo:
10. Acesse Novamente o Painel de Classificação de Riscos. O atendimento recém cadastrado, deverá estar na aba “Registro de Triagem”, pois não foi incluído em um horário de intervalo:

divs
