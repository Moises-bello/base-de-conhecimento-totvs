---
article_id: 28679743163031
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 58e51e35611e19197216bc55344c47ab98598521132b427208660f4a673f4bba
fetched_at: '2026-06-28T22:39:08.162357+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como não copiar o
  cadastro de produto relacionado com o MV_CADPROD
type: support-article
updated_at: '2025-03-12T12:26:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28679743163031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-n%C3%A3o-copiar-o-cadastro-de-produto-relacionado-com-o-MV-CADPROD
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28679743148439) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como não efetuar a copia do produto, vinculado as tabelas contidas no parametro MV\_CADPROD?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**Quando o produto possui amarração as rotinas de cadastros complementares como, por exemplo, "Produto x Fornecedor" ou "Complemento de produto".

**Se utilizar a relação de tabelas no parametro MV\_CADPROD:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Utilidade e configuração do parâmetro MV\_CADPROD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068032-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utilidade-e-configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CADPROD)

A cópia do cadastro de produto (MATA010), sera replicada para as demais rotinas que possuem a amarração. Este comportamento padrão visa copiar todos os relacionamentos do item, mantendo a integridade da cópia do registro.

É possível não efetivar a replica das tabelas e cadastros complementares, através do uso do ponto de entrada: [MTA010NC - Relaciona campos que não devem ser copiados na inclusão](https://tdn.totvs.com/x/bORc)

Para exemplos de uso e maiores informações sobre o ponto de entrada consulte a págna do TDN no link acima.

**Saiba mais**:

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
