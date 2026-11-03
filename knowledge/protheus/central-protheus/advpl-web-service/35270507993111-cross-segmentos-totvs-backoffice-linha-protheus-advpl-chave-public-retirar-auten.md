---
article_id: 35270507993111
category: ADVPL - Web Service
content_hash: 6407a9091c75357ff488d78d9a178ce534c77153ec45a0cc73e7acb4673540f4
fetched_at: '2026-06-28T22:40:10.573272+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Chave Public -
  Retirar autenticação de APIs
type: support-article
updated_at: '2025-09-29T14:56:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35270507993111-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Chave-Public-Retirar-autentica%C3%A7%C3%A3o-de-APIs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35270446773527) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possível realizar a requisição de uma API REST sem autenticação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - À partir da versão 12.1.2410  
  
**Solução**  
Para configurar rotas que não exigem autenticação, utilize a chave **Public** na seção **REST**. Ao listar as **APIs** desejadas nessa chave, elas se tornarão públicas e, portanto, não solicitarão autenticação para serem acessadas.

Exemplo de configuração, essa é realizada no **Appserver.INI,** chave **Public**:

|  |
| --- |
| [HTTPENV] URL=/rest PrepareIn=ALL Instances=2,3 ENVIRONMENT=environment CORSEnable=1 AllowOrigin=\* **Public**= api/crm/v1/customerVendor |

**Importante:**

**É altamente recomendável o uso de autenticação em todas as suas APIs, exceto quando estritamente necessário, para garantir a segurança dos seus dados e usuários. A configuração de rotas públicas deve ser feita com cautela.**

**Saiba mais:**  
[**Configuração WebService REST/Server**](https://tdn.totvs.com/pages/releaseview.action?pageId=185747842)
