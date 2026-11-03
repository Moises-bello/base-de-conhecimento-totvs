---
article_id: 360025899871
category: Financeiro - Contas a Pagar
content_hash: e6a70b557d7fd0fd2eed2494d4698b08b46684e71ec7d995c5929feb82ca05c4
fetched_at: '2026-06-28T22:38:08.407281+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento BackOffice Linha Protheus - Help: NOMOVADT'
type: support-article
updated_at: '2021-11-23T17:42:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025899871-Cross-Segmento-BackOffice-Linha-Protheus-Help-NOMOVADT
---

**Ocorrência**Ao tentar compensar um título do tipo PA é apresentado o Help NOMOVADT  
**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1.17

**Causa**O Help é apresentado devido a **inclusão** do **PA** na rotina **FINA050** ter sido feita com a pergunta **MOV. Banc. sem Cheque? = NÃO**  
**Solução**Corrija os **PA's** (Pagamento Antecipado) que não aparecem na relação dos **títulos** a serem **compensados** com a mensagem **Help NOMOVADT**, realize os seguintes passos:  
  
1. Acesse a rotina **FINA090** (Baixas Automáticas) e clique no botão **+AUTOMATICA**.   
2. Marque a opção **TITUTOS**= preencha os dados necessários como **Vencimentos**, **Banco** e **motivo de Baixa**.   
3. Quando a seleção de **títulos** apresentar, selecione o **PA** com erro e peça para **baixar**.  
4. Neste momento o sistema **NÃO** irá baixar o **PA** de fato, apenas irá movimentar a tabela **SE5** para que o **PA** fique disponível para a **compensação** com outros **títulos**;
