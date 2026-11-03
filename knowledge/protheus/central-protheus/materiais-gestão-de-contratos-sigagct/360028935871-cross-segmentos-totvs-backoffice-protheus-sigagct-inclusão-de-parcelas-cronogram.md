---
article_id: 360028935871
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: b04d78e117320ec2085af8ee57528911eb7f3e463b6e09a09c6fcea04c9d0f55
fetched_at: '2026-06-28T22:37:22.998157+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Inclusão de Parcelas
  / Cronograma e Medições fora da Vigência / Vencimento -  Parâmetro MV_CNFVIGE
type: support-article
updated_at: '2022-12-23T17:11:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028935871-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Inclus%C3%A3o-de-Parcelas-Cronograma-e-Medi%C3%A7%C3%B5es-fora-da-Vig%C3%AAncia-Vencimento-Par%C3%A2metro-MV-CNFVIGE
---

**Dúvida**Inclusão de Parcelas / Cronograma e Medições fora da Vigência / Vencimento - Parâmetro MV\_CNFVIGE  
  
**Ambiente**Microsiga Protheus – Gestão de contratos – A partir da versão 12

**Solução**Com o parâmetro habilitado MV\_CNFVIGE = S será Permitido realizar configuração de parcelas e realização de medições fora do período da vigência do contrato.

Para que seja permitido a medição e inclusão de cronograma dentro do período de vigência do contrato altere o conteúdo para N.

* **Exemplo do parâmetro habilitado *MV\_CNFVIGE = S***

Nesse exemplo foi permitido incluir o cronograma financeiro no contrato com uma data que ultrapassa a data final do contrato.

**Geração do Cronograma (CNTA300)**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030571691/mceclip2.png)

**Cronograma Gerado**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030572871/mceclip4.png)

**Inclusão de Medição (CNTA121)**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030607012/mceclip3.png)

Na imagem acima a data final do contrato é dia 10/07/2019 e nesse foi permitido selecionar a competência do mês 09/2019 para medição.

* **Exemplo do parâmetro habilitado *MV\_CNFVIGE = N***

Nesse exemplo o sistema não permitiu incluir o cronograma financeiro com uma data que ultrapasse a data final do contrato, apresentou o help **CNTA300DAT**.

**Geração do Cronograma (CNTA300)**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030610252/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030610352/mceclip6.png)

***Obs:***

A habilitação do parâmetro ***MV\_CNFVIGE = S*** também é recomendada quando ocorre o Help CNTA300ULT, ao realizar uma revisão de contrato no momento da Atualização de Cronograma Financeiro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11174774921367)

***Saiba Mais:***

[GCT0142\_Utilização do parâmetro MV\_CNFVIGE](https://tdninterno.totvs.com/pages/releaseview.action?pageId=560631740)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
