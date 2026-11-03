---
article_id: 360010162312
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e7178d9ca396508f6f9dd8ad8b14b3a678ee643b7a5cda7afd0b179904c8db70
fetched_at: '2026-06-28T22:42:02.412228+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registro C116: Cupom Fiscal Eletrônico Referenciado'
type: support-article
updated_at: '2025-02-11T21:27:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010162312-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registro-C116-Cupom-Fiscal-Eletr%C3%B4nico-Referenciado
---

**Dúvida**  
Como gerar o registro C116: Cupom Fiscal Eletrônico Referenciado.  
  
**Ambiente**  
Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Realize a emissão do cupom eletrônico incluído via SIGALOJA, Faturamento ou NF manual de saída com espécie SATCE e o campo **FT\_SERSAT**= “Com a serie do equipamento SAT”;  
  
2. Lance a nota fiscal de devolução via **Compras** ou **N.F. manual de entrada**;  
  
3. Realize o complemento da nota de devolução - opção Cupons Fiscais;  
**Caminho:** Módulo de Livros Fiscais > Atualizações > Movimentos> Nf. Entrada Manual ou Nf. Manual de Saída;  
  
4. Selecione a Nota Fiscal;  
  
5. Clique no botão Ações Relacionadas e depois em Complemento > Cupons Fiscais.

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-6%2018%3A44%3A20.png?version=1&modificationDate=1467841501000&api=v2)  
  
A geração desse registro tem seu roteiro operacional igual ao já existente para geração do registro C114. Quando a espécie do documento for igual a "SATCE" e houver complemento do documento, será gerado o registro C116 ao invés do registro C114.  
  
  
**Importante:****Complemento de Nota Fiscal Automático**   
Ponto de Entrada MATUCOMP: Utilizado para alterações automáticas nos complementos dos documentos fiscais após a emissão das Notas Fiscais. Para informações sobre o Ponto de entrada MATUCOMP, acesse: [MATUCOMP - Alterações automáticas.](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)O parâmetro MV\_ATUCOMP deve ser configurado para que seja possível utilizar o **Ponto de Entrada MATUCOMP,  MV\_ATUCOMP = T** .
