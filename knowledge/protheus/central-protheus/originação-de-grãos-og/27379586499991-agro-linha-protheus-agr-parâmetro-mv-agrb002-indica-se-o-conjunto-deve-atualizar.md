---
article_id: 27379586499991
category: Originação de Grãos (OG)
content_hash: 1d9ba5348732c15148dbce424d98923b0d9eb26ccc3f6235f0543970d563e559
fetched_at: '2026-06-28T22:45:41.199720+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parâmetro MV_AGRB002 - Indica se o conjunto deve
  atualizar estrutura da pluma
type: support-article
updated_at: '2025-04-23T13:31:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27379586499991-Agro-Linha-Protheus-AGR-Par%C3%A2metro-MV-AGRB002-Indica-se-o-conjunto-deve-atualizar-estrutura-da-pluma
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27379586487447)** Tempo aproximado para leitura: **00:00:40 min  
  
Dúvida**Para que serve os **Parâmetro MV\_AGRB002 - Indica se o conjunto deve atualizar estrutura da pluma**? **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12 **Solução**

Parâmetro MV\_AGRB002 - Indica se o conjunto deve atualizar estrutura da pluma:

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | O parâmetro MV\_AGRB002 é do tipo caractere e está localizado na rotina de cadastro de conjunto(AGRA611).  Se o valor for S, irá atualizar a estrutura(SG1) do produto do tipo pluma a partir do cadastro de conjunto.  Se o valor for N, não irá atualizar.  Tem impacto também na rotina de encerramento de fardão(AGRA620), quando o parâmetro MV\_AGRB002 esta como N e o produto pluma gera produção e os itens adicionais geram movimentações, é gerado movimentações interna dos itens adicionais conforme parametrizado no cadastro de conjunto. |
| **Parâmetro(s):** | MV\_AGRB002 |
| **País:** | Todos |
| **Banco de Dados:** | Todos Homologados pela Totvs. |
| **Sistemas Operacionais:** | Todos Homologados pela Totvs. |
