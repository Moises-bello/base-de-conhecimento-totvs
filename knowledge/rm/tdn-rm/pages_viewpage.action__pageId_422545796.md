---
content_hash: d49acfc0c20889b0c3317ac4c6617d22175849d8cb718765a961c43af203c1cc
fetched_at: '2026-06-29T00:09:21.069869+00:00'
page_id: '422545796'
product: rm
source: tdn-rm
title: Regime Especial/Simples 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545796
version: 4
---

A pasta "Regime Especial/Simples" deixou de existir no cadastro de apuração do ICMS, os campos que eram visíveis nesta pasta foram migrados para a pasta "Apuração", Para que estes campo sejam visíveis  existem duas parametrizações a serem realizadas:

Se o campo "Optante Regime Simplificado" no Cadastro de Filial |Anexos Dados Fiscais | Subpasta Tipo Estabelecimento estiver habilitado e a sigla do imposto for do tipo ICMS, serão visualizados seguintes campos na aba "Apuração":

* Alíquota Apuração;
* Valor Faturamento;
* Valor Exclusões Faturamento;
* Valor Receita Bruta:  Receita Tributável;  Receitas Não Operacionais;

Se habilitar o parâmetro "Apura ICMS sobre receita Bruta" em Ambiente | Parâmetros | TOTVS Gestão Fiscal | 03.01 - Identificação de Regras de apuração | 03.01.01 - CMS | Regras de ICMS Filial | ditar a filial desejada | Apurar ICMS sobre a Receita Bruta.

Nesse ultimo caso o sistema irá fazer o calculo para controles exigidos pela legislação das empresas fornecedoras de refeições coletivas para o estado de SP.   
 O campo Alíquota de Apuração deverá ser informado pelo usuário, os demais campos serão calculados pelo sistema ao ser encerrado o período de apuração.  
 O campo Receita Bruta é calculado da seguinte forma:  
 O sistema soma o valor contábil de todas as saídas não canceladas, que não se referem à operação de Transferência e que não estão vinculadas a um fornecedor "órgão Estadual". Sobre este valor aplica a alíquota informada.  
 O campo Valor do Faturamento é calculado da seguinte forma:  
 Soma o valor contábil de todas as saídas não canceladas, que não se referem à operação de Transferência. Deste valor subtrai as operações de Entrada do tipo Devoluções.
