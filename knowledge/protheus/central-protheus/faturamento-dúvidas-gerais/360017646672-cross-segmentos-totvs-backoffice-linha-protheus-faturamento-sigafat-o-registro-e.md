---
article_id: 360017646672
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 65085b1c1046db3640fcfa2886a4e80560415d85b9f542688e81db9b16b9065a
fetched_at: '2026-06-28T22:38:29.914194+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - O registro encontra-se bloqueado por outro usuário
type: support-article
updated_at: '2022-09-26T17:01:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017646672-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-O-registro-encontra-se-bloqueado-por-outro-usu%C3%A1rio
---

**Ocorrência**

Ao alterar um registro gera o Help: Mensagem: O registro número X do Arquivo X encontra-se Bloqueado por outro usuário.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) - a partir da release 11.80.

**Causa**

Esta inconsistência pode acontecer nas situações abaixo:

 1º Registro Bloqueado por outros Usuários (possivelmente com instância presa);

2º Parâmetros que auxiliam na resolução da reserva de registros;

3º Customizações / Personalizações em seu ambiente.

**Solução**

Para solucionar, acesse a F.A.Q. para entendimento do processo e efetue as avaliações propostas:

1-  Em caso de registro bloqueado por outro usuário, uma opção paliativa rápida é reiniciar o servidor (parando os serviços do TOP, Banco de dados e Server);

2- Desabilite os parâmetros **MV\_GNRENF** e deixe **MV\_FATTRAV = 4**

3-Em caso de customizações ou personalizações no ambiente, tente efetuar um teste com um RPO padrão baixado do portal e com os pontos de entradas desabilitados no catálogo de personalizações do Configurador

**Para mais detalhes, acesse: [O registro encontra-se bloqueado por outro usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=329024248)**
