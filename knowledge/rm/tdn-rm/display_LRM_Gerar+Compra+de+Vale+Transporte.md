---
content_hash: 615d868e71fdef5f821d27aa00a8edfc9641492bed9e7997bd6c62dfa2e285b6
fetched_at: '2026-06-29T00:10:07.195999+00:00'
page_id: '452719373'
product: rm
source: tdn-rm
title: Gerar Compra de Vale Transporte
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Compra+de+Vale+Transporte
version: 3
---

Neste módulo será possível realizar a compra de vale transporte para um ou mais funcionários, ou ainda para todos de uma única vez.  
Para que o processo fique visível é necessário que no assistente de implantação de processos da Folha de Pagamento, o parâmetro "Utiliza Histórico de Compra de Vale Transporte" esteja marcado. Para acessar o assistente: Configurações | Parâmetros | Parametrizador | Folha de Pagamento | Folha Normal | Vale Transporte  
   
Sempre que este parâmetro estiver marcado e existir um histórico de compra gerado para o funcionário, o sistema irá considerar o registro de histórico de compra de vale transporte para cálculo e lançamento de desconto de Vale Transporte. Caso não exista nenhuma compra efetuada para o funcionário, mesmo com o parâmetro marcado, o sistema irá considerar o registro de vale transporte do cadastro do funcionário.   
   
Para que o sistema calcule a compra de vale transporte é necessário que no cadastro do funcionário tenha as informações referentes a linha de transporte. O processo gera um registro de compra de vale transporte por linha cadastrada no histórico de vale transporte do funcionário.

**Executando o processo de compra de vale transporte**

Para realizar a compra de vale transporte para funcionários, o usuário deverá acessar: Folha Mensal | Processos | Lançamentos | Gerar Compra de Vale Transporte, selecionar o funcionário desejado, Definir a competência desconto em folha, definir período de compra, definir os dias para compra e executar o processo.  
   
Para cada compra de vale transporte gerada é incluído um registro histórico de compra de vale transporte no anexo de históricos do funcionário. Para visualiza-lo deverá acessar: Administração de Pessoal | Cadastros | Funcionários | Anexos | Históricos | Histórico de Compras de Vale Transporte  
   
É possível fazer mais de uma compra de vale transporte na mesma competência desde que a data de início da compra seja diferente da data informada em uma compra já realizada. Quando é informando a mesma data de início e Competência desconto em folha, o sistema somente atualiza os valores no histórico de compra de vale transporte gerado, como, data final da compra, Dias no período caso este seja informado com valor diferente e calculará o valor total entregue de vale transporte. No lançamento, o sistema somará todas as compras de vale transporte efetuadas na competência de desconto em Folha.   
   
   
**Realizando o processo de compra de vale transporte na competência atual**  
   
Para realizar a compra de vale transporte para funcionários, o usuário deverá acessar: Folha Mensal | Processos | Lançamentos | Gerar Compra de Vale Transporte, selecionar o funcionário desejado, Definir a competência atual para o campo competência desconto em folha, definir período de compra, definir os dias para compra e executar o processo.  
   
   
**Observação**  
   
Para fazer o lançamento da compra de vale transporte é necessário executar o processo de Lançar Grupo de eventos, com o parâmetro 'Lançar vale Transporte' marcado. Se a compra for feita depois do lançamento dos eventos para o envelope do funcionário, é necessário executar novamente o processo Lançar Grupo de Eventos ou o recálculo do envelope de pagamento através do processo Executa Recálculo, marcando o parâmetro 'Recalcula Total Entregue de VT (CC32)'. Para que o recálculo seja processado, é necessário também que no envelope de pagamento exista o evento com o Código de Cálculo 32. O sistema não recalcula a compra de vale transporte através do envelope de pagamento.  
   
   
**Realizando o processo de compra de vale transporte em competências anteriores**  
   
Para realizar a compra de vale transporte para funcionários, o usuário deverá acessar: Folha Mensal | Processos | Lançamentos | Gerar Compra de Vale Transporte, selecionar o funcionário desejado, Definir uma competência anterior a atual para o campo competência desconto em folha, definir período de compra, definir os dias para compra e executar o processo.  
   
   
**Observação**  
   
Fazendo o processo de compra de vale transporte em competências anteriores a atual, o sistema somente gera o histórico de compra de vale transporte, não sendo possível lançar o evento de compra de vale transporte para o envelope de pagamento do funcionário, mesmo que o período da compra seja igual ao mês da competência.  
   
   
**Realizando o processo de compra de vale transporte em competência posterior**  
   
Para realizar a compra de vale transporte para funcionários, o usuário deverá acessar: Folha Mensal | Processos | Lançamentos | Gerar Compra de Vale Transporte, selecionar o funcionário desejado, Definir uma competência posterior a atual para o campo competência desconto em folha, definir período de compra, definir os dias para compra e executar o processo.  
   
**Observação**  
   
Mesmo que o período da compra para vale transporte seja igual ao mês atual, o sistema não irá fazer o lançamento do vale transporte na competência atual. É possível fazer o lançamento de compra de vale transporte para competência posterior através do processo de Lançamentos de Multi-Coligadas.   
   
   
**Realizando o processo de compra de vale transporte informando dias para compra – total de dias no período**  
   
