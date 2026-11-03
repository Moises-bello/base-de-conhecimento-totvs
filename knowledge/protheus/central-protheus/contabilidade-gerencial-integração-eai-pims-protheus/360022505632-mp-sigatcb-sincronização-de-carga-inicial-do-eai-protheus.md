---
article_id: 360022505632
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: 214a742ac63061bc831ad9fd7b21e3fa63bb899bae0ac845675e1f095e507fa9
fetched_at: '2026-06-28T22:40:54.156804+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: MP- SIGATCB - SINCRONIZAÇÃO DE CARGA INICIAL DO EAI PROTHEUS
type: support-article
updated_at: '2021-04-28T22:07:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022505632-MP-SIGATCB-SINCRONIZA%C3%87%C3%83O-DE-CARGA-INICIAL-DO-EAI-PROTHEUS
---

**Ocorrência**

Na execução do sincronizador de carga inicial, retorna mensagem que centro de custo já existe e não gera informação no de/para

O centro de custo informado já existe

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019855891/mceclip1.png)  
 **Ambiente**

Protheus  – Contabilidade gerencial – A partir da versão 11.80  
   
 **Causa**

O sincronizador envia registros de um sistema para outro, e como o registro enviado já esta cadastrado no destino, retorna mensagem de que já existe.

**Solução**  
Disponível no configurador,  a rotina de sincronização é um facilitador da integração EAI, que a partir do adapter envia registros essenciais; como cadastro, de um sistema para outro.  
Na geração destes registros as informações no De-Para são geradas automaticamente.

Quando o registro já existe as informações no De-Para não são geradas, e quando o  registro já existe no destino, a opção é excluir o registro no destino e executar a rotina, ou criar as informações no De-Para manualmente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019855811/mceclip0.png)

Para mais detalhes  verifique o Link com informações sobre a rotina disponível na pagina do framework :[Selecionando o adapter para a sincronização inicial](http://tdn.totvs.com/display/framework/O+Sincronizador+de+Carga+Inicial+do+EAI+Protheus)
