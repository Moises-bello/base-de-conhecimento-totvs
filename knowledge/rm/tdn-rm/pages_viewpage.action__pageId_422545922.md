---
content_hash: 25be5c299b51144e0023d57dc254af5c166f440859f86c6e65ef555ca139ad68
fetched_at: '2026-06-29T00:09:21.820257+00:00'
page_id: '422545922'
product: rm
source: tdn-rm
title: Inserir Lançamento de Diferencial de Aliquota
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545922
version: 2
---

Este processo só estará visível para filiais do estado de São Paulo, cujo parâmetro Considera Dif. Alíquota - Outros Débitos esteja desativado.  
 Conforme decreto 45.490/2000 do RICMS SP, o diferencial de alíquota deve ser lançado como Outros Débitos e Créditos nos livros doc contribuintes. Deverão ser gerados dois lançamentos, um referente a Outros Débitos com o valor da base de cálculo do diferencial de alíquota aplicando a alíquota do Estado e outro referente a Outros Créditos, com a alíquota do diferencial.

* **Informações do Cálculo**

Serão selecionados os lançamentos de acordo com a regra a seguir:

1. Entradas da coligada, filial e período informados na geração do processo,
2. Registros com status diferente de Cancelado ou Estorno,
3. Registro com valor de diferencial de alíquota maior que zero e Natureza de Operação de Origem/Destino como Interna ou Interestadual.

***Observação***:O valor do débito será a soma do produto da Base do ICMS de Diferencial de Alíquota pela Alíquota Interna e o resultado deste cálculo dividido por 100.   
 O valor do crédito será a soma do produto da Base do ICMS de Diferencial de Alíquota Interestadual e o resultado deste cálculo dividido por 100.  
 Será criado um lançamento de outros débitos e créditos com o tipo Outros Débitos e outro com o tipo Outros Crédito, ambos com subtipo Não se aplica e classificação conforme dado informado na tela de geração do processo.
