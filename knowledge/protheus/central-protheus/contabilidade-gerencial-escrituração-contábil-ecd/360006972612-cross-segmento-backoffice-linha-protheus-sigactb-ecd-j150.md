---
article_id: 360006972612
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 3fce4a457d622c5ecb9f4db094b3528e0ff86b8c7f8a2b215e2f792d9062040f
fetched_at: '2026-06-28T22:40:44.681898+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD - J150
type: support-article
updated_at: '2024-06-18T12:09:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006972612-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-J150
---

***ECD validação J150*****Ocorrência**O valor informado nas contas de maior detalhamento do registro da DRE não corresponde à soma dos valores informados nos registros de Saldos das Contas de Resultado antes da apuracão na mesma data 

**Ambiente**Protheus – Contabilidade – A partir da versão 11.80  
  
  
  
**Solução**

J150 -DRE –>  as contas aglutinadoras tem que ser demonstradas, informando as contas sintéticas que devem estar na parte superior e as contas analíticas na parte inferior, fazendo dessa forma o PVA entenderá e não gerará erros nos saldos quando o J150 não bate.  
  
J100 -Balanço Patrimonial -> é ao contrário, as contas aglutinadoras analítica ficam na parte superior e as sintéticas na parte inferior.   
 Se não possui uma estrutura dessa forma para mandar o SPED Contábil você cria uma estrutura com esse layout só para fazer a entrega do SPED.

J150 -DRE –>  as contas aglutinadoras tem que ser demonstradas, informando as contas sintéticas que devem estar na parte superior e as   
contas analíticas na parte inferior

No cadastro da Visão Gerencial, verifique as contas contábeis que estão compondo as entidades gerenciais da estrutura.  
  
Um outro detalhe importante que deve ser avaliado na estrutura, é a ordem e o código da entidade, onde deve seguir a hierarquia.  
  
Emo modo arvore   
  
![](https://totvssuporte.zendesk.com/attachments/token/mYO10dUtni1sSEN0T3PGSdPKH/?name=inline-247929148.png)​  
  
Veja se para a entidades sintéticas o campo TOTAL Geral esta sendo informado  
  
![](https://totvssuporte.zendesk.com/attachments/token/7kp1PSCfHuWcCNETra2g3vLpv/?name=inline-1272819770.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/U8lghKczk2k66AY8YtubCLZmR/?name=inline180685218.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/hVMR7xzGuULlhbnZm6SvMyDSE/?name=inline-1727055024.png)​

Exemplo de estrutura para a DRE :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010100351)  
  
  
Devemos lembrar que J100 -Balanço Patrimonial -> é ao contrário, as contas aglutinadoras analítica ficam na parte superior e as sintéticas na parte inferior.

Veja melhoria liberada :  [ORDENAÇÃO RELATÓRIO (DRE e BALANÇO) X ECD (J00 e J150)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023832631-MP-SIGACTB-CTBA161-ORDENA%C3%87%C3%83O-RELAT%C3%93RIO-DRE-e-BALAN%C3%87O-X-ECD-J00-e-J150-?source=search)

 e  mais [J150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-COMO-GERAR-O-REGISTRO-J150-?source=search)  
  
No cadastro da Visão  
  
CTS\_IDENTI - é necessário estar preenchido  
CTS\_TPSALD - é necessário estar preenchido  
  
CVF\_DETHCG -não preencher  
CVF\_FATSLD -não preencher  
CVF\_SLDENT -não preencher  
CVF\_TOTVIS -não preencher  
CVF\_VISENT -não preencher

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

Veja mais :

<http://tdn.totvs.com/display/PROT/ECD0001_ECD_ADVERTENCIA_J150_J100>

<http://tdn.totvs.com/display/PROT/ECD0028_J150_VL_CTA_ULT_DRE_ACUMULADO>

[MP- SIGACTB : ECD : J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)

[MP-SIGACTB-ECD RELATORIO J150 (DRE) NO PGE NÃO CORRESPONDE AO EMITIDO NO PROTHEUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026626772-MP-SIGACTB-ECD-RELATORIO-J150-DRE-NO-PGE-N%C3%83O-CORRESPONDE-AO-EMITIDO-NO-PROTHEUS?source=search)

[MP-SIGACTB ECD : J100 e J150 MV\_GRVISOR ORDEM DA VISAO GERENCIAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026127292-MP-SIGACTB-ECD-J100-e-J150-MV-GRVISOR-ORDEM-DA-VISAO-GERENCIAL?source=search)

[MP- SIGACTB : ECD : Deve existir pelo menos um registro J100 (Balanço) e um J150 (DRE) para cada registro J005 (Demonstração Contábil) informado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049318233-MP-SIGACTB-ECD-Deve-existir-pelo-menos-um-registro-J100-Balan%C3%A7o-e-um-J150-DRE-para-cada-registro-J005-Demonstra%C3%A7%C3%A3o-Cont%C3%A1bil-informado-?source=search)
