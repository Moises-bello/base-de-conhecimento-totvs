---
article_id: 360025945892
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 96deae6f2462c3de87d971749fdadd58e097a480362880d2eeca41517a40e901
fetched_at: '2026-06-28T22:39:58.533566+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Tag Valor
  Serviços e Valor Total Recebido - São Paulo
type: support-article
updated_at: '2024-05-17T14:24:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025945892-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Tag-Valor-Servi%C3%A7os-e-Valor-Total-Recebido-S%C3%A3o-Paulo
---

**Dúvida**Como configurar as tags de Valor Serviços e Valor Total Recebido?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Primeiramente deverá ser criado o parâmetro **MV\_NFSTREC**.

- Criação de **Parâmetros** no arquivo **SX6 – Parâmetros**:

* **Nome da Variável**: MV\_NFSTREC
* **Tipo:** Caractere
* **Descrição:** Habilita a tag <valortotalrecebido> para a emissão de NFSE no município de São Paulo
* **Valor Padrão:** O conteúdo deve constar códigos de serviço utilizados na emissão da NFSE.  
    
  Deverá ser informado neste parâmetro os Códigos de Tributação de Município relacionados aos itens 10.08 e 33.01 conforme legislação.  
  E esses mesmos códigos municipais devem ser informados também no campo B1\_TRIBMUN.

Mais detalhes da configuração:  
- <https://tdn.totvs.com/pages/releaseview.action?pageId=844249273>

Em quais situações deverá informar a tag **ValorTotalRecebido**, e o que deve ser informado em **ValorTotalRecebido**? Como deve ficar a tag **ValorServicos**? Quando houver valor de dedução quais campos deverão ser informados?

Para mais detalhes acesse:  
- <http://tdn.totvs.com/pages/releaseview.action?pageId=382554689>**Obs.:**  
O Valor Total do Serviço é o conteúdo do campo C6\_VALOR.  
O Valor Total Recebido é o calculo dos campos C6\_VALOR - C6\_ABATISS.
