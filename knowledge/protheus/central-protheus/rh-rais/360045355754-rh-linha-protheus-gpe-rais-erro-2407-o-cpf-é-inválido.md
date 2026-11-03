---
article_id: 360045355754
category: RH - RAIS
content_hash: ba007b523eb7bebf912f205d23f6b2bd1621249c1e740296ab08b470d1537f33
fetched_at: '2026-06-28T22:44:05.804637+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - RAIS erro - 2407 - O CPF é inválido
type: support-article
updated_at: '2025-08-06T14:52:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045355754-RH-Linha-Protheus-GPE-RAIS-erro-2407-O-CPF-%C3%A9-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33987409636631) Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**

RAIS erro - 2407 - O CPF é inválido

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal –  Todas as versões  
  
**Solução**

Ao realizar a alteração do CPF no protheus, o sistema retorna a mensagem:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064197233)

Esta mensagem ocorre porque a empresa está com os parâmetros do eSocial habilitado.

Atenção: Não pode desabilitar para realizar a inclusão, pois se o numero do CPF está errado terá que ajustar também na base do governo.

Para este cenário não é possível realizar a exclusão da tabela SRA, pois o empregado tem cálculo de folha no ano base.

Deverá realizar o seguinte procedimento:

Para o envio da RAIS deverá alterar o CPF na tabela SR2 e gerar o arquivo magnético, rotina GPEM530 novamente para esta pessoa.

Ou deverá ajustar dentro do validador da rais GDRAIS

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
