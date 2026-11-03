---
article_id: 360040636454
category: GPE - eSocial - Periódicos
content_hash: 335cb6dc9dfe619a2319cd57dd9bc8fc359440d0e52f2988a84be05fdb1534ec
fetched_at: '2026-06-28T22:45:09.074895+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2200 - Inconsistência do RET - 1 -
  Campo de preenchimento obrigatório: Descrição do Salario Variável'
type: support-article
updated_at: '2025-04-24T20:27:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040636454-RH-Linha-Protheus-GPE-eSocial-S-2200-Inconsist%C3%AAncia-do-RET-1-Campo-de-preenchimento-obrigat%C3%B3rio-Descri%C3%A7%C3%A3o-do-Salario-Vari%C3%A1vel
---

**Ocorrência**No módulo Gestão de Pessoal, ao tentar realizar o envio de uma nova admissão para o TAF e ao enviar para o eSocial o evento S-2200 apresenta inconsistência: Código da Ocorrência: 1 - Descrição: Campo de preenchimento obrigatório: Descrição do Salario Variável  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Esse incidente ocorre, pois não foi preenchido o campo **RA\_DESEPS**no cadastro do funcionário, conforme leiaute do eSocial, para funcionários comissionados deve ser enviada a *tag***dscSalVar**referente a descrição do salário por tarefa ou variável e como este é calculado  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar o cadastro do funcionário comissionado, preencher o campo **RA\_DESEPS;**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053528494)  
  
2. Após preencher o campo realize o envio do evento **S-2200** para o eSocial  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31647001338519)  
  
**Saiba mais**Para saber mais consulte os links abaixo:  
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
