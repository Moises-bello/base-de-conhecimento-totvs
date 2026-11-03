---
content_hash: 3189b70a1969fa64a0063b989333b6abc4b0cb43529d1b0340d56017e03186f7
fetched_at: '2026-06-29T00:09:32.318298+00:00'
page_id: '425458823'
product: rm
source: tdn-rm
title: Contabilização por Competência - Parametrizações necessárias no TOTVS Gestão
  Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458823
version: 3
---

---

Contabilizar é basicamente transformar um fato monetário em informações contábeis que se dá através da geração de um ou vários *lançamentos contábeis* registrando assim os fatos ou transações ocorridas nas empresas, permitindo um gerenciamento e controle patrimonial, assim como a apuração dos resultados das empresas.

Os lançamentos contábeis serão incluídos diretamente no TOTVS Gestão Contábil através das *contas contábeis*, registrando-as a débito e também a crédito com os seus respectivos valores.

Para gerar um lançamento contábil é necessário então alguns cadastros prévios dentro do TOTVS Gestão Contábil: 

* Contas contábeis e Contas gerenciais\*

As contas contábeis utilizadas para contabilização dos lançamentos deverão estar previamente cadastradas no sistema contábil. Este cadastro é feito no sistema contábil no menu *Cadastros | Plano de Contas | Contábil*.

Se forem utilizadas contas contábeis que tenham distribuição gerencial, as contas gerenciais também devem estar previamente cadastradas no sistema contábil no menu *Cadastros | Plano de Contas | Gerencial.*

Estas contas serão utilizadas nos *defaults* e nos *eventos contábeis*.

* Período Contábil\*

O período contábil ou exercício contábil, determina o período em que o sistema contábil poderá receber movimentações contábeis. Este período é definido dentro dos parâmetros do sistema contábil no menu *Ambiente | Parâmetros | TOTVS Gestão Contábil | Fechamento | Fechamento do Exercício| Período Contábil.*

A Data Inicial é informada uma única vez, ao iniciar a utilização do TOTVS Gestão Contábil, não podendo ser alterada manualmente, somente através da execução de processo específico do sistema contábil.

A Data Final pode ser alterada a qualquer momento e indica até que data máxima o sistema contábil poderá receber movimentações contábeis.

A Data de Fechamento também pode ser alterada a qualquer momento e indica uma data limite até a qual o sistema contábil não poderá sofrer manutenção (inclusão e/ou alteração) em suas movimentações. Na prática ela indica até que data a conciliação contábil fá foi realizada, bloqueando assim qualquer alteração na movimentação contábil no período entre a data inicial e a data de fechamento.

Portanto, os lançamentos a serem gerados pelo TOTVS Educacional devem estar dentro do período contábil permitido para receber lançamentos.

* Período do Usuário para manutenção em lançamentos contábeis\*

Período para Manutenção de Lançamentos Contábeis do usuário é um período em que o usuário tem permissão para incluir, alterar ou excluir lançamentos contábeis. Este período deve estar compreendido dentro do Período Contábil que é definido nos parâmetros do sistema contábil.

Qualquer tentativa de incluir, alterar ou excluir lançamentos contábeis fora do período definido para manutenção será barrada pelo sistema. Este período deve ser definido dentro do sistema contábil no menu *Utilitários | Alteração do Período para Manutenção de Lançamentos Contábeis.*

Portanto, os lançamentos a serem gerados pelo TOTVS Educacional devem estar compreendidos no período em que o usuário tem permissão para gerar lançamentos.

* Lotes\*

Os Lotes são utilizados no TOTVS Gestão Contábil para armazenar lançamentos contábeis que ainda estão em período de conferência. Cada sistema que integra com o sistema contábil deverá ter um Lote exclusivo para armazenar suas movimentações, sendo eles identificados no sistema por um código numérico. Nos parâmetros do TOTVS Educacional devem ser indicados dois números de Lotes distintos e exclusivos: um para receber as contabilizações geradas e outro para receber estornos realizados para estas contabilizações. Ao indicar os dois números de Lotes no TOTVS Educacional, estes serão automaticamente criados dentro do TOTVS Gestão Contábil e poderão ser consultados dentro do sistema contábil através do menu *Escrituração Contábil | Operações Contábeis | Lotes*.

Depois que a conferência ou conciliação contábil for realizada dentro do TOTVS Gestão Contábil, estes lançamentos que estão em *Lote N* serão integrados ao Lote oficial da contabilidade, conhecido como *Lote 0* (lote zero).

Os lançamentos contábeis que têm origem externa ao TOTVS Gestão Contábil ficam bloqueados para qualquer manutenção dentro do sistema contábil. As manutenções necessárias deverão ser feitas diretamente nos seus sistemas de origem.
