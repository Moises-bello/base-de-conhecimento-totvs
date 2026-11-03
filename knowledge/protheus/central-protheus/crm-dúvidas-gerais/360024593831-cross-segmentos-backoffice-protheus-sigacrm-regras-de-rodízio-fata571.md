---
article_id: 360024593831
category: CRM - Dúvidas Gerais
content_hash: e5679903a81946954bc19313e0b27d125f769cd4a5662069260bcc0a1639fcc8
fetched_at: '2026-06-28T22:40:27.501669+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Regras de Rodízio (FATA571)
type: support-article
updated_at: '2024-03-21T14:58:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024593831-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Regras-de-Rod%C3%ADzio-FATA571
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22239034596631) Tempo aproximado para leitura: **00:03:00 min****Dúvida**

Como configurar as "Regras de Rodizio" (**FATA571**)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - Todas as Versões  
  
**Solução**

Este cadastro permite definir as faixas de valores que serão comparadas com as faixas de valores provenientes do cadastro do Suspect ou Prospect, de acordo com o tipo de regra escolhido. Define e mantém a posição do vendedor na fila do rodízio.

Deverá ser cadastrada uma regra para cada vendedor que fará parte da fila.

O vendedor que não constar neste cadastro não entrará na fila e será desconsiderado no processamento do rodízio.

Ao ser cadastrado, o vendedor ocupará o último lugar na fila.

* **Procedimentos**

Para cadastrar uma Regra de Rodízio:

1. Em Cadastro/Cenário de Vendas/Regras de Rodízio, clique em "Incluir".  
O sistema apresenta a tela de inclusão.

2. Cadastre o vendedor e as regras a ele vinculadas.  
3. Preencha os dados conforme orientação do help de campo.  
4. Confirme.  
Se o campo "Contas" for selecionado, serão disponibilizados:

• Vendedor - verifica se a quantidade de contas do vendedor atingiu o limite e este será barrado.  
• Subordinados - verifica se a quantidade de contas dos subordinados atingiu o limite e o vendedor/gerente de vendas será barrado.  
• Ambas - verifica se a quantidade de contas do vendedor somadas às dos subordinados atingiu o limite e o vendedor/gerente de vendas será barrado.

* **Exemplo de Regra de Rodízio**

Parâmetros utilizados no Atendimento ao Suspect ou Prospect

* MV\_TMKSEV = Código da severidade (Prospect com reserva)
* MV\_VENDPAD = Vendedor padrão
* MV\_FATCON = Limite de contas padrão

A rotina Rodízio de Vendedores avalia o Suspect ou Prospect no atendimento  Call Center e define o vendedor para atendê-lo. Esta avaliação depende das regras de Rodízio cadastradas anteriormente. Para melhor entendimento veja o exemplo com descrição do processamento interno demonstrado em 3 fases:

**Saiba mais**:

[Regras de Rodízio](https://tdn.totvs.com/x/EC_IGw)
