---
content_hash: 0f8360cdd3634f2ccb7a317d38022c1c241f66f2c6c67826cf631557a6ceb41f
fetched_at: '2026-06-29T00:09:34.453257+00:00'
page_id: '425459157'
product: rm
source: tdn-rm
title: Alterar Vencimento do Desconto por Antecipação do Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459157
version: 2
---

---

Ao gerar os lançamentos para as parcelas dos alunos, o sistema verifica se há algum Desconto por Antecipação programado e já inclui o respectivo lançamento calculando-se todos os valores levando em consideração os possíveis descontos a serem aplicados conforme a data definida em cada faixa de desconto.

Eventualmente, após os lançamentos já terem sido gerados, as instituições de ensino podem precisar prorrogar as datas para concessão dos descontos. Através deste processo é possível alterar as datas das faixas de descontos por antecipação que já foram processados para os lançamentos. Este processo pode ser executado através no menu Financeiro/Contábil | Financeiro ou diretamente através da parcela do contrato. 

**Por exemplo:**

Descontos por antecipação original:  
 1ª. faixa – Pgto até o dia 05 = 30 % de desconto  
 2ª. faixa – Pgto até o dia 10 = 20 % de desconto  
 3ª. faixa – Pgto até o dia 20 = 5 % de desconto

Supondo que do dia 04 ao dia 05 ocorreram instabilidade no portal do aluno no que diz respeito à recebimento via cartão. Neste caso a instituição irá prorrogar o vencimento do 1º desconto para o dia 08.

Como o lançamento já foi gerado, a realização da alteração deste vencimento deverá ser realizada através do processo "Alterar Vencimento do Desconto por Antecipação do Lançamento", disponível no menu Financeiro/Contábil | Financeiro (ou através do mesmo processo acessado diretamente através da parcela do contrato).

Na execução do processo, crie um filtro que selecione as informações (parcelas, contratos, etc...) dos alunos que terão os vencimentos dos descontos alterados. Este filtro tem o objetivo de facilitar e flexibilizar a seleção de dados de uma forma genérica.

Após a seleção do filtro clique em "Carregar vencimentos dos descontos por antecipação".

Após o processamento do filtro, serão apresentadas na aba "Alteração dos vencimentos" as informações dos vencimentos dos descontos por antecipação identificados através do filtro.

As informações serão apresentadas agrupadas pelo agrupador do desconto e vencimentos das parcelas. Para cada agrupador serão mostrados os descontos processados para a parcela. Preencha na coluna em destaque a data correspondente ao novo vencimento.

Como as informações serão apresentadas agrupadas, foi disponibilizada a opção "Pré-visualizar Aluno(s)". Esta opção apresenta todos os alunos que fazem parte do agrupamento da linha em questão e que terá o vencimento do desconto alterado para a nova data informada.

Após o preenchimento da data correspondente ao novo vencimento, clique em *executar* o processo.

Ao final da execução o será apresentado um LOG com as informações do processo e quais os alunos tiveram o vencimento da concessão do desconto alterado.

**Importante**

• Este processo altera pontualmente o vencimento somente dos descontos processados para as parcelas / lançamentos filtrados, ou seja, o cadastro oficial do desconto por antecipação não será alterado e assim, na geração dos próximos lançamentos o sistema respeitará o cadastro oficial do desconto que estiver vinculado à matriz ou ao contrato do aluno.  
• Caso o lançamento que teve o vencimento do desconto alterado seja regerado o sistema vai reprocessar os descontos por antecipação considerando os descontos do cadastro oficial, ou seja, a alteração do vencimento será perdida e serão aplicados os descontos oficiais.  
• Dependendo da data do novo vencimento, a mesma poderá sobrepor a data de outros vencimentos. Neste caso, o segundo vencimento será inativado:

**Por exemplo:**

Descontos por antecipação original:  
 1ª. faixa – Pgto até o dia 05 = 30 % de desconto  
 2ª. faixa – Pgto até o dia 10 = 20 % de desconto  
 3ª. faixa – Pgto até o dia 20 = 5 % de desconto

Supondo que do dia 04 ao dia 05 ocorreram instabilidade no portal do aluno no recebimento via cartão, neste caso a instituição irá prorrogar o vencimento do 1º desconto para o dia 10/05.

Observem que o dia 10/05 é quando finaliza o 2º vencimento, para este cenário o sistema realizará a alteração do 1º vencimento para o dia 10/05 e o 2º vencimento será inativado.

**− Visualização dos Descontos\***  
 Os descontos processados para as parcelas / lançamentos poderão ser consultados através do menu "Financeiro/Contábil | Desconto por Antecipação das Parcelas / Lançamento" e a mesma informação também está disponível no anexo da parcela do contrato.  
 Através da visualização destes dados é possível consultar a data do vencimento original (preenchida somente quando for alterada), se o desconto está ativo e qual usuário realizou a alteração.
