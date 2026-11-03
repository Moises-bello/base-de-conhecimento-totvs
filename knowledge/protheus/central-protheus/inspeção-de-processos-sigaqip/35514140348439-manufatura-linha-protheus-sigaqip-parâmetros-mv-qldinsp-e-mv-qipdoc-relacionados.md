---
article_id: 35514140348439
category: Inspeção de Processos (SIGAQIP)
content_hash: d49a026e950fee6491fa58fea2ea622ee4f247d3b32a2fdc0bc566044a7e28fe
fetched_at: '2026-06-28T22:42:25.905373+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Parâmetros MV_QLDINSP e MV_QIPDOC relacionados
  à opção Anexos na rotina QIPA215
type: support-article
updated_at: '2025-10-09T17:33:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35514140348439-Manufatura-Linha-Protheus-SIGAQIP-Par%C3%A2metros-MV-QLDINSP-e-MV-QIPDOC-relacionados-%C3%A0-op%C3%A7%C3%A3o-Anexos-na-rotina-QIPA215
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35514148738967) Tempo aproximado para leitura: **00:00:35 min**  
  
**Dúvida**  
No módulo **SIGAQIP - Inspeção de Processos**, na rotina **QIPA215 - Resultados**, qual o conceito do parâmetro **MV\_QLDINSP - Diretorio no Rootpath para salvar anexos inspeção** edo parâmetro **MV\_QIPDOC - Define o diretorio onde serao armazenados os documentos anexados nas Inspecoes - ambiente Inspecao de Processos**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Solução**  
Na rotina QIPA215 - Resultados temos dois parâmetros para anexos, cada qual tem um conceito e comportamento diferente. São eles:  
  
1 - O parâmetro **MV\_QLDINSP - Diretorio no Rootpath para salvar anexos inspeção** define o diretório de salvamentos de **Anexo Amostras** incluídos via **APP Minha Produção**. Seu diretório padrão é system\anexos\_inspecao\ ;  
  
2 - O parâmetro **MV\_QIPDOC - Define o diretorio onde serao armazenados os documentos anexados nas Inspecoes - ambiente Inspecao de Processos** define o diretório de salvamento de anexos incluídos diretamente via rotina **QIPA215 - Resultados**, indo em **Outras Ações > Anexos Ensaio**. Seu diretório padrão é \SYSTEM\DOCS.
