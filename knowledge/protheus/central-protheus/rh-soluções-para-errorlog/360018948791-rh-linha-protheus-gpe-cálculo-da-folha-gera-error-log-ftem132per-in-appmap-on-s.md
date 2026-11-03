---
article_id: 360018948791
category: RH - Soluções para error.log
content_hash: 213990deaced370aaf47fc06ff7fc7fee82da116e0af5dd1d282e19a20ba74b2
fetched_at: '2026-06-28T22:44:08.795040+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Cálculo da Folha gera error log: FTEM132PER in
  AppMap on S_CARGARCH'
type: support-article
updated_at: '2025-08-20T17:42:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018948791-RH-Linha-Protheus-GPE-C%C3%A1lculo-da-Folha-gera-error-log-FTEM132PER-in-AppMap-on-S-CARGARCH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34323280072343)** Tempo aproximado para leitura:**00:01:00 min**

**Ocorrência**No módulo gestão de pessoal, ao calcular folha de pagamento sistema gera *error log* FTEM132PER in AppMap on S\_CARGARCH.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Sistema não calcula o complemento de 13º fora do mês 12, gerando *error log*.  
  
**Solução**Ajuste nas validações do sistema para que seja possível calcular o complemento de 13º em qualquer mês que o 132 tenha sido calculado.  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realize o *backup* prévio;  
2. Aplique o pacote de atualização: [RH Expedição Contínua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search)  
3. Refaça o teste

**Saiba Mais:**

Pacote de Expedição Contínua do RH:[https://centraldeatendimento.totvs.com/hc/pt-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)[br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)
