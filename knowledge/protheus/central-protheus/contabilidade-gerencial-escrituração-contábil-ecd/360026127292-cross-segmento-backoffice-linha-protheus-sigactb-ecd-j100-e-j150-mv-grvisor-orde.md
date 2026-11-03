---
article_id: 360026127292
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 39180968c4f2a6a4b8de27bc24d7b4d07d8225dc66d482e5f3239d2afaa45286
fetched_at: '2026-06-28T22:40:44.513451+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB -  ECD : J100 e J150  MV_GRVISOR
  ORDEM DA VISAO GERENCIAL'
type: support-article
updated_at: '2022-06-13T19:54:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026127292-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-J100-e-J150-MV-GRVISOR-ORDEM-DA-VISAO-GERENCIAL
---

**Dúvida**No PGE a ordem do J150/ J100 não correspondem ao emitido no protheus como solucionar?  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – **A partir da versão**

**Solução**

O que precisa ser avaliado é em que momento o DRE e no BP ficam desposicionados.

Exemplo DRE

1) Emita o DRE no Protheus (CTBR510)  
  
![](https://totvssuporte.zendesk.com/attachments/token/AAMOnO9xQEAnchsIpk6yAXptz/?name=inline-437192759.png)  
  
Após exportar o ECD (central de escrituração)​​, verifique se a "ordem" que visualiza no CTBR510 foi respeitada.  
Se foi respeitada o txt saída assim:  
  
![](https://totvssuporte.zendesk.com/attachments/token/SwNfDEUGDJ0ERA7hHL8FyjjSy/?name=inline1353430016.png)​  
  
E no J005 a composição será da mesma forma que visualiza o DRE no Protheus.

![](https://totvssuporte.zendesk.com/attachments/token/N7OV9EemxlKRBm6BX00XUksSV/?name=inline185456483.png)​​  
  
  
Caso a ordem não tenha sido respeitada o txt ficará da seguinte forma:  
  
![](https://totvssuporte.zendesk.com/attachments/token/zPcHExkUC8QfYBzQBrkYRrnAX/?name=inline-1560585418.png)​  
  
Para essa situação foi criado o parâmetro: **MV\_GRVISOR**  
  
O parâmetro **MV\_GRVISOR** foi criado para considerar o campo ORDEM na exortação dos demonstrativos. Neste caso o parâmetro deve ser habilitado = .T. No padrão o parâmetro esta como  .F. 

Para isso é preciso aplicar o patch e criar o parâmetro.  
  
Pacote:  
<http://tdn.totvs.com/display/PROT/ECD>

Criação do parâmetro via SIGACFG:  
**MV\_GRVISOR**  
**<http://tdn.totvs.com/display/PROT/ECD_SPED_CONTABIL_Alteracoes_para_Leiaute_7_00>**  
  
![](https://totvssuporte.zendesk.com/attachments/token/nV4St022SXH7BmWBO9G0R1eWV/?name=inline553008428.png)

 Veja mais : [MP-SIGACTB-ECD RELATORIO J150 (DRE) NO PGE NÃO CORRESPONDE AO EMITIDO NO PROTHEUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026626772-MP-SIGACTB-ECD-RELATORIO-J150-DRE-NO-PGE-N%C3%83O-CORRESPONDE-AO-EMITIDO-NO-PROTHEUS?source=search)

Veja o compartilhamento as tabelas  :

[Compartilhamento de tabelas no Contabilidade Gerencial (SIGACTB)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018270032-MP-SIGACTB-Como-realizar-compartilhamento-de-tabelas-no-Contabilidade-Gerencial-SIGACTB-?source=search)

|  |  |
| --- | --- |
| • | CTS - Entidade Gerencial |

|  |  |
| --- | --- |
| • | CVE - Visão gerencial |

|  |  |
| --- | --- |
| • | CVF - Itens da Visão Gerencial |

|  |  |
| --- | --- |
| • | CT1 - Cadastro Plano de Contas. |

|  |  |
| --- | --- |
| • | CTD - Cadastro Itens Contábeis. |

|  |  |
| --- | --- |
| • | CTH - Cadastro Classe de Valor. |

|  |  |
| --- | --- |
| • | CTS - Planos Gerenciais. |

|  |  |
| --- | --- |
| • | CTT- Cadastro Centros de Custo. |

|  |  |
| --- | --- |
| • | SL - Tabela de Tipos de Saldos. |

 

|  |  |
| --- | --- |
| • | CTG - Calendários Contábeis |

|  |  |
| --- | --- |
| • | CTN - Configuração de Livros Contábeis |

|  |  |
| --- | --- |
| • | CTO - Moedas |

 [TABELAS ECD E ECF COMPARTILHAMENTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF-COMPARTILHAMENTO?source=search)

|  |  |
| --- | --- |
| • | CSE - Balanço cabeçalho |

|  |  |
| --- | --- |
| • | CSD - Balanço Itens |
