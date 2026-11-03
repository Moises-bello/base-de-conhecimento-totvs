---
content_hash: e132c47593b9b72c8b969bd2148caf2476ea7df53dcbd79563fe491a550f820c
fetched_at: '2026-06-29T00:08:36.106938+00:00'
page_id: '284355201'
product: rm
source: tdn-rm
title: Integridade e Autenticidade de DLLs e EXEs
type: documentation
url: https://tdn.totvs.com/display/LRM/Integridade+e+Autenticidade+de+DLLs+e+EXEs
version: 2
---

A partir da **versão 12.1.18** todas as DLLs e EXEs dos ambientes RM.Net, Portal Corpore.Net, Portal frame HTML e Mobile serão assinadas digitalmente durante cada processo de integração contínua. Assinar digitalmente um arquivo tem como finalidade garantir a integridade e também a autoria do mesmo, aumentando assim a confiabilidade de nossa aplicação.

      Entre os fatores que motivaram essa iniciativa, estão:

* Garantir a integridade de nossos executáveis e DLLs, ou seja, que nenhum código malicioso seja “injetado” no arquivo após o deploy da aplicação.
* Aumentar a confiança de nossos clientes em relação aos artefatos distribuídos.
* Mitigar problemas com antivírus, antimalware ou qualquer outro mecanismo de defesa presente nos computadores que executam nossas aplicações.

Desta forma, qualquer arquivo DLL ou EXE que seja criado pela TOTVS a ser liberado para o mercado e/ou cliente deve passar pelo processo de assinatura. Por exemplo, arquivos criados pela fábrica, arquivos alterados por desenvolvedores in loco, arquivos para geração de logs para identificação de problemas, etc.

Para que isso seja possível, criamos um portal para realizar a assinatura de pacotes dessa natureza. Portanto antes de enviar para o cliente qualquer DLL ou EXE, que não faça parte do nosso pacote de liberação padrão, siga o manual abaixo:
