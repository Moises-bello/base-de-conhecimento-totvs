---
article_id: 360054076053
category: RH - Integração de Titulo
content_hash: 279962c0e4f9f5fa315cea00a1831273cce8689ce3d3fb3e8e4fe6badf1c73f4
fetched_at: '2026-06-28T22:43:36.362325+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Geração de títulos não grava fornecedor já  cadastrado
  no financeiro, gerando um novo fornecedor
type: support-article
updated_at: '2025-07-22T20:48:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054076053-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-de-t%C3%ADtulos-n%C3%A3o-grava-fornecedor-j%C3%A1-cadastrado-no-financeiro-gerando-um-novo-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33641480192151) Tempo aproximado para leitura: 00:02:00 min

**Dúvida**Geração de títulos não grava fornecedor já cadastrado no financeiro, gerando um novo fornecedor.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**Para que a geração de títulos grave um fornecedor já cadastrado no financeiro, é necessário que tenha ocorrido a amarração entre funcionário e fornecedor, seja pela geração automática de títulos ou pela amarração manual.

A amarração entre o Funcionário e o Fornecedor sempre será feita pela tabela de **Participantes (RD0)**, pelos campos **FORNECEDOR** (RD0\_FORNEC) e **LOJA** (RD0\_LOJA), independentemente do código do fornecedor estar igual à matrícula do funcionário ou não.

Caso já exista algum Funcionário cadastrado como Fornecedor, deverá ser feita a amarração manual na rotina Cadastro Participantes (tabela RD0), nos campos **FORNECEDOR** (RD0\_FORNEC) e **LOJA** (RD0\_LOJA), pois caso esses campos estejam em branco, será cadastrado um novo fornecedor para este participante.  
  
1) Acesse o módulo 06 - Financeiro: Atualizações / Cadastros / Fornecedores e verifique o código e loja do fornecedor.

2) Verifique o código do fornecedor: ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088853154)

3) Em seguida, acesse o módulo 53 - Avaliação e Pesquisa de Desempenho: Atualizações / Participantes / Cadastros.

4) Na aba "Viagem",   preencha o campo Fornecedor e loja , de acordo  com o código do cadastro:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088856074)

5) Acesse a rotina GPEM650 e efetue a geração do título.

**Saiba mais:** [MP - GPE - Cadastro Automático de Fornecedores com as informações de Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015466272-MP-GPE-Cadastro-Autom%C3%A1tico-de-Fornecedores-com-as-informa%C3%A7%C3%B5es-de-Funcion%C3%A1rios)
