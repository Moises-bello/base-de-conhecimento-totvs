---
content_hash: 3f4319297fd600be848721563b692a9250f803dabd7da05d17256dfec5740538
fetched_at: '2026-06-29T00:08:59.698947+00:00'
page_id: '364910647'
product: rm
source: tdn-rm
title: Ignora Ausência Planejada - Portal RH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364910647
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Automação de Ponto |
| **Versões:** | 12.1.19 |
| **Passo a passo:** | Neste documento será demostrado a nova funcionalidade incluída no Portal RH: o cadastro de **Ignorar Ausência Planejada**.  Acessando o Anexo do Espelho de Cartão de Ponto, será possível realizar o lançamento de Ignorar Ausência Planejada. Com este registro, mesmo existindo cadastro de um intervalo de refeição para o dia, e o funcionário não efetuar as batidas do almoço, será desconsiderado o intervalo de refeição e o sistema irá computar as horas extras para o funcionário.  Segue abaixo o passo a passo para realizar este cadastro:    **Acessar RM.exe | Serviços Globais | Segurança | Acesso | Perfis**  Neste cadastro, deverá realizar a alteração da permissão do item [11.01.21] Ignorar Ausência Planejada      **Portal RH | Automação de Ponto | Espelho do Cartão | Anexos | Ignorar Ausência Planejada**  Utilize esta opção para realizar a inclusão de um novo registro de Ignorar Ausência Planejada. Será exibido uma janela para realizar este cadastro.  Utilize esta opção para exclusão de um registro já existente.  Utilize esta opção para a edição e modificação de um registro já existente.      Nesta tela deverá ser informado o período a ser considerado no registro de Ignorar Ausência Planejada. Poderá ser informado período de apenas um dia ou mais dias.  Segue abaixo algumas considerações deste cadastro:   * Não poderá ser cadastrado data fora do período Atual e Ativo; * Não poderá ser cadastrado data final menor que data Inicial; * Os campos De e Até são de preenchimento obrigatório; * O cadastro de Ignorar Ausência Planejada irá definir o campo IGNORAINTREF com o valor "1" da tabela AIREFFUN. |
| **Observações:** |  |
