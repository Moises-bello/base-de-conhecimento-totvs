---
article_id: 360044966953
category: GPE - eSocial - Periódicos
content_hash: ef352d521888ec155280b437ce1e024ee8fc8238cd910f1578733aaf6a2654b7
fetched_at: '2026-06-28T22:45:08.652924+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Inconsistência do RET - 261
  - Categoria do trabalhador #39;XXX#39; incompativel com a lotacao do tipo #39;YY#39;
  e classificacao tributaria do empregador #39;ZZ#39
type: support-article
updated_at: '2025-07-21T15:37:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044966953-RH-Linha-Protheus-GPE-eSocial-S-1200-Inconsist%C3%AAncia-do-RET-261-Categoria-do-trabalhador-39-XXX-39-incompativel-com-a-lotacao-do-tipo-39-YY-39-e-classificacao-tributaria-do-empregador-39-ZZ-39
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27013636469527) Tempo aproximado para leitura: 05:00:00 min****Ocorrência**Categoria do trabalhador [#39](https://totvssuporte.zendesk.com/agent/tickets/39);**XXX**#39; incompativel com a lotacao do tipo [#39](https://totvssuporte.zendesk.com/agent/tickets/39);**YY**#39; e classificacao tributaria do empregador [#39](https://totvssuporte.zendesk.com/agent/tickets/39);**ZZ**#39;.  
  
Acao Sugerida: O valor informado no campo deverá ser compativel com a Lotacao e classificacao tributaria do CONTRIBUINTE informada no Evento de quot;Informacoes Cadastrais do Empregador, conforme Tabela 11 (Compatibilidade entre Categoria de Trabalhadores, Classificacao Tributaria e Tipos de Lotacao) **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
 **Causa**Esse erro de retorno ocorre devido a categoria do trabalhador **XXX**não ser compatível com o tipo de **lotação tributaria (S-1020)** e **classificação tributaria (S-1000)** que está no governo, conforme tabelas de compatibilidade do eSocial.  
  
Por **exemplo**: Se a mensagem de retorno do governo for "*Categoria do trabalhador [#39](https://totvssuporte.zendesk.com/agent/tickets/39);**722**#39; incompativel com a lotacao do tipo [#39](https://totvssuporte.zendesk.com/agent/tickets/39);**04**#39; e classificacao tributaria do empregador [#39](https://totvssuporte.zendesk.com/agent/#/tickets/39);**99**#39*".   
Isso significa que o trabalhador está com categoria eSocial 722, com o tipo de lotação 04 (S-1020) e a classificação tributária 99 (S-1000).   
  
Porem conforme tabela só pode utilizar a categoria 722, se a empresa for *tpInsc* 01 (CNPJ), a *classeTrib* (classificação tributária) **NÃO** for  04, 21, ou 22, e o tipo de lotação **FOR** 01, 90, ou 91.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11230659049879)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11230775246103)  
  
**Solução**Para ajuste verifique os seguintes passos:  
  
**1.** Analise e verifique qual deve ser a combinação correta para o seu trabalhador entre categoria, tipo de lotação tributária e classificação tributária;  
  
**2.** Após isso, verifique onde está incorreta as informações no GPE, TAF e Governo no caminhos abaixo;

**a)** a **classificação tributária fica localizado no TAF** e **Governo**:  
Caminho Sigataf: atualizações > *configs. taf > complemento cadastral**(campo ID. Class Trib.)*Caminho site eSocial:*[Como consultar no site do eSocial dados do evento de S-1000 (Informações do Empregador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043149934)***b)** o **tipo lotação tributária fica localizado no GPE, TAF** e **Governo**:  
Caminho Sigagpe: atualizações*>**cadastros >**centro de custo (campo tipo de lotação)*  
Caminho Sigataf: atualizações >*eventos eSocial >**tabelas > lotações tributária (campo id. tplotação)*Caminho site eSocial: *[Como consultar no site do eSocial dados do evento S-1020 (Tabelas de Lotações Tributárias)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043671553)***c)** a **categoria do trabalhador fica localizado no GPE, TAF e Governo**:  
Caminho Sigagpe: atualizações*>**funcionários>**funcionários ou contr. individual ( campo cat esocial)*  
Caminho Sigataf: atualizações >*eventos eSocial >**trabalhador > cadastro trabalhador (campo id.cat)*Caminho site eSocial: *[Como consultar no site do eSocial dados do evento S-2200 (Cadastramento Inicial do Vínculo e Admissão)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042805974)*

**3.** Após ajuste das informações transmita novamente o evento S-1200.  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
