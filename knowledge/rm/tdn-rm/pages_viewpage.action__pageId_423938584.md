---
content_hash: 812312bab20533f35f884d235b02b6eef9fbba9c6151237ae3681bc05810a666
fetched_at: '2026-06-29T00:09:27.947678+00:00'
page_id: '423938584'
product: rm
source: tdn-rm
title: Mão-de-Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938584
version: 7
---

Através do cadastro de Mão de Obra é possível inserir e editar os dados referentes às mãos de obra necessárias para execução das ordens de serviços, bem como identificar através do Parque de Máquinas, quais os objetos foram instalados por tais mãos de obra.   
***Atenção!*** Estarão disponíveis para o cadastro de mão de obra, funcionários e/ou pessoas previamente cadastrados. Através do parâmetro "Listar Somente Funcionários" será possível listar somente pessoas cadastradas como funcionários ativos. O cadastro de Funcionários pode ser realizado no aplicativo RM Officina ou no RM Labore e o cadastro de Pessoas no RM Vitae.  
Caso a empresa não possua o aplicativo RM Vitae, somente funcionários estarão disponíveis para o cadastro de mãos-de-obra.  
Observação: Toda vez que for cadastrada uma nova mão-de-obra para uma determinada coligada, será dada ao usuário a opção de escolher em quais Tipos de Objetos de Manutenção este funcionário terá permissão para trabalhar. Será apresentada uma janela perguntando ao usuário se ele deseja associar a mão de obra a algum tipo de objeto. Caso a resposta seja sim, ele poderá escolher o(s) tipo(s) de objeto(s) que será(ao) associado(s) ao funcionário.  
Se for inserido um funcionário como mão de obra que esteje com status demitdo, a mesma não aparecerá para ser alocada no momento de alocar mão de obra na Ordem de Serviço.  
Dica: Caso o funcionário não possua serviço alocado, será apresentada a última data e hora de atualização (clicando no botão Atualiza Previsão de Disponibilidade). Caso o funcionário esteja executando algum serviço ou tenha serviços já alocados (o que é possível verificar em Mão-de-Obra | Cronograma Pessoal | Visão de Cronograma Pessoal), o campo apresentará data e hora em que o funcionário terminará o último serviço e poderá começar outro.

**Recalculo do Custo da Mão de Obra**

Esta funcionalidade permite recalcular o valor de um item da ordem de serviço de acordo com o valor do custo da mão de obra que esta alocada para ele.  
Para que essa funcionalidade possa ser acessada no sistema o usuário deverá marcar o parâmetro "Somar Custo da Mão de Obra ao Custo Financeiro da OS" em Opções | Parametros | Sistema | Aba – Ordem de serviço, ao marca-lo o botão Recalcular Custo será exibido na tela de visão da ordem de serviço.  
Para realizar o recalculo o usuário deverá clicar no botão "Recalcular Custo" e selecionar o serviço que se deseja realizar o recalculo. Ao finalizar o recalculo será exibido um log de atualização dentro da tela do WIZARD e os campos "Preço Unitário" e "Valor Total do item" que fica dentro do item da OS serão atualizados com o novos valores recalculados. Exemplo: Por exemplo, se para o serviço A houve apontamento da mão-de-obra H nos intervalos de 08:00 às 12:29 e 14:18 às 17:51, as horas efetivas dessa mão-de-obra no serviço A são 8 horas e 2 minutos. Logo, supondo que o custo/hora da mão-de-obra cadastrado para a mão de obra em questão é R$ 5,66, tem-se que 8,03 X 5,66 = R$45,45

Então R$ 45,45 (quarenta e cinco reais e quarenta e cinco centavos) será o valor adicionado ao preço unitário do serviço.  
Se o preço do serviço for R$ 15,00, o seu preço unitário será atualizado para R$ 60,45 pois será contabilizado a ele o preço do custo da mão de obra que foi de 8 horas.  
***Observação***: Ao final do processo de recalculo do custo será exibido um log de atualização dentro do WIZARD, esse log pode ser visualizado em bloco de notas clicando no botão "Bloco de notas".

---
