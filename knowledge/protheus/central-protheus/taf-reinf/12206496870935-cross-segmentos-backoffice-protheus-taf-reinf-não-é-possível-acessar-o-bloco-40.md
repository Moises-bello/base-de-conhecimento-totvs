---
article_id: 12206496870935
category: TAF - REINF
content_hash: 1acdc9d9e97399f03edb8b9e4f3d616b1c2d4beb4183803795e6888b41642b34
fetched_at: '2026-06-28T22:41:34.726904+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - REINF - Não é possível acessar
  o bloco 40 no Painel REINF.  '
type: support-article
updated_at: '2023-08-15T21:59:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12206496870935-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-N%C3%A3o-%C3%A9-poss%C3%ADvel-acessar-o-bloco-40-no-Painel-REINF
---

**Dúvida**O Ambiente foi atualizado, porém único bloco disponível no painel REINF é o bloco 20.

**Ambiente**Microsiga Protheus - Automação fiscal - TAF- A partir da versão 12.

**Solução** Para correção do problema relatado realize a correção do parâmetro MV\_TAFVLRE, inserindo o conteúdo correto: 2\_01\_02

[Automação Fiscal - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233-Automa%C3%A7%C3%A3o-Fiscal-CONFIGURADOR-Como-acessar-os-par%C3%A2metros-do-sistema-?source=search)

 Após correção do parâmetro reinicie o seu Smartclient, acesse o ambiente novamente.

![2.2 Painel.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16794576030871)

Importante: Recomendamos a aplicação dos pacotes primeiramente em ambiente de homologação para que seja possível realizar os testes com o parâmetro MV\_TAFAMBR = 2 (Ambiente de produção restrita da EFD-REINF). **Atenção**: **não** utilizar o mesmo ambiente que foi transmitido eventos em Homologação para transmitir em Produção.
