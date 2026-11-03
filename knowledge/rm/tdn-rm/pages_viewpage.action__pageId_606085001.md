---
content_hash: be99e67e14925912f27c4ede8f2bbd8a6fc345daa15c29a9ac542bd7a2c13a7c
fetched_at: '2026-06-29T00:10:58.364389+00:00'
page_id: '606085001'
product: rm
source: tdn-rm
title: Taxas e Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=606085001
version: 29
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Validações**
   1. **Caderno de Gabaritos**
3. **Cálculo do valor**
4. **Local de Uso**
5. **Regra Dentro/Fora da conta**
6. **Procedimento Vinculado**
7. **Divisão de lançamento**
8. **Tabelas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

A página de Taxas e Serviços serve para visualizar as taxas e ou serviços lançadas para o atendimento e para ser lançadas manualmente pelo faturamento.

Validações

## **02. VALIDAÇÕES**

* **Atendimento**
  + Deverá estar com o status diferente de "Cancelado"

* **Parcial**
  + Deverá estar com o status diferente de "Faturada", "Liberada" ou "Cancelada".
  + Não poderá ter nota fiscal emitida e o convênio particular.
* **Centro de custo**
  + Obrigatório se o parâmetro "Centro de Custo obrigatório nos lançamentos?" estiver marcado em Parâmetros Gerais > Faturamento II
  + Paciente interno
    - Matmed
      * Obrigatório se o parâmetro "Centro de Custo sem possibilidade de alteração" estiver marcado
    - Outros lançamentos
      * Obrigatório se o parâmetro "Centro de Custo vinculado ao leito sem possibilidade de alteração" estiver marcado
  + Paciente Externo
    - Obrigatório se o parâmetro "Centro de Custo vinculado a Estação de Trabalho sem possibilidade de alteração" estiver marcado
* Item estornado não pode ser alterado
* O item especial não pode ser alterado. Deve ser estornado e incluído novamente pela página Especial.
* O valor da taxa e serviço incluído deverá ser maior que 0.
* Caso o parâmetro (aba Eletrônico III - Tiss | Limita quantidade máxima definida pela TISS) nas condições contratuais esteja marcado, e a quantidade informada for maior ou igual a 1000, o sistema não permitirá salvar o registro.
* Data:
  + A data da taxa deve estar dentro do período da parcial
  + A data/hora de início não pode ser maior que a data/hora final
  + A hora não pode ser igual 24:00. Deve-se lançar com a hora igual a 00:00 e acrescentar 1 dia na data

### **02.1 Caderno de Gabaritos**

Ao salvar uma taxa ou serviço, o sistema verifica se existe um gabarito em aberto para a conta e se comporta de acordo com os parâmetros gerais:

* Se os parâmetros estiverem marcados: "Verificar existência de Gabarito ao incluir novo item - Elaboração de Contas"  e "Ação ao identificar Gabarito: Questionar inclusão no pacote". O sistema pede a confirmação do usuário para incluir a diária no pacote. Ou seja, a taxa será cobrada além do pacote.
* Se os parâmetros estiverem marcados: "Verificar existência de Gabarito ao incluir novo item - Elaboração de Contas"  e "Ação ao identificar Gabarito: Incluir automaticamente no pacote". O sistema não pede confirmação e incluirá a taxa automaticamente junto com o pacote.
* Caso não tenha um gabarito em aberto, a taxa não será cobrada
Cálculo do valor

## **03.** **CÁLCULO DE VALOR**

falseValorGeral

