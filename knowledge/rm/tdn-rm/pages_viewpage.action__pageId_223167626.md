---
content_hash: aef4ae1dc49c31cbb5a8f6fbaf8556b7a3018cd39e1cad28d729e122fae47dbe
fetched_at: '2026-06-29T00:06:21.287881+00:00'
page_id: '223167626'
product: rm
source: tdn-rm
title: DT_Vigência_em_Condições_Contratuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223167626
version: 125
---

# Implementação de Vigência nas Condições Contratuais com Convênios

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Faturamento |
| **Rotina:** | |  | | --- | | **Rotina** | | Condições Contratuais com Convênios |  |  | | --- | | **Rotina(s) envolvida(s)** | | Elaboração de Contas | |
| **Requisito (ISSUE):** | [PCREQ-2285](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-2285 "PCREQ-2285") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZCONDCONTRAT |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.9 |

## Descrição

  Esta implementação tem como objetivo, possibilitar o cadastro de mais de uma condição contratual para um Convênio, em uma mesma Unidade de Faturamento, porém com vigências distintas.

## Procedimento para Implantação

   Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.9 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.9.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.9

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

  **CÓPIA** **DAS CONDIÇÕES CONTRATUAIS E CONFIGURAÇÃO DA NOVA CONDIÇÃO**

1. Acesse o menu “**Cadastros / Faturamento > Condições Contratuais com Convênios**”.
2. Selecione um registro para edição. A tela de edição agora tem um novo campo (**Data Vigência**):
3. Na própria tela de edição, ou na grid anterior, selecione um dos registros e clique em “**Processos / Copia Condições Contratuais e Financeiras**”.
4. Uma nova tela abrirá, solicitando a Unidade de Faturamento e a data de vigência da nova condição contratual. **Coloque uma data futura, para que a nova condição ainda não cause reflexo**:
5. Informe os dados solicitados e clique em “**Executar**”. Caso a cópia ocorra com sucesso, a seguinte tela será exibida.

* **LANÇAMENTOS AUTOMÁTICOS**

1. Acesse o menu “**Cadastros / Faturamento / Lançamento Automático no registro de Atendimento**”.
2. Cadastre um item para lançamento automático do **Tipo Interno.**
3. Cadastre um item para lançamento automático do **Tipo Externo.**
4. Acesse o menu “**Cadastros / Faturamento / Tabela de Procedimentos e Serviços**”.
5. Inclua dois novos itens na mesma tabela DTS que está configurada nas condições contratuais com o convênio. **O item deve ter o mesmo código dos itens cadastrados nos passos 2 e 3**:
6. Acesse o menu “**Atendimento / Pronto Atendimento / Ambulatório / Registro de Atendimentos Externos**”.
7. Registre um novo atendimento externo com os mesmos “**Tipo de Atendimento, Convênio, Unidade de Atendimento e Unidade de Faturamento**“, cadastrados no lançamento automático.
8. Depois de registrado o atendimento, acesse a **Elaboração de Contas** e verifique a aba “Taxas e Serviços”. O item deverá estar lançado nesta aba.
9. Acesse o menu “**Atendimento / Internação / Registro de Internações**”.
10. Registre uma nova internação com os mesmos “**Tipo de Atendimento, Convênio, Unidade de Atendimento e Unidade de Faturamento**“, cadastrados no lançamento automático.
11. Depois de registrado o atendimento, acesse a **Elaboração de Contas** e verifique a aba “**Taxas e Serviços**”. O item deverá estar lançado nesta aba.

* **MANUTENÇÃO DAS TABELAS DE PREÇOS**

1. Acesse o menu “**Cadastros / Faturamento / Tabelas de Preços Utilizadas**”.
2. Inclua novas tabelas (com referências nas tabelas da condição contratual configurada).
3. Acesse o menu “**Cadastros / Faturamento / Tabelas de Mat/Med usadas**”.
4. Inclua novas tabelas (com referências nas tabelas da condição contratual configurada).
5. Acesse o menu “**Cadastros / Faturamento / Tabelas de Portes Usadas**”.
6. Inclua nova tabela (com referência na tabela da condição contratual configurada).
7. Inclua portes anestésicos (com referência no porte copiado).
8. Acesse o menu “**Utilitários / Rotinas / Manutenção de Tabelas de Preços**”.
9. Selecione tabela de Origem (**tabela configurada nas condições Contratuais**) e Tabela de Destino (**Tabela correspondente criada recentemente**).
10. Clique em **Inicia** e **Confirmar**.
11. Marque a opção “**Reajustar itens tabela de preço**”, selecione a tabela criada (50%), e clique em inicia. Na tela que abrirá, informe o percentual de reajuste (**utilizado 50% nos testes**):

* **TESTAR NOVAMENTE OS LANÇAMENTOS AUTOMÁTICOS**

1. Acesse o menu “**Atendimento / Pronto Atendimento / Ambulatório / Registro de Atendimentos Externos**”.
2. Registre um novo atendimento externo com os mesmos “**Tipo de Atendimento, Convênio, Unidade de Atendimento e Unidade de Faturamento**“, cadastrados no lançamento automático.
3. Verifique a **Elaboração de Contas**. A aba "**Taxas e****Serviços**" deverá conter o lançamento automático com o valor 50% maior.
4. Acesse o menu “**Atendimento / Internação / Registro de Internações**”.
5. Registre uma nova internação com os mesmos “**Tipo de Atendimento, Convênio, Unidade de Atendimento e Unidade de Faturamento**“, cadastrados no lançamento automático.
6. Verifique a **Elaboração de Contas**. A aba "**Taxas e****Serviços**" deverá conter o lançamento automático com o valor 50% maior.

* **ELABORAÇÃO DE CONTAS**

1. Acesse a elaboração de contas e lance um honorário;
2. Acesse novamente o cadastro de condições contratuais e altere as datas de vigência, de modo que a condição contratual antiga volte a ficar vigente;
3. Acesse novamente a elaboração de contas do mesmo paciente e lance o mesmo honorário. O valor deverá estar condizente com o que está na respectiva tabela;
4. **Repita os testes para as abas Diárias, Taxas e Serviços, MatMed, Diagnose e Terapia e Especial.**

* **CADASTRO DE ITENS DE DÉBITO**

1. Acesse o menu "**Cadastros / Unidade de Diagnóstico / Exames e Serviços**".
2. Acesse o cadastro de um exame qualquer.
3. Clique em "**Anexos / Item de débito**" e inclua um novo item de débito. A tela de cadastro de item de débito devera permitir a seleção da vigência desejada.
4. Verifique se ao buscar o item a respectiva tabela está correta.
5. Realize o mesmo teste nos seguintes locais:  
   "**Cadastros / Cuidados com o Paciente / Prescrição Médica / Itens da Enfermagem**".  
     
     
   "**Cadastros / Uso Geral / Agendamento / Atividades (Aba Serviços e Taxas)**".  
     
     
   "**Cadastros / Cuidados com o Paciente / Cirurgias / Procedimentos Cirúrgicos (Aba Itens de débito)**".  
     
   "**Cadastros / Cuidados com o Paciente / Cirurgias / Recursos Para Cirurgias (Aba Taxas do Recurso)**".

divs