Para realizar a compra de vale transporte para funcionários, o usuário deverá acessar: Folha Mensal | Processos | Lançamentos | Gerar Compra de Vale Transporte, selecionar o funcionário desejado, Definir a competência para o campo competência desconto em folha, definir período de compra, definir dias para compra marcando a opção total de dias no período e informar a quantidade de dias, e executar o processo.  
   
Informando o total de dias no período, o sistema irá multiplicar a quantidade de dias informado, pelo número de viagens diárias informado na linha de transporte cadastrada para o funcionário. Neste cálculo, o sistema encontrará o total de vales entregues, que será multiplicado pelo valor da tarifa de transporte configurado para a Linha de transporte.  
   
**Exemplo**  
   
Número de viagens para Linha de transporte cadastrado para o funcionário = 2  
Valor da tarifa de transporte = R$ 2,00  
Campo total de dias no período = 10  
   
O sistema irá calcular 10 x 2 = 20, que é a quantidade de vales transporte que devem ser entregues para o funcionário.  
O sistema irá multiplicar a quantidade de vales transporte entregues pela tarifa de transporte: 20 x R$ 2,00 = R$ 40,00.   
Portanto o valor de compra de vale transporte para o funcionário será de R$ 40,00.  
   
   
**Realizando o processo de compra de vale transporte informando dias para compra – total de vales entregues**  
   
Para realizar a compra de vale transporte para funcionários, o usuário deverá acessar: Folha Mensal | Processos | Lançamentos | Gerar Compra de Vale Transporte, selecionar o funcionário desejado, Definir a competência para o campo competência desconto em folha, definir período de compra, definir dias para compra marcando a opção total de vales entregues e informar a quantidade de vales entregues, e executar o processo.  
   
**Observação**  
   
Informando o total de vales entregues, o sistema irá multiplicar este valor informado pela tarifa de transporte. No histórico de compra de vale transporte os campos 'Dias no Período' e 'Viagens Diárias', são preenchidos pelo valor 0, pois o sistema não considera e nem faz a projeção de quantidade de dias e número de viagens diárias.  
   
   
**Realizando o processo de compra de vale transporte informando dias para compra – fórmula total de vales entregues**  
   
Para realizar a compra de vale transporte para funcionários, o usuário deverá acessar: Folha Mensal | Processos | Lançamentos | Gerar Compra de Vale Transporte, selecionar o funcionário desejado, Definir a competência para o campo competência desconto em folha, definir período de compra, definir dias para compra marcando a opção total de vales entregues, marcar o flag 'Alterar Valor(es) por fórmula' e informar uma formula, e executar o processo.  
   
**Sugestão de Fórmula**  
   
DECL (TOTVALES);  
DECL (STRAUX);  
   
SETVAR (TOTVALES, **HISTCOMPRAVT**  ( ANO , MES, LINHAVTCORRENTE ('CODLINHA') , **DATANULA**, **-1**, **'TOTALVALESENTREGUE'**) );  
SETVAR (TOTVALES, **ARRED**(TOTVALES / 20 \* 22));  
   
SETVAR (STRAUX, '');  
SETVAR (STRAUX, CONCATVT (STRAUX , 'TOTALVALESENTREGUE', TOTVALES));  
SETVAR (STRAUX, CONCATVT (STRAUX, 'DIASPERIODO',  22));  
   
STRAUX  
   
**Campos válidos na CONCATVT:**  
   
"TARIFA"  
"VALORTOTALENTREGUE"  
"REJEITADO"  
"TOTALVALESENTREGUE"  
"DIASPERIODO"  
"VIAGENSDIARIAS"  
   
   
**Função HISTCOMPRAVT**  
   
**HISTCOMPRAVT**(Ano Comp., Mês Comp., Código da Linha, Data Início, Viagens Diárias, Campo da Tabela PFHSTFCOMPRAVT)  
   
   
**Realizando o processo de compra de vale transporte informando dias para compra – substituir compra alterada manualmente**  
   
Para realizar a compra de vale transporte para funcionários, o usuário deverá acessar: Folha Mensal | Processos | Lançamentos | Gerar Compra de Vale Transporte, selecionar o funcionário desejado, Definir a competência desconto em folha, definir período de compra, definir os dias para compra, marcar o parâmetro 'Substituir Compra Alterada Manualmente' e executar o processo.  
   
Este parâmetro marcado irá recalcular as compras de vale transporte que foram alteradas manualmente, no histórico de compra de vale transporte do funcionário, de acordo com as informações 'competência desconto em Folha' e 'Período de compra' existentes. Depois de executado o processo com o parâmetro marcado, o histórico de compra de vale transporte não ficar mais com flag 'Alterado Manualmente' marcado. Caso não exista a compra de vale transporte no histórico de compra de vale transporte do funcionário, o sistema irá fazer um novo cálculo de compra de vale transporte e inserir no histórico de compra.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Histórico de Compra de Vale Transporte

Grupo de Eventos

Assistente de Grupo de Eventos

[Histórico de Vale Transporte](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718292)
