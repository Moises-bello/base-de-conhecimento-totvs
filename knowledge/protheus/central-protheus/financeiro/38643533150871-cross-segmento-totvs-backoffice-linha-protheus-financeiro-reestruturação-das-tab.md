---
article_id: 38643533150871
category: Financeiro
content_hash: 21bebf29a89a6be472a3c2d5ca0856b2f9ba0a1d28734ec0caf3ae424cfdb254
fetched_at: '2026-06-28T22:38:00.859908+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Reestruturação
  das Tabelas de Movimentação Financeira
type: support-article
updated_at: '2026-02-25T21:12:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38643533150871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Financeiro-Reestrutura%C3%A7%C3%A3o-das-Tabelas-de-Movimenta%C3%A7%C3%A3o-Financeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38643518260503) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
A tabela SE5 deixará de ser utilizada com esta nova reestruturação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Versão 12.1.2210.  
  
**Solução**  
Não. Com o objetivo de preservar a compatibilidade com as customizações atualmente em utilização e evitar impactos operacionais no ambiente, optou-se por **manter a gravação das informações na tabela SE5** (Movimentos e Baixas) de forma paralela às novas tabelas implementadas na reestruturação.

Essa estratégia assegura a continuidade dos processos existentes e das personalizações do cliente, permitindo uma transição mais segura e gradual, sem prejuízo às rotinas já desenvolvidas ou integrações legadas que realizam a leitura direta desta tabela.

Documentação técnica detalhada referente ao novo comportamento após a reestruturação:

[Reestruturação Financeiro - Baixas e Movimento Bancário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=181965434)