Para o sistema fazer o calculo de taxas ao lançar o item na elaboração de contas é necessário fazer a parametrização das tabelas de preço,  acesse o menu **Cadastro /** **Condições Contratuais.**

img: 1

Para acessar o cadastro de **Padrão de Faturamento e Codificação** que foi definido na tela anterior, clique no link em azul a direita do campo  **Padrão de Faturamento e Codificação** e será apresentada a tela abaixo**:**

img: 2

Para acessar o cadastro da **Tabela de Preço Usada** que foi definida no campo**"DTS - Diárias Taxas e Serviços"** na tela de **Condições Contratuais**, clique no link em azul a direita do campo  **DTS - Diárias Taxas e Serviços**e será apresentada a tela abaixo**:**

img: 3

**Configurando os valores de CH**

Acesse o menu Cadastros | Condição Financeira, será apresentado a **Visão do cadastro de Condições Financeiras:**

img: 4

Clicando sobre registro apresentado na tela anterior, será apresentado a tela de cadastro das **Condições Financeiras.**

img: 5

Clicando no menu **Anexos / Valores de CH/CO** da imagem anterior, será apresentada a visão do cadastro de **Valores de CH/CO**

img: 6

Clicando sobre registro apresentado na tela anterior, será apresentado a tela de cadastro  de **Valores de CH/CO.**

Neste exemplo abaixo estamos utilizando o **tipo CH/CO** como **especial**, desta forma estamos sendo mais especifico, ou seja, estamos indicando que esse cadastro será utilizado para fazer o calculo somente quando o item for do grupo de gasto de **TAXAS** e o código for "**60023139**". Está configuração pode ser mais genérica quando seleciona o **tipo CH/CO** como principal ou utiliza os campos de faixa inicial e final.

Para a **Condição Contratual** / **Condição Financeira / Unidade de Faturamento / Enfermaria / Taxas / item "60023139"**cada unidade **CH/CO** terá o valor de R$150,00.  

img: 7

**Configurando Tabela de preços utilizadas:**

Acessando Tabelas de Procedimentos e Serviços, acesse menu **Cadastro /  Outros Cadastros / Tabelas de Procedimentos e Serviços**

img: 8

Visão Cadastro de **Tabelas de Procedimentos e Serviços**:

Fizemos o filtro pelo o **código do item "60000422"**, este item está correlacionada ao **código de tabela "76"** que foi definido no campo **"DTS - Diárias Taxas e Serviços"** na tela de **Condições Contratuais conforme**apresentado na "img1" deste documento**.**

img: 9

Clicando sobre registro apresentado na tela anterior, será apresentado a tela de cadastro de **Tabelas de Procedimentos e Serviços**.

Com base nos dados preenchidos nos campos **Custo Operacional CH, Custo Operacional** que irá definir qual o valor vai ser utilizado para o calculo da taxa no momento do lançamento do item na elaboração de contas.

O sistema não permite preencher os dois campos **Custo Operacional CH, Custo Operacional,** ou seja, se o usuário preencher o campo **Custo Operacional CH** o sistema limpar o campo **Custo Operacional**e da mesmo forma ocorre quando é preenchido  **Custo Operacional,** o sistema limpa o campo **Custo Operacional CH.**

No campo **Custo Operacional CH** é informado a quantidade de CH quer será utilizado para fazer o calculo do valor do item, conforme exemplificação abaixo:

Custo Operacional CH = 10 (Definido na img10 abaixo)

Valor do CH/CO = R$150,00 (Definido na img7 deste documento)

Valor do Item = 10 \* 150,00 = R$1.500,00

img: 10

No campo **Custo Operacional R$**é definido o valor em moeda do item conforme apresentado na imagem abaixo:

img: 11

**Lançando um item de taxa na elaboração de contas com a configuração para utilizar CH/CO:**

Calculo do item da taxa:

Valor da unidade do CH/CO: R$150,00 (Definido na img 7 deste documento)

Custo operacional do CH/CO: 10 (Definido na img 10 deste documento, lembrando que o 10 é quantidade de CH/CO e não o valor em moeda)

Quantidade lançada : 1 (Na Aba de Taxas e Serviços / Elaboração de contas)

**Valor** =  1 \* (10 \* 150,00) = R$1.500,00

**Valor Total** = Quantidade lançada  \* Valor = R$1.500,00

img: 12

img: 13

**Lançando um item de taxa na elaboração de contas com a configuração para utilizar Tabela de Preço:**

Calculo de taxas:

Custo operacional : 17,87 (Definido na img 11 deste documento, esse valor é em moeda, ou seja, não tem conversão para **CH/CO**)

Quantidade lançada : 1 (Na Aba Taxas e Serviços / Elaboração de Contas)

**Valor** =  1 \* 17,87 = R$17,87

**Valor Total** = Quantidade lançada  \* Valor = R$17,87

img: 14

img: 15

IPSEMG e IAMSPE

Para esses convênios a regra para obter a tabela DTS é a mesma da regra geral. A diferença está na obtenção dos valores.

Acesse o menu Cadastros | Faturamento | Outros Cadastros | Tabela de procedimentos e serviços.

Filtre pelo código da tabela utilizada pelo convênio e selecione um item de taxas. Em Anexos, selecione a opção "IPSEMG/IAMSPE - Valores".

O sistema seleciona o valor de acordo com a vigência mais atual e o valor unitário da taxa corresponde ao campo Vlr. Total e o valor total corresponderá à quantidade de taxas multiplicado pelo valor unitário.

Local de Uso

## **04.** **LOCAL DE USO**

Existe uma parametrização nos parâmetros gerais

Ao realizar a definição desses parâmetros ao lançar uma taxa e serviço o sistema vai obrigar a informar o LOCAL DE USO , caso contrario vai surgir a mensagem: "Local de uso obrigatório."

Regra Dentro/Fora da conta

## **05.****REGRA DENTRO/FORA DA CONTA**

* Se no momento da inclusão da Taxa o usuário marcar a opção **Fora da Conta,** verificar o credenciamento do prestador junto ao convênio:
  + Se **Indireto:** gravar a coluna TAXAFORA com o valor FALSO
  + Se **Direto**: gravar VERDADEIRO.
* Se no momento da inclusão da Taxa a opção **Fora da Conta** desmarcada, gravar a coluna TAXAFORA com o valor FALSO
* Se o convênio for particular, sempre gravar na coluna TAXAFORA o valor FALSO.
Procedimento Vinculado

## **06. PROCEDIMENTOS VINCULADOS**

* Se nas condições contratuais, marcar o parâmetro “Lançamento automático de porte para procedimentos de mesma via e via diferente” e preencher o campo “Percentual”

* Se no momento da inclusão da Taxa o código da TAXA começar com “80.02” e estar dentro da faixa de Taxas e serviços, sendo assim o sistema vai habilitar a opção "PROCED VINCULADO"

Observações : Caso o procedimento vinculado tenha um porte associado dentro do cadastro de **procedimentos e serviços** o sistema vai surgir um alerta , dizendo que o porte e MAIOR ou MENOR, no caso de menor o sistema permite a inclusão na conta , diferente do Maior onde deve ser revisado o cadastro do procedimento e serviço não permitindo a inclusão.

Maior = Significa que o porte do Proc Vinculado e Maior que a Taxa principal

Menor = Significa que o porte do Proc Vinculado e Menor que a Taxa Principal

Segue a imagem exibida:

Divisão de lançamento

## **07.****DIVISÃO DE LANÇAMENTO PARA FATOR HORA OU MINUTO**

A divisão consiste em identificar lançamentos com fator igual a hora ou minuto, e que ultrapassem mais de 1 dia. Baseado nos campos de data/hora início e data/hora fim, o sistema calcula a quantidade de horas/minutos que devem ser lançadas por dia. Caso a quantidade total ultrapasse um dia, ele faz a quebra dos lançamentos por dia.

Unidades parametrizadas que são comparadas às unidades dos itens lançados.

Campo Fator que é considerado nos lançamentos.

Caso o item esteja na faixa de gasoterapia e tenha quantidade fracionada e o parâmetro de "Código de específico hora/fracionada (gasoterapia)" esteja informado, o sistema fará um novo lançamento somente com a parte fracionada.

Então, ao se lançar um item com fator hora, onde a data inicial seja 01/03/2021 01:30 e data final 03/03/2021 03:00, o sistema dividirá este lançamento da seguinte maneira:

* 01/03/2021 01:30 a 01/03/2021 02:00 e quantidade = 0,5
* 01/03/2021 02:00 a 02/03/2021 00:00 e quantidade = 22
* 02/03/2021 00:00 a 03/03/2021 00:00 e quantidade = 24
* 03/03/2021 00:00 a 03/03/2021 03:00 e quantidade = 3

## **08.****TABELAS UTILIZADAS**

* **SZATENDTAXASERV**
