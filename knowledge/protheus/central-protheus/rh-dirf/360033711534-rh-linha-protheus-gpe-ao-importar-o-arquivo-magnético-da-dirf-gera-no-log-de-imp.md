---
article_id: 360033711534
category: RH – DIRF
content_hash: e5e8a7653069ed346ea66c63557f9ef3c3c3cecc9919d10e4ecf0befe38f7b7f
fetched_at: '2026-06-28T22:44:06.766576+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao importar o arquivo magnético da DIRF gera no
  log de importação: OPSE valor não previsto para este campo'
type: support-article
updated_at: '2025-08-20T18:57:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033711534-RH-Linha-Protheus-GPE-Ao-importar-o-arquivo-magn%C3%A9tico-da-DIRF-gera-no-log-de-importa%C3%A7%C3%A3o-OPSE-valor-n%C3%A3o-previsto-para-este-campo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34325668295319)** Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao importar o arquivo magnético da DIRF, gera erro no log de importação: **OPSE valor não previsto para este campo,** conforme exemplo abaixoOPSE|016850530001-5|SUL AMERICA COMPANHIA DE SEGURO SAUDE|006246|

![](https://totvssuporte.zendesk.com/attachments/token/iIchdkJs8wUsuQG1iXpiJsbrm/?name=inline1062128529.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Preenchimento errado dos dados do fornecedor de plano de saúde.  
  
**Solução**Verifique que no arquivo magnético conforme imagem acima, esta levando um hífen no CNPJ do Fornecedor de Planos de Saúde/Odontológico, então, entre no cadastro de fornecedor na rotina **Manutenção Tabelas** pelo caminho **>Atualizações >Definições de cálculos >Manutenção de Tabelas**, e verifique nas Tabelas **S016** e **S017** se o campo CNPJ está com conteúdo correto:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11159823105431)  
  
Após verificar e ajustar o cadastro, gere novamente a rotina Gerar Arquivo e Arquivo Magnético.  
  
**Saiba mais**  
[RH - Linha Protheus - GPE - Passo a Passo para gerar dados/gerar Arquivo DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012)   
[RH - Linha Protheus - GPE - Passo a Passo para geração do Arquivo magnético da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092)
