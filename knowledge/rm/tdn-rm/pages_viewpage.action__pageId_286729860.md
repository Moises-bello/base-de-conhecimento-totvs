---
content_hash: b3370a592a493f6d7c62571400566938875c6843a6e379e65b469693a7fe535a
fetched_at: '2026-06-29T00:08:41.473908+00:00'
page_id: '286729860'
product: rm
source: tdn-rm
title: DT Exportação da TISS (XML) - Hora Fim para Elaboração de Contas Internos e
  Externos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286729860
version: 117
---

# Horário final de Procedimento na Tela de Elaboração de Contas Internos e Externos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento / Faturamento para Convênios | | Cuidados com paciente / Centro Cirúrgico / Registro de Informações Cirúrgicas | | Unidade Diagnóstico/Pedido de Exames Pacientes Internos | | Faturamento/Particular e Convênios/Lançamentos na Conta do Paciente |  |  | | --- | | **Rotina(s) envolvida(s)** | | Faturamento / Particular e Convênios / Lançamentos na Conta do Paciente | | Cadastros / Faturamento / Condições Contratuias com Convênio | |
| **Tickets relacionados** | [Ticket #982159](https://totvssuporte.zendesk.com/agent/tickets/982159 "Open ticket in Zendesk Support") |
| **Requisito****:** | [SAUHRM02-1343](http://jiraproducao.totvs.com.br/browse/SAUHRM02-1343) [SAUHRM02-1393](http://jiraproducao.totvs.com.br/browse/SAUHRM02-1393) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZATENDHONORARIO, SZATENDHONORARIOGLOSA, SZATENDSADT, SZATENDSADTGLOSA |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado na tela de Faturamento para Convênios, o campo**Hora Fim** na geração do XML e alteração na exportação da TISS. Esta melhoria tem por objetivo a indicação de faixa de horário correspondente à execução de um procedimento ou exame, hora inicial e hora final, visando o correto preenchimento dos campos correspondentes nas guias TISS.

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

**Exportação da TISS (XML) - Hora Fim para Elaboração de Contas internos e externos**

1. Acesse **Faturamento/Particular e Convênios/Lançamentos na Conta do Paciente.**
2. Na aba **Honorários** ou **Diagnose e Terapia**, certifique que o campo **Hora Fim** foi preenchido diferente do campo **Hora** (hora inicial).

**Na nova MDI**

1. Acesse aba **Faturamento**, opção **Faturamento para Convênios**.
2. Selecione uma fatura e clique em Edita
3. Clique na opção **Processos**, selecione **Faturamento de Convênio**.
4. O assistente de faturamento abrirá, clique em **Avançar**.
5. Na tela seguinte selecione **Tipo de Paciente** **Interno** ou **Externo** dependendo do cadastro informado na **Elaboração de Contas**, nesse exemplo o paciente é externo.
6. Selecione o(s) paciente que deseja faturar, clique em **Avançar**.
7. Na tela seguinte clique em **Executar**.
8. O processo de geração de XML para TISS será finalizado, clique em **Finalizar.**
9. Acesse Computador/ OS(C:) e encontre o arquivo XML similar ao exemplo abaixo.
10. Note que os campos de **Hora Fim** estão sendo preenchidos no XML:

**Lançamentos originados pelo Registro de Informação de Cirurgia**

1. Acesse **Cadastros / Faturamento / Condição Contratural com Convênio**.
2. Selecione uma condição contratual\*, acesse a  aba **Eletrônico III – TISS** (2) **/ Área de Parâmetros** (3).
3. Marque o parâmetro **Horário final da cirurgia igual ao horário inicial**.

Observação

O paciente que será utilizado posteriormente na execução da rotina deverá ser do mesmo convênio configurado neste passo.

IMPORTANTE

O intuito desta funcionalidade é manter a hora fim sempre preenchida. Os parâmetros utilizados seguem a ordem descrita abaixo:

* Usa a data e hora do Registro de Informação da Cirurgia
* Horário final da cirurgia igual ao horário inicial
* Caso o sistema não encontre nenhuma informação a partir destes parâmetros, as informações do horário inicial e final serão preenchidos igualmente.

1. Acesse **Cuidados com o Paciente / Centro Cirúrgico / Registro de Informações Cirúrgicas**.
2. Selecione um registro que será utilizado posteriormente no processo. Cerifique-se que há procedimentos do tipo honorário lançados no **Registro de Informações de Cirurgia**.
3. Na aba **Equipe do procedimento**, certifique que há prestadores associados ao procedimento. Ex.: Um cirurgião e um Anestesista.
4. Após verificar as pré-condições do processo, selecione o registro que deseja processar (1) acesse **Processos** (2) / **Enviar dados para o faturamento**(3).
5. Clique em **Executar**.
6. Ocorrerá a execução do processo.
7. O processo será executado com sucesso.
8. Para verificar o resultado do processo, clique no ícone de Lançamento na conta do paciente, na barra de ferramentas.
9. Clique em **Pesquisa Atendimento**.
10. Preencha os dados do paciente(1) para executar a pesquisa(2) selecione o atendimento(3) e clique em **OK**(4).
11. Na aba **Honorários** os procedimentos oriundos do registro de informação de cirurgia estarão lançados conforme a configuração do parâmetro **Horário final da cirurgia igual ao horário inicial**.
12. Fluxo Alternativo: Parâmetro **Usa Data e Hora do Registro de Informação de Cirurgia**.
13. Dados do registro.
14. Resultado do processo.

Observação

Mesmo que nenhum parâmetro esteja marcado ou nenhum cenário seja atendimento, para que o campo HORA FIM não fique em branco, ele será preenchido com a hora realização do procedimento.

**Lançamentos originados pelo PEP 2**

1. No **Prontuário Eletrônico do Paciente**, selecione um paciente.
2. Acesse a aleta **Planejamento Terapêutico** e libere um aprazamento\*.

\*É Necessário que a prescrição possua pelo menos uma solicitação de exame com item de débito configurado.

Caso o processo seja concluído com êxito, o status da prescrição será alterado.

 

O resultado será apresentado na **Elaboração de Contas** do respectivo paciente.

**Campo horário final de procedimento na tela de elaboração de contas internos e externos**

1. Acesse **Unidade Diagnóstico/Pedido de Exames Pacientes Internos.**
2. Clique em **Novo Pedido.**
3. Pesquise por um paciente.
4. Na aba **Exames Solicitados** inclua um novo exame, clicando no botão **Inclui,** e após concluir o preenchimento dos campos clique em **Grava.**
5. Note que na **Elaboração de Contas** o pedido de exame foi inserido com a hora fim preenchida.

**Gerar SADT através da aba Especial com Kit Cadastrado (somente procedimento)**

1. Acesse **Faturamento/Particular e Convênios/Lançamentos na Conta do Paciente.**
2. Inclua um kit de lançamento.
3. Na aba **Itens** inclua pelo menos um procedimento.
4. Na **Elaboração de Contas** na aba **Especial** selecione **Kit de Lançamentos** nas opções de **Tipo Lançamento**, e no cadastro, na opção **Kit de Procedimento** selecione o kit cadastrado no passo anterior.
5. Clique no botão **Grava**, para inserir o kit de procedimentos.

Observação

Não é possível informar o campo Hora Fim na aba Especial quando o kit Lançamentos for selecionado.

Note que o procedimento foi inserido com a Hora Fim gerada pela rotina do Kit de lançamento.

divs
