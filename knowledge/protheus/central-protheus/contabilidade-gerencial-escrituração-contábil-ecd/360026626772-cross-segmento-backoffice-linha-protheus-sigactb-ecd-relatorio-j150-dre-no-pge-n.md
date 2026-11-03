---
article_id: 360026626772
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: b43ebdbea8f320b20139ebbe157fd9907011b302dabba57a53da8c3443e2a497
fetched_at: '2026-06-28T22:40:44.741955+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD RELATORIO J150 (DRE)
  NO PGE NÃO CORRESPONDE AO EMITIDO NO PROTHEUS
type: support-article
updated_at: '2022-05-26T11:43:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026626772-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-RELATORIO-J150-DRE-NO-PGE-N%C3%83O-CORRESPONDE-AO-EMITIDO-NO-PROTHEUS
---

**Dúvida**O relatório DRE, no PGE, não corresponde a ordenação do relatório impresso no Protheus.  
   
 **Ambiente**Protheus– Contabilidade Gerencial – A partir da versão 11.80

**Causa**

No leiaute 7, com a criação dos campos  IND\_COD\_AGL e COD\_AGL\_SUP  
O Relatório, dentro do PGE, passou a considerar o posicionamento das entidades conforme ordem dos códigos de aglutinação, considerando a estrutura hierárquica informada (níveis das contas).

Abrimos um chamado na SEFAZ e foi nos posicionado da seguinte forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026191451/mceclip1.png)

* Primeiro o programa coloca em ordem todas as linhas de nível  "1”. No exemplo acima, há apenas uma linha de nível "1” (campo 4 do registro J150), com código de aglutinação igual a “3” campo 2 do registro J150).
* Depois, o programa coloca em ordem todas as linhas de nível "2” que são “filhas” da linha de código de aglutinação “3”, ou seja, todas as linhas de nível “2” que com a informação o código de aglutinação da linha superior igual a “3” (campo 5 do registro J150). No exemplo acima, á duas linhas de nível “2” que são “filhas” da linha de código de aglutinação “3”,
* Portanto, a linha de nível “2” de código de aglutinação “3.1” virá antes da linha de código de aglutinação “3.2”.
* E assim por diante, ou seja, o programa utiliza o mesmo procedimento =cima para todos os níveis informados nas demonstrações contábeis (registros J100 e J150).

**Porque meu relatório esta invertido no PGE?**

Após avaliação verificou-se que os relatórios que estão sendo "invertidos" no PGE, possuem em sua estrutura totalizadores com menor nível de aglutinação na parte inferior do relatório, ou seja, o "Totalizador Geral" esta no final do relatório.

Relatório no Protheus:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026206812/mceclip2.png)

CTS - Tabela que armazena o cadastro da visão e exporta para ECD

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026206992/mceclip3.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026207252/mceclip5.png)

**Solução**

O problema está apenas no relatório do Programa Gerador de Escrituração (PGE), pois o arquivo gerado pelo Protheus atendente conceito da exibição do DRE, conforme as regras de validação do manual.

O PGE é de responsabilidade da Receita Federal, para maiores informações o contribuinte poderá entrar em contato com a Receita Federal.

<https://receita.economia.gov.br/contato/fale-conosco/empresa/sped/demostracoes%20contabeis>

**Importante:** A entrega da ECD está ocorrendo sem nenhuma advertência/erro.

Caso queira proceder com adequação **no Protheus**, temos a proposta abaixo:

**Criar uma nova visão gerencial** com seu código de aglutinação conforme padrões estipulado pela Receita Federal, da mesma forma como é feito no Balanço Patrimonial (registros J100 e J150 mesma validação).

A entidade "Resultado do Exercício" deve ser  "Total geral", sem superior.

E os "filhos" sempre depois do "totalizador".

* Exemplo da Receita Federal:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026198191/mceclip6.png)

* Rotina CTBA161 ( Entidades + Visão Gerencial) + F12  modo de exibição? TRADICIONAL (Tabela CTS)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026215832/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026204731/mceclip1.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026216372/mceclip2.png)

**Observação:** Para esta adequação, orientamos criar uma nova versão e não alterar a visão gerencial utilizada atualmente, caso a receita disponibilize apenas a correção do relatório.

**Saiba mais:**

DRE (J150) Ordenação ate o Leiaute 6:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026127292-MP-SIGACTB-ECD-J100-e-J150-MV-GRVISOR-ORDEM-DA-VISAO-GERENCIAL>

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
