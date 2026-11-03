---
article_id: 19276098003863
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 727219276f8889886244307cdc1121914242ca549ae56d31eda234b80a80119b
fetched_at: '2026-06-28T22:37:23.898434+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Mensagem de Compartilhamento
  de Tabelas do Gestão de Contratos x Financeiro
type: support-article
updated_at: '2026-02-10T18:21:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19276098003863-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Mensagem-de-Compartilhamento-de-Tabelas-do-Gest%C3%A3o-de-Contratos-x-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19276088501399) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao entrar em rotina do módulo de Gestão de Contratos ocorre mensagem referente ao Compartilhamento Tabelas do Gestão de Contratos x módulo Financeiro

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19276119826711)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Sobre a mensagem ela ocorre quando ocorre uma incompatibilidade de compartilhamentos de tabelas do Gestão de Contratos e o módulo Financeiro (SE1 e SE2), e o módulo realiza essa essa validação de compartilhamento de tabelas quando quando da utilização conjunta com o módulo Financeiro.

Assim pode ser verificado o Artigo abaixo que menciona o parâmetro **MV\_GCTFIN** da mensagem e as tabelas de validação deste parâmetro que necessitam ter o mesmo compartilhamento:

[GCT0066\_Integração Gestão de Contratos e Financeiro](https://tdn.totvs.com/x/I2ctE)

E neste processo, caso se opte por alterar o compartilhamento padrão das tabelas do módulo de Gestão de Contratos, deve-se verificar o artigo abaixo que menciona também o conjunto de tabelas do SIGAGCT que necessitam estar com o mesmo tipo de compartilhamento:

[GCT0010 - Compartilhamento Tabelas SIGAGCT](https://tdn.totvs.com/x/FTMjJw)

***Saiba Mais:***

[GCT0066\_Integração Gestão de Contratos e Financeiro](https://tdn.totvs.com/x/I2ctE)

[GCT0010 - Compartilhamento Tabelas SIGAGCT](https://tdn.totvs.com/x/FTMjJw)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
