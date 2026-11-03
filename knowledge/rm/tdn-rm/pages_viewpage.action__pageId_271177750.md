---
content_hash: f2e6f7abddbfdf4efbf9bec155e69e2cdcac86c9eeca5262bff1a76ebc8fe21e
fetched_at: '2026-06-29T00:08:26.381766+00:00'
page_id: '271177750'
product: rm
source: tdn-rm
title: DT Bloqueio por Faixa Etária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271177750
version: 112
---

# Exames - Agendamento e Solicitações de Exames - Bloqueio por Faixa Etária

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Exames e Serviços | | Agenda de Atendimentos | | Pedidos de Exames Pacientes Internos | | Registro de Atendimentos Externos | | Prontuário Eletrônico do Paciente | | Agenda Exames | |
| **Requisito (informe o requisito relacionado):** | SAUHRM02-325 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Incluída rotina de restrição por faixa etária nos exames.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.15 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.15.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte);

   2. Faça o login, com seu E-mail e Senha;

   3. Na barra de menu superior, clique em "DOWNLOAD";

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM;

   b. Versão: RM 12.1.15;

   c. Tipo: Patch.

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

Configuração das regras de restrição por faixa etária:

Acesse "**Atendimento / Agendamento / Agenda de Atendimentos**". Na tela de detalhes do registro, "**Anexos / Restrição por faixa etária**", selecione a restrição para o sexo e a faixa etária desejada

Telas onde é realizada a verificação das restrições:

"**Unidades Diagnóstico > Pedidos de Exame Pacientes Internos**", aba de Exames Solicitados, ao selecionar um exame no campo "Cód. ou Mnemônico".

"**Unidades Diagnóstico > Registros de Atendimentos Externos**", aba de Exames Solicitados, ao selecionar um exame no campo "Cód. ou Mnemônico".

Menu Prontuário, aba Avaliações Complementares, botão de "Solicitação de Exames".

Ao selecionar um exame e clicar no botão de incluir,

"**Atendimento > Agendamento > Agenda de Atendimentos**".

Ao criar ou editar um registro, na aba Exames, ao adicionar um exame, é feita a validação.

"**Atendimento > Agendamento > Agenda de Atendimentos**", opção "Agendar Exames".

Ao incluir um exame, é realizada a validação

divs
