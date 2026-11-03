---
article_id: 23975453215767
category: PMS - Integrações
content_hash: d433a1a0b2de44af9e03eba9ac5788ec4a52d2ab6145977621abc1f80ce50d57
fetched_at: '2026-06-28T22:37:16.709016+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Chaves necessárias no Protheus
  para a Integração com TOP RM
type: support-article
updated_at: '2024-07-16T11:25:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23975453215767-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Chaves-necess%C3%A1rias-no-Protheus-para-a-Integra%C3%A7%C3%A3o-com-TOP-RM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23975476657303) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Quais as chaves no Protheus necessárias para a Integração TOP x Protheus?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**

Essa configuração é destinada quando coligadas do RM integram com o Protheus:

* MV\_RMCOLIG > 0
* MV\_PMSITMU = 0
* MV\_INTPMS = S

**OBSERVAÇÃO 1:** O Protheus deve possuir WebServices rodando previamente, essa documentação não tem foco nessa etapa.

Para o correto funcionamento e para não serem apresentados erros como:

Erro 1: "Inconsistencias na integração Microsiga Protheus x TOP"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23975476661527)

Erro 2: "Erro na configuração ou conexão do ByYouDbAccess para a base de dados do TOP"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23975476664087)

Deve ser configurado no appserver.ini do Protheus as seguintes chaves nos blocos:

* [PROTHEUS] Alias para logar no banco de dados Protheus  
  (...)  
  **TOPServer=LOCALHOST - Servidor onde é localizado os bancos de dados**  
  **TOPALIAS=PROTHEUS – Nome do banco de dados Protheus**  
  **Panel Server=LOCALHOST – Servidor**  
  **TopAliasRM=RM – Nome do ODBC que conecta no banco de dados RM/nome banco RM em ambiente Oracle.**

* [JOB\_WS]

  (...)

  **NAMESPACE=http://www.totvs.com.br/rm/**

  **WEBSERVICELOCATION=http://localhost:83**

  **URLLocation=http://localhost:83**

**OBSERVAÇÃO 2:** Para testar a conexão, entre com "/[Wsindex.apw](http://localhost:83/Wsindex.apw)?" após o fim do servidor. Se por exemplo o endpoint for:

* [localhost:99/ws]

Coloque no navegador para testar:

* localhost:99/ws/[Wsindex.apw](http://localhost:83/Wsindex.apw)?

**OBSERVAÇÃO 3:** Os valores das chaves anteriormente demonstradas devem ser mudados conforme o ambiente e não apenas coladas da maneira que está acima, exemplo dos valores que podem ter (deve ser ajustado para cada ambiente):

```
TOPSERVER=localhost  
TOPALIAS=12.1.2210d  
TOPDATABASE=MSSQL  
TOPALIASRM=12.1.2210a  
PanelServer=localhost  
;---------------------------------------------  
NAMESPACE=http://www.totvs.com.br/rm/  
WEBSERVICELOCATION=http://localhost:93  
URLLocation=http://localhost:93
```

**Saiba mais:**

[Integração TOP X Protheus – Configurando Protheus](https://tdn.totvs.com/x/AEASCw)
