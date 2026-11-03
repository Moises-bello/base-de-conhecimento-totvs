---
article_id: 360052997173
category: NFe - Nota Fiscal Eletrônica
content_hash: 0c4452f88d8d0495ee50df53b19e3fa455b3a610161a52bfea5d704593cb43da
fetched_at: '2026-06-28T22:40:01.535571+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 701 Rejeição :
  Não informado Nota Fiscal referenciada (CFOP de Exportação Indireta)'
type: support-article
updated_at: '2025-10-17T20:50:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052997173--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-701-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-Nota-Fiscal-referenciada-CFOP-de-Exporta%C3%A7%C3%A3o-Indireta
---

**Dúvida**Como corrigir a rejeição abaixo, na transmissão de nota de exportação?  
701 Rejeição : Não informado Nota Fiscal referenciada (CFOP de Exportação Indireta).

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**Esta rejeição costuma ocorrer quando está transmitindo uma nota de exportação indireta sem referenciar a nota origem.  
Quando for emitida uma nfe com CFOP igual a **3.503** ou **7.501**, e não for referenciada a nfe (na *tag* **refNFe**) recebida com fim específico de exportação, será retornada a rejeição 701 - Não informado Nota Fiscal referenciada (CFOP de Exportação Indireta). 

Descrição dos CFOP's:

* **3.503 -** Devolução de mercadoria exportada que tenha sido recebida com fim específico de exportação;
* **7.501 -** Exportação de mercadorias recebidas com fim específico de exportação.

Exemplo hipotético:  
Foi emitida uma nfe com CFOP 7.501, com o Grupo de Exportação Indireta (*tag* **exportInd**) e sem a chave de acesso da nfe recebida para exportação, informada no Grupo de Documento Fiscal Referenciado (*tag* **refNFe**). Nessa situação a nfe será rejeitada pelo motivo 701.

Para solução desta rejeição, deve-se informar a chave de acesso da nfe de origem (recebida para exportação), preenchendo os campos a seguir pelo módulo Livros Fiscais.

Primeiramente é preciso se certificar de que trata-se de uma exportação indireta, pois é sabido que na exportação indireta existe transmissão de uma nota de importação anterior.

Confirmado que é uma exportação indireta, acesse o módulo Livros Fiscais, e vá em:  
- **Atualizações**  
- **Movimentos**  
**- NF Manual de Saída**  
**- Complementos**  
**-** Pasta **Exportação**, e informar os dados a seguir.

Preencher nos complementos de exportação, os três campos que são obrigatórios para esse tipo de nota:  
-CDL\_NRREG   
-CDL\_CHVEXP   
-CDL\_QTDEXP

Após o preenchimento dos complementos, basta retransmitir a nota rejeitada.

**\*Importante**: Caso tenha integração com o módulo de exportação **SIGAEEC**, será necessário desabilitar a integração antes da transmissão, configurando o parâmetro **MV\_EECFAT=.F.**, e reativar após a transmissão.

Veja regra de validação da Sefaz: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084236654/mceclip0.png)**

Referência

* Nota Técnica 2015/002 (v. 1.40) - <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VNyyxYte6T4=>
