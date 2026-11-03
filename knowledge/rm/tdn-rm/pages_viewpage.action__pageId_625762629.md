---
content_hash: 7c256159de68b26d045b7b1573a7de51a7035eac2e725ec3884e65015d534331
fetched_at: '2026-06-29T00:11:04.211108+00:00'
page_id: '625762629'
product: rm
source: tdn-rm
title: Restrições de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625762629
version: 14
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Proibido**
4. **Grátis**
5. **Particular**
6. **Liberado Parcialmente**
7. **Exige Liberação do Convênio**
8. **Exige Liberação do Responsável Financeiro**
9. **Tabelas Utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

As restrições estabelecidas nas Condições Contratuais são verificadas sempre que um item é lançado na parcial nas seguintes rotinas:

* Elaboração de Contas
* Agendamento de Atendimentos (Consulta/Exame)
* Agendamento Cirúrgico
* Movimentação Estoque
Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Esta tela permite a configuração de diversos filtros, garantindo que o item se enquadre em uma das restrições estabelecidas conforme as regras do Convênio.

O comportamento atribuído à restrição é determinado pelos seguintes tipos, que serão detalhados nesse documento.

Importante!

Os campos "Local de Uso" e "Quantidade" serão habilitados como filtros apenas quando o tipo selecionado for "Liberado Parcialmente".

Não é permitido utilizar os filtros de especialidade e faixas simultaneamente no mesmo cadastro, apenas um deles deve ser utilizado.

Proibido

## **03. PROIBIDO**

Ao tentar adicionar um item proibido na parcial, será exibida uma mensagem de aviso informando que o item não é permitido, e ele não será incluído.

Grátis

## **04. GRÁTIS**

Todo item classificado como **Grátis**, ao ser lançado na parcial da Conta, será automaticamente redirecionado para a aba "Itens Grátis". O lançamento original será estornado de forma automática, permanecendo visível na aba original para fins de conferência e rastreabilidade.

Particular

## **05. PARTICULAR**

Todo item classificado como **Particular**, ao ser lançado na rotina de Elaboração de Contas, será automaticamente redirecionado para a aba "**Gastos Part**". O lançamento original será estornado de forma automática, permanecendo visível na aba original para fins de conferência e rastreabilidade.

Liberado Parcialmente

## **06.** **LIBERADO PARCIALMENTE**

Importante!

Esse tipo de restrição se aplica exclusivamente a Materiais e Medicamentos.

Todo item classificado como **Liberado Parcialmente**, após ser lançado na rotina de Elaboração de Contas, ele será enviado para a Central de Autorização para que o setor realize a sua autorização junto a operadora. Somente após a autorização ser concedida, o item será adicionado à parcial.

Para esse tipo, o preenchimento do campo **Quantidade** é obrigatório. Opcionalmente, o filtro **Local de Uso** pode ser utilizado em conjunto.

### **RESTRIÇÃO POR LOCAL DE USO E QUANTIDADE**

É possível realizar a criação de regras para itens não cobertos pela operadora por item, quantidade e local de uso. É retirada automaticamente a quantidade excedente da conta ao encerrá-la.

1. 1. Acesse Cadastros \ Faturamento \ Condições Contratuais com Convênios.
   2. Em anexos clique em Restrições de Contrato.
   3. Clique em Incluir.
   4. Selecione no Tipo do Item “MATMED”, no Tipo de restrição “Liberado Parcialmente” e preencha o campo Quantidade.
   5. Acesse Faturamento \ Particular e Convênio \ Lançamento na Conta do Paciente.
   6. Efetue lançamentos na guia MatMed do produto configurado.
   7. Clique em Encerrar (caso a quantidade do item seja superior à configurada, será gerado mensagens de alerta).

Exige Liberação do Convênio

## **07.** **EXIGE LIBERAÇÃO DO CONVÊNIO**

Se o item estiver configurado para **Exigir Liberação do Convênio**, é necessário informar o percentual coberto pelo convênio ou o valor pago pelo paciente como gasto particular.

Caso o convênio cubra 100%, nenhum valor será gerado para o paciente.

Simultaneamente, será gerado um processo de mensagem, notificando os setores configurados sobre a restrição do atendimento. Além disso, o item será incluído na Central de Autorizações.

Exige Liberação do Responsável Financeiro

## **08.** **EXIGE LIBERAÇÃO DO RESPONSÁVEL FINANCEIRO**

Todo item configurado com esse tipo, ao ser lançado na rotina de **Elaboração de Contas**, será redirecionado para a aba '**Gastos Part**'. O lançamento original será estornado de forma automática, permanecendo visível na aba original para fins de conferência e rastreabilidade.

Simultaneamente, será gerado um processo de mensagem, notificando os setores configurados sobre a liberação necessária do responsável financeiro para o atendimento.

Tabelas Utilizadas

## **09. TABELAS UTILIZADAS**

* SZCONDCONTRATPROIBIDO
* SZATENDITEMGRATIS
* SZATENDSADT
* SZATENDHONORARIO
* SZATENDDIARIAS
* SZATENDTAXASERV
* SZATENDMATMED
* SZATENDGASTOPARTIC
