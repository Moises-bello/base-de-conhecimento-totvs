---
content_hash: f6de58a69648dec33d484cc66cd23d17f7b983e66eb33e9ab26c308bc9a5c6eb
fetched_at: '2026-06-29T00:09:24.074769+00:00'
page_id: '423937880'
product: rm
source: tdn-rm
title: Tipo de Recebimento de NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937880
version: 2
---

**Filial**: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Dados Fiscais | Parâmetros por Filial | Importação/Envio de Arquivo XML 1/2 e informe o Tipo de Recebimento que será utilizado na empresa.

**Fornecedor**: Cadastros > Tabelas Auxiliares > Definições de Cli/For - Importação de Arquivo XML  
O campo "Tipo de recebimento de NF-e' define a forma como o sistema irá realizar o processo de recebimento automático das NF-e. Esta informação é parametrizável por Filial e/ou por Fornecedor. Assim, quando do recebimento automático de uma NF-e, caso o emitente da mesma conste na tabela de definições do Cli/For para a importação, essa informação prevalecerá, caso contrário o sistema obedecerá ao que foi parametrizado para a filial de destino da NF-e.  
Os Tipos de Recebimento possíveis são:

* **Inclusão de Movimento Sem Vínculo Com Pedido**: O sistema não considera o código do pedido no XML e realiza a inclusão do movimento de NF-e com base nos dados existentes no XML. O movimento será criado normalmente, acatando a todas às parametrizações do seu tipo de movimento.
* **Inclusão de Movimento Sem Vínculo Com Pedido (a Processar)**: O sistema não considera o código do pedido no XML e realiza a inclusão do movimento com base nos dados existentes no XML e status "Não Processado", ou seja, estes movimentos não irão gerar lançamentos financeiros, contábeis, atendimentos no RMAgilis, etc. Os movimentos criados com o status "Não Processado", deverão obrigatoriamente ser submetidos ao processo "Processar Grupo de Movimentos".
* **Inclusão de Movimento Vinculando Pedido (Recebimento)**: O sistema utiliza o código do pedido contido no XML para buscar o movimento correspondente e realizar o faturamento do mesmo, sendo que se o pedido não for encontrado na base de dados, o sistema abortará o processo e informará o motivo através do log de execução.
* **Inclusão Direta de Movimento ou Vinculando ao Pedido (Recebimento)**: Através do conteúdo do XML, o sistema tentará identificar o respectivo pedido, e caso seja bem-sucedido, será realizado o faturamento do mesmo. Se o sistema não conseguir identificar nenhum pedido, a inclusão do movimento será feita através dos dados existentes no XML e sem nenhum relacionamento com qualquer outro movimento já existente na base de dados, ou seja, o movimento será criado acatando a todas às parametrizações do seu tipo de movimento.
* **Inclusão de Movimento Vinculando Pedido (Recebimento) ou a Processar**: O sistema tentará identificar o pedido, e se for bem sucedido será realizado o faturamento, caso contrário, será feita a inclusão do movimento sem o relacionamento e com o status "Não Processado". Os movimentos criados com o status "Não Processado", deverão obrigatoriamente ser submetidos ao processo "Processar Grupo de Movimentos".
