---
article_id: 36394665774359
category: Financeiro - Análise de Crédito Financeiro
content_hash: 663a9fe639ac51ec2356debe636e0379235329af363bd4025a41a07cab8aad53
fetched_at: '2026-06-28T22:37:25.535677+00:00'
product: protheus
section_id: 36607745462423
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINAPP001 - Tabelas
  utilizadas na rotina
type: support-article
updated_at: '2025-12-23T23:18:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36394665774359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINAPP001-Tabelas-utilizadas-na-rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36394665765399) Tempo aproximado para leitura: **08:00 min**

**Dúvida:**  
Onde são gravadas as informações de ajuste de crédito do cliente na rotina FINAPP001?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - 12.1.33 e superiores  
  
**Solução:**

A análise de crédito utiliza a tabela de **histórico de crédito do cliente (F7F)**e **SA1** (Clientes).  
Para que as informações sejam registradas corretamente e as linhas de histórico apareçam na rotina, é indispensável que **ambas estejam configuradas com o mesmo nível de compartilhamento**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36394675195031)

Caso esse alinhamento não exista, o sistema pode deixar de gravar os dados adequadamente, exigindo a correção por um analista especialista in loco.

Além dessas tabelas, os arquivos anexados (upload de documentos) são armazenados nas tabelas **ACB** e **AC9**, seguindo o padrão da base de conhecimentos.

Para que o sistema permita o envio e o download desses arquivos, é necessário que o **agente local** esteja habilitado no ambiente.
