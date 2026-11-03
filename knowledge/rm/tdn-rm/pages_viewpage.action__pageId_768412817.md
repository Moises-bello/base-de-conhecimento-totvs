---
content_hash: 1cfbf1c641413ed63b03d402122aca34f380075d356432e09d006f8e4ef7757b
fetched_at: '2026-06-29T00:11:35.901387+00:00'
page_id: '768412817'
product: rm
source: tdn-rm
title: Apuração de Plantões Realizados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=768412817
version: 22
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Configuração**
3. **Exemplo de Utilização**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Nesta Funcionalidade, será apurado o plantão do prestador por período.

## **02.  CONFIGURAÇÃO**

Essa rotina é acessada através do menu Faturamento > Apuração de Plantões Realizados

Para apurar um plantão é necessário que ele seja configurado:

* + Criar uma regra de plantão através do menu: Cadastro=>Faturamento => Regra de Plantão

Após criar regra é necessário criar  valores para regras de plantão,  sendo obrigatório a data de vigência. Os campos são :

* + - * Vigência
      * Aplicar regra de bônus por hora
      * Valor Fixo: é o valor a ser aplicado por hora trabalhada durante o plantão
      * Valor Sobre aviso: é o valor a ser aplicado por hora trabalhada durante o sobreaviso.
      * Valor Hora adicional
      * Especialidade
      * Prestador
* + Valores da Regra de Plantão

* Durante a apuração dos plantões, será considerado o Valor Fixo para as horas trabalhadas dentro do período de início e fim definido na regra de plantões. Já as horas trabalhadas além do término desse período serão calculadas com base no Valor da Hora Adicional para fins de apuração.

                      Exemplo:

* Aplicar regra de bônus / hr - Ao ativar essa configuração, será necessário definir a vigência e o percentual de acréscimo no Cadastro => Faturamento => Adicional por Volume de Horas. Ao realizar o processo de apuração, automaticamente será gerado um movimento na folha de pagamento de prestadores aplicando o percentual de acréscimo cadastrado para cada período trabalhado no plantão.
* + Para cadastrar um prestador sobre aviso entre no menu: Cadastro => Faturamento=> Cadastro Sobre aviso

Todos os campos abaixo são obrigatórios

## 

Feito o cadastro é necessário criar um registro de plantão de acordo com os dados cadastrados.

* + Atendimento => Pronto atendimento => Registro de plantão

Sendo obrigatórios data do plantão, horário de inicio e fim de plantão, unidade de atendimento, médico e especialidade.

O **"plantão cinderela"** no ambiente hospitalar refere-se a um regime de trabalho com duração reduzida, geralmente no período noturno.

## **03.****EXEMPLO DE UTILIZAÇÃO**

* Cadastro de plantões

Essa rotina é acessada através do menu Atendimento>Pronto Atendimento> Registro de Plantão

* Processo para Alteração de Data de Plantões cadastrados

Este processo permite a alteração da data de plantões selecionados na visão de Alteração de Plantão.

* Apuração de Plantões Realizados

Essa rotina é acessada através do menu Faturamento > Apuração de Plantões Realizados

* Incluir apuração

Deverá ser preenchido o período do movimento e o prestador, neste momento a situação ficará como não processado.

## 

* Processo de criação do período de movimento de plantão automatizado
* Em processos teremos as ações abaixo:
  + Realizar apuração

## 

Neste processo serão verificados  as regras de bônus e incluídas na folha de pagamento

* + - Se existir cadastro de sobreaviso para o prestador, ele será aplicado
    - Senão será verificado a regra do bônus para o valor fixo
    - Será inserido um movimento de plantão.

Após o processamento será possível verificar lançamento em:

Faturamento =>Gestão de Repasse=>  Crédito/Débito/Desconto

* + Liberar apuração

Neste processo será liberado o plantão para repasse.

## 

Após liberação será possível verificar lançamento em:

Faturamento - Folha de pagamento dos prestadores - Aba: Liberado para pagamento

1. * Retornar apuração
2. Neste processo será retornado para não processado o plantão.
   1. ##
3. * Cancelar apuração

O processo de cancelamento do plantão será possível se o item não estiver sido lançado na folha de pagamento.

## 

## **04. TABELAS UTILIZADAS**

* SZPLANTAOBONUS
* SZPLANTAODETALHES
* SZPLANTAOPERIODO
* SZREGRAPLTVAL
* SZREGRAPLTADIC
* SZREGRAPLTSOBAVISO
* SZREGRAPLT
* SZFOLHAPRODPREST
* SZFOLHAPAGTOPREST
