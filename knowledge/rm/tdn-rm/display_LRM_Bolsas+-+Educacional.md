---
content_hash: efcbd3903cfbf3f5b0537857688ee7eb5a03e80469d130dd98550237647cd9e8
fetched_at: '2026-06-29T00:09:35.967887+00:00'
page_id: '425459451'
product: rm
source: tdn-rm
title: Bolsas - Educacional
type: documentation
url: https://tdn.totvs.com/display/LRM/Bolsas+-+Educacional
version: 34
---

---

Bolsas são um tipo de benefício que a instituição de ensino tem a oferecer para os seus alunos. Cada instituição, conforme sua realidade, pode possuir diversas Bolsas com finalidades e maneiras distintas de cálculo e aplicação.

Além das Bolsas próprias que cada instituição de ensino pode utilizar para conceder descontos aos seus alunos, as instituições de ensino podem trabalhar também com '' onde o benefício concedido ao aluno é subsidiado por terceiros.

Neste cadastro são feitos os registros de todas as Bolsas que posteriormente poderão ser vinculadas aos alunos e utilizadas em seus contratos.

Somente as Bolsas cujo campo 'Bolsa ativa' esteja marcado ficarão disponíveis para utilização.

**Campos a serem preenchidos no cadastro da Bolsa:**

**Classificação:**  Este campo somente ficará disponível no cadastro de bolsa caso o parâmetro Aplicação de Bolsa esteja apontando para 'Classificação de Bolsa'. Este parâmetro está disponível em 'Ambiente| Parâmetros | Educacional | Integração | Financeiro | Fin – Geral 2/3 | Aplicação de Bolsa' e, caso esteja apontando para Contrato, a Classificação será definida dentro do contrato do aluno.

A Classificação refere-se ao *tipo* de bolsa e pode ser de 4 tipos:   
- Somar bolsas   
- Aplicar bolsas em cascata   
- Aplicar somente a maior bolsa   
- Exclusiva  
 **Tipo de Sacado:**   
- Nenhum   
- Responsável do aluno   
- Outro sacado  
  
Quando o tipo do sacado for = 'Nenhum', significa que o benefício da bolsa será concedido ao aluno em forma de desconto, havendo um abatimento sobre o valor de determinados serviços prestados.

Quando o tipo do sacado for = 'Responsável do aluno' ou 'Outro sacado' esta bolsa será tratada pelo sistema como uma '', onde o responsável do aluno ou o outro sacado passarão a ser responsáveis pelo valor do benefício concedido ao aluno.

**Tipo de desconto:**  Os descontos concedidos pelas bolsas podem ser calculados conforme um Percentual ou um Valor fixo aqui informado. A quantidade de casas decimais utilizadas neste campo obedecerá a quantidade de casas decimais definida no TOTVS Gestão Financeira. Se o tipo de desconto for indicado em *Percentual*, a quantidade de casas decimais utilizadas na digitação irá respeitar a quantidade de casas decimais definida no parâmetro do sistema financeiro "Nº Decimais Percentual". Se o tipo de desconto for indicado por *Valor*, a quantidade de casas decimais utilizadas na digitação irá respeitar a quantidade de casas decimais definida no parâmetro do sistema financeiro "Nº Casas Decimais". A utilização de casas decimais nos processos disponíveis no sistema que utilizam Bolsa também respeitarão estes parâmetros do sistema financeiro.

**Bolsa incondicional:**Este campo, por default, se apresenta *marcado*. Se desmarcado indica que a instituição trabalha com Bolsas condicionais ou escalonamento de bolsa e automaticamente é liberado neste mesmo cadastro o campo '*Ordem de perda*', para que seja informada a ordem em que serão retirados os benefícios. Os locais onde o sistema armazenará os valores dos descontos das bolsas, sejam eles incondicionais ou condicionais, são criados no TOTVS Gestão Financeira e depois devem ser indicados nos parâmetros do sistema Educacional.   
As Bolsas Incondicional que estiver associada a um contrato que possui contabilização, não será possível desmarcar no cadastro o parâmetro "bolsa incondicional".

