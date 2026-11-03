---
content_hash: 2bfa4408c5f1d5681ad9f533845b8f15dd9f1c3331499174eeed97251750b3e8
fetched_at: '2026-06-29T00:10:09.941291+00:00'
page_id: '452719745'
product: rm
source: tdn-rm
title: Campos do Cadastro
type: documentation
url: https://tdn.totvs.com/display/LRM/Campos+do+Cadastro
version: 2
---

Campos do cadastro de funcionários e campos complementares podem ser alterados de forma global, ou seja, para vários funcionários de uma única vez utilizando fórmula.   
    
 Para cada cadastro, seja de funcionários ou campos complementares, serão listados os itens possíveis de alteração, sendo que para funcionários serão listados itens que o usuário tem permissão de acesso e para campos complementares serão listados somente os ativos.  
    
 Após selecionar o(s) item(s) a ser(em) alterado(s) será habilitado o campo para seleção da fórmula de alteração.  
    
 Há duas formas para seleção da fórmula:  
 **1 -** Digitar o código na primeira caixa e pressionar a tecla TAB. A descrição da fórmula aparecerá automaticamente.  
 **2 -** Selecionar a fórmula usando o botão de seleção.  
    
 **Atenção:**  
 **1 -** Para os campos, no cadastro de funcionário, que exigem a atualização dos históricos (ocorrência, tipo, situação, seção e função), deverá ser informado a data e o motivo da mudança para serem registrados nos respectivos históricos. Os campos data e motivo estarão visíveis e desabilitados, estes campos somente serão habilitados após o cursor ser colocado no campo fórmula.  
 **2 -** A alteração de situação de Licença Maternidade (Ativo para Licença Maternidade ou Licença Maternidade para Ativo) não poderá ser realizada por este módulo. A alteração só poderá ser feita diretamente no cadastro da funcionária.  
 **3 -** O usuário deve criar uma fórmula que retorne 1 ou 0, sendo que 1 significa que o funcionário tem contrato com prazo e 0 ele não tem, e associá-la a esse campo.   
 Caso a formula seja para alterar o campo Contrato com Prazo para 1, ou seja, marcar o campo devesse também alterar a data final de contrato. Caso isso não seja feito, a base pode ficar inconsistente, que pode atrapalhar na hora de uma possível rescisão.  
 **4 -** A alteração para "Fim do prazo do contrato" somente será processada quando o parâmetro Contrato com prazo no cadastro de funcionários estiver marcado. E a fórmula deve sempre retornar um valor tipo Data no formato DD/MM/YYYY.
