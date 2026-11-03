---
article_id: 36076164478103
category: Materiais - Compras (SIGACOM)
content_hash: 934e7e53f70dbd1005709d5375bee159ab98ed2d5e3381b972bb1a0c5b489e67
fetched_at: '2026-06-28T22:41:21.774176+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Erro ao realizar
  o parse do arquivo json
type: support-article
updated_at: '2025-11-03T20:47:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36076164478103-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Erro-ao-realizar-o-parse-do-arquivo-json
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36076219121815) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como solucionar ocorrência do erro: "Erro ao realizar o parse do arquivo json " ao selecionar um fornecedor para a cotação na tela de Necessidade de Compra do Novo Fluxo de Compras?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36076219123607)

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
Para corrigir esse erro, efetue os dois procedimentos abaixo:

**1º passo:**

Por gentileza realize teste em ambiente de Homologação com as atualizações a seguir:

- [Acumulado Compras conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)  
- [Acumulado Gestão de Contratos conforme sua versão](https://tdn.totvs.com/pages/viewpage.action?pageId=679961416)  
- [Acumulado SIGAGCP conforme sua versão](https://tdn.totvs.com/pages/viewpage.action?pageId=679961656)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112215) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168420)

- Smartclient - [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)

- Smartclient WebApp - [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168455)

- DBAccess - [MP - FRAME - Atualização do DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033789713-MP-FRAME-Atualiza%C3%A7%C3%A3o-do-DBAccess?source=search)

Obs: Recomendamos backup e validação primeiramente em ambiente teste.

**2º passo:**

Acesse o **cadastro dos fornecedores** participantes dessa cotação e verifique se há caracteres especiais na **Razão Social** ou **Nome Fantasia**. Se houver, **r****emova o caractere especial** identificado (por exemplo, o símbolo **&**), **s****alve as alterações** e **realize um novo teste** no processo de cotação. **Valide** se o problema foi solucionado.

Conforme demonstra na documentação: [Cadastro de fornecedor - Retirada de caracteres especiais](https://tdn.totvs.com/display/public/PROT/DT+Cadastro+de+fornecedor+-+Retirada+de+caracteres+especiais), o time de produto realizou um tratamento para que caracteres especiais sejam removidos da rotina de cadastro de fornecedores. Portanto se trata de um novo comportamento do sistema. As rotinas do NFC não permitirão caracteres especiais.

**3º passo:**Acesse o cadastro de produto dos produtos selecionados nessa cotação e verifique se há algum caractere especial no nome / descrição do produto.

***Saiba Mais:***

[Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
