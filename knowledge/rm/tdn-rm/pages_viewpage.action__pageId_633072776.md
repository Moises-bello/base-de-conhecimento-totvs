---
content_hash: 6c10f9a14cda4a9497f616ab7dc29f40049fa6423916916dc5fac64203b6781f
fetched_at: '2026-06-29T00:11:06.292427+00:00'
page_id: '633072776'
product: rm
source: tdn-rm
title: Reajuste - Atualização de Valores Online (Em tempo real)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=633072776
version: 7
---

Este documento tem por objetivo descrever o funcionamento do reajuste das parcelas provenientes dos contratos de venda do TCGI Vendas que passaram a ser parametrizados como online, e a sua correta parametrização para ser utilizada.

Observando a evolução do mercado e a necessidade de armazenamento dos valores que compõe as parcelas provenientes do contrato de venda no tempo e até mesmo o hiato operacional das áreas dentro de nossos clientes, de até gerar boletos antes mesmo que todas as parcelas de contratos estivessem reajustadas e outras situações, o TCGI Vendas criou na apresentação dos parâmetros do Financeiro o seguinte campo *"Reajusta os valores de integração dos lançamentos até a data de reajuste" e "Permite reajustar lançamentos registrados ou remetidos ao banco na Baixa Manual e Rec. Via Cheque"* para quando se executa um processo até o seu fim envolvendo parcelas a receber ou a pagar relacionadas a contratos de vendas. Contudo, passa a ser obrigatório a marcação do campo *“Permitir alterar lançamentos a receber remetidos ao banco”* nos parâmetros gerais do Financeiro para o correto funcionamento da nova funcionalidade. 

Com isso, TCGI passou apresentar o parâmetro *"Reajusta os valores de integração dos lançamentos até a data de reajuste"*, sendo este parâmetro de marcação obrigatória desde a versão 12.1.29. para todos os clientes que desejam ter a apresentação da evolução dos lançamentos ao longo do tempo e ainda poder consultar a situação retroativa de um contrato, permitindo ainda a possibilidade da criação de N boletos registrados a banco com os valores reajustados apenas em memória.  
O sistema agora passa a registrar o log da parcela ao fim de todo processo (baixa, cancelamento de baixa e outros).

Ao marcar o campo *"Reajusta os valores de integração dos lançamentos até a data de reajuste"* no parâmetro do Financeiro, os campos *"Permitir reajustar parcelas enviadas a banco no modelo PRICE"* e *"NÃO ALTERAR parcelas enviadas ao banco, no modelo de cálculo PADRÃO"* nos parâmetros do TCGI dentro das opções de reajuste passo 2/2 são automaticamente desabilitados e os valores dos mesmos passa a ser desconsiderado. Ficando agora o reajuste sempre ocorrendo, não havendo divergência dos valores entre envio a banco e retorno o sistema funcionará normalmente.

Ao longo do tempo ainda percebemos que ao reajustar e enviar a banco, tínhamos muitas inconsistências de valores com relação a boletos no momento de processar o retorno bancário para o momento da baixa. Para que os valores possam ser compreendidos e sempre possam estar coerentes, ao enviar a banco o valor passa a ser reajustado e no momento do retorno bancário as parcelas são novamente reajustadas. Os valores sendo iguais, a baixa ocorre normalmente e o ultimo log fica com o valor correto do momento do reajuste para a baixa. Havendo alguma divergência deverá ser entendido essa divergência, onde poderá ser uma alteração de índice do momento do envio a banco para o momento do processamento do retorno bancário, alguma falha operacional no momento de gerar os boletos e no momento de processar o retorno ou alguma outra situação.

Criando assim uma confiabilidade ainda maior em nossas soluções!

As imagens abaixo traz os parâmetros configurados corretamente para a utilização do processo de reajuste on-line para os processos gerais relacionados aos títulos a receber ou a pagar provenientes de contratos de vendas do TCGI. Lembramos que uma vez marcado o parâmetro *"Reajusta os valores de integração dos lançamentos até a data de reajuste"* ele não poderá ser desmarcado.

Campo *"Reajusta os valores de integração dos lançamentos até a data de reajuste"* e *"Permite reajustar lançamentos registrados ou remetidos ao banco na Baixa Manual e Rec. Via Cheque"* nos parâmetros gerais do Financeiro >> Integração Imobiliária, deverá ser marcado.

Ainda nos parâmetros gerais do Financeiro na visão de contas a receber e a pagar deverá ir até a etapa 23 e marcar o campo *“Permitir alterar lançamentos a receber remetidos ao banco”.*

Ao marcar o campo *"Reajusta os valores de integração dos lançamentos até a data de reajuste"*descrito acima, na visão dos parâmetros gerais do Gestão de Imóveis você poderá visualizar que os campos *Permitir reajustar parcelas enviadas a banco no modelo PRICE"* e *"NÃO ALTERAR parcelas enviadas ao banco, no modelo de cálculo PADRÃO"* passam a ficar desabilitados.

Assim o processo de reajuste online passa a funcionar corretamente!
