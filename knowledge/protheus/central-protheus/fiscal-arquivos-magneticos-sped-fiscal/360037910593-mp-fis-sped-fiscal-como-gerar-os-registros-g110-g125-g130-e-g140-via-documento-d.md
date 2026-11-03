---
article_id: 360037910593
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: baff923e9792131dedf11647cc63b52f27aab195c98140b012737206444363aa
fetched_at: '2026-06-28T22:42:03.838483+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - SPED FISCAL - Como gerar os registros G110, G125, G130 e G140 via
  Documento de Entrada
type: support-article
updated_at: '2025-03-19T17:54:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037910593-MP-FIS-SPED-FISCAL-Como-gerar-os-registros-G110-G125-G130-e-G140-via-Documento-de-Entrada
---

**Dúvida**Como gerar os registros G110, G125, G130 e G140 via Documento de Entrada?  
   
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
   
**Solução**  
 Para solucionar essa dúvida, realize os seguintes passos:  
  
 1. Realize o lançamento da nota fiscal através da rotina Documento de Entrada (**MATA103**).  
O cadastro da TES para a entrada da nota deve ser feito da seguinte maneira:

CFOP = 1551  
 Calcula ICMS = Sim  
 Livro Fiscal de ICMS = Outros  
 Material de Consumo = Sim  
 Livro Fiscal CIAP = Sim  
Atual.Ativo = Sim

![BLOCO_G_-_DOC_ENTRADA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360049928493/BLOCO_G_-_DOC_ENTRADA.gif)

Observe no módulo Livros Fiscais/Atualizações/Cadastros/Manutenção CIAP, a geração de um registro na tabela SF9, com as informações lançadas por meio da nota fiscal e valor de ICMS calculado no documento.

2. Após o lançamento da nota fiscal, realize a classificação da nota através da rotina Classificação de Compras (**ATFA240**) no módulo de Ativo Fixo.

Obs.: Esse processo é de orientação da equipe de suporte Ativo e Contábil.

![BLOCO_G_-_CLASSIFICACAO_DE_COMPRAS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360049926873/BLOCO_G_-_CLASSIFICACAO_DE_COMPRAS.gif)

3. Acesse a rotina "Estorno CIAP" (**MATA906**) no módulo Livros Fiscais e faça a apropriação do bem.

**Importante:**  
Deve ser informado sempre o último dia do mês para geração da apropriação do crédito CIAP para gravação das informações na tabela SFA. Após a apropriação, verifique se as informações foram gravadas corretamente na tabela mencionada.

![BLOCO_G_-_APROPRIACAO_CIAP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360049041454/BLOCO_G_-_APROPRIACAO_CIAP.gif)

Com a correta apropriação a legenda do bem ficará VERDE.  
Caso existam dúvidas ou problemas com relação a este procedimento, por favor, consulte nossa equipe de suporte Escrita Fiscal e Relatórios.

![BEM_APROPRIADO.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360049927173/BEM_APROPRIADO.JPG)

4. Acesse a rotina Sped Fiscal e gere o arquivo magnético. Veja que os registros do Bloco G foram gerados.

![BLOCO_G_-_GERACAO_SPEDFISCAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360049927493/BLOCO_G_-_GERACAO_SPEDFISCAL.gif)
