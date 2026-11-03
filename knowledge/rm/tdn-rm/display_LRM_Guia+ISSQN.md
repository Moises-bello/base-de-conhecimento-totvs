---
content_hash: 3aec1c5477e2946254b1136fa00bf87edd8a8920aa649129ac6482484ac55e16
fetched_at: '2026-06-29T00:11:12.353944+00:00'
page_id: '652394065'
product: rm
source: tdn-rm
title: Guia ISSQN
type: documentation
url: https://tdn.totvs.com/display/LRM/Guia+ISSQN
version: 9
---

A geração das Guias ISSQN estará disponível para o tributo ISS. Estas Guias serão geradas de seguinte forma:

* Agrupadas por alíquota que o contribuinte possuir débito. O sistema irá separar ISS Devido na Saída do ISS Retido na Entrada.
* São geradas também as guias referentes ao depósito Judicial. Estas Guias são agrupadas por município que foi efetuado o depósito, independente da alíquota. Neste caso NÃO é preenchido o campo de alíquota na tela desta guia
* Para cada nota do período de apuração se o parâmetro "Gerar  ISS por Nota Fiscal" na etapa 3 – Apuração do ISS no processo 03.02.03 – Apuração do ISS – Parâmetros por filial estiver marcado. Neste caso a separação por alíquota continuará sendo feita.
* Uma guia para cada município dos itens dos lançamentos se o parâmetro "Usa Município de Prestação de Serviço no Item do Lançamento", na etapa 2 - Regras de apuração do ISS – Construção Civil. Neste caso a separação por alíquota continuará sendo feita. Este parâmetro pode ser utilizado juntamente com o parâmetro para gerar guia de ISS por Nota Fiscal.

#ffffff#514d49Defaults por Município

A partir da versão 12.1.33 é possível configurar os Default abaixo para facilitar a gestão das guias de ISS

0Data de VencimentoData de Vencimento

Através do Cadastro do Município| Anexos | Dados Fiscais do Município, poderá ser configurado um dia de vencimento default do ISS, e neste caso, durante a geração das guias de ISS, o processo irá considerar o dia de vencimento que foi definido para cada município.

Caso não esteja preenchido no município, será considerado a data de vencimento do período de apuração.

Exemplo

Cadastro do Município| Anexos | Dados Fiscais do Município

Dia de vencimento informado, no exemplo abaixo a guia será gerada com data de vencimento no dia 10 de cada mês:

Guia gerada:

Cli/For na integração com FinanceiroCli/For na integração com Financeiro

Através do Cadastro do Município| Anexos | Dados Fiscais do Município, é possível indicar um Cliente/Fornecedor Default por município

Para gerar Lançamentos Financeiros com o Default dos "Dados Fiscais" no cadastro do Município, basta configurar a opção "Utilizar Cliente/Fornecedor do Município" que o processo irá respeitar o cli/for definido para cada município de cada guia.

Imagem

Se o Default não estiver preenchido para algum município o processo irá apresentar uma mensagem indicando que o município não foi configurado e o Lançamento financeiro não será gerado.

648432
