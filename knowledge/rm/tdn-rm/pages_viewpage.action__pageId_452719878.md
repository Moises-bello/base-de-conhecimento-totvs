---
content_hash: 7ea043fd026887fc10ad6e6567c75cf8b2af7c45b47a46f34f7ddf9b2ffc300c
fetched_at: '2026-06-29T00:10:10.568891+00:00'
page_id: '452719878'
product: rm
source: tdn-rm
title: RAIS / CAGED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719878
version: 4
---

falseATENÇÃO:

A partir da release **12.1.2606**, esta rotina foi descontinuada, pois sua funcionalidade passou a ser atendida pelo **eSocial**.

Para a emissão da RAIS e geração do CAGED, é importante que esta pasta tenha as informações corretas, pois serão consistidas pelo sistema.  
   
Informe o número de Não Empregados Proprietários, ou seja, proprietários ou de sócios que exercem atividades no estabelecimento sem terem relação de emprego. A empresa sem atividade no ano-base deverá deixar este campo zerado.

**Atividade Econômica:**  
CNAE Preponderante : Informe o código CNAE referente a atividade econômica preponderante do estabelecimento.  
Esta informação será considerada no esocial.   
   
Quando o campo acima estiver em branco o sistema irá considerar o código CNAE cadastrado no campo **CNAE 2.0.**  
   
O Prefixo da RAIS somente deverá ser utilizado para diferenciar sub-arquivos que possuam a mesma inscrição do CNPJ/CEI/CPF. Essa situação pode ocorrer quando um mesmo funcionário exerce funções distintas em uma mesma empresa. Assim, na RAIS, seu CPF bem como o CNPJ da empresa a que está vinculado aparecerão mais de uma vez, em surb-arquivos distintos.   
   
**Exemplo:**  
Em um arquivo RAIS, existem 2 (dois) sub-arquivos com a mesma inscrição no CNPJ, identificados pelos prefixos "AL01" e "AL02" (em razão de um mesmo empregado exercer as funções de professor e secretário).   
Estes prefixos deverão permanecer nos sub-arquivos até o final do processamento da RAIS e a emissão dos relatórios.  
   
**Observação:**  
Não poderá haver espaços em branco neste campo. Será emitida uma mensagem de alerta no momento da emissão da RAIS quando houver espaço em branco neste campo.   
   
Informe a natureza jurídica do estabelecimento, conforme Códigos aprovados pela Comissão Nacional de Classificação (CONCLA).  
Selecione o mês da data-base da categoria a que estiver vinculado o maior número de funcionários na empresa.  
   
Preencha com a data de encerramento das atividades da empresa no ano base referente ao qual será gerado o arquivo de RAIS e automaticamente o sistema informará no arquivo de RAIS que a empresa encerrou suas atividades no ano base informando também a data deste campo. Quando esta data for informada será gerado, automaticamente, um gatilho de encerramento do evento S-1005 na fila de eventos com o tipo de operação Encerramento para ser enviado ao eSocial.  
   
Se a empresa é participante do Programa de Alimentação do trabalhador - PAT, instituído pela Lei nº 6.321/76, o campo Tem participação no PAT será utilizado na emissão da RAIS. Informe o número de trabalhadores beneficiados pelo PAT de acordo com a faixa salarial e os percentuais (sem decimal) da(s) modalidade(s) utilizada(s) pela empresa, em relação ao número total de beneficiados.  
   
**Observação:**  
O Programa de Alimentação do Trabalhador - PAT, instituído pela Lei nº 6.321, de 14 de abril de 1976 e regulamentado pelo Decreto no. 05, de 14 de janeiro de 1991, prioriza o atendimento aos trabalhadores de baixa renda, isto é, aqueles que ganham até 05 salários mínimos mensais. As empresas que aderem ao PAT são beneficiadas com incentivo fiscal e a alimentação concedida ao empregado não integra o salário-de-contribuição.  
   
Na Primeira Declaração de CAGED é informada a opção de acordo com o manual do CAGED. E na Alteração no CAGED deverá ser selecionada obrigatoriamente uma das opções disponíveis.
