---
content_hash: b45be2ddcb55516618cc25c09885e5c97a55ab9476d760f6fd8850c7688bc513
fetched_at: '2026-06-29T00:09:32.737827+00:00'
page_id: '425458912'
product: rm
source: tdn-rm
title: Associação de Matrícula no Período Letivo a Itens de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458912
version: 8
---

---

O TOTVS Educacional, permite o vínculo de matrículas realizadas em um período letivo com um item de contrato do TOTVS Gestão de Estoque, Compras e Faturamento.  
   
Dessa forma, todo o financeiro e Contábil é gerenciado pelo TOTVS Gestão de Estoque, Compras e Faturamento associado às regras de um contrato no módulo de Contratos.  
   
Esse tipo de vínculo permite o gerenciamento financeiro e contábil, através de um contrato, de turmas fechadas ou de um grupo de matrículas.

****1.********Parametrização****

Para utilização do processo de associação de matrículas com um Item de Contrato é necessário informar ao sistema que essa integração está habilitada.  
   
Para isso, é necessário acessar o parâmetro que disponibiliza esse serviço.

Menu: *Configurações | Parâmetros* | *Integração | Financeiro* |***Fin – Geral 3/4 | "Utilizar integração com o módulo Contratos"***

Através dessa tela de parametrização, também, é possível informar se o sistema levará em consideração a inadimplência financeira, dos contratos associados, na realização de uma nova matrícula pelo aluno.

Menu: ***Configurações | Parâmetros|******Integração | Financeiro |******Fin – Geral 3/4 | "Bloquear matrícula por inadimplência financeira"***

A validação por inadimplência financeira do contrato, somente, acontecerá se o sistema estiver parametrizado para bloquear a matrícula de alunos inadimplentes.

Verificar os parâmetros:

* Matrícula -> Movimento -> Bloquear matrícula para inadimplentes
* Matrícula -> Movimento -> Bloquear mudança de situação de matrícula para inadimplentes
* RM Portal -> Portal - Geral -> Exibir aviso de inadimplência no quadro de avisos
* RM Portal -> Portal - Matrícula/Geral -> Débitos financeiros - Bloquear alunos
* RM Portal -> Portal - Matrícula/Geral -> Débitos financeiros - Alertar alunos
* Integração -> Financeiro -> Fin – Geral -> Bloquear matrícula por inadimplência financeira

Em caso de dúvidas consulte o help do aplicativo ou entre em contato pelo Help Desk.

**2. Processo para associação de matrículas com Itens de Contrato**

Esse processo tem a finalidade de associar matrículas realizadas em período letivo a um Item de Contrato cadastrado no módulo Gestão de Estoque, Compras e Faturamento

Processo:  ***Educacional | Educacional |******Financeiro/Contábil | Assistentes | Associar matrículas a um item de contrato***Para execução do processo é necessária a seleção de um Contrato e um Item de Contrato que serão utilizados na associação às matrículas.

Serão disponibilizados apenas contratos que se enquadram no item abaixo:

* Contratos e Itens de Contrato que não estão cancelados;

Através do mesmo processo é possível associar e desassociar uma matrícula a um Item de Contrato. A desassociação acontecerá, caso a caixa "Remover associação entre matrículas e item de contrato" esteja marcada.

Caso o aluno já tenha algum Contrato gerado no Educacional, não será possível realizar a associação a um Item de Contrato do módulo de Gestão de Estoque, Compras e Faturamento.

Somente será possível associar a matrícula do aluno uma vez. Caso, seja executado o processo novamente, será registrado no log do processo um erro informando que a associação existe.

Para associar uma matrícula a outro Item de Contrato, será necessário executar o processo para a desassociação da matrícula antes de uma nova associação.

**3. Cadastro de Contratos e Itens de Contratos**

O Cadastro de Contratos e Itens de Contratos utilizados para a realização dessa associação, serão cadastros no módulo Gestão de Estoque, Compras e Faturamento, através do menu:

Módulo: ***BackOffice | Gestão de Estoque, Compras e Faturamento |******Contratos | Manutenção de Contrato***

**4. Visualização das matrículas associadas**

Todas as matrículas associadas podem ser visualizadas no cadastro do Item de Contrato associado.

Módulo: *BackOffice | Gestão de Estoque, Compras e Faturamento |* ***Contratos | Manutenção de Contrato| Itens| Itens |*** ***Educacional | "Matrículas de alunos"***

A visualização das matrículas estará disponível, somente, quando um Item de Contrato tiver associação com alguma matrícula de aluno do Educacional.

É permitido associar vários Alunos ao mesmo item de contrato do TOTVS Gestão de Estoque, Compras e Faturamento, mas para isso todos os alunos dever estar na mesma matriz aplicada. Na matriz aplicada podemos informar os cadastros como item contábil, classe de valor e caso essas informações sejam diferentes teríamos conflitos na contabilização ao deixar associar diferentes matrizes.
