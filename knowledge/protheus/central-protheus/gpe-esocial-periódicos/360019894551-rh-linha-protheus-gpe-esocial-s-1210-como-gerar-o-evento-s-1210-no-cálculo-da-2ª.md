---
article_id: 360019894551
category: GPE - eSocial - Periódicos
content_hash: 18b909ddd17a0372a9f8fcc824aa0b29a094d1856b1918efe9b07f43e86c835f
fetched_at: '2026-06-28T22:45:08.918175+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Como gerar o evento S-1210 no
  cálculo da 2ª parcela do 13º Salario
type: support-article
updated_at: '2025-07-21T14:46:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019894551-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-gerar-o-evento-S-1210-no-c%C3%A1lculo-da-2%C2%AA-parcela-do-13%C2%BA-Salario
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19464864988567)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como gerar o evento S-1210 no cálculo da 2ª parcela do 13º Salario?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Conforme o **MOS do leiaute vigente,** deve ser enviado um único evento S-1210 por competência de apuração para cada trabalhador/servidor/beneficiário. Então os valores de 13º salário serão gerados em um único evento junto com outros valores que também foram pagos em dezembro.  
  
No modulo SIGAGPE para o **mês de Dezembro deve existir 2 eventos S-1200**.  
  
**1º para o pagamento dos valores do calculo da da 2ª parcela do 13º Salário**, que deve ser gerado com a competência **12/AAAA** (Ex. 12/2023) e campo  REF. 13 igual a **SIM**,   
  
**2º outro S-1200 para o pagamento da folha mensal competência** **12/AAAA** (Ex. 12/2023) e com o campo REF. 13 igual a **NÃO**.  
  
Rotina de geração dos eventos periódicos no SIGAGPE - S-1210 referente ao mês 12/2023

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19464895020567)  
  
Porém, conforme regra atual do **eSocial**, no evento **S-1210** **não existe separação entre 13º e Folha**, devido a isso na competência **12/AAAA** (Ex. 12/2023) é necessário deixar o campo **Ref. 13º** com **NÃO** para marcar a opção S-1210 gerando um único evento que deve ser transmitido com os dados da folha e 13º Salário.  
  
Instrução do MOS **Manual de Orientação do eSocial**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19464865006359)  
  
**Exemplo** do evento **S-1210 no TAF** referente ao mês 12/2022  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10840528077335)  
  
Veja também o vídeo que preparamos referente ao assunto:  
[How To - S-1210 - 2ª parcela 13º salário](https://www.youtube.com/watch?v=UOYv0UWme_E&list=PLXa8l0dq5zRlIwdslfRrrlgYg4v9X4Upc&index=14)  
  
Para saber mais consulte o artigo: [RH - Linha Protheus - GPE - eSocial - S-1210 - Quais os prazos para envio de S-1200, S-1210 e S-1299 referentes à folha anual e Como informar período de apuração anual no evento S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020493932-RH-Linha-Protheus-GPE-eSocial-S-1210-Quais-os-prazos-para-envio-de-S-1200-S-1210-e-S-1299-referentes-%C3%A0-folha-anual-e-Como-informar-per%C3%ADodo-de-apura%C3%A7%C3%A3o-anual-no-evento-S-1210)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[Artigos Calculo 13º Salario](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
