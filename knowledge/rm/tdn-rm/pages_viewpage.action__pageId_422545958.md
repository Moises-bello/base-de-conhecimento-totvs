---
content_hash: 299fe7d920d27acd57a0a3b73f5670d94e7182010d941e2277bab71da19d6494
fetched_at: '2026-06-29T00:09:22.067415+00:00'
page_id: '422545958'
product: rm
source: tdn-rm
title: Apuração ICMS ST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545958
version: 15
---

A apuração do ICMS ST se faz de forma distinta à apuração do ICMS próprio. É necessário a criação do período de apuração especificamente para este tributo.

O sistema fará o controle e apuração do Saldo imposto ICMS ST Devido em um determinado período. Ao encerrar o período associado ao tributo ICMS ST, será calculado o Saldo Credor / Devedor, considerando o Saldo do Tributo ICMS ST do período anterior, e posteriormente será armazenados os registros com estes dados para cada UF movimentada no período, na Pasta ICMS ST do Período de Apuração selecionado.

Os valores de ICMS ST destacados nos Lançamentos Fiscais de saída serão considerados como débito do Imposto, exceto para a Natureza de Operação do Tipo Outros de ICMS ST, este tipo não gera débito do Imposto.

Os contribuintes que receberam Nota Fiscal com destaque do ICMS ST devem destacar em suas Notas Fiscais de Venda o valor do ICMS ST recolhido por seu Fornecedor.

Os valores de ICMS ST destacado nos Lançamentos Fiscais de Entrada, cuja Natureza de Operação associada é do tipo ICMS ST Retido na Compra, será considerado como débito do Imposto. Nestas operações o ICMS ST é devido ao Estado da Filial recebedora da Nota Fiscal.

**Observação:** Serão considerados os [Códigos de Ajuste](https://tdn.totvs.com/x/-U90GQ) associados aos lançamentos de Entrada, Saída, Outros Débitos/Créditos para o cálculo da Apuração do ICMS e para a geração do registro E210, no arquivo do SPED Fiscal.

No Campo **Saldo Credor\Devedor** é considerado o **Valor de Ajuste do ICMS**, informado na Pasta de Ajuste do Lançamento Fiscal ou Item do Lançamento.

**Ajuste de Débito** (Considerado como Outros Débito) os Códigos de Ajuste cujo o Terceiro caractere for igual a for ‘3’, ‘4’ ou ‘5’ e o Quarto caractere for igual a for “1”(um).

Exemplo de código: UF31xxxxxx, UF01xxxxxx

**Ajuste de Crédito** (Considerado como Outros Crédito) os Códigos de Ajuste cujo o Terceiro caractere for igual a ‘0’, ‘1’ ou ‘2’ e o Quarto caractere for igual a ‘1’.

Exemplo de código: UF01xxxxxx, UF01xxxxxx.

Particularidades1true1Por Estado

* Para o estado de Minas Gerais o sistema está considerando o valor do S.T nas operações de devolução como crédito de S.T. Ao encerrar o período de apuração de ICMS ST, estes valores de devoluções são carregados na tabela DPERIODOST como crédito.

Exemplo: operações de entrada com um dos seguintes tipos de ICMS: Venda C/ S.T., Isento C/ S.T., Red. B.C. e S.T. e Complementar S.T., cujo Tipo da Natureza de Operação é Devolução, o valor ST destas operações será considerado como crédito.

* Quando não houver valor apurado mas for usado no Lançamento Fiscal código de ajuste iniciado por MG71\*\*\*\*\*\*\*  pertinente a Débitos especiais, será gravado o valor zerado no período de apuração para geração do registro E210 do Sped Fiscal.

  Exemplo
2ST pago na Chancela

Para as operações em que o ICMS ST é pago na Chancela, o usuário deverá desmarcar o campo Contribuinte Credenciado da Tela de Substituição Tributária do lançamento Fiscal.

No momento em que encerrar o Período de ICMS ST, o sistema irá totalizar o ICMS ST Total Devido, irá totalizar o ICMS ST Retido na Chancela e o valor do ICMS a Pagar.

O valor a pagar será o Valor Total Devido - o ICMS ST Retido na Chancela.

Além dos valores de ICMS ST destacados nos Lançamentos Fiscais de Entrada / Saída serão considerados no cálculo do imposto, os valores associados aos Lançamentos de Outros débitos / Créditos para este Tributo e Período de Apuração que está sendo Encerrado.

Pode ocorrer de ter crédito do Imposto, se tiver cadastrado algum lançamento de Outros Débitos com um valor de crédito superior ao Débito. Neste caso, o valor a Pagar será ZERO.

3Operações de TransporteAtenção***Atenção!*** O parâmetro "Operações de Transporte compõem Saldo Devedor de ICMS ST" foi criado para atender ao Art.7° do Anexo XV do RICMS, que trata das Operações de Substituição Tributária, onde o valor do ST Retido nas operações de Transporte não poderá ser compensado com qualquer crédito de imposto. Caso esse parâmetro esteja DESMARCADO o sistema irá funcionar da seguinte forma:4Lançamentos de Outros Débitos/CréditosInformações***Observação*:**Lançamentos Fiscais pertencentes a Lotes em Aberto não serão considerados no cálculo.  
Saldo do Período anterior será considerado. Os Lançamentos de Outros Débitos / Créditos para o ICMS ST deverá ter a informação da UF para que o sistema calcule corretamente este tributo. Este campo somente é habilitado para este tributo5FECPfalseFECP

A apuração do FECP será feita quando a Regra de ICMS vinculada à Natureza seja de ICMS ST, o campo "% FECP Item" seja preenchido da mesma forma que ocorre atualmente para o Diferencial de Alíquota (o sistema carrega o valor do campo "% FECP" dos Dados Fiscais por UF do Produto).

Para que o percentual do FECP seja carregado, no caso dos Lançamentos de Saída (dentro e fora do estado), o sistema verificará se o Tipo de Operação é de Situação Tributária.

Foram disponibilizados dois campos na Situação Tributária do Lançamento Fiscal:   
"%FECP ST": campo que não pode ser alterado e corresponde ao percentual do FECP do(s) Item(ns) do Lançamento.

"Valor ICMS FECP": campo que não pode ser alterado e corresponde à soma dos valores do FECP dos Itens do Lançamento Fiscal.

Informações*Observação*: Para que o FECP seja calculado é necessário realizar o recálculo do lançamento para que o campo "Base ICMS ST" seja preenchido e assim feito o correto calculo do FECP.
