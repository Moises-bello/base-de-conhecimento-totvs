---
article_id: 25670752307479
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: aa175eaa2050a5fa96eabbb92d178ab687705a557929a3e67a27caf61cfb79f5
fetched_at: '2026-06-28T22:45:20.901066+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial -  Como limpar arquivos de LOG no TAF e
  TSS?
type: support-article
updated_at: '2026-06-26T11:56:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25670752307479-RH-Linha-Protheus-TAF-eSocial-Como-limpar-arquivos-de-LOG-no-TAF-e-TSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25670752286487) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como limpar arquivos de LOG no TAF e TSS?  
  
**Ambiente**RH - Linha Protheus - TAF - eSocial - TOTVS Automação Fiscal - Todas as versões  
  
**Solução**

1. Pare o serviço do DBACCESS, TAF-WS, TAF-APPSERVER ou o TSS;
2. Para limpar o arquivo do DBACCESS, acessa a pasta onde está sendo executado o DBACCESS.EXE e procure pelos arquivos (DBACCESS.LOG e DBCONSOLE);
3. Com os arquivos encontrados, renomeie ou delete-os;
4. Para limpar o arquivo de LOG do TAF-WS, acesse a pasta de instalação do TAF em BIN/APP e procure o arquivo CONSOLE.LOG;
5. Renomeie ou delete o arquivo na sequência;
6. Para limpar o arquivo de LOG do TAF-APPSERVER, acesse a pasta de instalação do TAF em BIN/APPSERVER e localize o arquivo CONSOLE.LOG;
7. Renomeie ou delete o arquivo em seguida;
8. Para limpar o arquivo de LOG do TSS, acesse a pasta de instalação do TSS ou Totvssped (vai depender como foi realizado a instalação, mas basta procurar onde está sendo executado o APPSERVER.EXE do TSS para encontrar o diretório) e acesse a pasta BIN/APPSERVER e encontre o arquivo CONSOLE.LOG;
9. Renomeie ou delete o arquivo;
10. Inicie os serviços, em seguida repita a operação (que estiver com erro/problema) para que seja gravado alguma mensagem de erro no novo console, que possa auxiliar o suporte na análise da situação reportada.
