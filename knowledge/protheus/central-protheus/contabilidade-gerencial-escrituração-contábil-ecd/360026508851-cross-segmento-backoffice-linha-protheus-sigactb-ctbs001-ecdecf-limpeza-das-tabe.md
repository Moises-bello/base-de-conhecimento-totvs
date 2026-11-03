---
article_id: 360026508851
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: b9d61a3d35435becf8e77ff1ff08ad02c9f161d5614d4be75026e077b489aedd
fetched_at: '2026-06-28T22:40:44.471331+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGACTB CTBS001 ECD/ECF Limpeza
  das tabelas de Revisão
type: support-article
updated_at: '2023-01-03T13:14:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026508851-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-ECF-Limpeza-das-tabelas-de-Revis%C3%A3o
---

**Dúvida**A tabela CS(s) estão ocupando uma parte considerável do banco, posso efetuar uma limpeza?

**Ambiente**Protheus– Contabilidade gerencial – A partir da versão 11.80  
  
**Solução**Cada revisão gerada na ECD, a tabela CT2 (lançamento contábil) é exportada para a CSB, conforme parametrização, o número de revisões e teste pode provocar lentidão e consumir um grande espaço no banco.

A limpeza dessa tabela pode ser efetuada, desde que as tabelas relacionadas sejam apagadas também.

Obs: Limpeza das demais tabelas CS podem ser realizadas

Na rotina CTBS001, posicione na revisão + excluir.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025731032/mceclip1.png)

Tabelas Relacionadas: CS0 ate CS9 / CSA até CSZ

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025730892/mceclip0.png)

[MP- SIGACTB - TABELAS ECD E ECF COMPARTILHAMENTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF-COMPARTILHAMENTO?source=search)

Foi criado o parâmetro **MV\_CTBDLRV,** que após ser ativado deletará os registros de todas as tabelas das revisões fisicamente da base de dados.

.T.  -  Ativa a deleção física na base de dados

.F.  -  Mantêm a deleção lógica (Valor *Default* do parâmetro)

**Obs**. Cabe ao usuário o controle de apagar ou não a revisão transmitida.

Porém mesmo que seja apagada, basta gerar uma nova revisão;

Caso o ambiente não tenha sofrido alterações, os dados serão os mesmos transmitidos.

<http://tdn.totvs.com/pages/releaseview.action?pageId=469441937>
