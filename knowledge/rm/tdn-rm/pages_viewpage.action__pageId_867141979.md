---
content_hash: 3c6b48e393ba05afb5d54fa96963ec7aecb62768deff588cb46ca1b09875a1e9
fetched_at: '2026-06-29T00:11:56.527225+00:00'
page_id: '867141979'
product: rm
source: tdn-rm
title: FOPTRP0015 - Relatório de Provisão de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867141979
version: 15
---

## 

## **CONTEÚDO**

1. **Versão**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Visão de Dados/Relatório**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizadas**

## **01. VERSÃO**

O Recurso estará disponível a partir do release 12.1.2410

## **02. VISÃO GERAL**

O objeto de negócios e relatório de provisão de férias tem como objetivo entregar para o usuário os valores calculados no processo de provisão e armazenados no histórico de provisão do funcionário, assim como retornar os valores de encargos de INSS e FGTS que serão calculados direito no objeto de negócios e ter em um único local todos os valores, para facilitar a conferência e envio do relatório para as partes interessadas.

A geração do relatório assim como na visão de dados poderão ser feitas utilizando parâmetros pré-definidos, como coligada, chapa, seção, mês/ano competência, sendo o mesmo gerado por competência.

O relatório ainda retorna no final um totalizador por seção.

Abaixo os campos disponíveis no objeto de negócios e as regras de como os dados são obtidos.

