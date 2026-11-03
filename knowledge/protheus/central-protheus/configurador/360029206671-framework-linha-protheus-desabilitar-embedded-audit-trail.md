---
article_id: 360029206671
category: Configurador
content_hash: 5c53918d8c090986ae5fcc6bc3303192e766a14a7fc2cdf276e7a205dff29573
fetched_at: '2026-06-28T22:42:19.042830+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Desabilitar Embedded Audit Trail
type: support-article
updated_at: '2025-08-20T11:14:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029206671-Framework-Linha-Protheus-Desabilitar-Embedded-Audit-Trail
---

**Dúvida**  
Como fazer para desabilitar o Embedded Audit Trail?  
  
**Ambiente**  
Protheus - Configurador - A partir da versão 12  
  
**Solução**  
Para desabilitar a funcionalidade de auditoria do Embedded Audit Trail, siga o procedimento abaixo:  
1. Efetue backup da tabela XA4  
2. Acesse o Configurador  
3. Menu Ambiente > Embedded Audit Trail > Aplicador  
4. Na Área Grupo de Empresas, altere a(s) Empresa(s) para o Escopo=Exceção e Operação=Não se Aplica  
5. Na Área Tabela, delete todas as entradas (clique no registro e pressione a tecla DEL)  
6. Clique em Confirmar  
  
Observação: Para consultar no Banco de Dados se foram excluídos os registros, execute a query abaixo:  
  
SELECT \* FROM sys.triggers
