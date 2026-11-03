---
article_id: 27761530624279
category: Financeiro - Configurador
content_hash: 046d6057bceca6e6bbe0cf91af78e71fedff343072b4e462da92f73135a5d828
fetched_at: '2026-06-28T22:37:57.634483+00:00'
product: protheus
section_id: 1500001539601
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - É possível realizar
  a antecipação do vencimento em caso de feriado?
type: support-article
updated_at: '2025-05-09T20:20:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27761530624279-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-%C3%89-poss%C3%ADvel-realizar-a-antecipa%C3%A7%C3%A3o-do-vencimento-em-caso-de-feriado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27761530607895) Tempo aproximado para leitura: **00****:03:00 min****Dúvida**É possível antecipar vencimento no feriado?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**

O cadastro na **tabela 63 – Feriados** tem como objetivo postergar o vencimento de títulos que coincidam com feriados ou finais de semana. Por padrão, o sistema **não permite a antecipação automática** desses vencimentos.

No módulo **Financeiro**, não há parametrização disponível que viabilize a antecipação, uma vez que o sistema não permite que a data de **"Vencimento Real"** seja anterior à data de **"Vencimento"**. Como alternativa, recomenda-se cadastrar o título já com a data de vencimento ajustada para uma data anterior ao feriado ou final de semana, conforme a necessidade da operação.

Caso seja necessário flexibilizar esse comportamento, é possível utilizar o **ponto de entrada A103VCTO** para alterar programaticamente a data de vencimento do título. Alternativamente, a data pode ser ajustada **manualmente** no momento da inclusão do documento de entrada.

Para mais informações ou suporte quanto à utilização do ponto de entrada, orientamos a abertura de um ticket junto ao módulo de **Compras**.

[Ponto de Entrada - A103VCTO](https://tdn.totvs.com/display/public/PROT/A103VCTO)  
  
Segue documentação referente a prorrogação (postergar)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Vencimento Final de Semana](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7813907111447-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Vencimento-Final-de-Semana)

Saiba mais:

[Cadastrar\_Feriado\_Tabelas\_Genericas\_63](https://tdn.totvs.com/display/public/PROT/FIN0041_Cadastrar_Feriado_Tabelas_Genericas_63)
