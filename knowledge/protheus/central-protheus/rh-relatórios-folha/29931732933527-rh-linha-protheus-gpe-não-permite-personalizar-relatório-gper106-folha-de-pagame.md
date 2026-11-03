---
article_id: 29931732933527
category: RH - Relatórios Folha
content_hash: 7cfea9b24d298f0e495eb4d124ac8be38ce405a0a414cad78a604a80587d2e2f
fetched_at: '2026-06-28T22:43:17.532444+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Não permite Personalizar relatório GPER106 - Folha
  de Pagamento
type: support-article
updated_at: '2025-02-12T14:03:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29931732933527-RH-Linha-Protheus-GPE-N%C3%A3o-permite-Personalizar-relat%C3%B3rio-GPER106-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29931732919703) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao incluir um campo na personalização do relatório da Folha de Pagamento GPER106, Sistema traz a mensagem: Atenção! A configuração deste relatório não permite a inclusão de campos do usuário. Estes campos do usuário. Estes campos poderão ser desconsiderados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29931743079447)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**Este relatório, por conceito do sistema, não pode de fato ser personalizado, pois além de ser sumarizado (utiliza variáveis para impressão), também utiliza QUERY com UNION (para melhoria de performance).

Sendo assim, mesmo quando os campos são padrões do Sistema, ele não permitirá a inclusão de novos campos para personalização.

**Sabia mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
