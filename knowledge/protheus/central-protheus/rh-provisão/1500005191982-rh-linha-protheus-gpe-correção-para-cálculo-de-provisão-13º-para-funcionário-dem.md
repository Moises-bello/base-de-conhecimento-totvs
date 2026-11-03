---
article_id: 1500005191982
category: RH - Provisão
content_hash: 8c711102191eb89fe265238c5a07d897d755bc866f4033a4013f5ce61bce310b
fetched_at: '2026-06-28T22:43:55.887445+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Correção para cálculo de provisão  13º  para funcionário
  demitido que apresenta baixa com identificadores incorretos
type: support-article
updated_at: '2025-09-23T12:57:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005191982-RH-Linha-Protheus-GPE-Corre%C3%A7%C3%A3o-para-c%C3%A1lculo-de-provis%C3%A3o-13%C2%BA-para-funcion%C3%A1rio-demitido-que-apresenta-baixa-com-identificadores-incorretos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32904201041047)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Cálculo de provisão de 13º para funcionário demitido apresenta verbas de baixa com identificadores incorretos.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.

**Causa**Ausência de verba com ID de cálculo 1854 (Novo ID).  
  
**Solução**

Houve um ajuste na provisão para gerar baixa da antecipação da 1ª parcela do 13º salário na verba do novo ID **1854** (que deve ser criada com base na verba do ID 0334) quando funcionário teve rescisão e o parâmetro **MV\_PROVRES** está configurado com **N**. Também foi incluído um aviso ao entrar na rotina de provisão para direcionar o usuário a essa documentação.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008110661)  
  
**Observação:**

A Baixa da Antecipação da 1ª Parcela do 13º Salário será na verba com ID 1854 apenas quando o parâmetro MV\_PROVRES estiver configurado com N.  
Quando o parâmetro estiver configurado com S, a baixa será realizada na verba com ID de Cálculo 0334.

**Aviso:**

A falta do cadastro de verba para o ID 1854, ou de qualquer um dos IDs de baixa de rescisão (0274, 0275, 0276, 0277, 0425 e 1854) fará com que não seja gerado a baixa da rescisão nessas verbas, mas sim nas verbas padrão de baixa de pagamento de 13º, o que pode causar divergências nos valores exibidos no relatório de provisão de 13º salário.

Mais informações: <https://tdn.totvs.com/pages/viewpage.action?pageId=592553661>

**Saiba Mais:**

[RH-Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
