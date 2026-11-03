---
article_id: 8836816075927
category: Materiais - Compras (SIGACOM)
content_hash: 71591258fdfeb5c0f9388a33141bc874d10168b070954b639b4d841bf688b4a4
fetched_at: '2026-06-28T22:41:18.789551+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HeLP : A103BENATF'
type: support-article
updated_at: '2022-09-13T12:11:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8836816075927-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HeLP-A103BENATF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

O help A013BENATF ao incluir Nota Fiscal de Entrada

![a103.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8836583770391/a103.png)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS -  Versão 12  
  
**Solução**

Atualmente, a inclusão do documento de entrada, somente será permitido a inclusão com decimais caso na TES o campo F4\_BENSATF(Indica se desmembra os item gerados no Ativo Fixo a partir da NF) esteja informado igual a 2 (para não desmembrar).

![TES.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8836770024343/TES.png)

1. Alterar no Cadastro de TES o parâmetro "Atual Ativo" para "NÃO";

2. Utilizar uma TES que nãi atualiza ativo Fixo;

3. Não utilizar quantidadaes não inteiras Ex: 123,45, usar 123,00

**SAIBA MAIS EM :**

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)**
