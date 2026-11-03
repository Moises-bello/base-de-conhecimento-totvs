---
content_hash: 8c1fd1e512da0410b995d9ad5039478eb377c8b7f84cf95a54f494015cb49c63
fetched_at: '2026-06-29T00:11:50.452164+00:00'
page_id: '841173878'
product: rm
source: tdn-rm
title: DT - Processo - Atualiza campo Desconto Simplificado para as Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=841173878
version: 3
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Processo - Atualiza campo Desconto Simplificado para as Férias |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-6359](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6359) |

## **02.****LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2306.244
* 12.1.2310.185
* 12.1.2402.120 e Superiores.

## **03.****SITUAÇÃO/REQUISITO**

Disponibilizar um processo que permita ajustar o campo **IRRFFERSIMPLIFICADOCAIXA** na ficha financeira do funcionário. 

**04.****SOLUÇÃO**

Foi criado o processo de atualização do campo "Desconto Simplificado em Férias", no qual será realizado o processo de alimentação do campo através da informação da tabela de recibo de férias **PFUFERIASRECIBO,**onde o campo receberá o valor 0 ou 1, 0 para quando não for utilizado o desconto simplificado no recibo e 1 para quando for utilizado o desconto do IRRF simplificado no recibo.

Abaixo serão descritos os passos necessários:

1) Liberar permissão de acesso ao processo **Atualiza campo Desconto Simplificado**:

2) Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Processos | Atualiza campo Desconto Simplificado, conforme demonstração abaixo:

Nesta tela, deverá selecionar um intervalo do Ano Caixa preenchendo os campos "Caixa Inicial" e "Caixa Final". Além disso, é possível realizar filtros utilizando a seleção de funcionários e/ou a quebra de seção.

Ao executar o processo, o sistema processará o campo **IRRFFERSIMPLIFICADOCAIXA** que tenham o registro de uso do **IRRFSIMPLIFICADO** na tabela **PFUFERIASRECIBO**.   
O campo será alimentado com 1 ou 0, seguindo o mesmo padrão utilizado na tabela de recibo de férias. Para alimentar o mês caixa, será utilizada a data de pagamento do recibo para identificação do mês caixa.

**ATENÇÃO!**

1. Devido à vigência da legislação do "Desconto Simplificado" que teve início em 05/2023, não será permitido informar uma data anterior a esse período.
2. No log, serão registrados todos os funcionários e períodos que passarem por alterações no campo.

Segue abaixo o exemplo de utilização:  
  
Funcionário que não utilizou do desconto do IRRF SIMPLIFICADO em seu recibo de férias:

Funcionário que utilizou do desconto do IRRF SIMPLIFICADO em seu recibo de férias:

## **05. DEMAIS INFORMAÇÕES**

[DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719351)
