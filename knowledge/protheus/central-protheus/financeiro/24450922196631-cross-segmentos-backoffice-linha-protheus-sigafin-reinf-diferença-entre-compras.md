---
article_id: 24450922196631
category: Financeiro
content_hash: d42367021e43af7e76dfa93c97f4cb93663fc71a8ea573242c6b027856e6d832
fetched_at: '2026-06-28T22:38:03.433304+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Diferença entre
  Compras e Financeiro
type: support-article
updated_at: '2024-07-01T13:21:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24450922196631-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Diferen%C3%A7a-entre-Compras-e-Financeiro
---

**Dúvida**Para o reinf qual a diferença entre a geração do título no modulo do compras e financeiro?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Comportamento**

**No Financeiro**, o preenchimento da natureza de rendimento deve ser incluída no Cadastro de Natureza financeira. 

Módulo financeiro>atualizações>cadastros>Natureza

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24450905484951)

**No Financeiro**, se esquecer de informar a natureza de rendimento, é possível adicioná-la desde que o título esteja em aberto.**![Gravar_2024_06_26_13_42_15_450.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24450922167447)**

**No Compras**, o preenchimento da natureza de rendimento deve ser incluída no Cadastro de Produtos

Módulo compras>Atualizações>Cadastros>Produtos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24450905486999)

Se a natureza de rendimento não for informada e o título já foi integrado com o financeiro, será necessário excluir a nota e inseri-lo novamente, pois não é possível adicionar essa informação após a integração entre os módulo, pois o campo fica bloqueado.

**Importante**

Após incluir o título com a natureza de rendimento, para validar se ele será enviado para o painel, é necessário verificar se ele consta na tabela FKW, veja no ponto 2 e ponto 3 da documentação abaixo  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Extrator Fiscal não gera os layout T154 e T158 na tabela TAFST2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18155036570391-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Extrator-Fiscal-n%C3%A3o-gera-os-layout-T154-e-T158-na-tabela-TAFST2)

**Saiba mais:**

[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Executamos o Extrator Fiscal, porém o registro do título não aparece no painel do TAF, o que fazer?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19677367875607-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Executamos-o-Extrator-Fiscal-por%C3%A9m-o-registro-do-t%C3%ADtulo-n%C3%A3o-aparece-no-painel-do-TAF-o-que-fazer?source=search)
