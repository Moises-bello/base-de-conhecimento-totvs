---
article_id: 360019752011
category: Materiais - Compras (SIGACOM)
content_hash: 4f9e48849da7abf116e9c16c82ca74147d3fdb7349ed20a6335aae607e8c20f9
fetched_at: '2026-06-28T22:41:09.029955+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA020 - Como cadastrar
  fornecedor Estrangeiro no Protheus ?
type: support-article
updated_at: '2024-08-02T20:34:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019752011-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA020-Como-cadastrar-fornecedor-Estrangeiro-no-Protheus
---

**Dúvida**  
Como cadastrar um fornecedor estrangeiro no Protheus?  
  
**Ambiente**PROTHEUS – Compras – A partir da versão 11.80  
  
  
**Solução**

Para cadastrar um fornecedor estrangeiro devem ser preenchidos os campos obrigatórios do padrão, sendo que os campos abaixo devem ser configurados conforme segue.:

Estado (A2\_EST) = EX

Tipo (A2\_TIPO) = X

Município (A2\_MUN) =999999

Bairro (A2\_BAIRRO) = Bairro do Fornecedor

Campos obrigatórios no padrão além dos citados:

Código/loja/Razão Social/N Fantasia/Endereço

O campo de CNPJ/CPF não deve ser informado, pois esta informação não existe para fornecedor estrangeiro, por default/padrão, o campo A2\_CGC não é tratado como obrigatório.

Segue abaixo print da tela de cadastro do fornecedor estrangeiro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23509631489431)

Obs: Caso utilize o campo Cod. Municip (A2\_COD\_MUN) como obrigatório, é necessário criar o link do código de munícipio com o código EX informado no campo Estado (A2\_EST) na tabela CC2.

***Saiba Mais :***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
