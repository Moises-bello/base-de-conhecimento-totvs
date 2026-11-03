---
article_id: 360018356492
category: GPE - eSocial - Não Periódicos
content_hash: f80ffc8843066096b01eefcf1221435b2bc31855c3e1ba12d01d8c699eef0f94
fetched_at: '2026-06-28T22:45:04.442984+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200  - O valor "XX" informado na  tag
  UF não existe na base de dados
type: support-article
updated_at: '2026-06-16T13:33:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018356492-RH-Linha-Protheus-GPE-eSocial-S-2200-O-valor-XX-informado-na-tag-UF-n%C3%A3o-existe-na-base-de-dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30375554706199) Tempo aproximado para leitura: 00:05:00 min  
  
Ocorrência**Quando realizada a carga inicial do evento **S-2200** ou o envio de um novo funcionário através da inclusão no cadastro de funcionários, o sistema retorna mensagem de erro **O** **Valor "XX" informado na tag UF não existe na base de dado**", impedindo que os dados sejam integrados.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001046182)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Quando no **Gestão de Pessoal** as informações estão cadastradas corretamente para Estado e município no cadastro do trabalhador, este erro pode ocasionado devido inconsistência nas tabelas **Autocontidas** do **TAF**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Verificar se na tabela **C07** (**Módulo 84** - Consultas - **Tabelas Dinâmicas** - **C07**) constam os códigos de **UF i**nformados com os devidos municípios vinculados;  
  
**2.** Não estando cadastrado o **UF** vinculado ao funcionário, será necessário realizar a atualização das tabelas **Autocontidas**.  
[RH - Linha Protheus - TAF - eSocial - Configuração - Como atualizar as tabelas autocontidas no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017826812-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-atualizar-as-tabelas-autocontidas-no-TAF)  
  
**3.** Verificar se no cadastro do **funcionário** estão informados corretamente os códigos para município de nascimento (RA\_CODMUNN) e residência (RA\_CODMUN), assim como seus respectivos estados (**UF**).  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)    
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
