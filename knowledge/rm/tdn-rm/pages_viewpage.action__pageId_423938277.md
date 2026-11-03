---
content_hash: 008473d8d6255ebd3749fe3a96e9e845d7c05822ec76d957542ba9226ff789cd
fetched_at: '2026-06-29T00:09:26.137272+00:00'
page_id: '423938277'
product: rm
source: tdn-rm
title: Grupo de Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938277
version: 5
---

Responsável por agrupar patrimônios fazendo com que todas as informações e parametrizações definidas neste grupo possam ser aplicadas a cada patrimônio associado a ele.

Ao solicitar a inclusão de um novo grupo de patrimônio deve ser preenchida a aba de identificação, sendo que os campos código do grupo e descrição (campo livre) são obrigatórios. O Título amarrado e taxa default são parametrizações importantes, porém, opcionais. Amarrando um título ao grupo de patrimônio o sistema irá preencher o grupo automaticamente, quando realizado cadastros de patrimônios vinculados aquele título.

Após salvar o cadastro, na aba Identificação será habilitado o , além de uma nova aba chamada "Default Cenário/Grupo Patrimonial" ser apresentada.

No  é possível informar os dados que irão compor a contabilização de ocorrências (baixa, acréscimo ou transferência monetária) tais como conta contábil, filial, departamento, entre outros.

O  será utilizado caso o item do evento esteja parametrizado da seguinte forma:

* Buscar default:Tabela Default
* Grupo de Patrimônio e Origem da Conta: Tabela Default

Qualquer processo realizado no patrimônio está diretamente ligado ao correto preenchimento da aba "Default Cenário/Grupo Patrimonial", pois, nesta será definido os cenários de cálculo default para o grupo.

Clicando no botão "incluir" deverá ser inserido o cenário de cálculo e os eventos que este cenário irá utilizar. Perceba que para uma ocorrência, depreciação, contabilização e transferência ser executada corretamente, é necessário realizar vínculos entre cenário, cálculo, evento contábil e grupo de patrimônio.

Veja os passos a serem seguidos no exemplo abaixo:

1) Cadastrar Cálculos:

01 - Cálculo Principal de depreciação

02 - Cálculo para segunda moeda

2) Cadastrar Cenários de Cálculo:

01 - Cenário de Cálculo Padrão

Neste cenário de cálculo foi associado o ID Cálculo 1

02 - Cenário de cálculo para segunda moeda

Neste Cenário de Cálculo foi associado o ID Cálculo 2

3) Cadastrar Grupo de Patrimônio:

Veículos

Este grupo de patrimônio foi associado o cenário 01- Cenário de Cálculo Padrão, dentro deste inserido Eventos Contábeis de Aquisição, depreciação, baixa...)

Neste grupo também foi vinculado o cenário 02- Cenário de cálculo para segunda moeda, dentro deste inserido Eventos Contábeis de Aquisição, depreciação, baixa...)

**Observação**

Antes de excluir um grupo de patrimônio deve-se conferir se existem informações cadastradas no seu respectivo  default de cenário e campos complementares. Caso haja deve-se excluir primeiro estas informações e depois o grupo de patrimônio.

Anexos

* Default Cenário/Grupo Patrimonial
Informações complementares

* Adicionar Campo Complementar
