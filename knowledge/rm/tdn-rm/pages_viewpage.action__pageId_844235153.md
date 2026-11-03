---
content_hash: c067536df24b1fc5401a10ab23bf42e9d1b8e9355505da283e77cc6f0cc5004c
fetched_at: '2026-06-29T00:11:50.621994+00:00'
page_id: '844235153'
product: rm
source: tdn-rm
title: Solicitação de Materiais e Medicamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=844235153
version: 40
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Cadastro RM**
4. **Impressão do relatório**

Solicitação de Materiais e Medicamentos (V.2406)1. Visão Geral

## **01. VISÃO GERAL**

A nova funcionalidade de Solicitação de Materiais e Medicamentos será integrada na aba de Solicitações no menu do prontuário eletrônico e através do Painel de Pacientes e Painel de Internados. A funcionalidade permite que os profissionais em ambientes hospitalares ou ambulatoriais possam requisitar materiais e medicamentos de forma eficiente e rápida através do PEP, assegurando que todos os itens necessários para o cuidado do paciente estejam disponíveis em tempo hábil. As solicitações são enviadas diretamente à farmácia, promovendo uma comunicação clara e reduzindo o tempo de resposta. 

2.0 Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Usuários com permissão de acesso encontram a funcionalidade de Solicitação de Materiais e Medicamentos através de dois caminhos principais: na aba de "Solicitações" no menu lateral do PEP ou através do Painel de Pacientes e Painel de Internados, acessando o atalho "Solicitação MAT/MED".

**Na aba de Solicitações no PEP**, ao acessar o submenu de Materiais e Medicamentos, será exibido uma timeline de **solicitações de todos os profissionais**, composta por:

1. Data e hora de início e fim da solicitação
2. Status da solicitação: Pendente (farmácia não realizou o envio) ou Enviado (farmácia realizou o envio)
3. Especialidade e o nome do usuário responsável pela solicitação
4. Ao expandir o accordion, será exibido o conteúdo da solicitação realizada e o responsável pela criação e/ou suspensão do item, com a possibilidade de imprimir, suspender ou visualizar a tela de solicitação preenchida.

Para iniciar uma nova solicitação, clique no botão **"+ Novo"** e uma tela será exibida para preenchimento composta por:

1. Centro de custo e Local de uso (referente a unidade que o paciente está)
2. Data e hora com preenchimento automático e possibilidade de edição. Não é possível inserir data e hora futura.
3. Tipo de movimento
4. Local estoque
5. Material / Medicamento: a lista exibida será composta por materiais e medicamentos disponíveis nos itens de produto. O usuário poderá selecionar um número indeterminado de itens e os mesmos serão listados na tabela abaixo ao selecionar o check-box. Apenas os materiais e medicamentos autorizados podem ser solicitados. (Cadastro do RM: Estoque > Produto > Com a flag: Solicitação permitida pela equipe multidisciplinar).
6. A tabela contém as colunas de descrição dos itens selecionados, quantidade, unidade da prescrição e observações. Quando aplicável, especificações adicionais como tamanho, dosagem etc., deverão ser descritos no campo "Observação".
7. Para itens avulsos com a configuração 'Permite solicitação pela equipe multidisciplinar' o campo de quantidade estará liberado para edição, enquanto para itens vinculados a uma prescrição médica vigente esse campo ficará bloqueado, refletindo o valor exato definido pelo médico.
8. Quando for adicionado um produto composto a solicitação, o sistema irá se comportar da seguinte forma (funcionalidade implementada nas versões 12.1.2506 e 12.1.2510):
   1. O produto composto não será apresentado na lista de itens selecionados, mas sim a sua composição;
   2. Não será permitido incluir o mesmo produto composto mais de uma vez;
   3. Não será permitido alterar a quantidade ou unidade dos itens de composição, será utilizado sempre o que estiver definido no cadastro do produto;
   4. Não será permitido excluir um item de composição. Se desejar excluir deverá excluir toda a solicitação;
