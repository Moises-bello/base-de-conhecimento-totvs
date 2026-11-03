---
article_id: 360012521571
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 69891a1a1219e636d1e2e23a83e094b397c9098b1e86cdedfc06766c95e17775
fetched_at: '2026-06-28T22:41:48.243477+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA240 - Aquisição
  de imobilizado e classificação de compras
type: support-article
updated_at: '2026-05-27T18:14:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012521571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Aquisi%C3%A7%C3%A3o-de-imobilizado-e-classifica%C3%A7%C3%A3o-de-compras
---

**Dúvida**Como classifico/cadastro um ativo fixo?

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo fixo  – A partir da versão 11.8  
  
  
**Solução**

Através do documento de entrada, na aquisição de um bem ocorre a integração com o ativo fixo, que após sua classificação, efetivamente se torna um ativo  que passa a calcular depreciação.

A geração do bem no  modulo do ativo, ocorrerá ou não de acordo com a configuração da "TES" no modulo de compras. Nesta configuração através do campo F4\_ATUATF (Atual.Ativo) deve-se configurar como SIM, que Indica que o Ativo Imobilizado deve ser atualizado, quando ocorrer a  entrada de uma nota, que utilizará esta "TES".

É possível determinar tambem  através de configuração na TES se o bem será gerado para o ativo desmembrando a quantidade quando tem mais de uma unidade, ou para não desmembrar, que é realizado através do campo F4\_BENSATF (Desm.IT.Atf) 

A integração das informações  do ativo para o modulo contábil, acontece após executar rotina  classificação de compras (ATFA240).

* Para as integração com o modulo contábil, é necessário configurar lançamento padrão 801.

[Parâmetros e configurações para o ativo fixo](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/atfa010_ativo_fixo.htm)

[Importante! Classificação de Compras](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/atfa240_classificacao_de_compras.htm)

**Saiba Mais**

[Tabelas ativo fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020439351-MP-SIGAATF-Tabelas-do-Ativo-Fixo)

[Classificação do Bem não gatilha conta contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006575352-MP-SIGAATF-Ao-classificar-um-bem-o-sistema-n%C3%A3o-carrega-a-conta-cont%C3%A1bil)
