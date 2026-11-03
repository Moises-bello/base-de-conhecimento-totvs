---
article_id: 39957002202007
category: SIGAACD - Automação e Coleta de Dados
content_hash: 3e8a9755b291c04d13a777999bb63006260de7507752e2b0d8704f7f1adfb9fa
fetched_at: '2026-06-28T22:39:11.367777+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Ao excluir a Pré-Nota
  não excluir a tabela CB0.
type: support-article
updated_at: '2026-04-23T13:57:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39957002202007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Ao-excluir-a-Pr%C3%A9-Nota-n%C3%A3o-excluir-a-tabela-CB0
---

No SIGAACD, ao excluir uma Pré-Nota, os registros permanecem na tabela CB0 para garantir rastreabilidade e auditoria via rotina ACDA130. O relacionamento com o documento fiscal é limpo no campo CB0\_NFENT, permitindo nova geração de etiquetas sem perder o histórico, preservando a integridade das informações.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39957002188055) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como funciona a usabilidade do parâmetro MV\_CBPE002 no SIGAACD?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Na exclusão da Pré-Nota os registros permanece na tabela CB0,  esse comportamento é intencional e alinhado ao controle de rastreabilidade do sistema. Há um mecanismo de log de etiquetas que registra a geração e o histórico dessas informações para fins de auditoria e consistência operacional, que seria a rotina ACDA130.

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39956994866583)![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39956994866839)

Apesar de a etiqueta gerada pelo documento fiscal não ser deletada no padrão do sistema, o relacionamento com o documento fiscal é devidamente limpo no campo **CB0\_NFENT** , permitindo que novas etiquetas sejam geradas caso o mesmo documento seja incluído novamente.

Exclusão das etiquetas na tabela  CB0 impactaria na perda do relacionamento com o log, comprometendo a integridade das informações.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
