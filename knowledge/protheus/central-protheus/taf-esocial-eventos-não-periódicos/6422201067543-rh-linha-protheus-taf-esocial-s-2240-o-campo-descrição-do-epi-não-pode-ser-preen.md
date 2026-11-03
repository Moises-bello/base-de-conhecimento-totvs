---
article_id: 6422201067543
category: TAF - eSocial - Eventos Não Periódicos
content_hash: 101e53f6e9820f64d3282de516ba066fbd4d86c8f69fc03f0a7ac4ef1b763c15
fetched_at: '2026-06-28T22:45:18.138107+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - S-2240 - O campo "Descrição do EPI" não
  pode ser preenchido
type: support-article
updated_at: '2024-06-03T18:09:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6422201067543-RH-Linha-Protheus-TAF-eSocial-S-2240-O-campo-Descri%C3%A7%C3%A3o-do-EPI-n%C3%A3o-pode-ser-preenchido
---

**Dúvida**

Ao tentar transmitir o evento S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos  para o eSocial, ocorre a seguinte inconsistência:

- **Sequência:** 000001

- **Tipo:** Erro

- **Código da ocorrência:** 2

- **Localização:** /eSocial/evtExpRisco/infoExpRisco/agNoc/epcEpi/epi/dscEPI

- **Descrição:** O campo "Descrição do EPI" não pode ser preenchido. 

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Medicina - S-2240 -Condições Ambientais do Trabalho - Agentes Nocivos - Todas as versões  
  
**Solução**Com relação à inconsistência retornada pelo eSocial, o leiaute do eSocial indica que o campo <dscEPI> deve ser preenchido quando o campo <docAval> não estiver preenchido. Veja o trecho abaixo do novo leiaute eSocial S-1.0:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6421967523991)

Para correção no TAF:

1. Abra o evento S-2240 (TAFA264) para edição:

[Automação Fiscal - Medicina - Como acessar os eventos SST pelo TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409269554327)

2. Acesse a aba "Fator de Risco";

3. Localize o grupo "EPI(S)";

4. Verifique se os campos "ID Desc EPI" e "Certif. EPI" estão preenchidos;

5. Deixe apenas um dos campos preenchidos;

6. Se optar por preencher o campo "Certif. EPI", deixe o campo "ID Desc EPI" vazio.

**Exemplo:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6422083879703)
