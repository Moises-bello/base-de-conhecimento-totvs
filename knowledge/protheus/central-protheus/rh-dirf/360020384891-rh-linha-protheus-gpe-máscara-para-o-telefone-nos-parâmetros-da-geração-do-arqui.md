---
article_id: 360020384891
category: RH – DIRF
content_hash: 2cd2dfa43c02fd6abf1176761f3906d89f4470d6bd055cb0cf5e1eab1394cd48
fetched_at: '2026-06-28T22:44:07.052717+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Máscara para o telefone nos parâmetros da geração
  do arquivo DIRF
type: support-article
updated_at: '2025-08-19T13:12:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020384891-RH-Linha-Protheus-GPE-M%C3%A1scara-para-o-telefone-nos-par%C3%A2metros-da-gera%C3%A7%C3%A3o-do-arquivo-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34286762272407)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Não foi encontrada sequencia valida de registros DIRF + RESPO + DECPJ ou DECPF no inicio do arquivo, Linha 2 e ordem 4 ou 5.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões.  
  
**Causa**Quando o erro gerado no log do PDG for na Linha 2 e ordem 4 ou 5, devemos verificar no leiaute da DIRF o que é esperado para o arquivo magnético.   
Nesse caso, o leiaute informa que o numero do telefone deve ser enviado conforme abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435931620119)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435918486423)  
  
**Solução**Nos parâmetros de Geração do **Arquivo Magnético**, pelo caminho **>Miscelânea >Dirf >Arquivo Magnético**, informe o telefone conforme formato abaixo:  
**(099 ) 9999-9999/R:99999**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016149852)

Caso o telefone seja de **celular** que contenha mais um 9 o telefone deve ser preenchido conforme abaixo:  
**(099 )99999-9999/R:99999**   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016150752)

**Atente-se aos espaços eles fazem parte da máscara.**

**Saiba mais**  
[Layout DIRF 2023 - Receita Federal](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/documentos-tecnicos/dirf/leiaute-dirf-2023.pdf/view)  
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