9. Quando um item é solicitado através da tela de Materiais e Medicamentos (MAT/MED) e este provém de uma prescrição médica vigente, o sistema aplicará bloqueio automático de edição nos campos quantidade e unidade da prescrição sob as seguintes condições:
   1. O parâmetro "Permite solicitação pela equipe multidisciplinar" deve estar marcado no cadastro do produto (Caminho: RM > Cadastros > Produto > Anexo > Informações TOTVS saúde > Identificação II > Flag: Permite solicitação pela equipe multidisciplinar);
   2. Configuração da Unidade: A unidade de atendimento do paciente não deve utilizar aprazamento e checagem;
   3. A prescrição médica deve estar dentro do período de validade;
10. Quando o itemnão for proveniente de prescrição médica, o sistema exibirá as unidades de medida vinculadas ao cadastro do produto, podendo haver mais de uma opção disponível para seleção, sendo necessária a escolha manual pelo usuário.
11. Ao selecionar um item que cumpra os requisitos acima, o sistema carregará automaticamente a unidade de medida e a quantidade exatamente como definidas pelo médico na prescrição original.

Para finalizar a solicitação, clique no botão **"Finalizar"**. 

Ao prescrever e liberar um medicamento do tipo **“Se Necessário”** ou **“A Critério Médico”** que possua itens de diluição definidos como diluentes, materiais ou medicamentos, após a finalização, os itens de diluição serão adicionado na solicitação.

Serão incluídos automaticamente na solicitação apenas os diluentes definidos no momento da prescrição do medicamento.

Além disso, no Painel de Dispensação, serão apresentados o medicamento, o diluente e os materiais utilizados na diluição.

Ao adicionar os itens, caso exista mais de uma unidade de medida cadastrada para o produto, o sistema habilitará o campo de unidade, permitindo que o usuário altere a unidade.

**Solicitação realizada através do Painel de Pacientes e Painel de Internados:** ao clicar no atalho "Solicitação MAT/MED", será exibido uma modal com os mesmos campos para preenchimento presentes na solicitação da tela do PEP:

Ao finalizar a solicitação clicando no botão **"Finalizar"**, a modal será fechada e o usuário retornará ao painel.

* Se algum item estiver indisponível, a razão será comunicada por uma mensagem de alerta (saldo insuficiente, item proibido e/ou restrição contratual) e não será possível prosseguir com a solicitação.
* Quando o paciente apresentar mais de uma parcial de atendimento aberto, o sistema irá exibir a última parcial aberta como regra.
* Todas as solicitações de materiais e medicamentos são registradas automaticamente no prontuário eletrônico do paciente, garantindo o registro completo do cuidado.

Quando o cliente utilizar o PLT a solicitação de medicamentos prescritos deve ser realizada no momento do aprazamento/checagem, não utilizando esta funcionalidade.

Quando o cliente \*não\* utilizar o PLT a solicitação de medicamentos deve ser realizada por esta funcionalidade, permitindo apenas itens prescritos como SN ou ACM.

A equipe de enfermagem terá a segurança de conseguir solicitar apenas materiais permitidos pela instituição e medicamentos prescritos como SN e ACM.

2.1 Exemplo de utilização (12.1.2602)

## **02. EXEMPLO DE UTILIZAÇÃO (12.1.2602)**

Usuários com permissão de acesso encontram a funcionalidade de Solicitação de Materiais e Medicamentos através de dois caminhos principais: na aba de "Solicitações" no menu lateral do PEP ou através do Painel de Pacientes e Painel de Internados, acessando o atalho "Solicitação MAT/MED".

**Na aba de Solicitações no PEP**, ao acessar o submenu de Materiais e Medicamentos, será exibido uma timeline de solicitações, composta por:

1. Data e hora de início e data e hora fim quando a solicitação é enviada para farmácia;
2. Status da solicitação: 
   1. Rascunho (em digitação; permite excluir);
   2. Pendente (finalizado; a farmácia não realizou o envio; status na farmácia diferente de "processado"; não permite excluir);
   3. Enviado (finalizado; a farmácia realizou o envio; status na farmácia "processado"; não permite excluir);
   4. Observação: Se a solicitação for excluída no prontuário eletrônico seu status será alterado para suspenso. Os registros com status suspenso não serão exibida na tela (existiram apenas no banco de dados);
