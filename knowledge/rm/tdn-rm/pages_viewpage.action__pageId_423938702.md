---
content_hash: 07569991abb5f13a14743634f6388f5fcefea7dcc40944ea4a4547d4b2c2c951
fetched_at: '2026-06-29T00:09:28.539361+00:00'
page_id: '423938702'
product: rm
source: tdn-rm
title: Exercício Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938702
version: 7
---

Você sabia?

Você sabia que o tamanho do Período Contábil em aberto é diretamente responsável pela performance do módulo contábil?

É dessa forma porque, ao calcular o saldo de uma conta contábil, o sistema precisar varrer TODOS os lançamentos contábeis daquela conta, desde o início do período contábil!

Portanto, para melhorar a performance do sistema, utilize com frequência a opção de Fechamento do Exercício Contábil (Escrituração Contábil | Exercícios | Fechar exercício). **Nossa sugestão é manter no máximo dois anos em aberto.**

Esse processo tira os lançamentos contábeis das tabelas principais do sistema, movendo-os para uma tabela de Histórico, armazenando o saldo do período em tabelas específicas.

E não se preocupe, pois o sistema consegue emitir os relatórios normalmente a partir do Histórico. Além disso, se precisar desfazer o fechamento, basta executar o processo de Reabrir Exercício Contábil.

No módulo Contábil, Exercício Contábil não é nada mais que o intervalo de datas no qual é possível manipular os Lançamentos Contábeis (incluir, editar e excluir), respeitando, é claro, a Data de Fechamento (trava de segurança para não permitir a inclusão de Lançamentos Contábeis em período já conciliado e fechado pelo setor contábil).

Tendo isto como base, o sistema possui alguns processos específicos para manipulação desse período.

**IMPORTANTE!** Nas informações do histórico contábil o usuário não poderá fazer alterações ou exclusões, podendo apenas visualizar os registros e relatórios. Caso tenha a necessidade de modificar um exercício já fechado, o usuário deverá reabrir o último exercício fechado, desta forma, o sistema retornará com todas as informações do Histórico Contábil para a Manutenção de lançamentos.

Quando não for mais necessário a consulta do histórico dos lançamentos, o usuário poderá apagar um exercício contábil histórico. Desta forma todos os registros relacionados àquele exercício serão apagados da base de dados através do processo de Liberação de Exercício, permanecendo apenas o saldo do exercício que foi liberado. Mas lembre-se: o processo de **Liberação do Exercício é irreversível**!

Detalhamento do Saldo Inicial

* Fechar Exercício Contábil
* Reabrir Exercício Contábil
* Liberar Exercício Contábil
* Histórico de Contabilização
