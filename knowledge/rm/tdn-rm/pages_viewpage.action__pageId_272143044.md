---
content_hash: 593ce0c572f9ad31194079f3de9da278ef9e33d238384d46701176ec41b01ba4
fetched_at: '2026-06-29T00:08:29.047934+00:00'
page_id: '272143044'
product: rm
source: tdn-rm
title: DT Agendamento Cirurgia e Central de Autorização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272143044
version: 114
---

# Agendamento Cirurgia e Central de Autorização

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotinas** | | Cadastro De-Para: Status Agenda x Central de Guias  Vínculo da central de guias com a agenda de cirurgia  Atualização do status da guia ao alterar o status do agendamento da Cirurgia | |
| **Requisito****:** | SAUHRM02-677, SAUHRM02-678, SAUHRM02-679 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZRELCENTRALAGCIRURG  SZRELSTATUSAGCIRURGCENTRAL |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A melhoria consiste na automatização dos status correlacionados da Agenda de Cirurgia (status da cirurgia) e Central de Autorizações (status da guia). Através deste processo, o sistema atualizará o status das guias (na Central de Autorizações) de forma automática sempre que o status do agendamento for alterado.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.16 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.16.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.16

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

* **Cadastro De-Para: Status Agenda x Central de Guias**

1. Acesse o menu **Cadastros/Cuidados com o paciente/Cirurgias/De-Para: Status Agenda x Central de Guias**.
2. No primeiro campo, selecione o status da agenda de atendimentos e no segundo, o status correspondente para a **Central de Autorizações**. No caso mostrado na imagem, ao atualizar o status de um agendamento para **Cirurgia Concluída**, o sistema atualizará automaticamente o status da(s) guia(s) vinculadas com o agendamento para **Autorizado**.

* ## **Vinculo da central de guias com a agenda de cirurgia**

1. Para que este vínculo seja possível, é necessário realizar o cadastro do atendimento para o paciente. Pode ser atendimento ou pré-registro para atendimento interno ou externo. Também é necessário solicitar a(s) Guia(s) SADT no próprio cadastro do atendimento, para que o sistema gere os registros na **Central de Autorizações**.
2. Com o atendimento cadastrado, acesse o menu **Atendimento/Agendamento/Agenda de Cirurgias**.
3. Para vincular um atendimento ao agendamento de uma cirurgia, clique no botão **Atendimento** e escolha o atendimento cadastrado nos passos acima. Preencha o restante dos campos obrigatórios e salve o registro.
4. Após salvar o registro, acesse a aba **Guias Relacionadas**. Nessa aba, é possível selecionar as guias da central de autorizações para relacioná-las com o agendamento.

* ## **Atualização do status da guia ao alterar o status do agendamento da cirurgia**

1. A partir desse momento, ao alterar o status deste agendamento, o sistema atualiza automaticamente o status da guia na central de autorizações conforme o cadastro **Cirurgias/De-Para: Status Agenda x Central de Guias** descrito no primeiro item deste documento.
2. Para conferir a central de autorizações, acesse o menu **Faturamento/Central de Autorizações**.
3. Observe que o status do agendamento (Agendado) corresponde ao status **Agendado** da guia na **Central**.
4. Quando atualizado o status do agendamento para **Cirurgia Concluída** o status da guia é alterado para **Autorizado**.

Observação

A atualização automática é realizada apenas no Workflow Agenda de Cirurgia / Central de Autorizações. O processo inverso não é contemplado neste requisito.

divs
