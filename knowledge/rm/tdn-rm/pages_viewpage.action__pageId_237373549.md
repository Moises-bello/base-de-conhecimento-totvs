---
content_hash: 020d8c93d3234d318d463e6315c3ecf1617648bf630b061b74f072d1dffa0025
fetched_at: '2026-06-29T00:08:07.194200+00:00'
page_id: '237373549'
product: rm
source: tdn-rm
title: DT_Divisão_de_Cobranças
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237373549
version: 124
---

# Divisão de Cobranças

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Divisão de Cobranças |  |  | | --- | | **Rotina(s) envolvida(s)** | | Condições Contratuais com Convênios | | Reprocessamento de Divisão | | Elaboração de Contas | | Registro de Atendimentos | | Agendamento | | Registro de Informações Cirúrgicas | | Prontuário Eletrônico | |
| **Requisito (ISSUE):** | [PCREQ-10906](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10906 "PCREQ-10906") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle®/ SQL Server® |
| **Tabelas Utilizadas:** | SZDIVISAOCOBRANCA |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a funcionalidade de divisão de cobranças (Honorários e SADT), nos lançamentos presentes no sistema.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.11 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.11.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.11

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Cadastros / Faturamento / Condições Contratuais com Convênios** e selecione a Condição Contratual desejada.
2. Clique em **Anexos / Divisão de Cobranças** e inclua um novo registro.
3. Nesta tela, informe o Prestador, a Especialidade (Não obrigatório), Faixa Inicial e Final de Procedimentos e Percentual que será pago ao prestador principal.
4. Como o campo especialidade não é obrigatório, para SADT o mesmo não deve ser informado, pois o registro de SADT não contém a informação da especialidade do médico, **o contrário de Honorários, onde a especialidade do médico pode ser informada durante o registro**.

**Itens da Enfermagem (Prontuário)**

1. Acesse o menu **Cadastros / Cuidados Com o Paciente / Prescrição Médica / Itens da Enfermagem**.
2. Insira um novo registro do tipo **Itens P/ Registro Médico**, informando como Item de Débito o mesmo Honorário que foi definido como Item de Divisão (Devem ser definidos mesmo Convênio e Vigência).

### Lançamentos das Agendas

1. Acesse o menu **Cadastros / Uso Geral / Agendamentos / Atividades** e inclua um novo registro.
2. Na aba **Serviços e Taxas**, Inclua um novo registro, informando o honorário configurado como Item de Divisão.
3. Acesse o menu **Atendimento / Agendamento / Agenda de Atendimentos**.
4. Selecione a agenda desejada (Preferencialmente do Profissional para o qual está configurado o Item de Divisão) e clique em **Opções**.
5. Na aba **Atividades**, inclua a atividade configurada.
6. Na aba **Especialidades**, inclua a mesma especialidade definida no Item de divisão.

## Procedimento para Utilização

**Elaboração de Contas**

1. Acesse o menu **Atendimento / Pronto Atendimento/Ambulatório / Registro de Atendimentos Externos** e crie um novo atendimento externo, com o mesmo convênio para o qual as divisões foram configuradas.
2. Defina como médico responsável o mesmo médico para o qual as divisões foram configuradas.
3. Acesse a **Elaboração de Contas** do paciente (Ctrl + L).
4. Acesse a aba **Honorários** e inclua um novo registro de honorário para o paciente, definindo o mesmo honorário configurado anteriormente. Como foi definida uma especialidade específica para o honorário, informe a mesma no campo **Especialidade do Médico**.
5. Clique em **Gravar**. O sistema deverá buscar pela parametrização de divisão e efetuar a divisão entre o prestador informado no registro do Honorário e o prestador principal da unidade de faturamento que corresponde à unidade de atendimento atual;
6. Como para o Prestador foi definido 40% do Valor, no Lançamento para o Hospital serão incluídos os outros 60%. O procedimento em questão tem o valor definido, em reais, de R$32,00.
7. No lançamento para o Prestador, serão incluídos os outros 40% do valor do Honorário.
8. Acesse a aba “**Diagnose e Terapia**” e inclua um novo registro contendo o SADT configurado.
9. Clique em **Gravar**, o sistema deverá efetuar a divisão pelo percentual, conforme configurado.  
     
   ***\**\*Como para este procedimento foi definido o percentual de 35%, os outros 65% do valor total ficam para o Prestador Principal da Unidade de Faturamento. O Valor do SADT em questão é em CH, portanto o cálculo do mesmo é feito de acordo com o valor definido nas condições financeiras com o convênio (CH \* ValorCh \* Quantidade, que dá um valor total de R$13,80). Neste procedimento há também um valor de filme(R$3,34), que é integralmente somado ao lançamento para o Prestador Principal da Unidade de Faturamento, portanto, a equação para este lançamento é a seguinte: 13,80\*(65%)+3,34=12,31.**  
     
     
   **\*\*Como o valor definido para este SADT foi de 35%, o cálculo do valor para o prestador ficou o seguinte:13,80\*(35%)=4,83. Note que não há adição de valor de filme para o SADT que fica com o prestador:**  
   **\*\*Os lançamentos em outros pontos do Sistema seguirão exatamente a mesma lógica.**

