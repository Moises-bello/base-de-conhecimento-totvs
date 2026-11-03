---
article_id: 360018282551
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e2c5674ce1d7e92b7631cd31081857ed78e065384c719e7847301a30d2b2ee6d
fetched_at: '2026-06-28T22:42:00.988792+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Registro 0200
  Campo 08 (COD_NCM)
type: support-article
updated_at: '2024-06-19T18:12:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018282551-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Registro-0200-Campo-08-COD-NCM
---

**Dúvida**Como preencher o **NCM** do **Campo 08 (COD\_NCM)** do Registro **0200**?  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Preencha o Campo **Pos. IPI/NCM (B1\_POSIPI)** no cadastro do Produto.

O Campo **FT\_POSIPI**é preenchido após emissão ou inclusão do documento fiscal. Se o NCM não estiver preenchido no campo 08 - COD\_NCM do SPED FISCAL, deverá revisar o cadastro do produto, caso não exista, será necessário preencher o NCM no campo **Pos. IPI/NCM (B1\_POSIPI),** em seguida, exclua o documento fiscal e escriture novamente.

![Capturar1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360013488332)

Na Wizard de geração do arquivo **SPEDFISCAL,** informe o parâmetro **Tipo de atividade** = 0 INDUSTRIA ou EQUIPARADO.

Conforme trecho do Guia Prático:  
"Fica dispensado o preenchimento deste campo, quando o tipo de item informado no campo TP\_ITEM for igual a 07 - Material de Uso e Consumo; ou 08 – Ativo Imobilizado; ou 09 -Serviços; ou 10 - Outros insumos; ou 99 - Outras."  
No padrão configure o **Tipo de produto** com o tipo abaixo:  
ME = 00 Mercadoria para revenda  
MP = 01 Matéria-prima  
EM = 02 Embalagem  
PP = 03 Produto em processo  
PA = 04 Produto acabado  
SP = 05 Subproduto  
PI = 06 Produto intermediário  
  
Caso não seja os mencionados acima, preencha o parâmetro **MV\_LEVANCM**.
