---
article_id: 360010391531
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 8ad7ab0a8232b602494d4a1b42cebc3e7a4e6aa481199428c32da84e6e4daf46
fetched_at: '2026-06-28T22:42:01.195876+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro C173: Operações com Medicamentos (CÓDIGO 01 e 55).'
type: support-article
updated_at: '2025-02-11T21:05:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010391531-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-C173-Opera%C3%A7%C3%B5es-com-Medicamentos-C%C3%93DIGO-01-e-55
---

**Dúvida**  
Como gerar o registro C173: Operações com Medicamentos (CÓDIGO 01 e 55).  
  
**Ambiente**  
MP - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**  
Este registro é gerado para Nota Fiscal com operações de Medicamento, gerado para as espécies NF e SPED. Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Crie um Produto e preencha o campo **Grupo** (**B1\_GRUPO)**.   
2. Configure o parâmetro **MV\_MEDICA**, com os grupos de produto de medicamento para Habilitar o complemento de NF Medicamentos. Grupos de produtos, separados por '/', que identificam operações com medicamentos. 0023/0024/0025/;  
3. Escriture uma NF de medicamento com o produto medicamento;  
4. Realize o complemento de NF de medicamento.   
**Caminho:** Módulo de **Livros Fiscais > Atualizações > Movimentos > Nf. Entrada Manual ou Nf. Manual de Saída. >** **Selecione a NF >  Clique em Ações Relacionadas> Complemento > Medicamentos** (**Tabela CD7**).   

![Capturar3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360014642151/Capturar3.PNG)
