---
content_hash: cef57a01979689ee095d2936abe936ced719710d7dc52d80b175cb395a7ffa32
fetched_at: '2026-06-29T00:10:08.938215+00:00'
page_id: '452719610'
product: rm
source: tdn-rm
title: Restrições Cadastrais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719610
version: 6
---

Etapa utilizada para configurar restrições no cadastro de funcionários.  
   
**Campo e Parâmetros**  
   
Fórmula para Criticar o Cadastro de Funcionários  
Esse campo funciona associado a uma fórmula. Essa fórmula deve obrigatoriamente retornar uma mensagem.  
Este recurso não tem o objetivo de impedir a gravação, caso algo não esteja de acordo com a fórmula implementada, e sim gerar uma crítica ao que está sendo feito pelo usuário através da mensagem contida na fórmula escrita pelo usuário.

**Exemplo**  
se IDADE (HOJE) > 59   
entao "Funcionário com mais de 59 anos"   
senao se IDADE (HOJE) < 22   
entao "Funcionário com menos de 22 anos"   
senao "Funcionário com idade entre 22 e 59 anos"   
fimse   
fimse  
   
Quando o usuário salvar um novo funcionário, o sistema exibirá uma das seguintes mensagens:  
"Funcionário com mais de 59 anos";  
"Funcionário com menos de 22 anos";  
"Funcionário com idade entre 22 e 59 anos"  
*Histórico Salarial*  
   
Edita data de processamento  
Marcando esse parâmetro, é habilitado para edição o campo Data de processamento no cadastro de histórico salarial do Funcionário em Cadastros | Funcionários | Anexos | Históricos | Histórico Salarial  
   
   
*Alteração Global de Salários*  
   
Motivo Alteração Salarial Dissídio/Aumento Retroativo  
Neste campo é informado um motivo de Alteração salarial por dissídio retroativo. Os motivos são cadastrados na tabela dinâmica **INT26** em Administração de Pessoal|Cadastros|Cadastros Globais|Tabelas Dinâmicas**.** Quando é processada a alteração global de salário, informando uma data retroativa a ultima alteração, é criados dois registros no histórico de Salários: Um com data informada no processo e outro com a data igual a ultima alteração, acrescentada de 10 minutos. Esta ultima data é associado o motivo informado no campo 'Motivo Alteração Salarial Dissídio/Aumento Retroativo'.

**Exemplo**  
Ultima alteração salarial em 14-10-2017  
Penúltima alteração salarial em 01-04-2017  
   
Processando a alteração salarial para o dial 01-06-2017  
   
Foi inserido um registro no histórico com a data 01-06-2017 com o motivo informado no processo de alteração global de salários  
Foi inserido um registro no histórico com a data 14-10-2017 00:10 com o motivo informado no campo 'Motivo Alteração Salarial Dissídio/Aumento Retroativo'.  
   
   
**Observação**  
Este campo é obrigatório o preenchimento caso o usuário queira processar a alteração global de salários, mesmo que não seja retroativo  
O motivo informado neste campo não fica mais disponível para o processo de alteração global de salários

falseImportante!

Parâmetros abaixo serão habilitados na integração com o RM VITAE e para cálculo correto do salário a tabela salarial deve ser do tipo horista.

Utiliza Tabelas Salariais para evento de Salário Composto  
   
Marcando esse parâmetro, o sistema passará a utilizar na composição salarial dos funcionários as tabelas salariais do Totvs Gestão de Pessoas.  
Com isso, é possível associar um nível e faixa a cada evento da composição salarial. A tabela a ser considerada será a vinculada ao Cargo/Função ou Seção do funcionário de acordo com a parametrização no Totvs Gestão de Pessoas.  
   
   
Edita Tabelas Salariais nos Eventos de Salário Composto  
   
Marcando esse parâmetro, o sistema permitirá que seja incluso qualquer tabela, nível e faixa nos eventos de salário composto do funcionário, ou seja, ele poderá informar qualquer tabela salarial, não apenas a associada ao Cargo/Função ou Seção do funcionário.

**Observação**  
As mesmas regras aplicadas para edição do campo Hora do Funcionário se aplicará ao campo Valor Hora da composição Salarial onde são considerados também as seguintes parametrizações do Totvs Gestão de Pessoas:  
1) Requisição Obrigatória para alteração de Cargo e Salário;  
2) Requisição Obrigatória para Transferir ou promover Funcionário;  
3) Considerar os salários das tabelas salariais;  
4) Permitir alteração manual do salário;  
5) Código de Recebimento do funcionário;  
6) Parâmetro do Folha de Pagamento "Edita salário mensal para horistas/tarefeiros"
