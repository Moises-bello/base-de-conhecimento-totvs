---
content_hash: 90a4969ecfb21a3f153cb14ffa17bd8c3686e0c432b9cf7ece2cb8cdc6fb3cc6
fetched_at: '2026-06-29T00:08:47.064501+00:00'
page_id: '318603355'
product: rm
source: tdn-rm
title: 1330413 RMSAU-1273 DT Retorno de Consulta - Retorno configurável por item /
  Grupo de Consultas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=318603355
version: 5
---

# Retorno de Consulta/Exame

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Registro de Atendimentos Externos | PSARC023.pas |  |  | | --- | | **Rotina(s) envolvida(s)** | | Condições Contratuais com Convênios | | Exames e Serviços | | Agenda de Atendimento | | Elaboração de Contas | |
| **Cadastros Iniciais:** | Condições Contratuais com Convênios, Exames e Serviços |
| **Parâmetro(s):** | Condições contratuais com convênio, aba Parâmetros 1:  Considerar contagem de retorno a partir de atendimentos não classificados como retorno;  Considerar como retorno apenas o primeiro atendimento dentro do prazo |
| **Tickets relacionados** | 1330413 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-1273 / RMSAU-1485 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZCONDCONTRATRETORNO  SZATENDHONORARIO  SZATENDSADT |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Automatizar lançamentos fora da conta quando um procedimento for realizado dentro do período de retorno cadastrado na condição contratual do convênio.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados, bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

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

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

Menu **Cadastros / Uso Geral / Unidades de Atendimento**

Para que exista a verificação do período de retorno, deverá estar selecionada a opção "Validar retorno de consulta", na aba **Identificação**.

Menu **Cadastros / Faturamento / Condições Contratuais com Convênios**

Na aba **Parâmetros 1** localizam-se algumas opções que alteram o comportamento do cálculo de retorno:

* **Considerar contagem de retorno a partir de atendimentos não classificados como retorno**:

             Quando esta opção estiver marcada, ao buscar a data do atendimento anterior para o cálculo do período de retorno, será selecionado o atendimento mais recente que não foi classificado como retorno;

             Caso a opção esteja desmarcada, a data do último atendimento será selecionada para o cálculo, sem considerar se o atendimento é ou não um retorno.

* **Considerar como retorno apenas o primeiro atendimento dentro do prazo:**  
  Com esta opção marcada, apenas o primeiro atendimento dentro do período de retorno será considerado fora da conta, e o próximo atendimento do mesmo procedimento será cobrado normalmente.  
  Com a opção desmarcada, todos os atendimentos dentro do período de retorno serão lançados fora da conta.
* **Lança procedimentos das guias de autorização na conta do paciente se dentro da faixa de codificação**

            Na tela de registro de atendimentos externos, caso essa opção não esteja marcada, os procedimentos não são lançados na conta do paciente quando inseridos na guia, na aba Guia / Autorização.  
  
Menu **Opções /** **Parâmetros / Parâmetros Gerais**

Na aba **Registro e Controle,** caso a opção **Valida retorno de consulta de atendimento de emergência** não esteja marcada, o cálculo de retorno levará em consideração apenas os atendimentos eletivos.

## Procedimento para Utilização

**Cálculo de Retorno**

  Ao realizar um atendimento para um paciente, caso exista um atendimento anterior para a mesma especialidade, grupo ou item (de acordo com as regras de retorno cadastradas) e dentro do prazo estipulado, o procedimento será lançado na conta do paciente sem que haja cobrança.

**Cadastro da Regra de Retorno**

Para validar se um procedimento está em período de retorno, é necessário que exista um regra cadastrada para efetuar o cálculo.

O cadastro de regras para retorno de consulta encontra-se no seguinte caminho:

  Menu **Cadastros / Faturamento / Condições Contratuais com Convênio, Anexos – Retorno de Consulta**

Nesta tela é realizado o cadastro das informações que compõem uma regra de retorno.

- Plano: Plano do convênio sobre o qual a regra é aplicada

- Subplano: Caso a regra seja exclusiva de um subplano. Campo não obrigatório.

- Tipo: Se a regra é válida para uma especialidade (tipo mais amplo), um grupo ou apenas um item (regra mais específica)

- Especialidade / Grupo / Item: Informar o tipo do item sobre o qual será verificado o período de retorno. Pode ser uma especialidade (Ex: Consulta), um grupo específico (Ex: Consultas – Recém Nascido) ou um item (Procedimento / Diária / Taxa / Serviço, ex: Avaliação Nutricional)

- Retorno em Dias: O período de tempo em dias decorrido da primeira consulta até a consulta seguinte, para calcular se atendimento é considerado um retorno.

- Unidade de Atendimento: Campo não obrigatório. Caso não seja preenchido, a regra poderá ser aplicada em qualquer unidade.

Para este exemplo será utilizada regra de retorno conforme imagem abaixo:

Após o cadastro da regra de retorno, deverá ser realizado o registro de um Atendimento Externo.

**Registro de Atendimento Externo**

Abaixo a imagem de um atendimento registrado, utilizando o mesmo plano da regra cadastrada anteriormente.

Ao registrar um segundo atendimento para o paciente, na mesma especialidade, o sistema irá informar que o atendimento está em período de retorno:

**Retorno de Consulta**

Na aba de Guia / Autorização, ao registrar uma consulta que esteja associada à uma regra de retorno, o sistema irá informar que o procedimento está em período de retorno e efetuará o lançamento fora da conta do paciente. Para consultas que geram honorário médico, deve ser selecionado o tipo de guia como Guia de Honorário Individual.

Caso não exista regra de retorno associada ao procedimento, mas o atendimento esteja em retorno, o procedimento seja do tipo honorário e esteja dentro de uma faixa de codificação (Cadastros / Faturamento / Padrões de Faturamento e Codificação, aba Códigos 1), o lançamento será realizado fora da conta.

**Retorno de Exames**

Na aba Exames Solicitados, ao registrar um pedido de exame que possua regra de retorno, o sistema irá informar que o procedimento está em período de retorno e efetuará o lançamento fora da conta do paciente.

Abaixo,  na tela de elaboração de contas, o exame que está em período de retorno, foi considerado como lançamento fora da conta.

**Retorno de Consulta através da Agenda de Atendimento**

Na agenda de atendimentos, ao agendar uma consulta, o procedimento que possuir regra de retorno associada,  será lançado automaticamente fora da conta.
