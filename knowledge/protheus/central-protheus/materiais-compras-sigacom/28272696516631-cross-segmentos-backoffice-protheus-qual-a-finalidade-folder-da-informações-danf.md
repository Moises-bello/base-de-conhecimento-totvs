---
article_id: 28272696516631
category: Materiais - Compras (SIGACOM)
content_hash: fe2e32fc3ebeb4d4cba2fdf55975fa58f56bccd255bfe9bc9932351d3607ac28
fetched_at: '2026-06-28T22:41:11.877501+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Qual a finalidade Folder da Informações
  DANFE no Documento de Entrada?
type: support-article
updated_at: '2025-10-30T13:37:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28272696516631-Cross-Segmentos-Backoffice-Protheus-Qual-a-finalidade-Folder-da-Informa%C3%A7%C3%B5es-DANFE-no-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28272696493591) Tempo aproximado para leitura: **00:02:SS min** **Dúvida**

Qual a finalidade Folder da Informações DANFE no Documento de Entrada.

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Versão 12

**Solução**  
Esta pasta apresenta os dados para emissão da **Guia DANFE**, conforme Decreto 45.490/00 de São Paulo.

***Obs.:***

Para gerar a **Guia DANFE**, a partir das informações cadastradas no Documento de Entrada, é necessário solicitar o rdmake   
padrão, por meio do Suporte (Help Desk) da equipe Fiscal, e realizar a customização para geração do arquivo XML.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28272659964311)

**Código Transportadora** (F1\_TRANSP): Código de identificação da transportadora.  
**Placa** (F1\_PLACA): Placa do veículo.  
**Chave NFE** (F1\_CHVNFE): Numero da chave de acesso da Nota Fiscal Eletrônica.  
Dica 1: Utilize os parâmetros MV\_DCHVNFE e MV\_CHVESPE para habilitar a edição do campo F1\_CHVNFE, caso o documento não utilize formulário próprio.  
Dica 2: Utilize o parâmetro MV\_VCHVNFE para que o sitema valide se a chave confere com a nota que está sendo digitada.  
**Valor Pedágio** (F1\_VALPEDG): Valor de pedágio.  
**Espécie 1, 2, 3 e 4 (F1\_ESPECI(1,2,3,4)):** Espécie ou volume de embalagem. Ex: caixas.  
**Volume 1, 2, 3 e 4** (F1\_VOLUME(1,2,3,4)): Quantidade de volume referente a espécie de mesmo número.   
**Peso Bruto** (F1\_PBRUTO): Peso bruto da mercadoria contida na nota fiscal.  
**Peso Líquido** (F1\_PLIQUI): Peso líquido da mercadoria contida na nota fiscal.

**Fornecedor Retirada** (F1\_FORRET + F1\_LOJARET): Fornecedor onde foi retirada a mercadoria.

**Fornecedor Entrega** (F1\_FORENT + F1\_LOJAENT): Fornecedor onde foi entregue a mercadoria.  
**Tipo Frete** (F1\_TPFRETE): O frete poderá ser dos seguintes tipos: CIF (C), FOB (F), por conta de Terceiros (T), sem frete (S).  
**Tipo CT-e (F1\_TPCTE)**: O CT-e poderá ser dos seguintes tipos: Normal (N), Complemento de Valor (C), Anulação de Valor (A), Substituto (S).  
**Modalidade (F1\_MODAL)**: Indica a modalidade do transporte: Rodoviário (01), Aéreo (02), Aquaviario (03), Ferroviario (04), Dutoviario (05), Multimodal (06).  
**Número AIDF** (F1\_NUMAIDF): Numero da Autorização de Impressão de Documentos Fiscais (AIDF).

**Ano AIDF** (F1\_ANOAIDF): Ano da Autorização de Impressão de Documentos Fiscais (AIDF).  
Dica: Utilize o ponto de entrada MT103DCF para adicionar o botão “Mais Informações” e informar quais campos adicionais deseja visualizar no folder DANFE.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
