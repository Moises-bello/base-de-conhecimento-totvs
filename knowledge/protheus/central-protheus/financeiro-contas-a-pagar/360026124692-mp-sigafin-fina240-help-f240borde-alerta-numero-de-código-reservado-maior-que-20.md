---
article_id: 360026124692
category: Financeiro - Contas a Pagar
content_hash: bd700128e2f793977c878cbcba755af20e6838a8d9055e4e7ce71c4b54693be0
fetched_at: '2026-06-28T22:38:09.882917+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA240 - Help F240BORDE alerta "Numero de código reservado
  maior que 20"
type: support-article
updated_at: '2024-06-05T11:59:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026124692-MP-SIGAFIN-FINA240-Help-F240BORDE-alerta-Numero-de-c%C3%B3digo-reservado-maior-que-20
---

**Dúvida**Ao tentar gerar um borderô de pagamentos, o sistema apresenta o Help: F240BORDE alerta "Numero de código reservado maior que 20"  
  
 **Ambiente**Microsiga Protheus – Financeiro – FINA240 - A partir da versão 11.80

**Causa**   
 Esse incidente ocorre na **FINA240,** quando ao clicar no borderô o sistema exibe a mensagem:  
Help: F240BORDE **"Numero de código reservado maior que 20"**

**Solução**No momento da **geração do borderô**, indica que o número sequencial do **borderô**, apresentado em tela está divergente do número gravado no parâmetro **MV\_NUMBORP** ou seja está igual ao número gravado no parâmetro, porém menor que o registro na tabela **SEA** no campo **EA\_NUMBOR**.

Exemplo: Na tabela **SEA** o campo **EA\_NUMBOR** está 2249 e em tela e no parâmetro **MV\_NUMBORP**está 2255.  
Neste caso, a solução é alterar o parâmetro **MV\_NUMBORP**para 2256, para prosseguir com o processo.
