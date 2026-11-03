---
article_id: 24511855484183
category: Materiais - Compras (SIGACOM)
content_hash: 9412f9b02e3c132ced4726ecd6c6cc91bf15947c20b7d9d269e9a3cf1ec576ec
fetched_at: '2026-06-28T22:41:21.978924+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O que fazer quando
  o "Clique Aqui" no email do formulário não está habilitado? Novo Fluxo de Compras
  - NFC (PGCA010).
type: support-article
updated_at: '2025-11-12T14:30:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24511855484183-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-fazer-quando-o-Clique-Aqui-no-email-do-formul%C3%A1rio-n%C3%A3o-est%C3%A1-habilitado-Novo-Fluxo-de-Compras-NFC-PGCA010
---

**Dúvida**  
O que fazer quando o "Clique Aqui" no email do formulário não está habilitado?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24620474778519)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2210.  
  
**Solução**

Quando o link para o formulário não está habilitado para preenchimento da cotação será necessário realizar a validação abaixo:

O conteúdo do parâmetro **MV\_WFBRWSR** deve sempre começar com **http://**, pois este parâmetro armazena o endereço do formulário, e é necessário que seja reconhecido como um link válido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24512275575959)

**Importante:**

**1 -** Se o seu ambiente estiver hospedado no CLOUD da TOTVS, será necessário solicitar ao time de CLOUD o endereço e a porta para configurar o Workflow no Novo Fluxo de Compras.

**2 -** Se o seu ambiente for local, você deve validar com sua equipe de Infraestrutura para determinar o IP e a porta necessários para configurar o Workflow no Novo Fluxo de Compras.

Além disso, certifique-se se o IP e porta estão devidamente liberados em seu firewall. Também deve ser validado se trata-se de um endereço externo ou interno.

**Observação:**

Se, ao clicar no link, a página ficar carregando e gerar um erro como "Não é possível acessar esse site" ou "ERR\_RESPONSE\_HEADRS\_TRUNCATED, será necessário entrar em contato com sua equipe de Infra (se for base local) ou entrar em contato com o Suporte Cloud Protheus (se sua base estiver hospedada no T Cloud) para que eles possam fornecer o link e a porta corretos para utilizar no Workflow do Novo Fluxo de Compras. Esse link e porta corretos deverão ser preenchidos no parâmetro **MV\_WFBRWSR**, como explicado acima.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36281190771607)

****Saiba Mais:****

[Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
