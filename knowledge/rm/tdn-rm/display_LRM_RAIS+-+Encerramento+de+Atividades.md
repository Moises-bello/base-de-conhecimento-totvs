---
content_hash: 4c2f7e2f085ea3fcbf127e3c576f68b901f2c6906ba1f05106798846e26f810d
fetched_at: '2026-06-29T00:10:16.519779+00:00'
page_id: '471938754'
product: rm
source: tdn-rm
title: RAIS - Encerramento de Atividades
type: documentation
url: https://tdn.totvs.com/display/LRM/RAIS+-+Encerramento+de+Atividades
version: 12
---

# Como gerar a RAIS de Encerramento de Atividades

|  |  |
| --- | --- |
| **Produto:** | TOTVS RM - Folha de Pagamento |
| **Versões:** | 12.1.28.267 ou Superiores  12.1.29.222 ou Superiores  12.1.31.125 ou Superiores |
| **Observações:** | Conforme consta no [manual](http://www.rais.gov.br/sitio/rais_ftp/ManualRAIS2020.pdf)de orientação da RAIS do ano base 2020, no caso de encerramento de atividades no decorrer do ano atual, o estabelecimento poderá antecipar a entrega da declaração, utilizando o programa GDRAIS2020.  Ainda conforme o manual, a data de desligamento dos empregados é obrigatória e deverá ser menor ou igual à data de encerramento de atividades do estabelecimento. |

Para gerar a RAIS de encerramento de atividades pelo TOTVS RM - Folha de Pagamento, o estabelecimento deverá informar no cadastro da seção respectiva, aba RAIS / CAGED / eSocial,  sua data de encerramento, conforme figura abaixo:

Caso a seção tenha sido encerrada no ano atual e não exista validador disponível para este ano, poderá ser gerada a RAIS antecipada, utilizando o último layout disponível e também o último validador disponível.

Como pré requisito, ao escolher o ano base de geração da RAIS, o usuário deverá colocar o ano de encerramento do estabelecimento.

Foi criado um parâmetro específico para encerramento de atividades nos parâmetros específicos da coligada. Este parâmetro irá filtrar apenas as seções que possuam data de encerramento cadastrada, para geração da RAIS de encerramento antecipada.

Ao marcar o parâmetro "Encerramento de Atividades", será exibido a mensagem **"Para gerar a RAIS de encerramento de atividades, os funcionários da seção encerrada deverão ter data de demissão anterior à data de encerramento de atividades cadastrada. O campo Ano Base da tela inicial deverá corresponder ao ano de encerramento"**.

No caso de encerramento das atividades, em anos-base anteriores, os estabelecimentos deverão utilizar o programa GDRAIS Genérico, conforme consta no .

Para maiores informações, gentileza consultar o da RAIS atualizado.

Conforme ultima publicação, caso o estabelecimento tiver tido a baixa do seu cadastro no ano de 2020, mas aguardou o programa GDRAIS 2020, não precisa preencher o campo "encerramento de atividade".