3. Especialidade e o nome do usuário responsável pela solicitação;
4. Ao expandir o accordion, será exibido o conteúdo da solicitação realizada e o responsável pela criação e/ou suspensão do item, com a possibilidade de imprimir, suspender ou visualizar a tela de solicitação preenchida.

Para iniciar uma nova solicitação, clique no botão **"+ Novo"** e uma tela será exibida para preenchimento composta por:

1. Centro de custo e Local de uso (referente a unidade que o paciente está);
2. Data e hora com preenchimento automático e possibilidade de edição. Não é possível inserir data e hora futura.
3. Tipo de movimento;
4. Local estoque;
5. Material / Medicamento: a lista exibida será composta por materiais e medicamentos disponíveis nos itens de produto (O produto cadastrado deve estar ativo, deve ser um do tipo "produto" e não "serviço"). O usuário poderá selecionar um número indeterminado de itens e os mesmos serão listados na tabela abaixo ao selecionar o check-box.
6. A tabela contém as colunas de descrição (é apresentado o nome fantasia do produto) dos itens selecionados, quantidade, unidade da prescrição e observações. Quando aplicável, especificações adicionais como tamanho, dosagem etc., deverão ser descritos no campo "Observação".

Para finalizar a solicitação, clique no botão **"Finalizar"**. 

1. Ao finalizar será verificado se os materiais ou medicamentos solicitados atende os sequintes requisitos:
   1. Será verificado o seu saldo de estoque de todos os produtos, sendo ele composto, associado ou diluentes;
   2. Será verificado se o produto informado permite solicitação pela equipe multidiciplinar (Cadastro do RM: Estoque > Produto > Com a flag: Solicitação permitida pela equipe multidisciplinar). Caso contrário será verificado se o produto possui uma prescrição vigente e se ela esta "marcada" como SN (se necessário) ou ACM (a críterio médico);
   3. Tambem será verificado se a unidade de atendimento utiliza PLT e o produto é medicamento e esta desmarcado a opção "permite solicitação pela equipe multidiciplinar", neste caso o medicamento só será possivel ser solicitado via aprazamento/checagem;
2. Quando o paciente apresentar mais de uma parcial de atendimento aberto, o sistema irá exibir a última parcial aberta como regra;
3. Todas as solicitações de materiais e medicamentos são registradas automaticamente no prontuário eletrônico do paciente, garantindo o registro completo do cuidado;

**Solicitação realizada através do Painel de Pacientes e Painel de Internados:** ao clicar no atalho "Solicitação MAT/MED", será exibido uma modal com os mesmos campos para preenchimento presentes na solicitação da tela do PEP:

Tela modal que será aberta, ao finalizar segue as mesmas regras descritas anteriormente:

Ao adicionar os itens, caso existam itens associados, será exibido um ícone informativo. Ao clicar nesse ícone, serão apresentados os itens associados ao item selecionado.  
Além disso, se houver itens associados à diluição, eles também serão exibidos.

3. Cadastro RM

## **03.** **CADASTRO RM**

Cadastro da permissão para solicitação de materiais e medicamentos pela equipe multidisciplinar:  RM > Cadastro > Estoque > Produto > Anexos: Informações - TOTVS Saúde > Identificação I > Tipo Item = Material > Identificação II >  Flag: Solicitação permitida pela equipe multidisciplinar.

Apartir da versão 2506, o sistema introduz a funcionalidade de **Produtos Associado e Produtos Composto** nas Solicitações de Material e Medicamento.

A funcionalidade opera da seguinte forma:

1. **Cadastro Base:** O item principal (Ex: Seringa) é configurado no Cadastro de Produtos para incluir itens associados obrigatórios podendo definir o fator de multiplicação.
2. **Inclusão na Solicitação:** O usuário insere apenas o produto principal (Ex: Seringa).

4. Impressão do relatório

## **04.** **IMPRESSÃO DO RELATÓRIO**

Para que o relatório da solicitação de materiais e medicamentos seja gerado no PEP, é necessário configurar no RM o respectivo relatório que será utilizado: **RM > Ambiente > Parâmetros > Gestão hospitalar > Relatórios > Relatórios 1/4 > Requisição: selecionar relatório > Avançar > Concluir.**
