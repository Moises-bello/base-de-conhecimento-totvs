---
article_id: 1500012558701
category: esocial - Periódicos
content_hash: dc598e7745c96c8a0cbeb875ebace6278855a18a8a53dcca5a7412fb3abf9730
fetched_at: '2026-06-28T22:47:09.435277+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Origem da tag nrInsc dos grupos ideEmpregador e ideEstabLot
  do evento S-1200
type: support-article
updated_at: '2024-06-28T18:54:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012558701-RH-RM-FOP-eSocial-Origem-da-tag-nrInsc-dos-grupos-ideEmpregador-e-ideEstabLot-do-evento-S-1200
---

**Dúvida**  
Como validar a tag **nrInsc** dos grupos **ideEmpregador** e **ideEstabLot** gerada no evento **S-1200 a partir do leiaute S-1.0**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Para saber a origem de cada campo, veja as informações no detalhe abaixo:  
  
1. Grupo **ideEmpregador**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019579022)

A tag **nrInsc** do grupo **ideEmpregador** armazena a informação do número de inscrição do contribuinte. Desta forma, sempre irá apresentar as informações da seção do funcionário.

* **nrInsc** = CNPJ ou CPF da seção do funcionário

2. Grupo **ideEstabLot**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019579062)

A tag **nrInsc** do grupo **ideEstabLot** indica o número de inscrição do estabelecimento do contribuinte no qual o trabalhador está lotado. Desta forma, sua origem levará sem consideração os seguintes pontos:

* **nrInsc** = **CNPJ da seção** se a coligada não utilizar tomador de serviço ou, caso utilize, o tomador no qual o funcionário está alocado não se trata de uma obra própria;
* **nrInsc** = **CNPJ do tomador de serviço** quando o tomado no qual o funcionário está alocado referir-se à uma obra própria e, neste caso, o funcionário não estiver associação à um CEI/CNO deste tomador;
* **nrInsc** = **CNO do tomador** quando o tomador no qual o funcionário está alocado se tratar de uma obra própria e o funcionário estiver alocado no CEI/CNO deste tomador.

**Importante**  
Documentação válida somente para leiaute eSocial a partir da versão S-1.0 **Saiba mais**  
Para mais informações acesse:  
      • [Mapeamento do evento S-1200](http://tdn.totvs.com/display/LRM/Evento+S-1200)
