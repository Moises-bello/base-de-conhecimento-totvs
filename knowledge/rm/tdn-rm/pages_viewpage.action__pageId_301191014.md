---
content_hash: c7b58255d510af4246178744e8b3fa63bc2bfcf2880b8f906b10cb50da441392
fetched_at: '2026-06-29T00:08:43.139608+00:00'
page_id: '301191014'
product: rm
source: tdn-rm
title: DT Valores de Honorários e SADT cadastrados com valores diferentes de porte
  CBHPM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301191014
version: 3
---

# VALORES DE HONORÁRIOS E SADT CADASTRADOS COM VALORES DIFERENTES DE PORTE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Valores de Porte CBHPM | SauCondFinPorteCBHPMAction | | Elaboração de Contas | PSAFT001, MSAFT001 | | Registro de Informação Cirúrgica | SauRegInfCirurgiaAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Tabela de Procedimentos e serviços | SauTabProcedServicoAction | |  |  | |
| **Tickets relacionados** | #910559 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-4 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZCONDFINPORTECBHPM |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta melhoria consiste em permitir cadastrar valores de porte CBHPM para honorários e exames, sem ter que definir os procedimentos um a um. Com a melhoria é possível ter valores específico para determinados códigos de honorários e exames e um valor geral de porte para o grupo de gasto.

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

1. Acesse o menu Cadastros / Faturamento / Condições Financeiras
2. Selecione uma convênio que utilize a tabela CBHPM
3. Abra o anexo Valores de Porte CBHPM
4. Inclua um honorário específico com porte e valor
5. Inclua um porte com valor para Honorários
6. Acesse a Elaboração de Contas e inclua os dois procedimentos. Note que cada um utilizará o valor de porte correspondente ao cadastrado na funcionalidade alterada
7. O mesmo critério é utilizado em Diagnose Terapia

   Observação

   A sessão abaixo é referente ao efeito da tarefa no Registro de Informação Cirúrgica
8. Acesse **Cuidados com o Paciente / Centro Cirúrgico / Registro de Informação Cirúrgica**
9. No Registro de Cirurgia de um Paciente, informe os procedimentos necessários.
10. É importante que seja lançado ao menos um procedimento que teve valor de porte configurado especificamente e um procedimento que a regra de porte foi aplicado para honorários em geral.
11. Informe a equipe para cada procedimento lançado.
12. Acesse **Processos / Envio de Dados para Faturamento**
13. Ao final do processo, acesse a **Elaboração de Contas.**
14. Veja na imagem abaixo o efeito dos valores de porte mais o acréscimo da função de cada médico no valor do procedimento.
