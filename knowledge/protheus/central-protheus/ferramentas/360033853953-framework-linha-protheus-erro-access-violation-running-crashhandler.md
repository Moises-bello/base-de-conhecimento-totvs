---
article_id: 360033853953
category: Ferramentas
content_hash: 7a5903965b10fb249e8e7c2f69390774d02b9154bd6cd6235c7874294fdf4bc2
fetched_at: '2026-06-28T22:42:18.030725+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: 'Framework - Linha Protheus - Erro: ACCESS VIOLATION - RUNNING CRASHHANDLER'
type: support-article
updated_at: '2024-05-09T11:11:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033853953-Framework-Linha-Protheus-Erro-ACCESS-VIOLATION-RUNNING-CRASHHANDLER
---

**Dúvida**  
Por qual motivo ocorre o erro: ACCESS VIOLATION - RUNNING CRASHHANDLER  
  
**Ambiente**  
Protheus - DBAccess - Versão 12  
  
**Solução**  
O erro acontece em ambientes com o banco de dados MS SQL e que esteja com a configuração de MARS e/ou driver de conexão ODBC incorretos.  
  
Seguem abaixo instruções para a correta configuração destes 2 recursos:  
  
**MARS** - Configuração necessária para ambientes com MSSQL.  
Importante: Apesar de ser possível desabilitar o uso do MARS, a TOTVS não homologa o cenário com MARS desabilitado, e pode quebrar a compatibilidade a qualquer momento com drivers não recomendados.  
O uso de MARS é necessário para alguns recursos e para questão de desempenho do TOTVS | DBAccess.  
Documentação completa pode ser verificada aqui:  
<http://tdn.totvs.com.br/pages/viewpage.action?pageId=451269662>  
  
**ODBC** - Para MSSQL é recomendado o uso do DRIVER SQL Server Native Client 10.0 ou superior  
Informações detalhadas de como criar a conexão ODBC: <http://tdn.totvs.com/display/tec/DBAccess+-+Como+criar+uma+fonte+de+dados+para+uso+com+Microsoft+SQL+Server>
