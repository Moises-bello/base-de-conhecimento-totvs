---
article_id: 12784134072855
category: RH - Relatórios Folha
content_hash: 5a69e31a260fa1dbb6cb0d74b606409c20f3b5ef59c494021c7e4c3d586fa3e3
fetched_at: '2026-06-28T22:43:17.536413+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando o relatório GPER040 - Folha
  de Pagamento é gerado em branco
type: support-article
updated_at: '2025-08-04T11:59:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12784134072855-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-relat%C3%B3rio-GPER040-Folha-de-Pagamento-%C3%A9-gerado-em-branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23658830077719) Tempo aproximado para leitura: **00:03:00 min****Dúvida**O que verificar quando o relatório **GPER040 - Folha de Pagamento**, é gerado em branco?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de pessoal - Todas as versões  
  
**Solução**Verifique, de acordo com os parâmetros informados, se:   
  
1. O **Período informado** existe em Atualizações - Definições de Cálculo - Períodos;  
2. Faça a seleção nos parâmetros, **através do F3 - Lupa**, para que o **sistema carregue o número de pagamento** corretamente de forma automática;  
3. Caso esteja imprimindo de **Período Aberto**, verifique em **Consultas - Cadastros - Genéricos, a tabela SRC - Movimento mensal**, para certificar-se de que **existem dados para o processo, no período** informado nos parâmetros;  
4. Caso esteja imprimindo de **Período Fechado**, verifique em **Consultas - Cadastros - Genéricos, a tabela SRD - Movimento Acumulado**, para certificar-se de que **existem dados para o processo, no período** informado nos parâmetros.  
5. Verifique se a **LIB** do ambiente está **atualizada:** <https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/LIB>   
  
**Saiba Mais**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
