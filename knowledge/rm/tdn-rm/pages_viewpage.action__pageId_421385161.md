---
content_hash: 0279eab71bc30021ca27b3a685e7bda764b5f0d3fad6daee72302c13d53ad194
fetched_at: '2026-06-29T00:09:14.234655+00:00'
page_id: '421385161'
product: rm
source: tdn-rm
title: Liberar Medição acima de 100% por Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385161
version: 81
---

Contrato > Contratos > Processos > Alterar Parâmetro de Medição do Contrato") ou individualmente pelo mesmo caminho ou estando na tela de edição do respectivo contrato.
Os dois parâmetros para liberação de medição/consumo superior a 100% (do contrato e dos parâmetros do Projeto) existirão simultaneamente, sendo que, sempre irá prevalecer o que estiver definido em cada contrato, ou seja, ao ser efetuada uma medição ou consumo que supere 100% do contratado,  o sistema deverá ou não permitir essa medição/consumo atendendo ao que está definido no próprio contrato, e somente irá checar o parâmetro do projeto caso o contrato esteja parametrizado como 'Obedecer ao Projeto'.
Caso esteja utilizando o controle de Status de Contrato, este novo processo poderá ser executado apenas para os contratos no status "Em Negociação".
Para manter a segurança no processo de cadastro e medição dos contratos, o acesso ao processo "Alterar Parâmetro de Medição do Contrato" será controlado através do perfil do usuário. Para isso será criado em "Serviços Globais > Segurança > Perfis > Projetos > Construção e Projetos > Acesso a Menus" , na opção \[ 05 \] Controle - \[ 05.01 \] Básico -  \[ 05.01.02 \] Contrato - \[ 05.01.02.01 \] Contratos, o novo  item  de  Perfil '\[ 05.01.02.01.68 \] Parâmetro de Medir Contrato Acima de 100%'. Assim, somente terão acesso ao processo "Alterar Parâmetro de Medição do Contrato" , os usuários em cujo perfil esse novo item de permissão esteja liberado.
Quando da criação de um novo contrato a pagar, o campo 'Parâmetro Medição' será automaticamente preenchido com a opção 'Obedecer ao Projeto', já na criação dos contratos a receber, o campo será automaticamente preenchido com 'Sempre Permitir'. Fica a cargo do usuário executar o processo para alterar o conteúdo do campo, caso vá optar por uma parametrização diferente da default. O mesmo procedimento se dará com todos os contratos já existentes atualmente na base de dados, ou seja, a partir da atualização da versão 12.1.8, para todos os contratos a pagar será automaticamente definido que obedecerão aos parâmetros do projeto e para todos os contratos a receber será automaticamente definido que sempre permitirão medição/consumo superior a 100%, bastando executar o processo caso deseje alterar essa parametrização.
Aconselhamos que a liberação e a utilização deste processo sejam efetuadas com critério visto que o mesmo possibilita medir/consumir além do que foi planejado na obra.Nos contratos das finalidades Marco Contratual e Fornecimento de Material o novo parâmetro não será apresentado e o processo não poderá ser executado.
 
 ]]>
