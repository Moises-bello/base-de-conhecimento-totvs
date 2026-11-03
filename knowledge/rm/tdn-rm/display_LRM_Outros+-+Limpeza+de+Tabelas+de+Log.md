---
content_hash: 197740261fa315f6306a69b274d7c4e87ff506d7b439f3304492650e0da78f86
fetched_at: '2026-06-29T00:09:46.537713+00:00'
page_id: '435104828'
product: rm
source: tdn-rm
title: Outros - Limpeza de Tabelas de Log
type: documentation
url: https://tdn.totvs.com/display/LRM/Outros+-+Limpeza+de+Tabelas+de+Log
version: 3
---

É um processo que executa limpeza das tabelas de log da Venda, Item da Venda, Regra Componentes, Parcela Pagamento e Parcela Componente. O usuário informa o período de tempo onde deverá existir informações do log.

Por default é realizado a limpeza em lotes de 10.000 registros, mas que podem ser definidos pelo usuário, tendo o seu valor mínimo de 100 registros.

No processo é possível informar o tempo (em anos) de permanência dos registros conforme as situações da venda no qual está vinculado. Segue as situações da vendas onde é possível determinar diferentes tempos de permanência do log

* Efetivada
* Em preparação
* Quitada
* Cancelada
* Bloqueada
* Distrato Bilateral
* Distrato Unilateral
* Inadimplência
* Outros

O período informado para cada situação é de no mínimo 1 ano;  
 Esse processo pode ser agendado quando se estiver utilizando um ambiente 3 camadas.   
Para esse processo existe uma opção nos Parâmetros do "TOTVS Incorporação" onde será possível definir se os campos serão habilitados ou não e seus valores defaults. Para saber mais clique aqui
