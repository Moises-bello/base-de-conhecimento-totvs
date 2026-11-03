---
article_id: 360012396051
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 8a6d56281a570c7034345cf2afbeca29e55a95867024d992a81b83c7be201943
fetched_at: '2026-06-28T22:38:31.100020+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP - FAT - SC00: Error : 955 - ORA-00955: name is already used by an existing
  object'
type: support-article
updated_at: '2021-04-28T15:56:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012396051-MP-FAT-SC00-Error-955-ORA-00955-name-is-already-used-by-an-existing-object
---

**Ocorrência**

Ao abrir a mesma rotina em mais de uma instância, ocorre o erro:SC00: Error : 955 - ORA-00955: name is already used by an existing object

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17

**Causa**

O error.log ocorre quando o sistema tenta criar uma tabela temporária. O nome da tabela fica com “TSC00\_\_” faltando o numero sequencial que difere uma temporária de outras que serão criadas.

Além disso a versão do Oracle do cliente precisa ser 11.2 ou maior.

Somente ocorre em base Oracle, se o cliente estiver em uma versão anterior a 11.2. será necessário atualizar.

**Solução**  
Configure os grants mínimos necessários para o uso de uma base ORACLE : [Oracle - Grants mínimos para o funcionamento do DBAccess](http://tdn.totvs.com/pages/viewpage.action?pageId=329033932)

**Observação:**

* O próprio dbacces verifica se os grants mínimos foram aplicados, a partir da build 18.1.1.0, para maiores informações acesse a faq no tdn, sobre o assunto: [Implementação - Verificação de grants mínimos](http://tdn.totvs.com/pages/viewpage.action?pageId=372551937)
