---
article_id: 5709081555095
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 9b77f1c6d81a31a543cb03d1e116633242c107c4adfc1c6f27c0dee605a2e3d3
fetched_at: '2026-06-28T22:42:02.379466+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registro 0220 Erro: Não podem ser informados GTINs iguais para fatores de conversão
  diferentes'
type: support-article
updated_at: '2025-10-29T17:12:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5709081555095-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registro-0220-Erro-N%C3%A3o-podem-ser-informados-GTINs-iguais-para-fatores-de-convers%C3%A3o-diferentes
---

**Ocorrência**

Ao validar o arquivo txt do **Sped Fiscal** gerado pelo sistema ocorre o seguinte erro de validação no **PVA da Receita Federal**:

**0220 - Não podem ser informados GTINs iguais para fatores de conversão diferentes**  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Causa**Este incidente ocorre, pois a configuração está incorreta no **Cadastro de Produtos (Tabela SB1)**  e no **Indicador de Produtos (Tabela SB5)**  
  
  
**Solução**Como o ***Layout* 16** do **Sped Fiscal**  passou a validar operações que contemplam a segunda unidade de medida, o código de barras informado no **Campo 04 do registro 0200 - Tabela de Identificação do Item** e o informado no **Campo 04 do registro  0220 - Fatores de Conversão de Unidades** devem ser distintos a depender do tamanho do código conforme trecho abaixo do guia prático do **Sped Fiscal**:  
  
![](https://totvssuporte.zendesk.com/attachments/token/bdRHbf0TedXIbmQGzg3VCp8DJ/?name=inline1648552649.png)​  
  
Quanto a funcionalidade do sistema, para gerar o código de barras no **0200,** o  Protheus  valida dois campos: **Cod Barras - B1\_CODBAR** e **Cod.GTIN - B1\_CODGTIN.**  
  
Se somente o **B1\_CODBAR** estiver preenchido, o sistema busca informação desse campo. Se ambos os campos estiverem preenchidos o sistema busca os dados do **B1\_CODGTIN.**  
  
Já para gerar o **Código de Barras** no **0220** o sistema valida os dados do campo **2 - UN Cod Bar -  B5\_2CODBAR** quando o campo **B5\_UMDIPI - Unid. Medida da DIPI** estiver preenchido.  
  
Essa alteração é valida para movimento a partir de Janeiro/2022, a fim de atender a exigência do fisco quanto ao ***Layout 16.***  
  
Abaixo teste realizado, simulando cenário em que de acordo com o tamanho do GTIN o **Código de Barras** da 1ª unidade de medida deve ser diferente do código de barras da 2ª unidade de medida demonstrando que os registros são gerados corretamente pelo sistema:  
**Print do Cadastro de Produto:**  
  
![](https://totvssuporte.zendesk.com/attachments/token/gqRafbhO3P2tGHEcdIRLMz67q/?name=inline-1506810572.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/YhfbYgh51sdGENefTbLVl4BXE/?name=inline-841966141.png)​  
  
**Print do arquivo txt do Sped Fiscal gerado:**  
  
![](https://totvssuporte.zendesk.com/attachments/token/aYcjxNEgu2cjPIhchWeacHZAF/?name=inline1341550724.png)
