---
article_id: 19087535509271
category: TAF - REINF
content_hash: f9e849df258a613aabe685d08198f85e1765b754b3aef376161a2b81d917f05b
fetched_at: '2026-06-28T22:41:34.845139+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS1196 ao transmitir
  R-4010 com RRA
type: support-article
updated_at: '2023-11-15T14:58:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19087535509271-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1196-ao-transmitir-R-4010-com-RRA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19087573332375) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**

Ao efetuar a transmissão de um documento com retenção de IR onde possui RRA, está ocorrendo a rejeição MS1196 - Número de Processo inválido.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as versões  
  
**Causa**

Esse problema ocorre pois está sendo informado um número de processo judicial quando o tipo de RRA é do tipo 1 - Administrativo.

Conforme o Layout da Reinf, a tag **nrProcRRA** só deve ser informada se o **tpProcRRA** (tipo de Processo RRA) for igual a **2 -** **Judicial**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19087700378135)  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar o cadastro Despesas Processuais/RRA no TAF e efetuar os ajustes conforme o layout:

Se o tipo de RRA for 1 - Administrativo, **não** informar o número de processo.

Se o tipo de RRA for 1, o tipo de origem de recursos também deve ser 1 - Recursos do Próprio Declarante.

2. Excluir a apuração inconsistente pelo menu atualizações > eventos Reinf > periódicos > R-4010.  
3. Apurar e transmitir novamente o evento.

Para avaliar as regras de validação e envio dos eventos, segue link do manual da Reinf:

<http://sped.rfb.gov.br/arquivo/show/7185>
