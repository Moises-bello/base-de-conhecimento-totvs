---
content_hash: 1eb17173ece2bff7bc8a43aa76084872b522a8acdc555bc735fd42a2ef672baf
fetched_at: '2026-06-29T00:09:21.852152+00:00'
page_id: '422545926'
product: rm
source: tdn-rm
title: Bloco M - e-LALUR e e-LACS
type: documentation
url: https://tdn.totvs.com/display/LRM/Bloco+M+-+e-LALUR+e+e-LACS
version: 13
---

Este bloco contém as informações do Livro Eletrônico de Apuração do Lucro Real (e-Lalur) e do Livro Eletrônico de Apuração da Base de Cálculo da CSLL (e-Lacs). Ele é composto pelos seguintes registros.

BLOCOMleftM001M001

**Abertura do Bloco M**

Este é um registro de controle gerado automaticamente pelo processo da rotina que informa se existe ou não movimentação no bloco M.

M010M010

**Identificação da Conta na Parte B do e-Lalur e do e-Lacs**

Este registro é gerado com base nas informações das contas cadastradas no LALUR parte B.

M030M030

**Identificação dos Períodos de Apuração das Empresas Tributadas pelo Lucro Real**

Este registro será gerado para o regime de lucro real através da identificação dos Períodos de Apuração incluídos para os tributos IRPJ e CSLL. Será gerado uma linha para cada par de Tributo (IRPJ  CSLL).

M300M300

**Lançamentos A do e-Lalur**

As informações deste registro serão geradas a partir do detalhamento da Apuração do tributo IRPJ, considerando-se apenas os itens de Adições do Lucro, Adições por Doação, Exclusões do Lucro e Compensação de Prejuízo. Este registro só será gerado se os itens citados possuírem o código da tabela dinâmica da ECF associado a eles no Evento Tributário.

M305M305

**Conta da Parte B do e-Lalur**

Este registro será gerado sempre que existir no Registro M300 informação gerada a partir de um item de Evento Tributário que tenha sua origem na parte B do Lalur.

M310M310

**Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lalur**

Este registro será gerado sempre que existir no Registro M300 informação gerada a partir de um item de Evento Tributário que tenha sua origem em Contas Contábeis. [Ver regras aplicadas a este registros nas informações complementares.](http://tdn.totvs.com/pages/viewpage.action?pageId=422546047)

M312M312

**Números dos Lançamentos Relacionados à Conta Contábil**

Neste registro serão listados os lançamentos contábeis que compõe os registros M300 originados de Itens do Evento Tributário que tenham sua origem em Contas Contábeis e o tipo seja diferente de Saldo Atual. [Ver regras aplicadas a este registros nas informações complementares.](http://tdn.totvs.com/pages/viewpage.action?pageId=422546034)

M315M315

**Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento**

Este registro não será gerado.

M350M350

**Lançamentos da Parte A do e-Lacs**

As informações deste registro serão geradas a partir do detalhamento da Apuração do tributo CSLL, considerando-se apenas os itens de Adições do Lucro, Adições por Doação, Exclusões do Lucro e Compensação de Prejuízo. Este registro só será gerado se os itens citados possuírem o código da tabela dinâmica da ECF associado a eles no Evento Tributário.

M355M355

**Conta da Parte B do e-Lacs**

Este registro será gerado sempre que existir no Registro M350 informação gerada a partir de um item de Evento Tributário que tenha sua origem na parte B do Lalur.

M360M360

**Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lacs**

Este registro será gerado sempre que existir no Registro M350 informação gerada a partir de um item de Evento Tributário que tenha sua origem em Contas Contábeis. [Ver regras aplicadas a este registros nas informações complementares.](http://tdn.totvs.com/pages/viewpage.action?pageId=422546047)

M362M362

**Números dos Lançamentos Relacionados à Conta Contábil**

Neste registro serão listados os lançamentos contábeis que compõe os registros M350 originados de Itens do Evento Tributário que tenham sua origem em Contas Contábeis e o tipo seja diferente de Saldo Atual. [Ver regras aplicadas a este registros nas informações complementares.](http://tdn.totvs.com/pages/viewpage.action?pageId=422546034)

M365M365

**Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento**

Este registro não será gerado.

M410 M410 

**Lançamento na Conta da Parte B do e-Lalur e do e-Lacs sem reflexo na Parte A**

Neste registro serão gerados os lançamentos da parte B do Lalur excluindo aqueles que tiverem sido detalhados nos registros M300 e M350.

M415M415

**Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento**

Este registro não será gerado.

M500 M500 

**Controle de Saldos das Contas da Parte B do e-Lalur e do e-Lacs**

Este registro não será gerado pois o PVA o gerará automaticamente a partir do saldo inicial e das movimentações das contas do Lalur.

M510M510

**Controle de Saldos das Contas Padrão da Parte B do e-Lalur e do e-Lacs**

Este registro não é gerado.
