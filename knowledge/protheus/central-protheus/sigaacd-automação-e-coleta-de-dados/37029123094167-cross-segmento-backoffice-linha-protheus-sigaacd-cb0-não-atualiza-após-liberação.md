---
article_id: 37029123094167
category: SIGAACD - Automação e Coleta de Dados
content_hash: f5d5bf5a56609632eab90830e9c8af59e1f6e5cdbf67f9471631bbb1795b7ea6
fetched_at: '2026-06-28T22:39:11.433336+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - CB0 não atualiza após
  liberação do CQ para o armazém padrão ficando com armazém 98
type: support-article
updated_at: '2025-12-17T12:28:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37029123094167-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-CB0-n%C3%A3o-atualiza-ap%C3%B3s-libera%C3%A7%C3%A3o-do-CQ-para-o-armaz%C3%A9m-padr%C3%A3o-ficando-com-armaz%C3%A9m-98
---

A tabela  CB0 não atualiza após a liberação do CQ para o armazém padrão no TOTVS Protheus. A solução envolve aplicar um pacote de correção que altera a validação de execução em background para uso no app Minha Produção, recomendando backup e aplicação em ambiente de homologação.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37029123086871) Tempo aproximado para leitura: **01:00:00 min**  
  
**Dúvida**  
A tabela CB0 não atualiza após liberação do CQ para o armazém padrão como corrigir ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Solução**  
Alterado a validação de execução em background para uso no app minha produção. Para correção aplicar  o pacote de correção, em sua base de homologação realizando o backup das informações.

12.1.2210: <https://r.totvs.io/p/1229311>

12.1.2310: <https://r.totvs.io/p/1229310>

12.1.2410: <https://r.totvs.io/p/1229309>

 12.1.2510: <https://r.totvs.io/p/1229312>

**Issue TDN:** DMANMAT01-46316  
   
É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
