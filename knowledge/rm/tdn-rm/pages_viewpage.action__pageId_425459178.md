---
content_hash: 969f53adfad520e4ebd4c3b03b89ba0096820a09143c6ac1a02f97a950164afa
fetched_at: '2026-06-29T00:09:34.525786+00:00'
page_id: '425459178'
product: rm
source: tdn-rm
title: 14.09 - Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459178
version: 12
---

O objetivo desta etapa é definir as integrações e as características do TOTVS Gestão Bibliotecária com o TOTVS Gestão Financeira, TOTVS Folha de pagamento, TOTVS Gestão de estoques, compras e faturamento.

**14.09.01 - Financeiro**

O objetivo desta etapa é definir as características gerais da integração com o sistema financeiro, características para geração de multas da biblioteca   
no sistema financeiro e os valores opcionais que serão utilizados na geração de lançamentos de multa.  
  
 **Etapa 1**  
   
**Utilizar integração com o Financeiro:** Este parâmetro habilita a integração do TOTVS Gestão Bibliotecária com o TOTVS Gestão Financeira.   
   
**Código default para o responsável financeiro:** aqui  é informada a máscara do cliente/fornecedor que será responsável financeiro de usuários   
no caso da importação automática de usuários.

**Tipo de responsável financeiro:** Define qual será o tipo de responsável financeiro utilizado quando é realizada a importação automática de um usuário.  
   
 **Apresentar boleto de cobrança registrada ainda não registrado no Portal:** Permite que os boletos originados de cobrança registrada que ainda não estiverem registrados nos bancos possam ser impressos no Portal do aluno.  
  
**Boleto para pagamento de multa no portal:**Permite configurar qual o relatório de boleto para pagamento de multa do gerador de relatórios será utilizado no portal. Ao habilitar o parâmetro "Utiliza novo gerador?" será possível selecionar relatório do RM Reports. Caso contrário será informado do antigo gerador de relatórios.

* **OBS**: Clientes com contratos novos não poderão utilizar o Gerador de Relatório Delphi (Antigo) e deverão definir o relatório RM Reports para a impressão dos boletos.

**Empréstimo**

* **Bloquear empréstimo/renovação para inadimplentes financeiros da Bibliotecária:** Este parâmetro define que usuários que possuam pendências financeiras no TOTVS Gestão Bibliotecária (pagamentos de empréstimos e multas) não poderão realizar empréstimos de exemplares.
* **Bloquear empréstimo/renovação para usuários com lançamentos na Biblioteca em aberto:**Este parâmetro bloqueia empréstimos e renovações para usuários que possuam pendências financeiras no TOTVS Gestão Bibliotecária em aberto e que ainda não estejam vencidos, se o parâmetro estiver marcado o sistema irá bloquear a movimentação e mostrará um alerta em todos os ambientes, RM.exe, WebService e Portal da Biblioteca. Este parâmetro só será  habilitado se o parâmetro anterior "Bloquear empréstimo/renovação para inadimplentes financeiros da Bibliotecária" estiver habilitado.
* **Bloquear empréstimo/renovação para inadimplentes financeiros no Educacional:** Este parâmetro define que usuários que possuam pendências financeiras no TOTVS Educacional (atraso no pagamento de mensalidades) não poderão realizar empréstimos de exemplares.

**Reserva**

* **Bloquear reserva para inadimplentes financeiros na Biblioteca:**Este parâmetro define que usuários que possuam pendências financeiras no TOTVS Gestão Bibliotecária (pagamentos de empréstimos e multas) não poderão realizar reservas de publicações.
* **Bloquear reserva para inadimplentes financeiros no TOTVS Educacional:** Este parâmetro define que usuários que possuam pendências financeiras no TOTVS Educacional (atraso no pagamento de mensalidade) não poderão realizar reservas de publicações.

**Etapa 2**  
   
**Eventos contábeis:** Este parâmetro define os eventos contábeis para inclusão e baixa de lançamentos financeiros.  
   
**Geração de lançamentos**  
Neste passo é informado o % de juros, dias de vencimento, conta caixa, o tipo de documento e o tipo contábil dos lançamentos a serem gerados.   
   
**Agrupar valores de multas em um único lançamento:** Este parâmetro define que todos os valores referentes a uma mesma movimentação serão agrupados em um único lançamento.  
   
Gerar boleto bancário:

**Tipo de documento**: Este parâmetro define o tipo de documento do TOTVS Gestão Financeira que será utilizado na geração do lançamento de multas ou taxas da biblioteca. Caso o tipo de documento utilizado esteja definido para gerar o número do documento como "Definido pelo usuário", será definido o código do empréstimo no número do documento do lançamento, caso esteja definido para "Copiar referência" ou "Gerar número do documento sequencialmente", serão utilizadas as regras do TOTVS Gestão Financeira. Para mais informações acesse: .

