---
content_hash: 5ce85574742a648161a1737c73129eda33e07f52b5548e27711fa7c67a7b75b3
fetched_at: '2026-06-29T00:10:43.678798+00:00'
page_id: '550325241'
product: rm
source: tdn-rm
title: Ajuste de Dependentes Salário Família
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550325241
version: 27
---

## **ÍNDICE**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01.****VERSÕES**

* 12.1.25.283
* 12.1.26.230
* 12.1.27.194
* 12.1.28.122

## **02.****VISÃO GERAL**

Esse processo irá ajustar o número de Dependentes com direito a Salário Família afetados pela inconsistência encontrada nas versões expedidas a partir do dia 24/04/2020. O ajuste ocorrerão nos processos:

* Liberação de Competência
* Cadastrar um novo Dependente
* Realizar a importação de Dados do RM Labore
* Cadastrar um novo funcionário, sendo para uma pessoa já existente na base e foi realizada a opção de Copiar os Dados do Dependentes.

IMPORTANTE

* Essa situação não teve impacto no cálculo da folha de pagamento, somente em relatórios. O cálculo da folha não utiliza o histórico de dependente de salário família.

A inconsistência na atualização do número dependente com salário família ocorreu somente quando o dependente tem o grau de parentesco "1-Filho Valido" ou "M-Menor Pobre". Para estes casos, o sistema passou a somar todos os dependentes com os graus de parentesco citado acima, ignorando as validações de idade, entregou cartão de vacina ou frequência escolar.

PARA:  Para realizar os ajustes nesses dependentes, foi criado o processo de **Ajuste de Dependentes Salário Família.** Este processo irá:

* Buscar no histórico de dependentes os registros com data de mudança (PFHSTNDP.DTMUDANCA) entre o período informado na tela. Irá percorrer cada registro encontrado e realizar a soma de Nro. Depend. Salário Família quem teria direito na data de mudança encontrada e na data de criação do Dependente (PFDEPEND.RECCREATEDON).
* Irá validar se o Nro. Depend. Sal. Família do cadastro do Histórico é diferente do valor encontrado conforme citado acima, se sim, o sistema irá atualizar o histórico.
* Irá validar se o Nro. Depend. Sal. Família do cadastro do Funcionário é diferente do Nro. Depend. Sal. Família com a maior data no histórico de dependente, se sim, irá atualizar o cadastro do funcionário.

Caso atenda as condições acima, será atualizado o cadastro do funcionário, assim como o registro no histórico de dependente de forma automática e apresentado o log no final do processo com todas as chapas e data de mudança que tiveram alteração.

**OBSERVAÇÃO:**

* O processo irá realizar a alteração no cadastro de funcionário sendo: campo "Nro. Depend. Sal. Família" (campo PFUNC: NRODEPSALFAM)
* O processo irá realizar a alteração no Históricos de Dependentes sendo: ("Nro. Depend. Sal. Família" (campo PFHSTNDP: NRODEPENDSALFAM)

## **03. EXEMPLO DE UTILIZAÇÃO**

1true2ParametrizaçãoParametrização

Acesse o menu Serviços Globais | Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso ao grupo **11.09 Ajustes**

3Ajustes de Dependentes Salário Família23-1Processo

Acesse o menu RH | Folha de Pagamento | Configurações | Ajustes | Ajuste de Dependentes Salário Família

Informe o período de meses para realizar o processo; Clique em avançar.

Importante

Somente será permitido executar esse processo e realizar as alterações para os registros encontrados entre 04/2020 a 06/2020. Pois conforme verificado esse foi o período onde gerou a inconsistência na base.

Ao clicar em Avançar, é realizado a validação internamente e retornado o Log com todas as chapas que tiveram a alteração do Nro. Dependente Salário Família.

## **04. TABELAS UTILIZADAS**

* PFUNC, PFHSTNDP.

]]>
