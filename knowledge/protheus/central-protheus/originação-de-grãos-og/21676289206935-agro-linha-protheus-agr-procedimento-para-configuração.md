---
article_id: 21676289206935
category: Originação de Grãos (OG)
content_hash: 2b952fbaa273297e7a4168cc74080b9ba4c3ba71fe46c706d7a9fa576984e904
fetched_at: '2026-06-28T22:45:43.400665+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Procedimento para Configuração
type: support-article
updated_at: '2025-07-12T10:54:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21676289206935-Agro-Linha-Protheus-AGR-Procedimento-para-Configura%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21676251201687) Tempo aproximado para leitura: **00:00:45 min****Dúvida**  
Como atualizar o vinculo das tabelas de outros módulos com o Romaneio?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12.1.21  
  
**Solução**  
Para que a rotina de vínculo das tabelas possa ser executada deve-se adicionar ao menu do Sistema de Gestão Agroindústria, **SIGAAGR**, uma opção para executar o programa **OGX175**.

Ao executar a rotina o programa irá buscar todos os registros de romaneio cuja situação estiver diferente de cancelados **Status = 4** e irá gerar o vínculo das tabelas relacionadas quando este ainda não existir. A rotina poderá ser executada mais de uma vez, entretanto, somente irá gerar os registros quando algum dos relacionamentos estiver faltando.

Importante: Para os novos romaneios, gerados a partir da versão 12.1.21, os vínculos para as tabelas relacionadas serão criados por padrão, não sendo necessário executar a rotina.

## **Tabelas**

As tabelas serão gravadas ao executar o processamento da rotina **OGX175**:

**N8J → Relaciona os registros do pedido: SC5**

**N8I → Relaciona os registros de itens do pedido: SC6**

**N8H → Relaciona os registro da NF: SF2**

**N8K → Relaciona os registros do item da NF: SD2**

**N8L → Relaciona os registros de Títulos: SE1**
