---
article_id: 14303772301847
category: RH - MANAD
content_hash: c8bbd1a927597ae9776718d31ed86563f801429188a7194b844f786dd11b3214
fetched_at: '2026-06-28T22:43:33.728294+00:00'
product: protheus
section_id: 360008157193
source: central-protheus
title: RH - Linha Protheus - GPE - MANAD - Rubrica Informativa (PROV_DESC = 'O') Não
  Pode Ser Classificada como Base de Cálculo do IRRF 1
type: support-article
updated_at: '2025-09-19T22:01:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14303772301847-RH-Linha-Protheus-GPE-MANAD-Rubrica-Informativa-PROV-DESC-O-N%C3%A3o-Pode-Ser-Classificada-como-Base-de-C%C3%A1lculo-do-IRRF-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao importar o arquivo MANAD no SVA, é apresentado o erro: "Rubrica Informativa (PROV\_DESC = 'O') Não Pode Ser Classificada como Base de Cálculo do IRRF 1" no Bloco K300:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14302551116695)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**Esse incidente ocorre, quando a verba com Identificador de Cálculo 0167 está configurada como Base Desconto, como no exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14303392056855)  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse: Atualizações / Definições de Cálculo / Verbas (GPEA040), Localize a verba com Id 0167 e verfique se a verba está configurada como Base Desconto. A configuração correta do campo "Tipo do Cod." (**RV\_TIPOCOD**) é 3 - Base Provento.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14303456556823)  
  
2. Verifique se o arquivo MANAD.ini na pasta system está atualizado.  
Caso esteja desatualizado, realize a substituição pelo arquivo anexo.  
  
3. Após alterar o campo "Tipo do Cod." da verba, realize a Contabilização do MANAD e a geração do arquivo novamente.  
Para mais informações sobre o passo à passo para gerar o MANAD [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409142410263-RH-Linha-Protheus-GPE-Como-gerar-o-arquivo-MANAD).

Saiba Mais:

[RH - MANAD](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360008157193-RH-MANAD)
