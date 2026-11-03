---
content_hash: e79246d6664b7c7ffd2495cb4f5e5ee916a7b7812b4ab5792fd74a2199e168da
fetched_at: '2026-06-29T00:06:27.463425+00:00'
page_id: '232822274'
product: rm
source: tdn-rm
title: DT_Filtro_Aba_Evoluções_para_Exibição_de_Pareceres
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232822274
version: 123
---

# Novo Filtro na aba de Evoluções para exibir ou não os Pareceres

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Prontuário | Evolução Médica |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Prontuário Eletrônico do Paciente | Parecer Médico/Interconsulta/Acompanhamento | |
| **Requisito (ISSUE):** | PCREQ-9996 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZEVOLUCAO, SZPARECERPEP |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

O objetivo desta implementação é disponibilizar um novo filtro onde o médico possa filtrar as evoluções que deseja visualizar. Ele poderá visualizar todos as evoluções ou visualizar somente os pareceres de determinada especialidade.

 Foi criado o checkbox "**Exibir parecer de especialistas**" cujo valor default é marcado e incluído um combo que listará as especialidades médicas.

* Com o **checkbox marcado**, o sistema exibirá todos as evoluções, tanto de pareceres solicitados quanto as evoluções dos médicos. Ao selecionar uma especialidade, o sistema exibirá somente os pareceres daquela especialidade. Para exibir os pareceres de todas as especialidades, basta pressionar a tecla Backspace que limpará o item selecionado e sair do campo.
* Com **checkbox desmarcado** o sistema exibirá somente as evoluções médicas que não são os pareceres de especialistas.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.10 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.10.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

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

## Procedimento para Utilização

1. Acesse o menu **Prontuário** e selecione um atendimento de determinado paciente.
2. Acesse a aba **Evolução** médica e inclua uma evolução do paciente.
3. Acesse a aba **Evolução** médica, sub-aba **Parecer Médico/Interconsulta/Acompanhamento**.
4. Solicite pareceres para duas especialidades distintas.
5. Acesse o sistema com um usuário que possua a especialidade solicitada no parecer.
6. Ao acessar o Prontuário selecionando o atendimento correto.
7. Responda o parecer.
8. Repita os passos 4 a 6 com um outro usuário da segunda especialidade.
9. Acesse o sistema com o usuário que solicitou os pareceres.
10. Acesse o prontuário e selecione o atendimento em questão. Por padrão, todas as evoluções e pareceres são exibidos.
11. Selecione uma das especialidades dos pareceres solicitados. Serão exibidos somente os pareceres desta especialidade.
12. Altere a especialidade para a outra. Serão exibidas somente os pareceres desta especialidade.
13. Desmarque o checkbox para exibir somente as evoluções que não são pareceres de especialistas.

divs
