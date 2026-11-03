---
content_hash: 44e25273505790061df6155513fc22e390b83c41a8e8afe00eba66cae0f7fc63
fetched_at: '2026-06-29T00:11:06.884028+00:00'
page_id: '635984573'
product: rm
source: tdn-rm
title: Controle de Recebimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+de+Recebimentos
version: 10
---

InformaçãoImportante ressaltar que essa rotina não é uma etapa obrigatória no sistema, algum clientes optam em realizar o controle do recebimento diretamente no BackOffice.

**01. VISÃO GERAL**

Com esta funcionalidade, é possível realizar o controle dos **valores a receber**, dos **valores glosados**, dos **valores considerados como perda**, **recebidos a maior** ou com **descontos** dentro de uma fatura gerada a partir de uma remessa.

## **02.****INTEGRAÇÃO**

Essa rotina possui uma integração onde cada lançamento realizado será sincronizado com o BackOffice.

A integração ocorre tanto para os lançamentos de baixa parcial ou integral do respectivo lançamento.

Importante salientar é que a integração **ocorre somente em um sentido**, no caso do RM Gestão Hospitalar para o BackOffice.

Para que a integração ocorra, é pré-requisito que a rotina de Geração Movimento Fatura esteja realizada, dessa forma os dados da remessa já estarão no BackOffice provisionados.

Para habilitar a integração, acessar no menu Opções > Parâmetros > Integração e na aba Controle de Recebimentos marcar o parâmetro conforme imagem abaixo.

Caso o parâmetro estiver desligado, os dados só ficam registrados nas tabelas do TOTVS Gestão Hospitalar.

## **03. EXEMPLO DE UTILIZAÇÃO**

* Para realizar o recebimento de uma determinada fatura, acesse o menu Tesouraria | Controle de Recebimentos.
* Filtre a fatura pelo convênio e número.
* Na grid serão listadas todas as faturas de acordo com o filtro selecionado.
* Na tela de edição da fatura serão exibidos campos totalizadores do que já foi registrado
  + O campo Ref. Lançamento corresponde ao identificador do lançamento financeiro.
  + Na aba Recebimentos são listados todos os recebimentos realizados para a fatura em questão

### **03.01 RECEBIMENTO POR CONTA**

* Clique no botão Incluir
* Selecione o paciente desejado
  + Após selecionado, o sistema já preenche o campo Valor Recebido, com o valor a receber. Caso não seja o valor exato, deve-se alterar para o valore realmente recebido. Os demais campos devem ser preenchidos quando fizerem sentido.
  + No exemplo abaixo, o valor original seria 36,00, porém foi recebido 1,00 a mais. Para registrar os valores corretos, deve-se informar que foi recebido 37,00 e 1,00 como sendo o valor a maior. Assim o sistema sabe separadamente o que é valor a maior, o que é perda e desconto.
* Após preencher o campos obrigatórios e caso o parâmetro de "Gerar baixa no BackOffice ao realizar o controle de recebimento" esteja marcado, e a fatura tenha gerado um lançamento financeiro; o sistema fará a baixa deste recebimento.

Campos para integração com o BackOffice

### **03.02 RECEBIMENTO POR REMESSA**

No recebimento por remessa, basta não informar nenhum atendimento de paciente da fatura.

Em seguida informar os valores recebidos, a forma de recebimento, a data. Caso esteja integrado, informar os campos para realizar a baixa.

### **03.02 CANCELAMENTO DO RECEBIMENTO**

* Selecione o recebimento que quer cancelar (selecione apenas 1 único registro)
* Selecione o processo "Cancelar Recebimento"
* Execute o processo
* O sistema irá mudar o status para **Cancelado** e caso esteja integrado com o BackOffice, a baixa será cancelada.

## **04.****TABELAS UTILIZADAS**

* SZFATURACONVENIO
* SZCONTROLRECEB
