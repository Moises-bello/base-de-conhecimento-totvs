---
content_hash: d44311ce631818bc8749ccec80e1fb227a3b95ab91421b0ab1d868f8c87765ef
fetched_at: '2026-06-29T00:09:31.734033+00:00'
page_id: '425458699'
product: rm
source: tdn-rm
title: Impressão de Boletos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458699
version: 3
---

---

Os boletos são gerados automaticamente quando os seus respectivos lançamentos financeiros são gerados e podem fazer referência a um único lançamento financeiro ou a vários, quando os lançamentos forem gerados *agrupados*.

Para imprimir os boletos existentes, selecione-os e acesse o processo **Imprimir boleto**, disponível nos processos da tela de visão de Boletos e também na tela de visão de Contratos. Na visão dos contratos serão impressos todos os boletos para o contrato selecionado, exceto aqueles que estejam com o status igual a *Cancelado*. Em seguida, selecione o relatório que deverá ter sido criado previamente no TOTVS Gestão Financeira e mande imprimir.

**Observações:**- O relatório para impressão dos boletos, criado no TOTVS Gestão Financeira, deve possuir o campo CODAPLICACAO = Fluxus e deve utilizar as fórmulas de IPTE e de geração de código de barras do financeiro.

- A fonte de dados principal do relatório deverá ser do tipo Tabela da Base e o valor selecionado para essa fonte tem que ser a tabela de boletos (FBOLETO).

- O parâmetro do sistema **,** disponível em *Ambientes | Parâmetros | Educacional | Tesouraria | Relatórios* é responsável por controlar a impressão realizada diretamente no Educacional de boletos provenientes de convênios de cobrança registrada que ainda não tenham sido registrados nos bancos.
