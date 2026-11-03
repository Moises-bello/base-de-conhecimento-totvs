---
content_hash: a86b625d1904c51d769624489d5ca2eacb22444ab95452b8990b660d7b163b26
fetched_at: '2026-06-29T00:09:21.753736+00:00'
page_id: '422545894'
product: rm
source: tdn-rm
title: Apuração de Tributos Retidos na Fonte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545894
version: 15
---

#f5f5f5#363636noneApuração com Retenção na Fonte

## **Conteúdo**

Conteúdo

## **01. Visão Geral**

Os tributos retidos são: COFINS-RF, PIS-RF, CSLL-RF e Contribuição Social RF**.**O sistema TOTVS Gestão Fiscal irá selecionar todos os Lançamentos Financeiros que são do Tipo do Tributo em questão e que estão no Lançamento Original (Lançamento Financeiro que ao ser baixado gerou o débito das contribuições), na pasta Impostos que está cadastrado com o mesmo tipo do tributo.

## **02. Como funciona**

O sistema seleciona os Lançamentos Financeiros do Tributo agrupados por código de receita, gera a guia correspondente para cada código, e gera uma Fatura, sendo um vencimento de fatura para cada guia. Os lançamentos de débito do tributo ficam com o status de faturado.

O vencimento de fatura possui a informação da guia que o originou, tendo a opção de estornar a fatura gerada. Neste processo, além de cancelar a fatura, a guia gerada também é deletada - sendo um processo diferente do estorno dos outros tipos de tributo. Isso se deve à guia gerada automaticamente só poder estar cadastrada quando vinculada à fatura.

## **03. Apurações por tributos**

### **03.01. IRRF**

A cada inserção de guias automaticamente, o sistema irá gerar guias para os lançamentos que estão em aberto, sem nenhuma fatura relacionada.

Serão verificados os parâmetros de geração de guias em *Ambiente | Parâmetros | TOTVS Gestão Financeira | Apuração de Tributos | IRRF Pessoa Física – Etapa 11.* Nesta etapa, é possível definir se as guias serão geradas por beneficiário, por lançamento ou por filial. Quando a guia for gerada por filial, será verificado se o campo "Filial Matriz do Estabelecimento" está preenchido em *Ambiente | Parâmetros | TOTVS Gestão Financeira | Apuração de Tributos - Etapa 22 - Filial Matriz.* Se estiver, o usuário deverá gerar as guias em cada filial; caso contrário, as guias de todas as filiais serão geradas na filial matriz.

Ao gerar as guias DARF para o tributo IRRF, o sistema irá considerar o parâmetro "Data Base para Geração do IRRF" no TOTVS Gestão Financeira, em *Ambiente | Parâmetros | TOTVS Gestão Financeira | Manutenção de lançamentos | Cálculo de tributos – IRRF | Geração IRRF*.

Para os lançamentos gerados pelo TOTVS Gestão de Folha de Pagamento (Classificação 13), o sistema sempre considera a "Data de Emissão" para os lançamentos de IRRF, independentemente do parâmetro acima informado.

Ao gerar a guia DARF, o sistema estará considerando os lançamentos de IRRF a pagar gerados pelo TOTVS Gestão de Folha de pagamento. Para isto, o usuário deverá selecionar o tipo de funcionário na grade de seleção e informar o Código da Receita do Lançamento Financeiro no momento da geração dos lançamentos. Caso existam os dois tipos de funcionários na empresa, o usuário deverá realizar o processo uma vez para cada (para mais detalhes, verificar o *help* do TOTVS Gestão de Folha de pagamento). Estes lançamentos passarão a ser considerados pelo TOTVS Gestão Fiscal na geração de DARF. Para o tributo IRRF, se as guias forem inseridas manualmente, a pasta rateios será habilitada, para que sejam informados os rateios por centro de custo e departamentos.

Aviso

Como os lançamentos mencionados acima são considerados na geração das guias DARF, supõe-se que, consequentemente, seus valores seriam demonstrados pela DCTF. Porém, com o surgimento do bloco 40 da EFD-REINF, várias retenções passam a ser demonstradas por meio desta rotina. Logo, há dois layouts da DCTF disponíveis no TOTVS Compartilhamento: um com alterações antes de 2024, considerando o IRRF e outras retenções; e o layout à partir de 2024, que **não considera** IRRF e outras retenções em sua geração, mesmo que sejam geradas as guias DARF correspondentes.

### **03.02. IRRF PJ**

No lançamento fiscal de entrada, pasta "Outros Tributos", deve ser informado este tributo com seus respectivos valores e código de receita correspondente.

Ao encerrar o período de apuração, os valores do imposto do tipo IRRF PJ informados nos lançamentos de entrada serão somados. Lançamentos com status "Cancelado" e "Estornado" não serão considerados na soma.   
Caso exista "Saldo Credor do Período Anterior", ele será considerado na apuração do imposto.   
Também serão selecionados na apuração e geração do DARF Lançamentos Fiscais de Saída que contenham o tributo IRRFPJ com o código de receita 8045.

Ao gerar as guias de pagamento, são selecionados os lançamentos fiscais de entrada com o destaque do imposto.  
No momento de geração das guias, a guia DARF gerada será agrupada pelo código oficial da receita informado no cadastro de código de receita em, *Cadastros | Tabelas Auxiliares | Código da Receita*.  
As guias podem ser integradas ao TOTVS Gestão Financeira.   
A apuração do tributo e geração das guias DARF obedecerá a seguinte regra:

* Será verificado o parâmetro de geração do IRRF-PJ do TOTVS Gestão Financeira.
* Data de Emissão: Os Lançamentos Fiscais serão selecionados por sua data de emissão
* Data de Vencimento: Os Lançamentos Fiscais serão selecionados pela data de vencimento gravada na pasta Dados Financeiros. Não é necessário que o mesmo esteja integrado ao financeiro.
* Qualquer valor diferente dos acima citados: Os Lançamentos Fiscais serão selecionados pela Data do Documento (DALAF.DATALF)

Aviso

Para correta apuração do IRRF PJ com código de receita 8045 que se refere a Comissões e Corretagens Pagas a Pessoa Jurídica, o processo deverá ser o seguinte:  
Na empresa tomadora do serviço deverá ser destacado na Nota Fiscal de "Entrada" o tributo IRRF PJ, com o código 8045 e os valores relacionados com a operação.  
Estas operações deverão constar na REINF no evento 4020 do tomador constando o prestador como beneficiário.  
Na empresa prestadora do serviço deverá ser destacado na Nota Fiscal de "Saída" o tributo IRRF PJ, com o código 8045 e os valores relacionados com a operação.  
Esta operação deverá ser considerada na REINF no evento 4080.

#f5f5f5#feac0eDocumentos Relacionados10%90%10%90%10%90%10%90%10%90%
