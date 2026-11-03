---
article_id: 360035326313
category: RH - Relatórios Folha
content_hash: 1b5a2bbe3ae86a63691e0ed558d3275534c79b4ea65a00d921a9af244704869c
fetched_at: '2026-06-28T22:43:17.413501+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Ao emitir o relatório de Folha de pagamento(GPER040),
  é impresso o cabeçalho da filial logada
type: support-article
updated_at: '2025-08-04T11:23:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035326313-RH-Linha-Protheus-GPE-Ao-emitir-o-relat%C3%B3rio-de-Folha-de-pagamento-GPER040-%C3%A9-impresso-o-cabe%C3%A7alho-da-filial-logada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26003013417239) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Ao realizar a impressão do relatório de Folha de Pagamento rotina**(GPER040)**, o sistema emite no cabeçalho a filial que esta logada.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Por regra do produto, o  Protheus possui um **cabeçalho padrão** que é apresentado na impressão da maioria dos relatórios do sistema.  
Este cabeçalho mostra as informações referentes à geração do relatório, como por exemplo, nome e título do relatório, versão do sistema, data e hora de emissão e a **empresa/filial logada no momento da execução.**Foi criado o parâmetro **MV\_EMPCABE** para possibilitar que o Administrador determine se as informações da empresa/filial deverão ser impressas nos relatórios, com as seguintes opções.

* .T. – Imprime as informações da empresa/filial no cabeçalho padrão (Padrão do sistema);
* .F. – Não imprime as informações da empresa/filial no cabeçalho padrão.

Para configurar acesse o Configurador SIGACFG em Ambiente > Cadastros > Parâmetros (CFGX017), pesquise pelo MV\_EMPCABE e configure conforme a necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31435148306455)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31435202133015)

**Saiba Mais**  
[Artigos Gestão de Pessoal](%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