| Nome | Descrição | Campo na Tabela do RM |
| --- | --- | --- |
| Nome da Coligada | Retorna o nome fantasia da Coligada do funcionário | GCOLIGADA.NOMEFANTASIA |
| Código da Coligada | Retorna o código da coligada do funcionário. | PFHSTPROV.CODCOLIGADA |
| Estabelecimento | Retorna o nome fantasia da filial do funcionário | GFILIAL.NOMEFANTASIA |
| Código da Filial | retorna o código da filial do funcionário | PFUNC.CODFILIAL |
| Matrícula do Funcionário | Retorna a chapa do funcionário | PFHSTPROV.CHAPA |
| Nome do Funcionário | Retorna o nome do funcionário | PFUNC.NOME |
| Código da Seção | Retorna o código da seção. Este campo é usado como parâmetro podendo ser informado alguma quebra | PSECAO.CODIGO |
| Nome da Seção | Retorna o nome da seção. No relatório é retornado no totalizador de acordo com os funcionário lotados e não pela quebra informada | PSECAO.DESCRICAO |
| Mês de Referência | Retorna o mês da competência que será gerado retornado os dados. Este campo é obrigatório e só retorna uma competência por geração | PFHSTPROV.MES |
| Ano Referência | Retorna o ano da competência que será gerado retornado os dados. Este campo é obrigatório e só retorna uma competência por geração | PFHSTPROV.ANO |
| Salário do Funcionário | Retorna o Salário do funcionário da PFUNC. Não é retornado de acordo com o histórico salarial | PFUNC.SALARIO |
| Data de Admissão | Retorna a data de admissão do Funcionário. Para funcionários transferidos não será considerada a data de transferência como data de admissão | PFUNC.DATAADMISSAO |
| Data de Demissão | Retorna a data de demissão do funcionário | PFUNC.DATADEMISSAO |
| Mês Anterior | Retorna o valor provisionado no mês anterior a competência informada na geração  Exemplo: Provisão sendo gerada na competência 12/2024, este campo irá retornar o valor do campo PFHSTPROV.VALPROVFER da competência 11/2024 | PFHSTPROV.VALPROVFER |
| Valor com abatimento de Férias | Retorna o valor do campo PFHSTPROV.VALPROVCOMABATER da competência informada na geração | PFHSTPROV.VALPROVCOMABATFER |
| Valor sem abatimento de Férias | Retorna o valor do campo PFHSTPROV.VALPROVSEMABATER da competência informada na geração | PFHSTPROV.VALPROVSEMABATFER |
| Avos de Férias Vencidos | Retorna o valor do campo PFHSTPROV.NROAVOSVENCFERDEC da competência informada na geração | PFHSTPROV.NROAVOSVENCFERDEC |
| Avos de Férias proporcionais | Retorna o valor do campo PFHSTPROV.NROAVOSPROPORDEC da competência informada na geração | PFHSTPROV.NROAVOSPROPORCDEC |
| Valor Pago de Férias no mês | Retorna o valor do campo PFHSTPROV.VALPROVFERMES da competência informada na geração | PFHSTPROV.VALPROVFERMES |
| Férias Mensal | Irá retornar o valor Mensal provisionado da competência da geração. Este campo é calculado na geração dos dados da provisão e a regra para o cálculo do campo é: Valor provisionado no mês atual + valor férias pago no mês atual - valor provisionado no mês anterior  Exemplo: Provisão sendo gerada na competência 12/2024, irá retornar o valor do campo PFHSTPROV.VALPROVFER + PFHSTPROV.VALPROVFERMES da competência 12/2024 - PFHSTPROV.VALPROVFER da competência 11/2024 | Calculado |
| Férias em Dobro | Irá retornar o valor do campo PFHSTPROV.VALPROVFERDOBRO da competência informada na geração | PFHSTPROV.VALPROVFERDOBRO |
| Média de Férias Vencidas | Irá retornar o valor do campo PFHSTPROV.MEDIASFERVENC da competência informada na geração | PFHSTPROV.MEDIASFERVENC |
| Média de Férias proporcionais | Irá retornar o valor do campo PFHSTPROV.MEDIASFERPROP da competência informada na geração | PFHSTPROV.MEDIASFERPROP |
| INSS % Empresa | Irá retornar o percentual do INSS patronal referente a parte empresa. Este percentual será adquirido da seguinte forma:   * Caso o Parâmetro 'Habilita o histórico de INSS no Cadastro de Seção' esteja marcado, será considerado o valor do campo PSECAODADOSINSS.PERCENTEMPRESA dentro da vigência da competência informada na geração. * Caso no parâmetro esteja desmarcado, será considerado o percentual de 20% | PSECAODADOSINSS.PERCENTEMPRESA  Ou   20% (Fixo) |
| INSS % Acid. Trabalho | Irá retornar o percentual do INSS patronal referente o valor do percentual (Acidente de Trabalho \* Alíquota FAP).  Para o percentual de acidente de trabalho:   * Caso  o parâmetro 'Habilita o histórico de INSS no Cadastro de Seção' esteja marcado, iremos retornar o valor do Campo PSECAODADOSINSS.PERCENTACIDTRAB dentro da vigência da competência informada na geração. * Caso o parâmetro esteja desmarcado iremos retornar o valor do campo PSECAO.PERCENTACIDTRAB da seção de lotação do funcionário. Se não tiver informado irá retornar 0   Para Alíquota FAP:   * Iremos retornar o valor do campo PSECAOFAPALIQUOTA.VALOR do cadastro de FAP por Estabelecimento Empresarial cadastrado no anexo da Seção, dentro da vigência da competência informada na geração * Caso não exista valor cadastrado na tabela acima ou esteja fora da vigência, iremos retornar o valor da Tabela de valores fixos de finalidade Alíquota FAP (PVALFIX.FINALIDADE = 13), dentro da vigência da competência informada na geração.  Se a tabela de valores fixos estiver fora da vigência, irá retornar 0 | PSECAODADOSINSS.PERCENTACIDTRAB ou PSECAO.PERCENTACIDTRAB        PSECAOFAPALIQUOTA.VALOR ou PVALFIX.FINALIDADE = 13 |
| INSS % Terceiros | Irá retornar o percentual do INSS patronal referente o valor do percentual de terceiros.   * Caso  o parâmetro 'Habilita o histórico de INSS no Cadastro de Seção' esteja marcado, iremos retornar o valor do Campo PSECAODADOSINSS.PERCENTTERCEIROS, dentro da vigência da competência informada na geração * Caso o parâmetro esteja desmarcado, iremos retornar o valor do campo PSECAO.PERCENTTERCEIROS da seção de lotação do funcionário. Se não tiver informado irá retornar 0 | PSECAODADOSINSS.PERCENTTERCEIROS   ou  PSECAO.PERCENTTERCEIROS |
| Valor Encargo INSS | Este campo será calculado durante o processo de geração.  Irá retornar o valor calculado de recolhimento de INSS considerando a soma dos percentuais dos campos INSS % Empresa, INSS % Acid. Trabalho e INSS % Terceiros, multiplicado pelo valor do campo Férias mensal Exemplo: Férias mensal: 1056,05 x ((%Empresa) 20,00 + (%Acid. Trabalhdo x Aliquota FAP) 1,5 + (%Terceiros) 5,8) = 288,30 | Calculado |
| FGTS % | Irá retornar o percentual de FGTS do Colaborador:   * Para Funcionário menor aprendiz PFUNC.CODTIPO = Z irá retornar 2% * Demais tipos irá retornar 8% | Calculado |
| Valor Encargo FGTS | Irá retornar o valor calculado de recolhimento de FGTS considerando o percentual da regra 7 multiplicado pelo valor do campo Férias mensal  Exemplo: Férias mensal: 1056,05 x 8%= 84,48 | Calculado |