**Etapa 3**  
   
Nesta etapa é possível definir os valores opcionais que serão utilizados na geração de lançamentos da biblioteca. É possível informar as tabelas opcionais, campos e datas. As informações de valores opcionais é definido nos parâmetros do TOTVS Gestão Financeira.  
   
**Etapa 4**  
  
**Natureza financeira**  
Nos parâmetros **Cadastro/Renovação**, **Cobrança de empréstimo** e **Cobrança de multa**, é possível informar naturezas financeiras a serem utilizadas para rateios realizados por natureza financeira.  
   
**Atenção**

* As naturezas financeiras devem ser cadastradas no TOTVS Gestão de Estoques, Compras e Faturamento. Para isso, é preciso definir uma máscara para o código das naturezas financeiras.
* Toda natureza financeira cadastrada deve ser do tipo "Analítica", condição para serem apresentadas no TOTVS Gestão Bibliotecária.

**14.09.02 - Educacional**  
O objetivo desta etapa é definir as características gerais da integração da biblioteca com os sistemas educacionais.  
   
**Integração com o Educacional**  
Neste etapa é definido as integrações do TOTVS Gestão Bibliotecária com os seguintes módulos educacionais:

* RM Classis Ensino Básico
* RM Classis Ensino Superior
* TOTVS Educacional

**Bloquear Empréstimo/Reserva/Renovação para alunos sem disciplina em curso:** Este parâmetro define que alunos que não cursam nenhuma disciplina nos módulos educacionais não poderão realizar empréstimos e/ou reservas no sistema.  
   
**Bloquear importação automática para alunos sem disciplina em curso:** Este parâmetro define que alunos que não cursam nenhuma disciplina nos módulos educacionais não poderão ser importados para o TOTVS Gestão Bibliotecária, através das movimentações.

Importante

Para as duas opções acima o sistema considera uma disciplina em curso quando a disciplina possui uma situação que seja definida como "Disciplina em curso" e que a disciplina matriculada para o aluno não possua a situação de resultado final preenchida.

 

Caso a disciplina matriculada para o aluno esteja com uma situação que define como disciplina em curso porém esteja com a situação de resultado final preenchida, o sistema não irá considerar como disciplina em curso e não permitirá a empréstimo/reserva/renovação e nem mesmo a importação automática de alunos.

**Verificar documentos pendentes ao realizar o empréstimo do aluno:** Este parâmetro define que ao realizar empréstimos, o sistema irá verificar se há algum documento pendente do aluno nos módulos educacionais (serão considerados como pendentes documentos com status igual a "Não entregue" e "Rejeitado" ), para mais informações acesse .

**Importação automática no empréstimo de alunos não cadastrados**  
Este parâmetro define a importação automática de alunos para o TOTVS Gestão Bibliotecária. Aqui é definido qual será o tipo de usuário e perfil que este usuário será importado. Além de configurar se o acesso do usuário será por: Todas Filiais/Unidades ou Local.  
   
   
**14.09.03 - Folha de pagamento**  
O objetivo desta etapa é definir as características gerais da integração da biblioteca com o sistema de folha de pagamento.  
   
**Utilizar integração com a Folha de Pagamento:**Este parâmetro define a integração do TOTVS Gestão Bibliotecária com o TOTVS Folha de Pagamento.   
   
**Permite Empréstimos/Reservas para funcionários demitidos:**Este parâmetro define que usuários que estão cadastrados no TOTVS Folha de Pagamento como funcionários demitidos poderão realizar empréstimos e reservas no TOTVS Gestão Bibliotecária.   
   
**Importação automática no empréstimo de funcionários não cadastrados:**Este parâmetro define a importação automática de funcionários para o TOTVS Gestão Bibliotecária.   
   
**14.09.04 - Estoque**  
 O objetivo desta etapa é definir as configurações para solicitações de compra no sistema de controle de estoque.  
   
**Utilizar a integração com o Estoque:**Este parâmetro define a integração do TOTVS Gestão Bibliotecária com o TOTVS Gestão de Estoques, compras e faturamento.

**Tipo de movimento:** Define qual tipo de movimento serão utilizado ao realiza uma solicitação de compra através do TOTVS Gestão Bibliotecária. Para maiores informações acesse o .  
   
   
**14.09.05 - Protheus**  
O objetivo desta etapa é configurar as informações de base de dados do Protheus quando este estiver integrado.  
   
**Utilizar integração com o Protheus:** Este parâmetro define a integração do TOTVS Gestão Bibliotecária com o Protheus.  
   
**Base de dados - Integração Protheus**  
Aqui é definido o tipo de banco de dados a ser utilizado (SQLServer ou Oracle) além das informações de conexão, como **servidor, base de dados, usuário e senha.**
