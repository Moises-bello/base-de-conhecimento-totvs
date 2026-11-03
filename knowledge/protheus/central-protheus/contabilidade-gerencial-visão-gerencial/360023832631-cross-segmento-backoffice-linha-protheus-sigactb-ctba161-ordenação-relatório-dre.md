---
article_id: 360023832631
category: Contabilidade Gerencial - Visão Gerencial
content_hash: c4212735594f2ede2e00d9845ef5232761b03007d73c4a48e3ad151c956d5620
fetched_at: '2026-06-28T22:40:50.650334+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: CTBA161 ORDENAÇÃO RELATÓRIO
  (DRE e BALANÇO) X  ECD (J00 e J150)'
type: support-article
updated_at: '2022-05-30T18:41:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023832631-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA161-ORDENA%C3%87%C3%83O-RELAT%C3%93RIO-DRE-e-BALAN%C3%87O-X-ECD-J00-e-J150
---

**Dúvida**

Ao emitir relatório de balanço(CTBR500) e DRE(CTBR510)  com a mesma visão gerencial utilizada ao gerar a ECD J100(Balanço) e J150(Dre) são gerado com ordenação diferentes  
  
**Ambiente**  
Microsiga Protheus – Contabilidade – A partir da versão 11.80  
  
  
**Solução**

Ao emitir relatório de balanço(CTBR500) e DRE(CTBR510) o sistema considera o campo **ORDEM** , para ordenar a apresentação no relatório 

* Ao acessar a rotina "F12' "Modo de Exibição = Arvore" é possível verificar como esta configurado o campo CVF\_ORDEM

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019197002/mceclip0.png)

* Ao acessar a rotina "F12' "Modo de Exibição = Tradicional" é possível verificar como esta configurado o campo CTS\_ORDEM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021303771/mceclip3.png)

* Ao gerar a ECD J100(Balanço) e J150(Dre) o sistema considera a posição da Entidade na estrutura da Visão para gerar no arquivo ECD

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021302011/mceclip1.png)

Para essa situação foi criado o parâmetro: **MV\_GRVISOR**  
  
O parâmetro **MV\_GRVISOR** foi criado para considerar o campo ORDEM na exortação dos demonstrativos. Neste caso o parâmetro deve ser habilitado = .T. No padrão o parâmetro esta como  .F.

[MP-SIGACTB ECD : J100 e J150 MV\_GRVISOR ORDEM DA VISAO GERENCIAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026127292-MP-SIGACTB-ECD-J100-e-J150-MV-GRVISOR-ORDEM-DA-VISAO-GERENCIAL?source=search)

Veja mais :[MP\_SIGACTB - ECD - J150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006972612-MP-SIGACTB-ECD-J150-?source=search)

[MP-SIGACTB-ECD RELATORIO J150 (DRE) NO PGE NÃO CORRESPONDE AO EMITIDO NO PROTHEUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026626772-MP-SIGACTB-ECD-RELATORIO-J150-DRE-NO-PGE-N%C3%83O-CORRESPONDE-AO-EMITIDO-NO-PROTHEUS?source=search)

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
