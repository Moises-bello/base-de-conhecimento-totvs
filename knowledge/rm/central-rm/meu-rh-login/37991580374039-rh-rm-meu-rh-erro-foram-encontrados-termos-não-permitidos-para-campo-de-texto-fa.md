---
article_id: 37991580374039
category: Meu RH - Login
content_hash: dc6cf7e71978f5cbd98001db91fe39226c0e8ee21c83975bbaeb48a3dbacbc59
fetched_at: '2026-06-28T22:47:27.215122+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Erro "Foram encontrados termos não permitidos para campo
  de texto, favor revisar os dados inseridos!"
type: support-article
updated_at: '2026-01-28T19:59:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37991580374039-RH-RM-Meu-RH-Erro-Foram-encontrados-termos-n%C3%A3o-permitidos-para-campo-de-texto-favor-revisar-os-dados-inseridos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37991580359447) Tempo aproximado para leitura: **00:01:35 min**  
  
**Ocorrência**  
Ao tentar realizar login no Meu RH, é apresentado a mensagem de erro: "Foram encontrados termos não permitidos para campo de texto, favor revisar os dados inseridos!"

![erro_app.jpeg](https://totvssuporte.zendesk.com/attachments/token/lMPzzUCvTEbFgMCsM8jtSRKXn/?name=erro_app.jpeg&lotus_request=true)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH – Todas as versões  
  
**Causa**  
Este erro ocorre devido a uma medida de segurança que impede o uso do caractere ponto e vírgula (**;**)  na senha, com o objetivo de prevenir tentativas de ataque do tipo SQL Injection.

**Solução**  
Para solucionar este erro, atualize a senha do usuário removendo o caractere ponto e vírgula (;) e utilize outro caractere especial permitido, como @, &, !, entre outros.

Caso essa mensagem de erro seja apresentada em outras rotinas que contenham campos de texto, como, por exemplo, solicitação de abono, inclusão de batidas manuais ou atestados, é necessário revisar o conteúdo informado e verificar se não está sendo utilizada alguma palavra reservada que corresponda a comandos SQL, como GO, UPDATE, INSERT, entre outras.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37991580360215)

Para conhecer todas as palavras reservadas, consulte a documentação oficial:

[Palavras-chave reservadas SQL Server](https://learn.microsoft.com/pt-br/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-ver17#odbc-reserved-keywords)

[Palavras-chave reservadas Oracle](https://docs.oracle.com/cd/A97630_01/appdev.920/a42525/apb.htm)