Observação

* Quando o parâmetro 'Habilita o histórico de INSS no Cadastro de Seção' estiver marcado, será considerado o registro do histórico de percentual para INSS da seção centralizadora do colaborador. Caso a base esteja configurada para usar a quebra de FPAS, será considerando os registro de histórico de percentuais para INSS conforme a quebra.

Exemplo

Quebra de FPAS informada: ?????

Funcionário alocado na seção 01.01.001, logo irá buscar a informação dos percentuais na seção 01.01, que a seção conforme a quebra

* Se não existir registro na seção conforme a quebra de FPAS configurada, será retornado as informações de percentuais de INSS da seção centralizadora.  A quebra de FPAS é configurada em 'Parametrizador | eSocial | Configurações Gerais | Lotação Tributária'
* Para Alíquota FAP sempre irá verificar a existência de registro na seção centralizadora, independe dos parâmetros marcados para 'Habilita o histórico de INSS no Cadastro de Seção' e/ou 'Utiliza quebra de FPAS'
Dica

Nem todos os campos do objeto de negócios serão utilizados ou visualizados no relatório disponibilizado pela TOTVS. Alguns campos servirão para parâmetros/filtros. Outros foram disponibilizados para facilitar para o usuário caso o mesmo queira customizar algum relatório com estes dados sem a necessidade de customizar por fórmulas por exemplo.

## **03. EXEMPLO DE UTILIZAÇÃO**

Visão de dados

Gerando a visão de dados utilizando o Objeto de Negócios disponibilizado que retorna os dados da provisão:

Retornou os dados conforme o filtro informado e os campos definidos no objeto de negócios

Relatório

Gerando o relatório utilizando o SmartView:

O Relatório não são retornados todos os dados do objeto de negócios e ele retorna um totalizador por seção:

## **04. TELA VISÃO DE DADOS/RELATÓRIO**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Cód. Coligada | Neste campo deverá informar uma ou mais coligadas, clicando em + e adicionando o código da coligada que deseja informar. Caso o usuário queira gerar para todas as coligadas, deverá informar -1 |
| Chapa do Funcionário | Neste campo deverá informar uma ou mais chapas de funcionários, clicando em + e adicionando as chapas que deseja retornar os dados referente a provisão. Caso o usuário queira gerar para todas as chapas, deverá informar -1 |
| Cód. Seção | Neste campo deverá informar uma ou mais seção, clicando em + e adicionando as seções que deseja retornar. É possível utilizar este campo para retornar as seções a partir de uma quebra, informando por exemplo 01., onde irá retornar todas as seções a partir desta quebra. Caso o usuário queira gerar para todas as chapas, deverá informar -1 |
| Mês | Neste campo deverá informar o mês da competência que deseja gerar os dados/relatório de provisão, sendo o mesmo obrigatório, não podendo informar mais de um mês competência e não é aceito informar -1 como os demais parâmetros |
| Ano | Neste campo deverá informar o ano da competência que deseja gerar os dados/relatório de provisão, sendo o mesmo obrigatório, não podendo informar mais de um ano competência e não é aceito informar -1 como os demais parâmetros |

## **05. TABELAS UTILIZADAS**

* PFHSTPROV
* PVALFIX
* PPARAMADICIONAIS
* PFUNC
* PSECAO
* PSECAODADOSINSS
* PSECAOFAPALIQUOTA
* GCOLIGADA
* GFILIAL