**Lançamento pelo Prontuário Eletrônico do Paciente (Prontuário do TOTVS Gestão Hospitalar)**

1. Acesse o menu **Prontuário**.
2. Acesse a aba **Anamnese/Exame Físico**, sub-aba **HPP/Procedimentos**.
3. Busque pelo Item parametrizado, que contém o honorário a ser dividido:
4. Na tela de Confirmação, marque o CheckBox **Aplicar Item** e clique em **OK**.
5. Acesse novamente a **Elaboração de Contas** do paciente e verifique a aba **Honorários**. O honorário deverá estar lançado para o paciente, já com a cobrança dividida.  
     
   \*\*Os lançamentos realizados desta forma sempre serão inseridos na conta como Honorários.

**Lançamento Automático pelo Agendamento**

1. Acesse o menu **Atendimento /** **Agendamento / Agenda de Atendimentos**.
2. Procure pela agenda do Profissional configurado para o Item de Divisão e inclua um novo Agendamento.
3. Selecione um paciente qualquer (mesmo Convênio e Plano configurados) e selecione a atividade configurada com o item de débito sendo o item de divisão.
4. Na grid, selecione o registro correspondente ao agendamento recém marcado e clique em **Atend. Externo**, o registro de atendimento abrirá. Preencha os campos necessários e grave o atendimento.
5. Acesse a **Elaboração de Contas** deste novo atendimento. O registro correspondente ao item de débito (já com a divisão efetuada), deverá constar dentre os honorários.  
     
   \*\*Os lançamentos realizados desta forma sempre serão inseridos na conta como Honorários.

**Lançamento Automático pelo Pedido de Exames**

1. Inclua um novo Atendimento Externo em uma unidade de Exames.
2. Na aba **Pedido de Exames**, inclua um novo registro.
3. Na aba **Exames Solicitados**, inclua um novo registro, contendo um item de divisão cadastrado.
4. Clique em **Gravar**. Neste momento, o sistema lançará o item na conta do paciente, na aba **Diagnose e Terapia**, com o valor já dividido.  
     
   **\*\*O item em questão possui o valor em reais de R$76,00, a parametrização realizada foi de 45% (R$34,20) do valor para o Profissional Executante e 55% (R$41,80) para o Prestador Principal da Unidade de Faturamento.**

**Lançamento pelo Registro de Informações Cirúrgicas**

1. Acesse o menu **Cuidados com Paciente / Centro Cirúrgico / Registro de informações Cirúrgicas.**
2. Inclua um novo registro para um paciente qualquer.
3. Na aba “**Procedimentos**”, inclua um registro com o honorário pré configurado como Item de Divisão:
4. Salve o Registro e clique em “**Processos / Enviar dados para Faturamento**”;
5. Clique em “**Executar**”. Se o processo for executado com sucesso, o item deverá aparecer na Elaboração de Contas do Paciente, já dividido, na aba “**Honorários**”:

**Lançamento Automático pelo Registro de Atendimento (Nova MDI)**

1. Ao editar um Atendimento em uma unidade de Exames.
2. Na aba **Pedido de Exames**, inclua um novo registro.
3. Ao clicar para salvar o exame a divisão de percentual irá ocorrer.

### Reprocessamento de Divisão de Honorários e Exames

1. Acesse o menu **Cadastros / Faturamento / Condições Contratuais com Convênios** e selecione a Condição Contratual desejada.
2. Acesse o menu **Anexos / Divisão de Cobranças**, e exclua todos os registros, caso existam.
3. Acesse o menu **Atendimento** **/ Pronto Atendimento/Ambulatório / Registro de Atendimentos Externos**.
4. Inclua um novo registro de atendimento externo.
5. Acesse a **Elaboração de Contas** deste atendimento.
6. Inclua alguns itens diferenciados, para o prestador desejado, nas abas **Honorários** e**Diagnose e Terapia**.
7. Acesse novamente o **Cadastro de Divisão**, nas **Condições Contratuais com Convênios**, e defina para cada item lançado, uma nova regra de divisão.
8. Acesse o menu **Utilitários / Utilitários do RM Saúde / Reprocessamento de Divisão de Cobranças**.
9. Informe os dados referentes ao convênio e período desejado para Reprocessamento.
10. Após concluir o Reprocessamento, acesse novamente a **Elaboração de Contas** do Paciente e verifique que os itens lançados foram divididos conforme as regras.  
      
    **\*\* No caso de SADT, deve-se levar em consideração também o filme, que é integralmente adicionado ao registro correspondente ao Prestador Principal da Unidade de Faturamento.**

divs
