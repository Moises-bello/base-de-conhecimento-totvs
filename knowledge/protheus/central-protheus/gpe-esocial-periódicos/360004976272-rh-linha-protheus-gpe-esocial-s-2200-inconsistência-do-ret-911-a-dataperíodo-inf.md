---
article_id: 360004976272
category: GPE - eSocial - Periódicos
content_hash: 964fccd8b2747556c410bc82d34a8d384f46e2ad97d7bc096028a471d30789f3
fetched_at: '2026-06-28T22:45:09.093939+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Inconsistência do RET 911 - A
  data/período informado deve ser anterior ao início de obrigatoriedade do empregador
  ao eSocial
type: support-article
updated_at: '2025-07-16T12:54:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004976272-RH-Linha-Protheus-GPE-eSocial-S-2200-Inconsist%C3%AAncia-do-RET-911-A-data-per%C3%ADodo-informado-deve-ser-anterior-ao-in%C3%ADcio-de-obrigatoriedade-do-empregador-ao-eSocial
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30231912105495) Tempo aproximado para leitura: 00:03:00 min******Ocorrência**Transmissão de Eventos - S-2200 - Inconsistência do RET - 911 - a data/período informado deve ser anterior ao início de obrigatoriedade do empregador ao eSocial  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Pode ocorrer por algum problema na identificação cadastral da empresa no RET, ou pode estar relacionado ao preenchimento incorreto do parâmetro **MV\_DTCGINI**.  
  
**Solução  
O que deve ser verificado para tentar corrigir o erro:**1 - O sistema pode estar com a parametrização incorreta, verificar os parâmetros abaixo:  
[MP - GPE - eSocial - Parâmetros 1ª Fase esocial (Tabelas Iniciais)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048411)[MP - GPE - eSocial - Parâmetros 2ª Fase esocial (Não Periódicos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004980892)[MP - GPE - eSocial - Parâmetros 3ª Fase esocial (Periódicos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004981112)2 - Está sendo enviado enviado um S-2200 (admissão), e o campo afastamento está preenchido no TAF. Exemplo:  
A admissão (03/03/16) do trabalhador ocorreu antes do inicio da obrigatoriedade dos eventos não periódicos (01/03/18).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006524032)  
  
Por esse motivo o cad. inicial é SIM (cadastramento inicial). Note mais abaixo que existe um afastamento com data de 06/04/18.   
Esse afastamento está incorreto pois a partir do inicio da obrigatoriedade dos eventos não periódicos (01/03/18), só pode ocorrer qualquer movimentação para o trabalhador após a transmissão do S-2200 (funcionários). Sendo esse um cenário, o governo retorna o erro "**911:****a data/período informado deve ser anterior ao início de obrigatoriedade do empregador ao eSocial.**"

* O correto seria enviar o S-2200 e depois fazer a inclusão do afastamento no qual será gerado o evento S-2230.
* O Campo afastamento demonstrado no print só deve estar preenchido quando o inicio do afastamento ocorreu antes da obrigatoriedade dos eventos não periódicos (01/03/18).  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006524052)

**Saiba Mais**Para saber mais consulte os *links*abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
