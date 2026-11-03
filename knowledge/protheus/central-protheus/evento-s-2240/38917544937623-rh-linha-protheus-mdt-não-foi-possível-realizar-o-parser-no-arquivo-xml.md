---
article_id: 38917544937623
category: Evento S-2240
content_hash: 082de36d76283920cf3a0087f0a17f05c40982a49df4fa4db88a6f098d73c10b
fetched_at: '2026-06-28T22:45:23.766535+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - Não foi possível realizar o Parser no arquivo XML
type: support-article
updated_at: '2026-03-09T20:50:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38917544937623-RH-Linha-Protheus-MDT-N%C3%A3o-foi-poss%C3%ADvel-realizar-o-Parser-no-arquivo-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38917582344599) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Ocorrência**  
Ao integrar os eventos S-2210, S-2220, S-2221 ou S-2240 do módulo SIGAMDT ao SIGATAF, o sistema apresenta o erro: Não foi possível realizar o Parser no arquivo XML

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38917566465815)

**Ambiente**  
TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
  
**Solução**  
Verifique nas rotinas que compõem o evento a ser integrado se há alguma palavra com caracteres especiais, como ponto e vírgula (;) ou aspas, bem como acentuações.

Caso haja acentuações ou caracteres especiais, remova-os e realize a integração do evento novamente.

**Saiba Mais**  
[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
