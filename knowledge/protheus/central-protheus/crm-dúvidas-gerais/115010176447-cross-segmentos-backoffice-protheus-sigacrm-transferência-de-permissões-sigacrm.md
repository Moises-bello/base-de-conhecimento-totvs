---
article_id: 115010176447
category: CRM - Dúvidas Gerais
content_hash: 5a8d150abfdb38378d2df7f67a7db161957c6dd081ba7405ceb05210f2a36d40
fetched_at: '2026-06-28T22:40:27.505131+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Transferência de permissões
  SIGACRM
type: support-article
updated_at: '2024-04-25T12:13:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010176447-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Transfer%C3%AAncia-de-permiss%C3%B5es-SIGACRM
---

**Dúvida**Como efetuar a transferência de permissões?

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12

**Solução**1 - No Módulo **SIGACRM (73)** -> Atualizações -> Vendas-> Contas -> Gestão de contas -> Transferência de contas (**CRMA020**),  existem três opções: **Suspects, Prospects e Clientes**;

2 - Clique a aba da opção desejada, selecione o registro e clique em transferir;

3 - Responder sim para a pergunta “Deseja transferir as contas do vendedor X?”;

4 - Na próxima tela, preencha o código do usuário que receberá a transferência, o código do motivo, a observação e confirme;

5 -Será gravado um novo registro na tabela **AO4** para este usuário que recebeu a transferência.

**OBS: Somente o usuário que atualmente é o detentor do registro consegue transferir a permissão a outro usuário.**

```
Caso apresente o help abaixo para acessar a tela de Transferência de Contas:  
"ESTE VENDEDOR NÃO TEM PERMISSÃO PARA ACESSAR A ROTINA DE TRANSFERÊNCIA DE CONTA!"  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23048486625175)  
Acesse o link que mostra como configurar:   
Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-CRM-Help-na-Transferência-de-Contas-?source=search
```
