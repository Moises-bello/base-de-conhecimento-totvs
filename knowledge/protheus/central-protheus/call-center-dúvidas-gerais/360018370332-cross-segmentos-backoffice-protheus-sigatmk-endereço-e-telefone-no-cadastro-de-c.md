---
article_id: 360018370332
category: Call Center - Dúvidas Gerais
content_hash: 5095474b8aff72d7ad2ac603771bf85f440f5ce534f228f0306e29db1e863ff4
fetched_at: '2026-06-28T22:41:26.661543+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Endereço e Telefone no cadastro
  de Contatos TMKA070
type: support-article
updated_at: '2024-04-25T12:59:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018370332-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Endere%C3%A7o-e-Telefone-no-cadastro-de-Contatos-TMKA070
---

**Dúvida**

Endereço e telefone no cadastro de Contatos TMKA070  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

O registro e as alterações de Endereço ou Telefones no cadastro de Contatos devem ser realizadas sempre no grid inferior: **Aba Endereços > Tabela AGA** e **Aba Telefones > Tabela AGB**

Esses campos que transferem a informação para o Cabeçalho - Área superior > Tabela SU5.

Exemplo: Registrar o telefone no campo **AGB\_TELEFO** e cadastrá-lo como padrão no **AGB\_PADRAO** para que seja levado para a SC5.

O Help da rotina (Documento de Referência do Produto acessado através do **Canal de Ajuda**) também formaliza este comportamento:

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/tmka070_contatos.htm>

Podemos cadastrar vários endereços e telefones, entretanto apenas um deve ser definido como padrão, por meio do campo Padrão (Sim ou Não).

A informação definida como padrão é transferida para a área superior da tela e exibida em todas as rotinas que utilizarem o contato.

Observação:

Os campos cadastrais da área superior, inclusive, no dicionário de dados nativo, não possuem propriedade de alteração (no CFG - Configurador); de modo que sejam utilizados apenas como visualização / facilitador.
