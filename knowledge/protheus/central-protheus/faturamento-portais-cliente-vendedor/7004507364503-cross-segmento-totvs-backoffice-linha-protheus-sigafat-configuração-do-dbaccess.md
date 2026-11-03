---
article_id: 7004507364503
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 2c6a9ddadeb1cbb2e773fbc6f925c744601ffcd150a26698db091b40e8ebea19
fetched_at: '2026-06-28T22:38:23.810995+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configuração
  do DBACCESS para utilização Portal Gestão de Vendas (PGV)
type: support-article
updated_at: '2023-06-13T21:16:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7004507364503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-do-DBACCESS-para-utiliza%C3%A7%C3%A3o-Portal-Gest%C3%A3o-de-Vendas-PGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15286109088919) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como sincronizar os dados as APIs do Portal Gestão de Vendas;  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da release 12.1.33;  
  
**Solução**

Quer um passo a passo, com vídeos, sobre a implementação dessa funcionalidade? [Acesse: Implementação Portal Gestão de Vendas](https://tdn.totvs.com/x/Etk1LQ)

Para sincronizar os dados as APIs do **Portal Gestão de Vendas** utilizam o campo S\_T\_A\_M\_P\_ como parâmetro de busca, sendo necessária a inclusão da chave **UseRowStamp** e **Memoinquery** no **TOTVS DBAccess**.

**S\_T\_A\_M\_P\_**

O campo S\_T\_A\_M\_P\_ será criado somente nas tabelas utilizadas pelo TOTVS Gestão de Vendas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10958626464023)

Após executar a configuração do TOTVS DBAccess, conforme informado no procedimento acima, será necessário efetuar a carga inicial das tabelas de Schemas (A1V) e campos dos schemas (A1W), também será necessário efetuar a inclusão do campo S\_T\_A\_M\_P\_ nas tabelas utilizadas no portal Gestão de Vendas.

Caso já existam registros nas tabelas [Schemas do Gestão de Vendas](https://tdn.totvs.com/x/5J16J) (A1V) e [Campos do Schema](https://tdn.totvs.com/x/ZJ96J) (A1W), os dados serão atualizados.

**Observação:** O campo **S\_T\_A\_M\_P\_** é atualizado na inclusão de novos registros e na alteração de registros existentes com a data e hora atuais no fuso horário UTC, obtido de forma nativa pelo Banco de Dados.

[Boas práticas para utilização dos campos S\_T\_A\_M\_P\_ e I\_N\_S\_D\_T\_ do TOTVS | DBAccess](https://tdn.totvs.com/pages/viewpage.action?pageId=563943271)

**Saiba Mais:**[DT Descontinuação do programa SetupTGV](https://tdn.totvs.com/pages/releaseview.action?pageId=716359906)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - TOTVS Gestão de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415437052823)

[TOTVS Gestão de Vendas: Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=579468339#PortalGest%C3%A3odeVendas:GuiadeRefer%C3%AAncia-RELACIONADOS)

[Perguntas mais frequentes do Portal Gestão de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=649301318)