**FIES:**O Fundo de Financiamento Estudantil (FIES) é um programa do governo federal criado em 1999, com o objetivo de financiar cursos superiores em instituições privadas para estudantes de baixa renda. **Este campo tem por objetivo identificar se a bolsa é referente a FIES ou NOVO FIES.**

* **FIES**: O período de carência é de 18 meses após a formatura antes do início do pagamento e o pagamento da dívida é feito diretamente pelo estudante ao governo.

Exibição dos Boletos no Extrato Financeiro: Para o FIES a exibição dos boletos do aluno no Extrato Financeiro, seguem as regras gerais de Bolsa de Crédito: Se o parâmetro Exibir lançamentos de bolsa de crédito` estiver marcado os boletos são exibidos, se estiver desmarcados eles não são exibidos.  [RM Portal - Parâmetros Extrato Financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=425458882)

* **Novo FIES:** Criou diferentes modalidades de financiamento, com taxas de juros zero para estudantes de baixa renda (Modalidade 1) e taxas variáveis conforme o banco financiador (Modalidades 2 e 3). O pagamento começa ainda durante o curso, com valores proporcionais à renda do estudante. Possibilidade de financiamento por meio de bancos privados e regionais, não apenas pelo governo.

Exibição dos Boletos no Extrato Financeiro:: Quando os boletos forem de bolsas do Novo FIES não serão apresentados os boletos do aluno e nem do outro sacado (Banco Financiador), isso acontece pelo fato do Novo FIES o aluno fará o pagamento da mensalidade para a Banco e essa fará o repasse para Instituição de Ensino. [Extrato Financeiro do Aluno](https://tdn.totvs.com/display/LRM/Extrato+Financeiro+Aluno)

**Permite alterar valor:**Se marcado indica que o valor ou o percentual definido para o desconto poderá ser manipulado pelo usuário no momento da utilização da bolsa dentro do próprio contrato do aluno ou diretamente nos processos que atribuem bolsas aos alunos. Caso esteja desmarcado a alteração do valor ou o percentual definido para o desconto somente poderá ser realizada dentro do próprio cadastro da bolsa.

**Bolsa Funcionário:** Caso selecione a opção 'Não' indica que a bolsa cadastrada será válida para todos os alunos, ou então somente será válida para Funcionários ou Filhos de funcionários que estejam admitidos na instituição de ensino na 'Coligada corrente' ou em 'Todas as coligadas'. Estas duas últimas opções funcionam quando integrado com o sistema de Recursos Humanos.

**Default contábil:** Defaults contábeis são as indicações das contas contábeis que poderão ser utilizadas na realização da contabilização dos contratos e parcelas conforme definido nos eventos contábeis utilizados para este fim. As permissões de incluir, editar e excluir defaults contábeis estão relacionadas à permissão de edição da bolsa, ou seja, se o usuário não tiver permissão para editar a bolsa, também não conseguirá incluir, editar ou excluir algum default contábil embora consiga visualizá-lo.

**Tipo contábil do lançamento do outro sacado:** Se o campo “Tipo de sacado” for igual a “Outro sacado” será habilitado o campo “Tipo contábil do lançamento do outro sacado” que permite definir qual é o tipo contábil do lançamento da bolsa de crédito que será gerado juntamente com o lançamento do aluno, para mais detalhes, 

**Compõe contabilização por competência:**Somente as bolsas, presentes nos contratos dos alunos, que tiverem esta opção **marcada** serão consideradas na realização da contabilização dos contratos através do regime de competência. As bolsas que tiverem esta opção **desmarcada** serão desconsideradas de todos os cálculos e lançamentos contábeis realizados através do regime de competência.

**Aplicar desconto por antecipação:**Possibilita que o cálculo do  seja aplicado antes ou depois do cálculo de uma determinada bolsa vinculada ao contrato do aluno. Saiba mais acessando o documento técnico na guia "Ordem de Aplicação do desconto por Antecipação" na seção ['Cadastro de Bolsas'](http://tdn.totvs.com/pages/releaseview.action?pageId=325847718).

**Afeta base de cálculo:**Possibilita se a base de cálculo para as bolsas e para o desconto por antecipação vinculados ao contrato serão afetados durante o seus processamentos de cálculos pelo sistema. Fica visível somente se o campo "Aplicar desconto por antecipação" estiver configurado para depois do cálculo da bolsa.

**Customização de tipo de desconto por fórmula:** Possibilita vincular fórmulas para obter o valor do tipo de desconto (percentual ou/e valor) da bolsa conforme as regras específicas do cliente. [Saiba mais](http://tdn.totvs.com/pages/viewpage.action?pageId=354469739) 

**Verifica inadimplência do outro sacado:** Possibilita considerar os débitos de outro sacado, em casos de bolsa de crédito de outro sacado.  

**Aba “Contabilização”**A aba contabilização será habilitada quando o TOTVS Educacional estiver parametrizado para utilizar a contabilização por competência e estiver utilizando o modelo de contabilização revitalizado. Poderá ser definido um período de competência contábil default para bolsa.

**Atenção:** Esta informação é apenas um default que será considerado ao adicionar a bolsa no contrato do aluno, ou seja, automaticamente o sistema vai preencher a competência contábil na bolsa do aluno com a competência informada nesta aba.

Para saber sobre o comportamento desta informação na contabilização  [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=425458834)

**Campos Complementares**É possível cadastrar [campos complementares para a bolsa](http://tdn.totvs.com/display/LRM/DEDUINTEGRACOES-2437+DT+Campo+Complementar+Cadastro+Bolsa) caso o cliente tenha uma informação que julgue importante, sendo que está informação é apenas utilizada pela sua Instituição de Ensino.

**Nos Anexo do cadastro de Bolsa estão disponíveis os seguintes cadastros:**

1. **Dados da Bolsa para o Censo Escolar**: Possibilita que o usuário informe a origem dos recursos para o financiamento da bolsa seja por Financiamentos Reembolsáveis e/ou Financiamentos não Reembolsáveis;
2. **[Bolsas por Período Letivo](https://tdn.totvs.com/display/LRM/Bolsa+por+Periodo+Letivo)**: A bolsa somente poderá ser utilizada pelo usuário nos Períodos Letivos aqui informados;
3. **Bolsa por Filial**: Na geração da Nota Fiscal de Serviço, os descontos concedidos pelas bolsas possuem tratamento diferentes, por tanto, neste anexo deve ser cadastrado o tipo de desconto que a bolsa irá conceder para cada Filial, para que este receba tratamento correto no momento da geração do movimento. Só serão exibidas as filiais pertencentes à coligada do contexto que o usuário está logado.

   Caso exista algum movimento gerado para a bolsa daquela filial esse cadastro não poderá ser alterado no respectivo contexto.

  Informações Complementares 

---

[Documento Técnico - Conceito e Aplicação de Bolsas Condicionai](http://tdn.totvs.com/display/LRM/TVBWZB_DT_Conceito_E_Aplicacao_De_Bolsas)[s](http://tdn.totvs.com/display/LRM/TVBWZB_DT_Conceito_E_Aplicacao_De_Bolsas)

 Veja Também

---

Bolsas de Crédito  
[Classificação de bolsas](http://tdn.totvs.com/pages/viewpage.action?pageId=425459113)  
Concessão de bolsas futuras  
Assistente de concessão de bolsa futura  
Conceder bolsas para irmãos  
Desconto por Antecipação na Bolsa  
[Visão Geral dos processos WebSevices de Bolsas](http://tdn.totvs.com/display/LRM/Bolsas)   
[Fórmula visual para concessão de bolsa](https://tdn.totvs.com/pages/viewpage.action?pageId=425458885)

  Como Fazer

---

[Associação de desconto por antecipação à bolsas](http://tdn.totvs.com/pages/viewpage.action?pageId=425459039)

  Recursos Adicionais

---
