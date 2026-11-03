---
article_id: 360015913532
category: ADVPL - Ponto de Entrada
content_hash: 1983ffbdda5f0b25a4c88c8ebb8ced2c3b919ce43f2b8d10f6f7a51ec5b568b1
fetched_at: '2026-06-28T22:40:11.642599+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ao utilizar ponto
  de entrada LJ7020 cai em help do sistema
type: support-article
updated_at: '2022-06-21T17:59:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015913532-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ao-utilizar-ponto-de-entrada-LJ7020-cai-em-help-do-sistema
---

**Ocorrência**Ao utilizar o ponto de entrada LJ7020 o sistema não permiti utilizar a forma de pagamento que escondemos no ponto de entrada

```
"Não há nenhuma administradora financeira cadastrada para a forma de pagamento XXXXXXX".
```

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011634091/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Administradoras financeiras não encontradas na Tabela SAE.  
  
**Solução**É necessário ter as administradoras financeiras devidamente cadastradas. Tabela SAE (Módulo SIGALOJA /  Atualizações / Cadastros / Adm Financeiras). Sem o prévio cadastro, não será possível efetuar a finalização e com isso será exibida a mensagem: "Não há nenhuma administradora financeira cadastrada para a forma de pagamento X".  
Anexo evidencia com os dois cenários: Com e sem Adm Financeira.  
OBS.: essa ocorrência envolve os pontos de entrada FTVD7020 e LJ7020   
  
**Saiba mais**  
**[LJ7020 - Esconde todas as formas de pagamento](http://tdn.totvs.com/display/public/PROT/LJ7020+-+Esconde+todas+as+formas+de+pagamento)**  
**[ADV00076\_PE\_FTVD7020](http://tdn.totvs.com/display/PROT/ADV00076_PE_FTVD7020)**
