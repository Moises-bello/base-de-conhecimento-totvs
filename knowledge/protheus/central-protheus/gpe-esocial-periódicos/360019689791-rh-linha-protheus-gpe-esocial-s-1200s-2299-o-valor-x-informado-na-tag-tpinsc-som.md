---
article_id: 360019689791
category: GPE - eSocial - Periódicos
content_hash: a1c80e9ac4d86ccf469e43882a0c62b0c53edec5b5af177b3183146728e7a8a3
fetched_at: '2026-06-28T22:45:08.854239+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - O valor 'x' informado
  na tag 'tpinsc' somado ao valor 'x' informado na tag 'nrinsc' é uma chave composta
  e sua combinação não corresponde a nenhum registro da base de dados.
type: support-article
updated_at: '2026-01-14T19:47:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019689791-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-O-valor-x-informado-na-tag-tpinsc-somado-ao-valor-x-informado-na-tag-nrinsc-%C3%A9-uma-chave-composta-e-sua-combina%C3%A7%C3%A3o-n%C3%A3o-corresponde-a-nenhum-registro-da-base-de-dados
---

**Ocorrência**O valor '**x**' informado na tag '**tpinsc**' somado ao valor '**x**' informado na tag '**nrinsc**' é uma chave composta e sua combinação não corresponde a nenhum registro da base de dados.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**A mensagem é apresentada no Log gerado após tentativa de integração dos eventos periódicos do **GPE** com o **TAF**, em grande parte é causado devido a ausência do **tipo de inscrição** no cadastro da Empresa e/ou divergência entre o **modo de acesso (compartilhamento)** entre as tabelas do **GPE** e do **TAF**.  
  
**Solução**1. Através do Configurador(SIGACFG) verifique se no cadastro da Empresa o **tipo de inscrição** está preenchido de acordo com o número de inscrição informado;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015329571)  
  
2. Acessar no módulo **SIGATAF** o menu **Atualizações > Eventos Esocial > Tabelas > Estabelecimentos e Obras** e verificar se existe o evento S-1005 para o numero de inscrição apresentado na mensagem de inconsistência, caso não exista será necessário realizar o envio do evento S-1005 através do **SIGAGPE** pela rotina de carga inicial;  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098057953)  
  
3. Consulte as **FAQs** abaixo para entender o conceito de empregador no **eSocial** e como deve ser definido o **modo de acesso (compartilhamento)** das tabelas envolvidas.  
 [Faq: Aviso Conforme exigência do eSocial, cada empregador deve ter seu registro S-1000 e seu grupo de Tabelas Iniciais](http://tdn.totvs.com/x/tIHjFQ)[Faq: Como deve ser definido o Compartilhamento de Tabelas SIGAGPE x SIGATAF](http://tdn.totvs.com/x/kKSCEw)

4. Verifique se o cadastro de centro de custo do funcionário esta faltado algum dado, existem casos que no centro de custo é vinculado a um CNO, nesse caso deve ser realizado o envio do evento S-1005 para o TAF;  
  
[MP - GPE- eSocial - Obras - S-1005 x S-1020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030600113/)  
  
Em casos de **multiplos vinculos**, deve ser analisado se foi realizado o passo a passo abaixo:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013550551-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-funcion%C3%A1rios-com-m%C3%BAltiplos-v%C3%ADnculos-no-evento-S-1200>  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[Agenda de Eventos Tira Dúvidas Suporte](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-01-2023-retificada-em-20230124.pdf)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
