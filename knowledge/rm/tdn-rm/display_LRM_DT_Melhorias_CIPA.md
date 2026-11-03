---
content_hash: 2a3cf313a9b4029bac1a8ef8a041d07417cd04e28957abd6fa197fc31bf19856
fetched_at: '2026-06-29T00:06:06.897876+00:00'
page_id: '201733127'
product: rm
source: tdn-rm
title: DT_Melhorias_CIPA
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Melhorias_CIPA
version: 11
---

# COMISSÕES DA CIPA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Segurança e Saúde Ocupacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | **Cadastro de Comissão da CIPA** | **Melhorias da CIPA** | |
| **Versões/Release:** | *12.1.7* |

## Descrição

```
O objetivo deste documento é descrever as funcionalidades relacionadas a Comissões CIPA.
```

## Procedimento para Utilização

Cadastro de Comissões da CIPA: **Cadastros / CIPA / Comissões d****a CIPA**Cadastro de Candidatos de Eleições CIPA: **Cadastros / CIPA / Comissões da CIPA / Candidatos**Cadastro de Representantes da CIPA: **Cadastros / CIPA / Comissões da CIPA / Representantes**Portal: **Portal / CIPA / Candidatar**Portal:**Portal / CIPA / Votar**

No Cadastro de Comissões da CIPA é possível vincular quantas seções desejadas, desde que sejam da filial informada no momento do cadastro. As seções são informadas em um *lookup*que só estará disponível se a Filial for informada. Se o usuário trocar a filial, todas as seções que tenham sido informadas deverão ser removidas.

Só é permitido fazer a vinculação de seções no momento da criação de uma Comissão da CIPA. Após ser salva, as seções serão apenas para visualização. Pode ser vinculadas somente seções "folha".

Nas Comissões da CIPA, funcionários com situação “E” (Estatutário), não podem participar de eleições, seja votando ou candidatando-se. No cadastro de Comissões da CIPA é possível informar os tipos de funcionários que poderão participar de uma eleição CIPA. A validação do tipo de funcionário, que era fixa, foi ajustada para respeitar os tipos definidos no cadastro da comissão.

O cadastro de candidatos nas eleições, permite que sejam incluídos apenas funcionários da seção que foi informada no Cadastro da Comissão da CIPA. A partir do momento que várias seções podem ser vinculadas à Comissão, funcionários de todas essas seções poderão ser incluídos como candidatos.

A inclusão de candidatos permite que sejam vinculados apenas funcionários dos tipos estabelecidos no cadastro da comissão.  
Na apuração do resultado de eleições de CIPA, devem ser considerados para o cálculo os funcionários das seções e dos tipos definidos no cadastro da comissão.  
  
A inclusão de representantes da CIPA, seja como representante do empregado ou do empregador, permite que sejam vinculados apenas funcionários dos tipos estabelecidos no cadastro da comissão.

Quando são incluídos representantes dos empregados, deve ser indicado um candidato participante da eleição da CIPA. Consequentemente ele deverá pertencer a uma seção informada no cadastro da Comissão, pois isso é necessário para que ele tenha entrado na eleição. A regra, que é persistida no momento da indicação do candidato, deverá ser estendida para ser contemplada na indicação de representante dos empregados.  
  
Nas opções de Votação e Candidatura do Portal, o usuário só visualiza opções que permitam que ele interaja.  
Caso a Comissão da CIPA tenha em seu cadastro o vínculo com uma ou mais seções, o funcionário logado só poderá votar ou se candidatar na eleição dessa comissão se ele pertencer a uma das seções vinculadas. Além disso, deverá ser um tipo de funcionário contemplado entre os tipos permitidos de acordo com o cadastro da comissão.

O sistema permite que um funcionário que se candidatou a uma eleição da CIPA pelo Portal e em seguida cancelou sua candidatura, possa novamente se candidatar. Isso é feito apagando a data de cancelamento, o que fará com que a candidatura volte a ficar ativa.  
Não haverá histórico de candidaturas e cancelamentos.

- Como a vinculação de seções e tipos de funcionários é feita apenas na criação de comissões da CIPA, não é possível editar os dados das comissões já existentes na base de dados. Apenas os novos registros tem esse recurso disponível.
