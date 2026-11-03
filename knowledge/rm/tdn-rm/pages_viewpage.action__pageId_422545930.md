---
content_hash: bcd6189a0e69ed6f48b737a17a0535355545ba5c78315001b0b3084ae67a2157
fetched_at: '2026-06-29T00:09:21.915225+00:00'
page_id: '422545930'
product: rm
source: tdn-rm
title: Bloco I (EFD Contribuições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545930
version: 4
---

## Operações das Instituições Financeiras, Seguradoras, Entidades de Previdência Privada, Operadoras de Planos de Assistência à Saúde e Demais Pessoas Jurídicas Referidas nos §§ 6º, 8º e 9º do art. 3º da lei nº 9.718/98.

Conforme a IN RFB nº 1.387 de 2013, a escrituração do Bloco I é de natureza obrigatória em relação aos fatos geradores ocorridos a partir de 01 de Janeiro de 2014.  
O Bloco I só será gerado para clientes que possuem integração com o produto TOTVS Gestão Contábil.

1lefti001Registro I001**Registro I001 — Abertura do Bloco I**  
Bloco referente ao Indicador de Informação. Indicando que 0 - Bloco com Dados Informados, deve ser informado pelo menos um registro além dos registros de abertura e encerramento. Se o indicador for igual a 1 - Bloco sem dados Informados só será gerado a abertura e encerramento do bloco.i010Registro I010**Registro I010 — Documento — Identificação da Pessoa Jurídica/Estabelecimento**  
Gerado para cada filial que possui movimentação no período da escrituração.   
***Observação:*** Neste primeiro momento o Bloco é gerado somente na forma Descentralizada. A geração da forma Centralizada já está sob análise.i100Registro I100

**Registro I100 — Consolidação das Operações no Período**  
Este registro é específico para escrituração pelas pessoas jurídicas referidas nos §§ 6º, 8º e 9º do art. 3º da Lei nº 9.718. Sera gerado conforme o campo 14-IND\_ATIV (Indicador da Atividade) igual á "3" do registro 0000.  
Este registro é gerado para cada combinação de CST, alíquota PIS e COFINS.   
Caso a CST informada na aba Tributo do Processo do Bloco I for igual a 04, 05, 06, 07, 08 e 09, o campo Alíquota dos Tributos PIS e COFINS será gerado zerado, pois estes tipos não possuem alíquota determinada.

* Os campos 06-VL\_BC\_PIS (Valor da Base do PIS/PASEP) e campo 09-VL\_BC\_COFINS (Valor da Base do COFINS) será calculado internamente da seguinte forma: Campo 02-VL\_REC (Valor do Faturamento/Receita Bruta no Período)  Campo 04-VL\_TOT\_DED\_FER (Valor Total das Deduções e Exclusões de Caráter Geral  Campo 05-VL\_TOT\_DED\_ESP (Valor Total das Deduções e Exclusões de Caráter Específico).
* Os campos Alíquota do PIS/PASEP e COFINS, serão gerados conforme a alíquota informada no cadastro dos respectivos tributos selecionados nos processos do bloco.
* Os campos 08-VL\_PIS (Valor do PIS/PASEP) será calculado considerado os valores do campo 06  campo 07, e o campo 11-VL\_COFINS (Valor COFINS) será calculado automaticamente considerando os valores do campo 09  campo 10.
i199Registro I199**Registro I199 — Processo Referenciado**   
Neste primeiro momento não será gerado.i200Registro I200**Registro I200 — Composição das Receitas, Deduções e/ou Exclusões do Período**  
Este registro será gerado detalhado de forma sintética, considerando os códigos das contas Contábeis sintéticas. Será preenchido um registro para cada tipo de receita e/ou deduções e exclusões de acordo com os códigos constantes nas tabelas 7.1.1 e 7.1.2.  
Na parametrização do Processo do Bloco I serão selecionadas Conta Contábil Analítica, porém na geração do campo 05-COD\_CTA (Código da Conta Contábil), será gerado com a Conta Contabil do Nivel anterior (Código Sintértico).i299Registro I299**Registro I299 — Processo Referenciado**   
Neste primeiro momento não será gerado.i300Registro I300**Registro I300 — Complemento das Operações - Detalhamento das Receitas, Deduções e/ou Exclusões do Período**  
Este registro será gerado com as Contas Contábeis analíticas de acordo com cada tipo de receita e/ou deduções e exclusões conforme os códigos constantes nas tabelas 7.1.3 e 7.1.4.i399Registro I399**Registro I399 — Processo Referenciado**  
Neste primeiro momento não será gerado.i990Registro I990**Registro I990 — Encerramento do Bloco I**  
Este registro é gerado automaticamente pela rotina com a quantidade de linhas do bloco I.
