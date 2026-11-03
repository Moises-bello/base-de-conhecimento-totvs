---
content_hash: 52a945770abce482a18a6d62659b616bf6dcde93fb14b442d968b46de0000b76
fetched_at: '2026-06-29T00:09:19.490826+00:00'
page_id: '422545599'
product: rm
source: tdn-rm
title: Incentivos Fiscais
type: documentation
url: https://tdn.totvs.com/display/LRM/Incentivos+Fiscais
version: 5
---

Esta pasta é habilitada para impostos do Tipo IRPJ e ICMS. No caso de se utilizar o Regime de Apuração Lucro Real todos os incentivos informados nesta pasta serão deduzidos do Saldo Devedor do imposto.   
    
 **IRPJ**

Ao Encerrar o Período de Apuração, automaticamente o sistema faz as compensações do PAT, do mais antigo para o mais recente. Isso se o valor do campo no cadastro estiver zerado. Se já tiver um valor para o PAT no cadastro, utiliza este valor.  
 Antes de fazer o cálculo do PAT, o sistema automaticamente estorna as compensações do PAT referente ao mês e Ano do Período de Apuração que se está Encerrando.  
 Só de alterar o status do Período o sistema já faz o cálculo do PAT. Mesmo que o usuário altere o Status e depois cancele a gravação, a compensação do PAT ficará gravada.

***Observação***: Os nomes dos Incentivos Fiscais poderão ser alterados, através da Pasta Períodos de Apuração em Opções | Parâmetros | Gerais | Tabelas – Identificação de regras de apuração - IRPJ.  
 Apenas o nome para o Incentivo PAT não poderá ser alterado.

**ICMS**

Conforme a lei estadual 17.615, de 04/07/2008, os contribuintes do ICMS incentivadores de projeto artístico-cultural poderão deduzir parte do seu saldo devedor deste tributo. Esta dedução estará disponível no Sistema de Gestão Fiscal para os contribuintes do estado de Minas Gerais. Para a correta apuração do tributo, deverão ser seguidos os seguintes passos:  
 Caso o saldo de Incentivo à Cultura do período anterior não tenha sido calculado, e o contribuinte quiser inserir este saldo na apuração, deve-se reabrir o período do ICMS para se incluir o saldo, através do campo "Saldo de Incentivo à Cultura para Período Seguinte", na aba "Incentivos Fiscais".  
 Deverão ser incluídos Lançamentos de Outros Débitos/Créditos do tipo "Dedução" e subtipo "Incentivo à Cultura". A soma dos valores destes lançamentos será o valor do Incentivo à Cultura no período. É importante o preenchimento da pasta Referências desses lançamentos, para a correta geração da DAPI/MG.  
 O total da dedução por Incentivo à Cultura deste período será composto pelo saldo do período anterior (item 1) somado ao valor do Incentivo à Cultura no período (item 2).  
 O valor limite para dedução no período será calculado como um percentual do saldo devedor de ICMS no período, antes de se aplicar a dedução por Incentivo à Cultura. Se o saldo do período for credor, não haverá dedução. Este percentual estará fixado no sistema em 3% até que seja parametrizado posteriormente.  
 Ao se encerrar o período de apuração, a dedução por Incentivo à Cultura será subtraída do saldo devedor de ICMS calculado, limitado ao valor limite para dedução (item 4).  
 Caso o total da dedução por Incentivo à Cultura no período seja maior que o valor limite para dedução, a diferença será lançada no campo "Saldo de Incentivo à Cultura para Período Seguinte". Este campo será calculado somente se não estiver preenchido com um valor informado manualmente pelo usuário.  
 O valor de Incentivo à Cultura não utilizado (item 6) será usado no cálculo da dedução por Incentivo à Cultura do período seguinte.  
 Na geração da DAPI/MG, será preenchido o campo 98 – DEDUÇÕES, com o valor do incentivo deduzido do ICMS a pagar.
