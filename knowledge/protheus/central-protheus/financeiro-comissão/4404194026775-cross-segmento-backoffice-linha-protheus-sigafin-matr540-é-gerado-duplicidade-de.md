---
article_id: 4404194026775
category: Financeiro - Comissão
content_hash: e7f54d458ebcf528e95687621e352c78c2f0c9dcabcecd1046f68d435baa78da
fetched_at: '2026-06-28T22:37:50.744731+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - MATR540 - É gerado duplicidade
  de comissões na tabela SE3
type: support-article
updated_at: '2025-03-19T18:32:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404194026775-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-MATR540-%C3%89-gerado-duplicidade-de-comiss%C3%B5es-na-tabela-SE3
---

**Ocorrência**É gerado Duplicidade na tabela SE3 (Comissões).**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - MATA490 - A partir da 12.1.17  
  
**Causa**Ao executar a rotina FINA440, é gerado duplicidade na tabela SE3 (Tabela de comissões)  
  
**Solução**Para que não gere a duplicidade na tabela **SE3** das comissões criadas por meio da emissão da nota ou na baixa do titulo, as tabela **SE3** necessita estar no mesmo nível de compartilhamento das tabelas **SE1** e **SE2** conforme documentação abaixo.  
  
**Saiba Mais**  
<https://tdn.totvs.com/display/public/PROT/FIN0065_Compartilhamento_SE3>
