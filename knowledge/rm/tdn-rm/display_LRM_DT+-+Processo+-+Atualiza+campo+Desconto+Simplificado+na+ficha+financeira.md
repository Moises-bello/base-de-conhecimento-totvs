---
content_hash: b42668b5f88a17bf1dafc143151d0a750b11f6024d59e0d822b27bc8f3dd74eb
fetched_at: '2026-06-29T00:11:48.822791+00:00'
page_id: '828412897'
product: rm
source: tdn-rm
title: DT - Processo - Atualiza campo Desconto Simplificado na ficha financeira
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Processo+-+Atualiza+campo+Desconto+Simplificado+na+ficha+financeira
version: 9
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Processo - Atualiza campo Desconto Simplificado na ficha financeira |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-6212](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6212)  [DRHROTRM-9417](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9417) |

## **02.****LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2306.244
* 12.1.2310.185
* 12.1.2402.120 e Superiores.

## **03.****SITUAÇÃO/REQUISITO**

Disponibilizar um processo que permita ajustar o campo "Desconto Simplificado" (IRRFSIMPLIFICADO, IRRF13SIMPLIFICADO e IRRFFERSIMPLIFICADO) na ficha financeira do funcionário. Atualmente, este campo não é editável devido a ser um controle interno.

**04.****SOLUÇÃO**

Foi criado o processo de atualização do campo "Desconto Simplificado", no qual será realizado o recálculo dos campos IRRFSIMPLIFICADO, IRRF13SIMPLIFICADO e IRRFFERSIMPLIFICADO.

Abaixo serão descritos os passos necessários:

1) Liberar permissão de acesso ao processo **Atualiza campo Desconto Simplificado**:

2) Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Processos | Atualiza campo Desconto Simplificado, conforme demonstração abaixo:

Nesta tela, deverá selecionar um intervalo do Ano Caixa preenchendo os campos "Caixa Inicial" e "Caixa Final". Além disso, é possível realizar filtros utilizando a seleção de funcionários e/ou a quebra de seção.

Ao marcar o parâmetro "Atualizar apenas se o campo 'Desconto Simplificado' estiver nulo", o sistema processará e atualizará somente os períodos em que o campo estiver NULO. Caso contrário, todos os períodos serão atualizados de acordo com o filtro aplicado.

**ATENÇÃO**

1. Devido à vigência da legislação do "Desconto Simplificado" que teve início em 05/2023, não será permitido informar uma data anterior a esse período.
2. No log, serão registrados todos os funcionários e períodos que passarem por alterações no campo.
3. Ao concluir a atualização do campo, a flag "Desconto Simplificado Alterado Manualmente" na ficha financeira (PFPERFF) será marcada.

Segue abaixo alguns exemplos:

**CENARIO I :**Onde o funcionario não utilizou IRRF simplificado nem na folha nem no 13º

**CENÁRIO II :**Onde o funcionario utilizou IRRF simplificado na folha

**CENÁRIO III :**Onde o funcionario utilizou o IRRF simplificado no 13º 

## **05. DEMAIS INFORMAÇÕES**

[DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719351)
