---
content_hash: 68c8e74c45702e13d12640d1debcb8630c06b6c32ce2381a3b9ac18a175e9a08
fetched_at: '2026-06-29T00:11:11.081119+00:00'
page_id: '645472349'
product: rm
source: tdn-rm
title: TOTVSAudit
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVSAudit
version: 22
---

**Produto**: TotvsAudit

**Versão**: A partir da 12.1.31

**SGBD**: Oracle e SQL Server

**Introdução:**

O Log de Auditoria serve como um histórico para que sejam feitas todas as inclusões, alterações e exclusões que vierem a ocorrer na(s) tabela(s) selecionada(s) para serem auditadas. Ele é composto por uma série de Procedures, onde é(são) selecionada(s) uma tabela(s) a ser(em) auditada(s), criando-se uma "**Tabela Espelho**" em um **Schema** exclusivo do Log de Auditoria(**TOTVSAUDIT**) e **Trigger(s)**no banco de dados, dependendo da ação escolhida (**Insert, Update, Delete**).

Quando houver transações que utilizam a(s) tabela(s) selecionada(s), a Trigger é disparada e grava na tabela de Log (**ZAUDITCHANGES**) as informações sobre o autor da ação: os dados que foram criados, alterados ou deletados são salvos na "Tabela Espelho"  (Ex.: TOTVSAUDIT.PFUNC, tabela espelho a tabela do sistema RM.PFUNC).

**Obs.** Campos do tipo Memo(Text),nulo por definição da ferramenta não são auditáveis.

Estas informações podem ser consultadas através de QUERY´s no banco de dados ou através da interface do usuário do Log de Auditoria.

**\*Atenção** : é recomendável utilizar a TAG **<add key="UseRMUser" value="true" />** nos arquivos **RM.Atualizador** e **RM.TotvsAudit.** No caso desta configuração, apenas usuários do sistema RM poderão executar a atualização da base e configurar o TotvsAudit. Usuários do banco de dados não poderão realizar essas ações com a TAG "UseRMUser" ativa.

**Processos do TOTVS Audit**

* [Pré Requisitos para migração e utilização do Novo L](https://tdn.totvs.com.br/pages/viewpage.action?pageId=645486062)[og](https://tdn.totvs.com.br/pages/viewpage.action?pageId=645486062)
* [Requisitos validados no TOTVS Audit](https://tdn.totvs.com/display/LRM/Requisitos+validados+no+TOTVS+Audit)
* [Habilitando o TOTVS Audit](https://tdn.totvs.com.br/display/LRM/Habilitando+o+TOTVS+Audit)
* [Configurando o TOTVSAudit](https://tdn.totvs.com.br/display/LRM/Configurando+o+TOTVSAudit)
* [Configuração de Proteção de Dados (LGPD)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=645475098)
* [Expurgo de Dados armazenados pelo TotvsAudit](https://tdn.totvs.com.br/display/LRM/Expurgo+de+Dados+armazenados+pelo+TotvsAudit)

Dicas importantesTempo de espera ao ativar o TOTVSAudit

Ao ativar o TOTVS Audit as tabelas passam a ser auditadas instantaneamente. O RM armazena a informação sobre o envio do contexto de auditoria em um cache, o qual expira após 10 minutos, sendo aconselhável, desta forma, reiniciar o RM Host após a ativação do TOTVS Audit para limpar os caches.

Grants importantes para base Oracle

GRANT ALTER ANY TABLE, CREATE ANY TABLE, DROP ANY TABLE, DELETE ANY TABLE, SELECT ANY TABLE, INSERT ANY TABLE, UPDATE ANY TABLE, CREATE ANY INDEX, DROP ANY INDEX, CREATE ANY SEQUENCE, DROP ANY SEQUENCE, SELECT ANY SEQUENCE TO RM;
