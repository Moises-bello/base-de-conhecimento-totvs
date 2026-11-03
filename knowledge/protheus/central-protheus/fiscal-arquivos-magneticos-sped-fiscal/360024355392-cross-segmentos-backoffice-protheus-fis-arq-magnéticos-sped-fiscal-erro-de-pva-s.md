---
article_id: 360024355392
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: f4b3dd49ae01ca4236c68d36bf7773904820503a3dd7677ef9a484e545622e43
fetched_at: '2026-06-28T22:42:02.326560+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Erro de PVA: "Se o campo "COD_MOD" for igual a 07, 08, 8B, 09, 10, 11, 26 ou 27,
  a data informada deverá ser menor que 01/01/2019"'
type: support-article
updated_at: '2025-02-11T20:50:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024355392-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Erro-de-PVA-Se-o-campo-COD-MOD-for-igual-a-07-08-8B-09-10-11-26-ou-27-a-data-informada-dever%C3%A1-ser-menor-que-01-01-2019
---

**Ocorrência**Ao importar o arquivo do **Sped Fiscal**, consta o seguinte erro de validação no PVA:   
Se o campo "**COD\_MOD**" for igual a 07, 08, 8B, 09, 10, 11, 26 ou 27, a data informada deverá ser menor que 01/01/2019.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Causa**O erro não ocorre no arquivo gerado pelo **Protheus**, visto que, o mesmo contém o modelo de documento de acordo com o *Layout* do **Sped Fiscal**. O erro ocorre no validador da **Receita Federal**, onde o mesmo impede o lançamento dos modelos de documentos a partir da data 01/01/2019.  
O erro em questão ocorreu com um cliente da **TOTVS** que realizou uma consulta na **Receita Federal.**

**Solução**  
  
Alteração da Validação do **Campo 11** do Registro **D100**O registro **D100** é onde informamos os diversos tipos de conhecimentos de transporte, já o **campo 11** (Data da emissão do documento fiscal) é destinado a informar a data de emissão do conhecimento em questão.   
  
A partir de 1º de janeiro de 2019 a nova regra de validação deste campo não permitirá que os tipos de conhecimento de transporte emitidos em papel possuam data de emissão que seja igual ou superior a 1º de janeiro de 2018.  
  
Isso porque o [inciso VIII da Cláusula vigésima quarta do Ajuste SINIEF 09/2007](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2007/AJ_009_07) definiu como prazo máximo para a extinção dos conhecimentos de transporte emitidos em papel a data de 2 de outubro de 2017 e para acompanhar esta determinação na legislação essa validação se faz necessária. Segue abaixo a relação dos tipos de conhecimentos de transporte afetados por esta alteração do *layout* da **EFD ICMS/IPI**:

I – Nota Fiscal de Serviço de Transporte, **modelo 7**;

II – Conhecimento de Transporte Rodoviário de Cargas, **modelo 8**;

III – Conhecimento de Transporte de Cargas Avulso, **modelo 8B**;

IV – Conhecimento de Transporte Aquaviário de Cargas, **modelo 9**;

V – Conhecimento Aéreo, **modelo 10**;

VI – Conhecimento de Transporte Ferroviário de Cargas, **modelo 11**;

VII – Conhecimento de Transporte Multimodal de Cargas – CTMC, **modelo 26**; e

VIII – Nota Fiscal de Serviço de Transporte Ferroviário de Cargas, **modelo 27**.

Todos os modelos listados acima foram substituídos pelo pelos **modelos eletrônicos 57** (Conhecimento de Transporte Eletrônico [**CT-e**]), **63** (Bilhete de Passagem Eletrônico [**BP-e**]) e **67** (Conhecimento de Transporte Eletrônico Para Outros Serviços [**CT-e OS**]) de modo que apenas estes documentos serão aceitos para as escriturações a partir de 1º de janeiro de 2018.

Ressaltamos que o **Protheus** está adequado para gerar os documentos acima citados, a empresa é responsável por verificar na legislação, qual modelo de documento será de acordo para que não ocorra o erro de validação.
