---
content_hash: 816c987de694323d3041b959b6866765c7cbbf973d0c75ccf33eace1f5eeb5d9
fetched_at: '2026-06-29T00:08:34.846298+00:00'
page_id: '274846783'
product: rm
source: tdn-rm
title: DT Controle de Entrada e Saída de Paciente e Visitantes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274846783
version: 118
---

# Controle de Entrada e Saída de Paciente e Visitantes

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Motivo Saida Sem Realizar Exames | SauMotivoSaidaSEAction | | Cadastro de Cartão de Visitante | SauCartaoVisitantAction | | Entrada de Visitantes - Outros Setores | SauEntradaVisitanteOutrosSetoresAction | | Associar Cartão a Atendimento Paciente Externo | SauAssociaCartaoAtendimentoAction | | Saída Visitante - Outros Setores | SauSaidaVisitanteOutrosSetoresAction |  |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros Gerais | | Parâmetros por Estação de Trabalho | | Cadastro de Cartão de Visitante / Entrada e Saída | | Cadastro de Tipo Visitante / Entrada e Saída | | Motivo Saida Sem Realizar Exames | | Entrada de Visitantes / Entrada e Saída - Outros Setores | | Pedido de Exames - Atendimento Externo | | Associar Cartão a Atendimento Paciente Externo | | Saída Visitante - Outros Setores | |
| **Cadastros Iniciais:** | Cartão de Visitante / Entrada e Saída, Tipo Visitante / Entrada e Saída, Motivo Saída Sem Realizar Exames |
| **Parâmetro(s):** | Parâmetros Gerais/ Aba Registro e Controle III   * Associa Atendimento ao Nº Cartão Visitante * Não associar Leito ao Número de Cartão Visitante * Dar preferência p/ Cartão Pré Definido * Tipo Visitante Default   Parâmetros por Estação de Trabalho   * Setor Default |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [SAUHRM02-847](http://jiraproducao.totvs.com.br/browse/SAUHRM02-847) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZCARTAOVISITANTE  SZMOTIVOSAIDA  SZMOTIVOSAIDA  SZVISITANTE  SZLOGVISITANTE  SZLOGVISITANTE |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A partir dessa implementação é possível:

* Associar o cartão de acesso a um atendimento.
* Controlar a permanência do paciente dentro da instituição.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.17 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.17.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.17

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No menu**Opções/Parâmetros/Parâmetros Gerais**, acesse a aba **Registro e Controle III**.
2. Configure os parâmetros:

   1. Associa Atendimento ao Nº Cartão Visitante: No registro de atendimento será possível associar o Cartão de Visitante / Entrada e Saída.
   2. Não associar Leito ao Número de Cartão Visitante: No cadastro de Cartão de Visitante / Entrada e Saída não será obrigatório associar um leito.
   3. Dar preferência p/ Cartão Pré Definido: No controle de Entrada e Saída de Visitantes e Pacientes, ao dar entrada, será alertando a disponibilidade de cartões pré-cadastrados.
   4. Tipo Visitante Default: No controle de Entrada e Saída de Visitantes e Pacientes, ao dar entrada, o tipo de visitante será preenchido automaticamente.
3. Acesse **Opções/Parâmetros/Parâmetros/Parâmetros por Estação de Trabalho**.
   1. Configure o setor default.No controle de Entrada e Saída de Visitantes e Pacientes, ao dar entrada, o setor será preenchido automaticamente.

## Procedimento para Utilização

**Cadastro de Motivo Saída Sem Realizar Exames**

1. No menu**Cadastros/Registro e Controle/Visitante/Motivo Saída Sem Realizar Exames,** cadastre os motivos para permitir um paciente sair sem realizar exames agendados.
2. Clique em **OK**.

**Cadastro de Cartão de Visitante**

1. No menu **Cadastros/Registro e Controle/ Visitantes / Entrada e Saída /Cartão de Visitante / Entrada e Saída,** cadastre ou edite um cartão.

   Observações

   Ao marcar o parâmetro **Não Associar Leito ao Número de Cartão Visitante**, não será obrigatório vincular um leito ao cartão criado.

   1. Cartão pré-cadastrado com numeração manual
   2. Cartão com numeração gerada com dígito verificador.
2. Clique em **OK**.

 **Incluir novo visitantes - Outros Setores**

1. No menu **Atendimento/ Controle de Entrada e Saída**acesse**Incluir novo visitantes - Outros Setores.**
2. Processo de Entrada de Visitante e Outros
   1. Utilizando um cartão pré-cadastrado (cartão exemplo: 0010203040505, cadastrado previamente).
      1. Preencha o Número do Cartão / Clique no botão  (Inserir)
      2. Preencha todos os dados para realizar a entrada

         Observações

         Caso o parâmetro de estação de trabalho **Setor Default** esteja marcado, o sistema automaticamente preencherá o campo **Setor**.

         Caso o parâmetro **Tipo Visitante Default** esteja marcado, o sistema automaticamente preencherá o campo **Tipo de Visitante**.
      3. A entrada será realizada
   2. Gerando o número do cartão (etiqueta) no momento da entrada

      Observações

      Quando o parâmetro **Dar preferência p/ Cartão Pré Definido** está marcado e não preenchemos o número do cartão e ainda há cartões pré-cadastrados disponíveis, a seguinte mensagem é apresentada:

      Desta forma o usuário é informado que ele pode utilizar cartões pré-cadastrados, caso deseje, sem a necessidade de gerar um novo cartão (etiqueta).

      Para a sequência desta demonstração utilizaremos a opção Não.

      1. Clique no botão  (Inserir) sem preencher o número do cartão
      2. Preencha todos os dados para realizar a entrada / Clique no Botão Gerar
      3. A entrada será realizada

 

**Consultar visitante com cartão já cadastrado**

1. Para consultar visitante com a entrada já realizada, dê duplo clique na grid que lista os visitantes.
2. Os dados da entrada serão apresentados

**Vínculo do cartão ao Registro de Atendimento Externo.**

1. Para vincular um cartão e visitante a um Atendimento acesse **Atendimento/Pronto Atendimento Ambulatorio/ Registro de Atendimento Externos**.
2. Pesquise e/ou crie um atendimento.

   Observações

   Quando o parâmetro **Associa Atendimento ao Nº Cartão Visitante** não está marcado os seguintes campos não devem ser exibidos no Registro de Atendimento Externo

   Mesmo com o parâmetro marcado, o usuário não é obrigado a associar um cartão a um registro de atendimento.
3. Vinculando um Cartão de Visitante / Entrada e Saída ao Registro de Atendimento Externo  
   1. O paciente já possui um cartão (Entrada já foi realizada no Controle de Entrada e Saída)
      1. Preencha o número do cartão / Botão Associar Cartão Visitante / Registre o paciente para salvar as alterações
      2. O cartão estará associado

         Observações

         Caso o número do cartão seja inválido e/ou não esteja associado aos dados do Registro de Atendimento Externo, a seguinte mensagem de erro será apresentada:

         Número inválido

         Cartão associado à outro paciente
   2. O paciente não possui um cartão (Entrada não foi realizada no Controle de Entrada e Saída)

      1. Clique no botão Associar Cartão Visitante sem preencher o número do cartão  
           
         1. Caso a entrada do visitante tenha sido realizada no Controle de Entrada e Saída o sistema resgatará o número do cartão automaticamente
         2. Caso a entrada do visitante não tenha sido realizada no Controle de Entrada e Saída o sistema apresenta a seguinte mensagem  
            1. Escolhendo a opção sim a tela de entrada de visitante é apresentada / Botão gerar
            2. O número do cartão (etiqueta) será associado ao registro de atendimento / Botão Registra para salvar a associação.
            3. A entrada do visitante já estará no Controle de Entrada e Saída

**Saída do Visitante com exames a serem realizados**

1. Selecione um visitante/paciente na lista do Controle de Entrada e Saída ou digite o número do cartão  / Botão  (remover)
2. O sistema apresentará a lista de exames pendentes deste visitante/paciente

   Observações

   Se o processo de saída for realizado, mesmo com os exames pendentes, o campo Motivo Saída deverá ser preenchido.

   O processo de saída poderá ser revertido, conforme orientações a seguir.

   IMPORTANTE

   Os exames pendentes listados, levam em consideração o Status do Atendimento na Classificação de Risco, do **Painel de Eletivos**. As demais formas de solicitação de exame (ex.: via Registro de Atendimento diretamente) não são consideradas.

**Reversão da Saída**

1. Caso seja necessário realizar a reversão da saída de um cartão, acesse **Atendimento/Controle de Entrada e Saída**
2. Selecione um visitante/paciente na lista do Controle de Entrada e Saída  / Botão Reverter Saída
3. Preencha a justificativa da reversão
4. A saída é revertida

divs
