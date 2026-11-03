---
content_hash: af46ec91eb11319c00033494e800f0e9ed26543a72158854ae7861cb2c9b179f
fetched_at: '2026-06-29T00:09:21.784217+00:00'
page_id: '422545907'
product: rm
source: tdn-rm
title: Apuração PIS/COFINS por Centro de Custo e Diferimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545907
version: 14
---

## **Conteúdo**

**Conteúdo**

## **01. Regras**

Para realiza a apuração destes tributos por centro de custo, o parâmetro "Apura Tributo por Centro de Custo" deve ser habilitado.  
Acesse Ambiente | Parâmetros | TOTVS Gestão Fiscal | 03.01 - Identificação de Regra de Apuração | 03.01.07 - COFINS | avançar | Etapa 1 - Regra de Apuração do COFINS (mesmo caminho para o PIS).  
Após marcar este parâmetro será disponibilizado na tela de cadastro de eventos tributários o campo "Cálculo por Centro de Custo".

Desta maneira, mesmo com o parâmetro habilitado o usuário poderá definir se o cálculo será realizado desta maneira no momento do cadastro do evento. Poderão ser definidos ainda quais centros de custo farão parte da apuração.

O usuário poderá ainda optar por diferir o pagamento dos tributos habilitando o parâmetro Controla Diferimento para PIS/COFINS no assistente de implantação de processos. Habilitando esta opção a apuração destes tributos passará a ser feita com base nas baixas dos lançamentos financeiros gerados pelo sistema TOTVS Gestão de Estoque, Compra e Faturamento. O usuário irá definir no momento da inclusão do evento tributário quais centros de custo terão o pagamento do tributo diferido.  
Em ambos os casos o DARF para o pagamento dos tributos será gerada por centro de custo. O usuário poderá gerar para todos ou selecionar para os quais que deseja. Não será gerado DARF mais de uma vez para o mesmo centro de custo dentro do mesmo período. Caso haja mudança no valor do tributo para algum centro de custo que já tenha DARF gerado o usuário deverá excluir, encerrar o período novamente e gerar novo registro.

***Observação***: Caso haja alteração no valor dos tributos, por cancelamento de baixa ou mesmo alteração no valor de uma nota fiscal, por exemplo, o usuário deverá reabrir o período fazer todas as alterações necessárias referentes à contabilização e geração de informações financeiras, encerrar o período de apuração e gerar as guias novamente.  
Mesmo havendo dependência entre os processos que afetam o valor do PIS e da COFINS os sistemas envolvidos não impedirão o usuário de fazer alterações nas informações envolvidas no processo.   
Exemplo: A qualquer momento poderá ser feito o estorno da baixa de um lançamento financeiro ou baixar um novo lançamento que gere PIS e COFINS. Após fazer isto o usuário deverá reabrir o período de apuração e encerrar novamente para que o valor do tributo seja atualizado. Esta informação tanto para a apuração por centro de custo quanto para a apuração por centro de custo com pagamento diferido.

## **02. O Processo na Prática**

O sistema irá apurar o valor devido para o tributo através da regra definida no evento tributário. Este valor será armazenado. Em seguida zera o valor do tributo devido, considerando que nenhuma receita foi recebida, ou seja, diferi a totalidade do tributo devido. Em seguida irá realizar os valores:

* Para os títulos emitidos e baixados no mês da apuração o sistema irá realizar o valor do tributo relacionado, ou seja, somar o valor. A diferença entre o total devido e o realizado é o diferido no mês
* Para os títulos emitidos em meses anteriores e baixados no mês da apuração o sistema irá realizar o valor do tributo relacionado, ou seja, adicionar o valor.

Em ambos os casos o valor a somar será calculado da seguinte forma:  
1 – Calcula-se o percentual que o valor original do título pago representa em relação à receita total do mês em que foi emitido. O percentual do título em relação à receita total é feito com base no valor baixado para que sejam tratadas baixas parciais.  
2 – Aplica-se o percentual obtido no cálculo anterior sobre o valor do tributo devido no mês de emissão do título.  
3 – O resultado do cálculo anterior será o valor a pagar do tributo. O valor a diferir será a diferença entre o valor apurado e o valor a pagar.  
Uma vez baixado o título e encerrado o período de apuração do tributo, a baixa não poderá ser estornada. A baixa só poderá ser estornada se o período de apuração do tributo estiver aberto.  
Para os títulos relacionados ao faturamento de serviços com incidência do PIS/COFINS o usuário não deverá utilizar rateios por centro de custo. Os lançamentos financeiros devem estar associados com apenas um centro de custo. Se o lançamento estiver associado com vários centros de custo, o sistema irá considerar este lançamento na apuração de todos os centros de custo, o que irá gerar inconsistências no cálculo do tributo devido.

Atenção

No encerramento dos períodos de apuração dos tributos **PIS** e **COFINS** o sistema verificará se existe algum evento tributário vinculado a estes tributos (modelo antigo em Delphi), caso positivo realizará a apuração normalmente, caso contrário o período será encerrado sem mensagem de inconsistência porém, com os valores zerados ou desatualizados.
