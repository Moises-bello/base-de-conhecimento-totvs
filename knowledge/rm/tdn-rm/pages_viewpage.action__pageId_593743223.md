---
content_hash: b04cabfb16e354b4ddfd7517a09627c96544d887bd17d1f384f6b05f286f3e19
fetched_at: '2026-06-29T00:10:56.984546+00:00'
page_id: '593743223'
product: rm
source: tdn-rm
title: NFS-e - Deduções por item com percentual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593743223
version: 6
---

*O(s) processo(s) descrito(s) a seguir refere(m)-se ao serviço de Envio de **NFS-e** disponível no RM.*

De acordo com a Legislação de cada município, que utiliza **layout [DSFNET,](https://www.dsfnet.com.br/site/)**o Grupo de Dedução da **NFS-e,** quando parametrizado para gerar por **Percentual de Dedução,**será gerado considerando o valor do item aplicado o percentual de cada item.

Para definir **Deduções com percentual** para o item de um movimento, é necessária a parametrização do tipo de movimento. Acesse:  Gestão de Estoque, Compras e Faturamento, na aba "Ambiente" clique no meu **Parâmetros | Gestão de Estoque, Compras e Faturamento**. Selecione a classificação do Tipo de Movimento **(exemplo: Outras Movimentações)**, avance, selecione o tipo de movimento a ser parametrizado parametrize a **etapa 37**, conforme demonstra a imagem abaixo.

Imagem

Após o envio da NFS-e, o arquivo XML da nota terá a seguinte estrutura, sendo especificado o percentual definido por item e seu respectivo valor.

Imagem

**Percentual de Deduções deve ser informado no seguinte caminho:**

**Nos itens do movimento**, selecione e edite o item desejado. Clique na seção **Tributos e Valores** em seguida em **Valores.** Defina o percentual da dedução no campo **Percentual deduzido**, conforme demonstrado abaixo.

\* Percentual de Dedução

Disponível a partir da 12.1.28
