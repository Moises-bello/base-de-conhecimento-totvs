---
article_id: 26765684014231
category: Rental by ItUp Business
content_hash: 1798bfe798c0a9aa1e8e39152f050a810071de789e66d5be809f77dc85be5cbf
fetched_at: '2026-06-28T22:36:20.632112+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Estorno da Remessa e Faturamento
type: support-article
updated_at: '2026-01-21T12:58:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26765684014231-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Estorno-da-Remessa-e-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26765683971351) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Estorno de Faturamento e Remessa.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Solução**  
O estorno da Remessa e Estorno é realizado pela rotina de Exclusão de Documento MATA521A seguindo a ordem do ultimo para o primeiro faturamento.  
A exclusão deve ser feita da última para a primeira ocorrência. Isso se deve ao fato de que o SIGALOC realiza atualizações no ciclo de locação conforme cada faturamento é processado. Se a exclusão for feita fora dessa ordem, o sistema pode se desorganizar, resultando em dados inconsistentes e possíveis erros no ciclo de locação.  
  
Procedimento para Exclusão de Faturamentos:  
1- Identifique a ordem dos faturamentos: Verifique a sequência cronológica dos faturamentos automáticos registrados.  
  
2- Exclua do último para o primeiro: Comece a exclusão pelo faturamento mais recente e prossiga até o mais antigo. Isso garante que o sistema mantenha a integridade dos dados e atualizações do ciclo de locação.  
  
**Saiba mais:** [Estorno de faturamento e remessa](https://tdn.totvs.com/x/w5MdMw)
