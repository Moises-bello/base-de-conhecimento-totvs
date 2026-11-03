---
article_id: 31959868961559
category: Inspeção de Processos (SIGAQIP)
content_hash: f7bf4a3da81fef20dfe784cbfdf9496dbc41620c3b72f87bf37bded411435f46
fetched_at: '2026-06-28T22:42:25.860080+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Módulo não está implantado - Fale com
  a TOTVS e faça a implantação do módulo! (getProcessInspectionList)
type: support-article
updated_at: '2025-06-04T13:03:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31959868961559-Manufatura-Linha-Protheus-SIGAQIP-M%C3%B3dulo-n%C3%A3o-est%C3%A1-implantado-Fale-com-a-TOTVS-e-fa%C3%A7a-a-implanta%C3%A7%C3%A3o-do-m%C3%B3dulo-getProcessInspectionList
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31959864264215) Tempo aproximado para leitura: **00:00:45 min****Ocorrência**Ao utilizar o **APP Minha Produção - Inspeção de Processos** é apresentada a mensagem **Módulo não está implantado - Fale com a TOTVS e faça a implantação do módulo! (getProcessInspectionList)**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**A mensagem ocorre quando o parâmetro **MV\_QIPMAT - Indica se o módulo de Insp.de Processos está integrado com materiais** está com conteúdo igual a **N - Não**, ou quando estiver com conteúdo igual **S-Sim**, porém, ainda **não existe Ordem de Produção ou Apontamento integrado** para ser inspecionado na rotina **QIPA215 - Resultados**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Altere o conteúdo do parâmetro **MV\_QIPMAT para S-Sim**.  
2. Crie uma **Ordem de Produção ou Apontamento** para ser inspecionado na rotina **QIPA215 - Resultados**.  
  
**Observação**  
No artigo a seguir encontra-se o passo a passo para i**ntegrar uma Ordem de produção ou Apontamento com o SIGAQIP**: [Manufatura - Linha Protheus - SIGAQIP - Parametrizações necessárias para integrar uma OP ou apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021385511-Manufatura-Linha-Protheus-SIGAQIP-Parametriza%C3%A7%C3%B5es-necess%C3%A1rias-para-integrar-uma-OP-ou-apontamento)
