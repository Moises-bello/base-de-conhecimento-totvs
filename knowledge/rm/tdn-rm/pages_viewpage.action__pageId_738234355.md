---
content_hash: 74296ebf9bda566155a200ec2eac8db06d979ef40b1fa158a5219edf75478c01
fetched_at: '2026-06-29T00:11:31.481456+00:00'
page_id: '738234355'
product: rm
source: tdn-rm
title: Passagem de plantão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=738234355
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Itens vinculados**
4. **Informações adicionais**

Passagem de plantãoVisão Geral

## **01. VISÃO GERAL**

Recurso que possibilita ao usuário o registro de passagens de plantão.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao clicar no menu de passagem de plantão, a tela será aberta com o histórico das passagens lançadas para o paciente selecionado.

Ao clicar em filtros avançados é possível visualizar as passagens por período e profissional.

Por padrão são exibidos os 100 últimos registros, mas é possível carregar mais registros caso seja necessário.

É possível expandir os itens para que sejam apresentadas as informações referentes.

Ao expandir são disponibilizadas as opções:

* Excluir, quando status rascunho;
* Suspender e Imprimir, quando status finalizado;

Ao clicar no botão "novo", será aberta a tela para registro nova passagem de plantão.

Neste momento caso já exista um rascunho ele será carregado, caso contrário um novo rascunho será criado. Ao criar uma nova passagem alguns campos serão preenchidos automaticamente:

* **Data de início**, preenchido com 12 horas antes a data e hora atual;
* **Data de término**, preenchido com a data e hora atual;
* **Situação**, preenchido com o valor da passagem anterior caso exista;
* **Histórico/antecedentes**, preenchido com o valor da passagem anterior caso exista;
* **Previsão de alta**, preenchido com o valor da passagem anterior caso exista;
* **Procedência**, preenchido com o valor da passagem anterior caso exista;
* **Respiração**, preenchido com o valor da passagem anterior caso exista;
* **Dispositivos,**preenchido com os dispositivos prescritos na prescrição médica dentro do período do plantão;
* **Dietas****,**preenchido com as dietas prescritas na prescrição médica dentro do período do plantão;
* **Antibióticos****,**preenchido com os antibióticos prescritos na prescrição médica dentro do período do plantão (necessário informar no cadastro de produto que ele se trata de um antibiótico);
* **Sedativos****,**preenchido com os sedativos prescritos na prescrição médica dentro do período do plantão (necessário informar no cadastro de produto que ele se trata de um sedativo);
* **Drogas****,**preenchido com as drogas prescritas na prescrição médica dentro do período do plantão (necessário informar no cadastro de produto que ele se trata de uma droga);
* **Resultados de exame****,**preenchido com os 18 últimos distintos resultados de exame dentro do período do plantão (necessário informar no cadastro de exame que ele pode ser apresentado na passagem de plantão);
* **Isolamentos****,**preenchido com os isolamentos ativos para o paciente dentro do período do plantão;

**OBS: Ao alterar o período de plantão os itens vinculados serão recarregados, excluindo e recriando todos os itens da passagem de plantão, por isso o período deve ser sempre alterado antes de tudo.**

A medida que o registro de passagem de plantão é alterado é realizado um salvamento automático, possibilitando assim que exista um status de rascunho, deixando então toda e qualquer alteração disponível no timeline mesmo que não tenha sido finalizada. Caso o registro esteja no estado de rascunho é possível realizar a exclusão deste.

Após preenchimento, basta clicar no botão de finalizar ou finalizar e imprimir, assim será redirecionado para o timeline de passagem de plantão.

Caso a unidade utilize a certificação digital, ao finalizar o registro será solicitada a senha e após isso a passagem será impressa e assinada digitalmente.

Itens vinculados

## **03. ITENS VINCULADOS**

Controlado por permissão, é possível realizar inserção, edição e exclusão de alguns itens vinculados a passagem de plantão, são eles Dispositivos, Culturas, Dietas, Antibióticos, Sedativos, Drogas e Isolamentos

1. Função de inserção;
2. Função de edição;
3. Função de exclusão

Informações adicionais

## **04. INFORMAÇÕES ADICIONAIS**

Para realizar a inserção de culturas é necessário que existam itens cadastrados;

RM > Saúde > Hospitais e Clínicas > Cadastros > Uso Geral > Outros cadastros > Tipos de cultura:

Para que ao realizar passagem de plantão os medicamentos prescritos sejam carregados da prescrição médica, os medicamentos devem estar devidamente cadastrados, sejam antibióticos, sedativos ou drogas: 

RM > Saúde > Hospitais e Clínicas > Cadastros > Estoque > Produto > Anexos > Informações TOTVS Saúde > Aba Identificação II

Para que os resultados de exames disponibilizados sejam exibidos no período do plantão o exame deve estar **marcado** com a opção "Mostrar resultado na passagem de plantão"   
e a opção "Utiliza Laudo Pré-impresso" deve estar **desmarcada**

RM > Saúde > Hospitais e Clínicas > Cadastros > Unidades de Diagnóstico > Exames e Serviços

O parâmetro de resultado de exame também **não** deve ter as opções Subtítulo, Espaço e Comentário;

RM > Saúde > Hospitais e Clínicas > Cadastros > Unidades de Diagnóstico > Métodos e Parâmetros de Exame > Parâmetros

Para que a informação do campo peso seja herdada dos controles de enfermagem antropometria, o item de enfermagem deve ser configurado como tal:

RM > Saúde > Hospitais e Clínicas > Cadastros > Cuidados com o paciente > Prescrição médica > Itens da enfermagem
