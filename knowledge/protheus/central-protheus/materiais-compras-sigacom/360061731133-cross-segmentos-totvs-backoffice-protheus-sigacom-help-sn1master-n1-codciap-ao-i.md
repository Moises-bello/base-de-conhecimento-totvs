---
article_id: 360061731133
category: Materiais - Compras (SIGACOM)
content_hash: 1a85a662afa75b661f698d393c1782c305874f055eda971d9c841e1ab9399570
fetched_at: '2026-06-28T22:41:18.966453+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help SN1MASTER - N1_CODCIAP
  ao inclcuir um Documento de Entrada ( MATA103 )
type: support-article
updated_at: '2022-05-16T21:11:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061731133-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-SN1MASTER-N1-CODCIAP-ao-inclcuir-um-Documento-de-Entrada-MATA103
---

**Ocorrência**

Ao tentar incluir um documento de entrada de um ativo imobilizado o sistema apresenta a mensagem SN1MASTER - N1\_CODCIAP

**Ambiente**  
Protheus – Compras – A partir da versão 12.1.16  
  
**Causa**Este incidente ocorre pois módulo de Compras não possui as informações para preenchimento de todos os campos do Ativo. Quando um dos campos que não são preenchidos pelo Compras for obrigatório, será exibida a mensagem de alerta. Na versão 11, não existia esta validação, causando inconsistência no Ativo Fixo, pois vários campos obrigatórios ficavam em branco.  
  
**Solução**Para solucionar a inconsistência será necessário desmarcar a obrigatoriedade do campo N1\_XXXX e/ou N3\_XXXX no dicionário de dados para correta integração.

Nos casos que não é possível desativar a obrigatoriedade, poderá ser configurado um inicializador padrão nos campos que precisam ser obrigatórios ou então utilizar o ponto de entrada abaixo:

MA103ATF -> <http://tdn.totvs.com/pages/viewpage.action?pageId=319783498>

***Saiba Mais :***

* [Ponto de Entrada - MA103ATF](http://tdn.totvs.com/pages/viewpage.action?pageId=319783498)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
