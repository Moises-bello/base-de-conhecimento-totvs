---
article_id: 4417443072407
category: Faturamento - Integrações
content_hash: 87d36426fddc21752c9432695decd4f9412a44d621536255778127b03f3a38e4
fetched_at: '2026-06-28T22:38:26.505761+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Importador XML de pedido
  de vendas
type: support-article
updated_at: '2025-01-15T19:58:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417443072407-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Importador-XML-de-pedido-de-vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21617574227479) Tempo aproximado para leitura: **00:03:30 min****Dúvida**Como funciona o Importador XML de pedido de vendas no módulo faturamento?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - a partir da release 12.1.25.  
  
**Solução**

O Importador  XML é uma opção de integração do XMl via Schedule do Configurador, sem a necessidade de se contratar os serviços da Neogrid, porém o cliente será responsável por realizar o download de um XML válido e o inserir manualmente na pasta INN do Importador XML para que seja lido e integrado ao Protheus.

A funcionalidade foi disponibilizada a partir da release **12.1.25**, releases anteriores não tem acesso a funcionalidade. Utilizado para importar pedidos de vendas (código 005) e programação de entrega (código 252).

Para integrar:

1. Configurar parâmetros

* + **MV\_IMPXML =T**
  + **MV\_TCNEW =6**
  + **MV\_COLEDI ={"005","252"}**
  + **MV\_CROSFAT =1**

2. Renomeie o nome da tabela **CKO (X2\_ARQUIVO) para CKOCOL.** Salve a tabela e atualize o dicionário de dados;

3. Configurar o Agent Schedule e os jobs para a integração: **Colautoread** e **Ma411JOB** para que haja integração:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417442423063)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417434167319)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417442437271)

4. Criar dentro da Pasta System , a pasta  **XML ,**pois caso ocorra erros de integração, o sistema irá gerar um arquivo chamado**"Order"** que passará as informações que precisam ser corrigidas. Eventualmente também pode criar o arquivo "**deliveryschedule\_salesorder**, caso haja inconsistência no pedido no momento da integração, por exemplo, não ter encontrado a condição de pagamento no Protheus que está sendo informada no XML;

5. Informar o mesmo**CNPJ**do XML no cadastro de Filial para que não gere erro na integração de não encontrar o pedidos no servidor;

6. Cria as pastas INN, Lidos e Out numa estrutura de pasta dentro da pasta data e informar o caminho nos parâmetros:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417434594839)

**MV\_NGINN= \Import XML\inn**

**MV\_NGLIDOS=\Import XML\Lidos**

**MV\_NGOUT=\Import XML\Out**

7. Para importar o **XML** deve ser inserido na **pasta IN manualmente**, visto que o processo não possui integração com a ***Neogrid***para carregar na pasta  automaticamente. Estartar o server.ini para que os jobs já configurados no Schedule do Configurador possam efetuar a importação e integrar o pedido de vendas com o Protheus.

**Saiba mais:**

**[FAT0305 Integrador XML para Pedido de Vendas - módulo Faturamento](https://tdn.totvs.com/x/uQoxJw)**
