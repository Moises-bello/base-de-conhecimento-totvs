---
article_id: 360005056031
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 0ceaceaee5c11f4967a84b616ff84a9534fd7abe5bb64e014dc1499462178c47
fetched_at: '2026-06-28T22:37:55.034389+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Help: F150ARQ'
type: support-article
updated_at: '2024-01-04T14:13:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005056031-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Help-F150ARQ
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Ao realizar a geração do CNAB é exibido o Help: F150ARQ

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**Migração de versão e/ou manipulação de base de dados e dicionário incorreta e indevidamente.

**Solução**Verifique o parâmetro **(SX6)** **MV\_LOCREC** está preenchido, caso esteja a rotina considera o caminho do diretório informado nele, então o arquivo de Retorno tem que estar lá para ser processado corretamente.  
  
  
Observação: A rotina considera o **MV\_LOCREC** como prioridade, ou seja, sempre que ele estiver preenchido com o caminho do diretório o parâmetro será considerado, caso esteja em branco a rotina considera o **MV\_PAR04 (SX1 - AFI150)** **Arquivo de Entrada?.**

**Saiba Mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
