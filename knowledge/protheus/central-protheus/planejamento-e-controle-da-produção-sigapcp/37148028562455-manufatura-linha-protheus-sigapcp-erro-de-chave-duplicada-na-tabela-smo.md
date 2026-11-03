---
article_id: 37148028562455
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ec44abc7b30929bad4694f03418f6a836bba5c4795b95fc0a2996fa1a9d4bb53
fetched_at: '2026-06-28T22:42:42.278130+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Erro de chave duplicada na tabela SMO
type: support-article
updated_at: '2025-12-19T18:38:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37148028562455-Manufatura-Linha-Protheus-SIGAPCP-Erro-de-chave-duplicada-na-tabela-SMO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37147998258711) Tempo aproximado para leitura: **00:04:35 min**  
  
**Ocorrência**  
Ao realizar o apontamento de produção está ocorrendo o erro **Cannot insert duplicate key row in object 'dbo.SMO** ou **Não é possível inserir linha de chave duplicada no objeto 'dbo.SMO.**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**  
A partir da *release* 12.1.2410 , a numeração sequencial das notas fiscais de entrada, saída e movimentos internos realizada através do parâmetro **MV\_DOCSEQ - Último número sequencial utilizado para movimentos** foi substituída pelo controle via *License Server*, e essa mudança pode eventualmente resultar no erro de chave duplicada na tabela **SMO - Informação Complementar Apontamento**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Atualize o *License Server*;  
2. Certifique-se de que todos os **RPOs - Repositórios** possuem a mesma data para o fonte **MATA250.PRX** que deve ser igual ou superior a 19/02/2025;  
3. Certifique-se de que todos os **RPOs** possuem a mesma data para o fonte **backoffice.stock.newProxNum.tlpp** que deve ser igual ou superior a 14/07/2025;  
4. Certifique-se de que todos os ambientes que conectam ao mesmo banco de dados possuem a mesma chave **SpecialKey** configurada no **appserver.ini**, se realizar algum ajuste, reinicie o **appserver;**  
5. Certifique-se de que nenhum **appserver.ini** possui a chave **CheckSpecialKey=0** , se encontrar em algum remova e reinicie o **appserver;**  
6. Execute a consulta abaixo no seu banco de dados, corrigindo os nomes das tabelas para os nomes corretos no seu ambiente  
**SELECT MAX(NUMSEQ) NUMSEQ FROM (**  
**SELECT MAX(D1\_NUMSEQ) NUMSEQ**  
**FROM SD1**  
**WHERE D\_E\_L\_E\_T\_ = ' '**  
**UNION ALL**  
**SELECT MAX(D2\_NUMSEQ) NUMSEQ**  
**FROM SD2**  
**WHERE D\_E\_L\_E\_T\_ = ' '**  
**UNION ALL**  
**SELECT MAX(D3\_NUMSEQ) NUMSEQ**  
**FROM SD3**  
**WHERE D\_E\_L\_E\_T\_ = ' '**  
**UNION ALL**  
**SELECT MAX(D3\_IDENT) IDENT**  
**FROM SD3**  
**WHERE D\_E\_L\_E\_T\_ = ' '**  
**UNION ALL**  
**SELECT MAX(H6\_IDENT) IDENT**  
**FROM SH6**  
**WHERE D\_E\_L\_E\_T\_ = ' '**  
**) MAIOR**  
7. Acesse o **SIGACFG - Configurador** e na rotina de **APCFG110 - Controle de Numeração** procure pela chave que contém o conteúdo da **SpecialKey** do seu ambiente seguida de **@@@SD2.** Para esse registro, no campo **Número**, atribua o valor obtido a partir da query executada no passo 6 somado do valor 1.   
Exemplo: se o resultado da consulta é ABCDEF, então o valor que deve ser atribuído é no campo Número é ABCDEG.  
  
**Saiba Mais**  
Para maios informações sobre a mudança **no sequencial acesse:**  
[**2024 - 31/10 Parâmetro MV\_DOCSEQ**](https://tdn.totvs.com/pages/releaseview.action?pageId=840763998)
