---
article_id: 4416984563735
category: RH - Relatórios Folha
content_hash: df1d443252823435f1f537486ff7afa41752fa304fd2df7175b4681a7e64d222
fetched_at: '2026-06-28T22:43:17.500140+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Descrição do nome do funcionário não é apresentada
  em consultas de filtros
type: support-article
updated_at: '2024-08-21T21:05:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416984563735-RH-Linha-Protheus-GPE-Descri%C3%A7%C3%A3o-do-nome-do-funcion%C3%A1rio-n%C3%A3o-%C3%A9-apresentada-em-consultas-de-filtros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25809474699415) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo Gestão de Pessoal Sistema não apresenta a descrição de todos os nomes dos funcionários em consultas de filtros. A matrícula é informada, porém o nome aparece em branco.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416984384279)****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - todas as versões  
  
**Causa**O problema é devido a consulta padrão que está buscando as informações do campo RA\_NOMECMP (que possui 70 caracteres).   
A consulta em tela deve ser com base no campo RA\_NOME devido a visualização do Browser apresentar apenas 30 caracteres, assim como o campo mencionado.  
  
![](https://totvssuporte.zendesk.com/attachments/token/wCAtbWASqcLQ2xILyyCI8nKwO/?name=inline-1997274967.png)  
  
**Solução**Deve ser ajustada a configuração da Consulta padrão para busca de nomes pelo campo RA\_NOME  
Após abrir a consulta clicando no ícone da lupa, selecione as configurações no ícone de engrenagem, clique duas vezes no campo fórmula ao lado do nome e faça os ajustes.

Salve as alterações e reabra a rotina para verificar a consulta correta e os nomes serem apresentados corretamente.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416984512407)

**Saiba Mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
