---
content_hash: a4413bee44c67898c1ae6ebe454d506fac54e070e75db22ad9fc3d93eb45a214
fetched_at: '2026-06-29T00:09:21.763323+00:00'
page_id: '422545899'
product: rm
source: tdn-rm
title: Apuração IRRF PJ
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545899
version: 6
---

No Lançamento Fiscal de Entrada, Pasta Outros tributos, informar este tributo com seus respectivos valores e código de receita correspondente.  
Ao Encerrar o Período de Apuração, o sistema irá somar os valores do imposto do Tipo IRRF PJ, informado na Pasta Outros Impostos dos Lançamentos Fiscais de Entrada. Lançamentos Cancelados e Estornados não serão considerados. O Saldo Credor do Período anterior, se existir, será considerado na apuração do imposto. Também serão selecionados na apuração e geração do DARF Lançamentos Fiscais de entrada que contenham o tributo IRRFPJ com o código de receita 8045.  
Ao Gerar as Guias de Pagamento o sistema seleciona os Lançamentos Fiscais de Entrada, com o destaque do Imposto, não cancelados ou estornados.  
 No momento de geração das Guias o sistema irá gerar a DARF agrupa pelo código oficial da receita informado no cadastro de Código de Receita em Cadastros | Tabelas Auxiliares | Código da Receita.  
 As Guias podem ser integradas ao TOTVS Gestão Financeira.  
Na tela de geração da DIRF existe a opção "**Busca IRRF PJ lançado no Sistema de Gestão Fiscal**" se desejar selecionar os Lançamentos Fiscais de Entrada com o destaque deste imposto. A apuração do Tributo e geração do DARF obedecerá a seguinte regra:

* Será verificado o parâmetro de geração do IRRF-PJ do TOTVS Gestão Financeira.
* Data de Emissão: Os Lançamentos Fiscais serão selecionados por sua data de emissão
* Data de Vencimento: Os Lançamentos Fiscais serão selecionados pela data de vencimento gravada na pasta Dados Financeiros. Não é necessário que o mesmo esteja integrado ao financeiro.
* Qualquer valor diferente dos acima citados: Os Lançamentos Fiscais serão selecionados pela Data do Documento (DALAF.DATALF)
