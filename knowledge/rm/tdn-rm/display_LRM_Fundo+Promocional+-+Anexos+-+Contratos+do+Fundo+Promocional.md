---
content_hash: b6266bb08adf2f39b0be71002d81844581ece3d4574d1d6d4d7a96613588e391
fetched_at: '2026-06-29T00:11:15.705896+00:00'
page_id: '661871027'
product: rm
source: tdn-rm
title: Fundo Promocional - Anexos - Contratos do Fundo Promocional
type: documentation
url: https://tdn.totvs.com/display/LRM/Fundo+Promocional+-+Anexos+-+Contratos+do+Fundo+Promocional
version: 23
---

**Introdução**

---

O anexo de contratos do fundo promocional possibilita a inserção de vários contratos de aluguel que terão eventos de fundo promocional gerados.

**Importante:**

Há algumas premissas para associarmos contratos de locação ao fundo promocional relacionadas aos locatários do contrato.  
O sistema irá emitir erro e não permitirá a inclusão caso o contrato não se encontre nas situações abaixo:

* **Contratos de locação com locatário cadastrado na mesma coligada do fundo promocional.**  
  Exemplo: Fundo promocional cadastrado na coligada 2, contrato de locação e locatários devem estar cadastrados também na coligada 2
* **Contratos de locação com locatário cadastrado na coligada global.**  
  Exemplo: Fundo promocional cadastrado na coligada 2, contrato de locação na coligada 1 e locatário marcado como global.

Para saber como cadastrar um [cliente/fornecedor global, clique aqui](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+receber)

**Outra informação importante é que não será possível associar o mesmo contrato de locação em diferentes cadastros de fundo promocional.**

**Procedimentos para utilização**

---

Neste anexo, iremos definir os seguintes parâmetros

* **Coligada:** Coligada do contrato de locação
* **Código do contrato de locação:** Código do contrato de locação
* **Locatário**: Somente visualização. É a identificação do Locatário responsável pelo Contrato de Locação. Será carregado automaticamente quando selecionado o contrato
* **Dia de Vencimento:** Dia de vencimento da parcela. O mês e o ano do vencimento da parcela do fundo será calculado a partir da mesma competência da parcela de locação.
* **Data de vigência do contrato:** Exibir a data de termino do contrato, indicando quando o mesmo finaliza
* **Valor:** Valor que deverá ser cobrado através de um evento de fundo promocional
* **Fórmula:** Valor que deverá ser cobrado através de um evento de fundo promocional (ao utilizar a formula o valor será bloqueado para alteração e ajustado automaticamente para zero). Sobre váriáveis de fórmulas acese: [Fórmula do Fundo Promocional](https://tdn.totvs.com/pages/viewpage.action?pageId=823802112)

Caso o contrato não possua Data de Vigência informada, será apresentado para o usuário no formulário a informação **"Contrato com prazo indeterminado"**

**Aba de Histórico de Valores**

---

Aba que irá mostrar todo o histórico de alterações de valores, inclusive valores reajustados \ editados.

**Processos > Alterar Situação do Fundo Promocional**

---

Esta opção permite alterar a situação de uma cobrança de fundo promocional, influenciando nas parcelas que serão geradas no lançamento financeiro.

**Ativar**: Essa situação tem a finalidade de ativar todo contrato de fundo promocional, permitindo a geração de lançamentos financeiros.   
Ao acessar a tela, a opção Ativar já encontra-se como Default ao incluir um contrato do Fundo Promocional, contudo, quando um Contrato está paralisado, a situação ativar permite a geração de lançamentos financeiros a partir da data que foi informada no campo "Data da Alteração";  
***OBS: Para acessar este menu, é necessário conceder permissão a esta opção no perfil deste usuário.***

**Paralisar:** Essa Situação permite paralisar todo contrato de fundo promocional que esteja com situação "Ativar", impedindo a geração de lançamentos financeiros à partir da data que foi informada no campo "Data da Alteração";

**Cancelar:** Essa situação permite cancelar todo contrato de fundo promocional que esteja com as situações "Ativar" e "Paralisar", impedindo a geração de lançamentos financeiros à partir da data que foi informada no campo "Data da Alteração". A partir do momento em que um contrato estiver com essa situação, não será possível alterar a opção para **"Ativar" ou "Paralisar"**.   
A situação **"Cancelada é irreversível"** e após  a alteração o fundo não poderá mais ser reativado.

Observação

* Sempre que for realizado a alteração da situação do contrato do fundo promocional será necessário gerar novamente os lançamentos financeiros; Afim de que sejam incluídas novas parcelas referente a data informada no campo "Data de alteração".

**Processos > Alterar dados do Fundo Promocional**

---

Este processo permite ao usuário informar um novo valor a partir da data de vigência indicada, alimentando assim o histórico dos valores de acordo com as datas. O objetivo do histórico é retornar o valor no período especificado. Na mesma tela, é possível informar um novo dia de vencimento. Após clicar em "Executar", essas alterações serão concretizadas e as novas parcelas geradas a partir do Fundo Promocional utilizarão essas informações parametrizadas.  
***OBS: Para acessar este menu, é necessário conceder permissão a esta opção no perfil deste usuário.***

Observação

* O novo valor será bloqueado para alteração e ajustado automaticamente para zero se a fórmula de cálculo do Fundo Promocional estiver sendo utilizada nas configurações do Contrato do Fundo Promocional.
