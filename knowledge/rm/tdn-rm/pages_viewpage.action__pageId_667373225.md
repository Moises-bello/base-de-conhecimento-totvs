---
content_hash: 0ce8a9a2fea1c3344b451b24bf6a526da3f6de642eae2d9f9740555c3bff9036
fetched_at: '2026-06-29T00:11:16.397649+00:00'
page_id: '667373225'
product: rm
source: tdn-rm
title: Readmissão de Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=667373225
version: 24
---

1. **Versões**
2. **Visão Geral**
3. **Exemplo de Utilização**
4. **Parametrização**

## **01.****VERSÕES**

* 12.1.33.232
* 12.1.34.140
* ou superiores.

## **02. VISÃO GERAL**

Realiza a admissão de funcionários reaproveitando os dados dos registros anteriores existentes na base de dados, possibilitando também trazer os dados dos campos complementares e/ou informar campos defaults.

        Essa necessidade é bastante comum em empresas que contratam para safra.

## **03. EXEMPLO DE UTILIZAÇÃO**

O funcionário foi contratado por 3 meses e foi demitido, depois de algum tempo, a empresa precisa contratá-lo novamente para outra safra.

## **04. PARAMETRIZAÇÃO**

11ParametrizaçãoParametrização

Acesse o menu Serviços Globais | Segurança | Perfis, selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso [] - Administração de Pessoal: Readmissão de Funcionários.

2Readmissão de Funcionários Data de admissão mês atual

 Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Cadastros | Readmissão de Funcionários

## **TELAS DA READMISSÃO DE FUNCIONÁRIOS**

**Tela de Gravação de Perfil**

**Tela Seleção de Funcionários | Valores Default**

Nessa etapa temos a disposição o filtro de seleção para criar coleções com os funcionários que serão readmitidos.

Os valores default são informações que, quando preenchidas serão utilizadas para todos os funcionários da seleção, sobrepondo os dados do funcionário origem (funcionário da admissão anterior).

*Exemplo:*

*Foram selecionados 30 funcionários para a readmissão e a data de admissão será igual para todos. Assim, para não ter que preencher a data de um por um, basta preencher o campo "Data Admissão" da aba Valores Default que a mesma será atribuída para todos os funcionários da seleção.*

Os dados desses campos poderão ser salvos no perfil, exceto a aba dos Campos Complementares Default.

**Dados do Contrato Default**

Sobrepõe os dados do funcionário origem e poderão ser salvos no perfil.

**Campos Complementares Default**

Os campos complementares sobrepõe os dados do funcionário origem, mas, não são salvos no perfil, pois, são carregados com os valores default preenchido na criação do campo.

Criação do campo complementar.

Dado carregado no processo de readmissão.

**Lista de Funcionários Selecionados**

Nessa etapa temos a lista com os funcionários que foram selecionados através do filtro na etapa anterior.

Ao selecionar um funcionário na lista, seus dados serão exibidos ao lado e esses dados são os mesmos dados do funcionário origem, caso não tenham sido preenchidos os campos de valores default. No entanto, todos os dados dessa etapa poderão ser alterados.

Importante!

ATENÇÃO:

Todas as alterações realizadas nessa etapa serão perdidas caso retorne para etapa anterior.

**Consulta na lista**

É possível consultar um funcionário específico na lista. Para isso, basta inserir a chapa do funcionário que a seleção será posicionada e seus dados serão exibidos, conforme demonstrado abaixo:

**Tela de exibição de resultados do processo**

Após avançar, os resultados do processo serão exibidos.

**Utilizando fórmulas de validação e bloqueio no processo de readmissão**

Folha de Pagamento | Funcionário | Restrições Cadastrais.

No processo de readmissão é possível a utilização das fórmulas:

* **FÓRMULA PARA CRITICAR O CADASTROS DE FUNCIONÁRIO**  
  Essa fórmula não impedirá a efetivação do funcionário, apenas emitirá um aviso no log de acordo com os critérios da fórmula implementada.

* **FÓRMULA PARA VALIDAR READMISSÃO**  
  Essa fórmula impedirá a readmissão do funcionário. No log será registrado a chapa do funcionário bloqueado e o retorno da fórmula utilizada.

Assim que o processo for finalizado, será sinalizado no log a quantidade de registros que foram bloqueados pela fórmula utilizada.

Log com o retorno das formulas:

## **05.TABELAS UTILIZADAS**

PFHSTCPGTO, PFHSTFCO, PFHSTHOR, PHSTOCORRENCIA, PFHSTSAL, PFHSTSEC, PFHSTSIT ,PFHSTTIPOREGIMEJORNADA, PFUFERIAS, PFUNCPFCOMPL ,PFDEPEND,PFCODFIX,PFUNCPFCOMPL,, PFDEPEND,PFCODFIX,
