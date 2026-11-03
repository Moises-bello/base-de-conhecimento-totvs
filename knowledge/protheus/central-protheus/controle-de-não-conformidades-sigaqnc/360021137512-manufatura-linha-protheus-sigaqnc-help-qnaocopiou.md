---
article_id: 360021137512
category: Controle de Não Conformidades (SIGAQNC)
content_hash: d1620007f3d3e4bb84d9dda7c76ba160a3e526dede74e8d422a3a2af75551c69
fetched_at: '2026-06-28T22:42:27.971633+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Help QNAOCOPIOU
type: support-article
updated_at: '2021-09-08T12:58:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021137512-Manufatura-Linha-Protheus-SIGAQNC-Help-QNAOCOPIOU
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**No módulo de **SIGAQNC - Controle de Não Conformidades**, ao tentar abrir um documento anexo à uma **FNC - Ficha de Não Conformidade** na rotina **QNCA040 - Cadastro de Não Conformidades** é apresentada a mensagem: **QNAOCOPIOU** **- Não foi possível copiar o documento anexo a esta ficha de ocorrencias/não-conformidades.**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**  
A mensagem ocorre devido parametrização incompleta no ambiente.   
  
**Solução**  
Verificar se os parâmetros estão configurados conforme abaixo:  
**MV\_QNCPDOC - Define o diretório onde contem os arquivos dos documentos** como **\SYSTEM\DOCS**   
**MV\_QPATHWT - Define o diretório do Cliente onde ficarão os Documentos gerados pelo Sistema** como **GETTEMPPATH()**  
  
Caso já estiverem corretos, verifique se na instalação do **Protheus** existe o diretório **protheus\_data\system\DOCS.**Caso não existir, crie este diretório e realize um novo teste.
