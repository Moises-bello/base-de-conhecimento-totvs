---
content_hash: 878be9976c747f11fb49f831b23eac03d5308f128aa9b0f0db52b182f1fc85c5
fetched_at: '2026-06-29T00:10:57.892331+00:00'
page_id: '600301092'
product: rm
source: tdn-rm
title: Diárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=600301092
version: 38
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Validações**
   1. **Caderno de Gabaritos**
3. **Cálculo do valor**
4. **Local de Uso**
5. **Integrações**
6. **Tabelas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

A página de diárias serve para visualizar as diárias lançadas para o atendimento e para ser lançada manualmente pelo faturamento.

Se não estiver parametrizado o lançamento automático ou o lançamento da diária no encerramento do atendimento, o lançamento deverá ser manual.

Validações

## **02. Validações**

As seguintes validações são realizadas para incluir uma diária:

* Atendimento
  + Deverá estar com o status diferente de "Cancelado".
* Parcial
  + Deverá estar com o status diferente de "Faturada", "Liberada" ou "Cancelada".
  + Não poderá ter nota fiscal emitida e o convênio particular.
* Centro de custo
  + Obrigatório se o parâmetro "Centro de Custo obrigatório nos lançamentos?" estiver marcado em Parâmetros Gerais > Faturamento II
  + Paciente interno
    - Matmed
      * Obrigatório se o parâmetro "Centro de Custo sem possibilidade de alteração" estiver marcado
    - Outros lançamentos
      * Obrigatório se o parâmetro "Centro de Custo vinculado ao leito sem possibilidade de alteração" estiver marcado
  + Paciente Externo
    - Obrigatório se o parâmetro "Centro de Custo vinculado a Estação de Trabalho sem possibilidade de alteração" estiver marcado
* Item estornado não pode ser alterado
* O item especial não pode ser alterado. Deve ser estornado e incluído novamente pela página Especial
* Ao incluir uma diária, o sistema verifica se já existe a mesma diária lançada no mesmo dia. Caso exista, o usuário deve decidir se a mesma será salva ou não.

### **02.1 Caderno de Gabaritos**

Ao salvar uma diária, o sistema verifica se existe um gabarito em aberto para a conta e se comporta de acordo com os parâmetros gerais:

* Se os parâmetros estiverem marcados: "Verificar existência de Gabarito ao incluir novo item - Elaboração de Contas"  e "Ação ao identificar Gabarito: Questionar inclusão no pacote". O sistema pede a confirmação do usuário para incluir a diária no pacote. Ou seja, a diária será cobrada além do pacote.
* Se os parâmetros estiverem marcados: "Verificar existência de Gabarito ao incluir novo item - Elaboração de Contas"  e "Ação ao identificar Gabarito: Incluir automaticamente no pacote". O sistema não pede confirmação e incluirá a diária automaticamente junto com o pacote.
* Caso não tenha um gabarito em aberto, a diária não será cobrada

falseGabaritoParâmetrosPassos para associar um gabarito na conta

 

Cálculo do valor

# **03.** **Cálculo do valor**

falseValorRegra geral

Para o cálculo do valor da diária, o sistema segue a seguinte ordem de prioridade nas tabelas a consultar:

1. Tabelas de preços diferenciadas (se existir para o plano)
   1. Tabela especial
   2. Tabela DTS
2. Tabelas das condições contratuais
   1. Tabela especial
   2. Tabela DTS

Se não encontrar o item na tabela especial, o sistema procura na tabela DTS.

Caso haja diferença de honorário e a diária não seja coberta pelo plano, o sistema lança o código e descrição da diária utilizada do leito, com o valor da diária selecionada na alocação do leito.

Cálculo de Diferença de Diária para Gasto Particular

* **Registro de Atendimento**

No registro de atendimento é preenchido o campo "Responsável pela diferença da diária"

* **Condições Contratuais com Convênios**

Existe também uma parametrização nas condições contratuais do convênio, para gastos particulares.

* **Lançamento da Diária**

1. Ao incluir uma diária é verificado se existe um responsável pela diferença de diária.
2. Caso o responsável pela diferença de diária seja o **Paciente** ou o **Hospital**, será calculado o valor da diferença de acordo com a parametrização do convênio.
3. Caso exista uma tabela de gasto particular configurada nas condições contratuais do convênio deverá ser considero o valor do procedimento da tabela.
4. Caso o valor fixo de diferença de diária esteja preenchido este será considerado.
5. Após realizada as verificações o valor de um dos casos acima será considerado para o calculo da diferença e será inserido na aba de "Gastos Particulares". Este mesmo processo já insere o repasse quando parametrizado.

Caso haja algum prestador com repasse configurado para o centro de custo informado no lançamento da diária, o sistema também calculará o repasse dessa diferença de valor.

Informação

Para configurar o repasse por centro de custo, selecione o prestador no cadastro de prestadores, aba Repasse.

Marque as opções:

* Recebe repasse
* Repasse extra-honorários: Diárias
* Informe o centro de custo associado ao prestador. Todo lançamento para esse centro de custo, nos grupos selecionados, terão repasse
* Marque "**% Diária**" e informe o percentual . O repasse será calculado baseado neste percentual
IPSEMG e IAMSPE

Para esses convênios a regra para obter a tabela DTS é a mesma da regra geral. A diferença está na obtenção dos valores.

Acesse o menu Cadastros | Faturamento | Outros Cadastros | Tabela de procedimentos e serviços.

Filtre pelo código da tabela utilizada pelo convênio e selecione um item de diária. Em Anexos, selecione a opção "IPSEMG/IAMSPE - Valores".

O sistema seleciona o valor de acordo com a vigência mais atual e o valor unitário da diária corresponde ao campo Vlr. Total e o valor total corresponderá à quantidade de diárias multiplicado pelo valor unitário.

calcNegoDTSCalculo Negociação DTS

Aa regra para obter o valor da tabela DTS é a mesma da regra geral.

O valor será reajustado de acordo com a faixa de codificação determinada e o percentual de acréscimo para cobranças de diárias e ainda optar por discriminar como Acréscimo Contratual ou Reajuste na Tabela de Preços.

# 

Local de Uso

## **04.**

Existe também uma parametrização nos parâmetros gerais

Ao realizar a definição desses parâmetros ao lançar uma diária o sistema vai obrigar a informar o LOCAL DE USO , caso contrario vai surgir esta mensagem:

Integrações

## **05. Integrações**

falseIntegracoesCentral de Autorizações

Essa integração ocorre para convênios não sus e não particular e que estejam configurados nas Condições Contratuais | Parâmetros I | **Diárias OBRIGATORIAMENTE incluídas nas Guias/Autorizações de Internação**.

Ao se lançar uma diária com essas parametrizações, o sistema incluirá na Central de Autorizações, a diária requerida.

Validação para lançar na central de autorização:

* A quantidade de diária incluída + total de diárias já lançadas na conta do paciente deve ser menor que a quantidade de diárias autorizadas na Guia de Autorização do Atendimento + quantidade pendente na Central de Autorização

Caso exista alguma pendência associada ao tipo de documento Guia Hospital, o sistema cria um controle de documento e uma pendência associada.

 

## **06.** **TABELAS UTILIZADAS**

* **SZATENDDIARIAS**
* **SZATENDIMENTO**
* **SZPARCIALATEND**
* **SZPEDIDOATEND**
* **SZUNIDATEND**
