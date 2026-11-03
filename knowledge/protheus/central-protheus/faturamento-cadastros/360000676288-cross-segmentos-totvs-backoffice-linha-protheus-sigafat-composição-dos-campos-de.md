---
article_id: 360000676288
category: Faturamento - Cadastros
content_hash: ab442ec7ce20b2a6915065077ab72fdbc419f287b67f87254acff9ed5f301ea5
fetched_at: '2026-06-28T22:38:36.859957+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Composição
  dos Campos de saldo e vendas na tabela SA1 (MATA030)
type: support-article
updated_at: '2024-06-12T22:16:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000676288-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Composi%C3%A7%C3%A3o-dos-Campos-de-saldo-e-vendas-na-tabela-SA1-MATA030
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18707398419095) Tempo aproximado para leitura: 00:02:00 min***

**Dúvida**Como são compostos os campos relacionados à vendas e saldos de Cliente (MATA030) na Tabela SA1?  
Exemplo: A1\_MCOMPRA ,A1\_MSALDO ,A1\_SALPED ,A1\_SALPEDL ,A1\_SALPEDB ,A1\_SALDUP e A1\_ATR.

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**

**Relação dos campos disponíveis e suas informações:**

|  |  |
| --- | --- |
| CAMPO | INFORMAÇÕES |
| **Maior compra (A1\_MCOMPRA)** | Mostra o valor da maior compra que o cliente já fez na empresa. Não acumulativo |
| **Maior saldo (A1\_MSALDO)** | Mostra o maior saldo devedor que o cliente já ficou em sua empresa, ou seja, títulos em aberto. Acumulativo (campo para armazenar histórico). |
| **Saldo dos Pedidos (A1\_SALPED)** | Saldo dos Pedidos de Venda "Em aberto" na moeda corrente (Não Faturados).  Obs: Ao Liberar Credito/Estoque, o sistema abate deste campo e passa a alimentar um outro campo, o A1\_SALPEDL (Detalhes a seguir). |
| **Saldo de Pedidos Liberados (A1\_SALPEDL)** | Saldo dos Pedidos de Venda submetidos à liberação e Liberados por Crédito para este Cliente.  Pedidos já liberados, porém, ainda não faturados, consumindo o crédito. |
| **Saldo Pedidos Bloqueados (A1\_SALPEDB)** | Saldo dos Pedidos de Venda submetidos à liberação e Bloqueados por Crédito para este Cliente |
| **Saldo de duplicatas (A1\_SALDUP)** | Saldo de duplicatas do Cliente (duplicatas em aberto).  Demonstra quanto o cliente ainda está devendo para sua empresa.  Obs:   * Após baixa de algum título do cliente, o sistema vai abatendo o valor atualizando este campo (relacionado ao campo E1\_STATUS). * Regra: Acumulativo – baixa = Saldo de duplicatas do Cliente em aberto * Os títulos do tipo "RA" e "NCC" abatem o saldo do campo. |
| **Títulos em atraso (****A1\_ATR)** | Somatório dos títulos em Atraso que ultrapassam a tolerância concedida na configuração do parâmetro MV\_RISCO"x" e campo A1\_RISCO |

**Para mais detalhes , acesse:**

**[Composição dos Campos relacionados à Vendas a Clientes (MATA030) na Tabela SA1](http://tdn.totvs.com/pages/viewpage.action?pageId=253989073)**

**Outros artigos relacionados:**

* **[Cross Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configuração-básica-para-cadastrar-um-cliente-no-módulo-faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406431792663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-b%C3%A1sica-para-cadastrar-um-cliente-no-m%C3%B3dulo-faturamento)**
* **[Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT-Adição de mais de um Email no cadastro de cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033983134-MP-FAT-Adi%C3%A7%C3%A3o-de-mais-de-um-Email-no-cadastro-de-clientes)**
* **[Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT-Cadastro de cliente só apresenta a aba Outros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000369187-MP-FAT-Cadastro-de-clientes-s%C3%B3-apresenta-a-aba-Outros)**
