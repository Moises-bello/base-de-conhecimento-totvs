---
article_id: 360052009614
category: RH - Dissídio
content_hash: 287842befbad5dda79fbc8c06849ea98e1ef4f775152565fcfc280ac777f08a5
fetched_at: '2026-06-28T22:43:43.188896+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Ao calcular dissidio, sistema apresenta mensagem
  de Período Integrado  e não calcula
type: support-article
updated_at: '2025-08-08T14:53:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052009614-RH-Linha-Protheus-GPE-Ao-calcular-dissidio-sistema-apresenta-mensagem-de-Per%C3%ADodo-Integrado-e-n%C3%A3o-calcula
---

**Dúvida**Ao calcular dissidio, sistema apresenta mensagem de Período Integrado e não calcula.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução**Sistema apresenta mensagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083250294)

Essa mensagem aparece porque o cálculo de dissídio já foi integrado para a folha de pagamento através da opção Outras Ações -> Geração dentro da rotina do dissídio. Na coluna Geração Folha apresentará um S (Sim), de que ocorreu a integração do cálculo para a folha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17490859582999)

Neste caso, havendo necessidade de recálculo será necessário voltar o backup de todas as tabelas que são atualizadas no momento da geração:

* **SRA** - Cadastro de funcionário;
* **SR3** e **SR7** - Histórico Salarial;
* **SRC** - Cálculo de Folha de Pagamento (caso já tenha ocorrido cálculo da folha após integração);
* **RHH** - Dissídio Retroativo;
* **RGB** - Lançamentos por Funcionário (considerando se os valores foram integrados para Lançamentos mensais)
* **SRK** - Lançamentos Futuros (considerando se os valores foram integrados para Lançamentos futuros)

**Saiba Mais:**  
[Página Centralizadora do dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
