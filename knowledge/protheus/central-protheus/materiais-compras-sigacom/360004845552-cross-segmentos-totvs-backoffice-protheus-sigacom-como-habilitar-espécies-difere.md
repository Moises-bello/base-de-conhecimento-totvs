---
article_id: 360004845552
category: Materiais - Compras (SIGACOM)
content_hash: 3c4ee0c3de7a14e990b87daac7c570d432bca95a699d6e099d25c1dab0d02a16
fetched_at: '2026-06-28T22:41:07.662330+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como habilitar espécies
  diferentes de SPED e CTE no campo F1_CHVNFE para validação de Chave da DANFE ?
type: support-article
updated_at: '2026-02-18T20:39:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004845552-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-habilitar-esp%C3%A9cies-diferentes-de-SPED-e-CTE-no-campo-F1-CHVNFE-para-valida%C3%A7%C3%A3o-de-Chave-da-DANFE
---

**Dúvida**  
Como habilitar espécies diferentes de SPED e CTE no campo F1\_CHVNFE para validação de Chave da DANFE ?

**Ambiente**  
Protheus – Compras – A partir da versão 11.80  
  
**Solução**

O parâmetro MV\_CHVESPE tem a funcionalidade de definir quais Especies de Nota Fiscal permite a geração da Chave da DANFE. Assim a espécie criada na tabela 42 poderá ser informada no parâmetro mencionado para que o sistema habilite o campo F1\_CHVNFE no momento de inclua a nota de entrada.

Como exemplo informado no parâmetro a espécie NFA e NF separados por pipe (|)

Caso não tenha o parâmetro MV\_CHVESPE na SX6 poderá criá-lo conforme print abaixo:

![Capturar.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006237592)

**Observação:**

Exceto espécies de Notas de Serviço. Por exemplo: **NFS, NFSE, NFSC e NFST**

Para preenchimento da chave da nota fiscal de serviço, confira o artigo a seguir:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como inserir a chave das notas fiscais de serviço para as espécies (NFS, NFSE, NFSC, NFST) no Documento de Entrada MATA103?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29834438924439-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-inserir-a-chave-das-notas-fiscais-de-servi%C3%A7o-para-as-esp%C3%A9cies-NFS-NFSE-NFSC-NFST-no-Documento-de-Entrada-MATA103)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como inserir a chave das notas fiscais de serviço para as espécies (NFS, NFSE, NFSC, NFST) no Documento de Entrada MATA103?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29834438924439-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-inserir-a-chave-das-notas-fiscais-de-servi%C3%A7o-para-as-esp%C3%A9cies-NFS-NFSE-NFSC-NFST-no-Documento-de-Entrada-MATA103)
