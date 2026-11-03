---
article_id: 360007824751
category: RH - Dissídio
content_hash: 7e0213bcb2006e3f3c2d5f6abeb5febbb8142934dfbee77273f54e349437eed2
fetched_at: '2026-06-28T22:43:43.339288+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Dissídio retroativo, o que analisar quando não
  calcula valores de férias
type: support-article
updated_at: '2026-05-21T19:12:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007824751-RH-Linha-Protheus-GPE-Diss%C3%ADdio-retroativo-o-que-analisar-quando-n%C3%A3o-calcula-valores-de-f%C3%A9rias
---

**Dúvida**O que analisar quando no cálculo do dissídio retroativo o sistema não gera verbas de férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução**Primeiramente verifique se toda parametrização necessária foi realizada, segue **manual do dissidio retroativo**: <http://tdn.totvs.com/pages/releaseview.action?pageId=220889925>   
A rotina de dissidio passou por uma série de atualizações para corrigir os últimos problemas de conhecimento de Suporte Técnico.   
Por este motivo, **Mantenha sempre o ambiente devidamente atualizado.**

**Verifique os itens abaixo:**  
- A SRR pode estar sem informações ou com informações incorretas;  
- Verifique se a data de recebimento das férias estão iguais nas tabelas SRH e SRR, campos "Dt.Rec.Fer." -   **RH\_DTRECIB** e "Data Pagto.' - **RR\_DATAPAG**;  
- As verbas de férias não estão com as amarrações corretas;  
- As verbas pagas podem não estar na SRD;  
- O roteiro de férias pode não estar nas tabelas de períodos ou estar sem data de integração ou fechamento.  
- Verificar se a sequência 000780 - **S\_CADIFFER(),** dentro do roteiro de cálculo "**FOL**" está desabilitada. Em caso afirmativo, habilitar e refazer o cálculo do dissídio (Atualizações -> Definições de Cálculo -> Roteiros de cálculo -> Roteiro FOL).  
**Observação**: a sequência 000740 - **S\_CADIFFER()** deve permanecer desabilitada.  
- Verificar se a sequência 000390  - **S\_BMEDFER(),** no roteiro FER está desabilitada. Em caso afirmativo, habilitar para SIM.  
- Se houver preenchimento da Tabela S040, verificar se todos os campos estão preenchidos corretamente. Para essa validação, caso tenha dúvidas se a tabela S040 está impactando no cálculo de dissídio, efetue um cálculo de férias exatamente igual uma matrícula que não é calculada a verba de férias no dissídio e verifique se é apresentada a mensagem de Erro no preenchimento na tabela S040.

**Saiba Mais:**

[Artigos Relacionados a Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
