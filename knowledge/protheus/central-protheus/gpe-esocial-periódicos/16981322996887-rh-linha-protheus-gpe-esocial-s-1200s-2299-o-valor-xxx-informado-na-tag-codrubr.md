---
article_id: 16981322996887
category: GPE - eSocial - Periódicos
content_hash: c8229ae9db008452a6b5b1b2d302703f31b63f17ff08c057bfec76cbc19f09f4
fetched_at: '2026-06-28T22:45:07.343660+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - O valor 'XXX' informado
  na tag 'codrubr' não existe na base dados
type: support-article
updated_at: '2026-06-24T15:32:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16981322996887-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-O-valor-XXX-informado-na-tag-codrubr-n%C3%A3o-existe-na-base-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981308431767) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**S-1200/S-2299 - "O valor 'XXX' informado na tag '**codrubr**' não existe na base dados"  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34849354262551)  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**A mensagem de erro ocorre na integração dos eventos do **GPE** com o **TAF**, os problemas mais comuns são:  
 **Caso 1:** A Verbas/Rubrica não foi integrada, ou seja, não existe um evento S-1010 com o mesmo código de Rubrica na base do TAF ou o inicio de validade é posterior ao evento que está tentado gerar.  
  
**Caso 2:** Problemas no compartilhamento das tabelas SRV, C8R ou T3M.  
  
**Caso 3:** Ambiente desatualizado.   
  
**Solução****Caso 1:** Acesse o módulo do TAF e verifique se a Rubrica informada no erro existe na base do TAF.   
Utilizando o exemplo da imagem anexa acima, o valor "847" deverá ser localizado dentro da rotina de Rubricas (Módulo 84> Atualizações> Eventos Esocial> Tabelas> Rubricas), e deve estar com protocolo retornado do governo e com data início de vigência igual ou anterior ao período do evento remuneratório enviado.   
  
Caso não encontre a rubrica nessa rotina, realize sua integração da rubrica pela rotina Carga Inicial. O artigo abaixo lhe ajudará nesse processo:  
[RH - Linha Protheus - GPE - eSocial - S-1010 - Após a transmissão dos eventos iniciais (carga inicial), como enviar um único registro para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046341633)  
  
**Caso 2:** Verifique o se o compartilhamento encontra-se conforme documentação abaixo:   
[RH - Linha Protheus - GPE - eSocial - Como deve ser definido o Compartilhamento de Tabelas SIGAGPE x SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004178832-MP-GPE-eSocial-Como-deve-ser-definido-o-Compartilhamento-de-Tabelas-SIGAGPE-x-SIGATAF-?source=search)  
  
**Caso 3:** Realize a aplicação dos últimos pacotes conforme o link abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Para conhecimento dos eventos futuros, acessa a nossa página ***[TOTVS Informa](https://informa.totvs.com/)*** selecione em categorias a área e pesquise por "**Eventos**".
