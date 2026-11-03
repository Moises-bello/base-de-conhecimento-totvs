---
article_id: 360020261731
category: Materiais - Compras (SIGACOM)
content_hash: 306c6179dbc5bac7fd2dec27b416da49d13fdb9709a0445afdd4e494ca65dcaa
fetched_at: '2026-06-28T22:41:15.739910+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como desabilitar mensagem
  de validação de Nota Fiscal Origem no Documento de Entrada ?
type: support-article
updated_at: '2022-05-16T21:21:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020261731-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-desabilitar-mensagem-de-valida%C3%A7%C3%A3o-de-Nota-Fiscal-Origem-no-Documento-de-Entrada
---

**Dúvida**

Como desabilitar mensagem de validação de Nota Fiscal Origem no Documento de Entrada ?

Permite ao usuário que desabilite a validação do ítem da nota fiscal original informada nas operações de devolução ou complemento de preço/impostos.

**Ambiente**Protheus - Compras - A partir da versão 11.80

**Solução**Permitir ao usuário escolher se a mensagem de consistência será exibida ou não.

Este parâmetro permite a utilização da "Nota Fiscal Origem" de outro sistema sem a apresentação do assistente de consistência quando a nota fiscal original não for encontrada na base de dados do sistema Protheus.

O parâmetro "***MV\_VLDNFO***" não isenta o utilizador de informar um número de documento e série nas operações de devolução ou complemento de preço/impostos quando estiver com conteúdo falso (.F.)  
O número e série do documento original devem corresponder à numeração existente no livro de escrituração fiscal.

Acesse o “Configurador (SIGACFG)”, opção “Ambientes/Cadastros/Parâmetros” (CFGX017):  
***Nome:*** MV\_VLDNFO

***Descrição:*** Validar se a nota fiscal original existe no sistema (Consiste número/série/item)

***Tipo:*** Lógico

***Cont. Por.:***  .T.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
