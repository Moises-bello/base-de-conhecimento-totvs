---
article_id: 360024735991
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: b8549af398620cb1022d74f223b5e49ff83b24a746faf1dc9326c46cf4d2f78c
fetched_at: '2026-06-28T22:42:02.468584+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Unidade de medida com tamanho 06 no Sped Fiscal
type: support-article
updated_at: '2025-02-11T21:34:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024735991-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Unidade-de-medida-com-tamanho-06-no-Sped-Fiscal
---

**Dúvida**Como gerar o arquivo do Sped Fiscal com os campos 02 do registro 0190 e 06 do registro 0200 preenchido com a unidade de medida com 06 dígitos conforme a tabela da Receita Federal?  
   
 **Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
   
**Solução**Para gerar os campos 02 do registro 0190 e 06 do registro 0200 preenchidos com a unidade de medida com 06 dígitos, é POSSÍVEL aumentar o tamanho dos campos de unidade de medida no Protheus através da opção **GRUPO DE CAMPOS** (**Grupo 122**).

**Obs.:** A rotina Grupo de Campos está com error log, por isso, para a correção, recomendamos que seja aberto um ticket para a equipe de Framework solicitando a associação a **ISSUE DFRM4-676**.

**ATENÇÃO!!!**O Guia Prático do Sped Fiscal não faz referência a tabela da Receita Federal, sendo assim, entendemos que a utilização da mesma não é obrigatória no Sped e que a unidade de medida com tamanho 02 atende o que pede o Guia Prático.

Por padrão, o Protheus utiliza a unidade de medidas com tamanho 02, por isso, será necessário avaliar todos os impactos que tal alteração poderá causar caso o tamanho seja alterado para 06.

Estes impactos poderão estar relacionados a:

- Relatórios customizados;  
- Procedimentos referentes ao estoque.
