---
article_id: 360024360512
category: GPE - eSocial - Carga Inicial
content_hash: 9faf9f8f9356c0d7e2922ed50dea9dccc937648a961c572fb0dee8b5300df47f
fetched_at: '2026-06-28T22:45:03.059409+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5001 - Como ajustar incidência e validade
  de rubricas no governo, TAF e GPE
type: support-article
updated_at: '2025-07-25T14:09:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512-RH-Linha-Protheus-GPE-eSocial-S-5001-Como-ajustar-incid%C3%AAncia-e-validade-de-rubricas-no-governo-TAF-e-GPE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33713522107159) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Como ajustar as verbas para o esocial quanto a incidência e validade de rubricas no Governo, TAF e GPE?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Para o eSocial quando existe alteração de rubrica deve ser enviada para o governo a mesma rubrica alterada com uma data de vigência inicial (validade inicial). Assim somente a partir da nova vigência será considerada a alteração realizada.  
Isso tem impacto direto na folha pois o governo faz o calculo dos valores de acordo com a incidência e data inicial da rubrica, ou seja, se houver uma alteração de incidência em 05/2018 o governo vai apurar os valores de acordo com a nova incidência para as folhas a partir de 05/2018, para as folhas anteriores a incidência considerada continuara sendo a antiga.

* Exemplo Tela de rubricas página do RET:

Pode existir mais de um registro para mesma rubrica com inicio da validade diferente.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33713522108823)  
  
**Para corrigir erros de incidências e validade inicial realize os seguintes passos:**  
1. A incidência está correta no Governo, TAF e GPE, porem a validade inicial da rubrica não está correta:  
Nesse caso a data de validade pode ser ajustada no TAF, desde que exista a rubrica com as mesmas incidências no Governo, TAF e GPE para que não ocorra erro na integridade das transmissões.  
Exemplo:  
O campo **Per. Ini. Vld** no TAF represente a validade inicial da rubrica.![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022913271)  
  
2. A incidência está incorreta no TAF e correta no GPE:  
Nesse caso a incidência deve ser ajustada no TAF, desde que exista a rubrica com as mesmas incidências no Governo, TAF e GPE para que não ocorra erro na integridade das transmissões.  
  
3. Houve alteração de incidência mas, ela está incorreta no GPE, TAF e Governo:  
Nesse caso deve ser acessado o cadastro de verbas no SIGAGPE e feita uma alteração da verba deixando a data base do sistema no mês que no qual deve ser criada a data inicial.  
Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022878792)  
  
No TAF vai ser criada a mesma rubrica, porem com o **Per. Ini Vld** (validade inicial) com o mesmo mês da data base onde houve o ajuste. Com isso a alteração de incidências só vai valer na folhas geradas a partir da data inicial da rubrica.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022878912)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022911771)  
  
4. Quero somente retificar uma incidência sem gerar nova validade inicial, ou seja, não houve alteração de incidência, ela já foi transmitida incorreta.  
Nesse caso deve ser feita uma alteração cadastro de verbas do SIGAGPE deixando a data base do sistema igual a data inicial de uma rubrica existente no TAF.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022912431)  
  
No TAF a alteração ocorre no mesmo registro ficando com legenda amarela de retificação, ou seja, nesse cenário não é criada um novo registro com outra data de validade, está sendo ajustada o mesmo registro.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022912991)  
  
 **Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
