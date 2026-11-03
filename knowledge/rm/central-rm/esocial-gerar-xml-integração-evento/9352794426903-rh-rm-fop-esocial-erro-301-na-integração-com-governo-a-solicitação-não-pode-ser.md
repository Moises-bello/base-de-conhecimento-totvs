---
article_id: 9352794426903
category: eSocial - Gerar XML/ Integração Evento
content_hash: 8b0a6c19e6e98a7ca95c2525cce8c5ecbe63e594bcf8e8286200f1f6762fa6af
fetched_at: '2026-06-28T22:47:12.114153+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 301 na integração com governo: A solicitação
  não pode ser atendida devido a uma falha não identificada que pode ou não ser temporária'
type: support-article
updated_at: '2024-06-19T19:44:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9352794426903-RH-RM-FOP-eSocial-Erro-301-na-integra%C3%A7%C3%A3o-com-governo-A-solicita%C3%A7%C3%A3o-n%C3%A3o-pode-ser-atendida-devido-a-uma-falha-n%C3%A3o-identificada-que-pode-ou-n%C3%A3o-ser-tempor%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Ocorrência** Ao transmitir o eventos para o governo é retornado a inconsistência **Erro código 301: Código do erro: 301.0. Identificador: xxxxxxxxxxxxx. A solicitação não pode ser atendida devido a uma falha não identificada que pode ou não ser temporária. Favor tentar novamente mais tarde. Caso o erro permaneça por um período superior a 6 (seis) horas, favor acessar o Portal do eSocial através do endereço** <https://www.gov.br/esocial/pt-br/canais_atendimento.> **Na opção CONTATO, na seção EMPRESAS, selecione PRODUÇÃO EMPRESAS. Preencha o formulário sobre erro 301 informando o identificador do evento para rastreamento do erro. Obrigado.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9353697884055)**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse erro será gerado por uma falha na conexão com o ambiente do eSocial. O eSocial utiliza o **código 301** para tratar situações não esperadas pelo Sistema.

As situações que podem gerar esse erro são:

**• Falha Temporária:**[Indisponibilidades momentâneas](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/semaforo) no Portal do eSocial.

**• Falha não catalogada:** Erros incomuns que não foram criadas mensagens de orientação ao usuário ou um erro do sistema que precisa de correção (bug).  
  
**Solução**  
Para solucionar essa ocorrência, favor realizar as validações abaixo  

**•  Falha Temporária**

**1.** Aguarde um momento e tente transmitir os eventos mais uma vez;

**2.** Para isso, selecione os eventos na Fila e envie novamente ao eSocial.

**• Falha não catalogada**

O evento não será enviado, então será necessário que a equipe técnica do eSocial (governo) atue para resolver a situação.

Neste caso, você pode aguardar para que o Portal do eSocial resolva a situação ou cadastre uma solicitação conforme a seguir:

**1.** Acesse o [Portal eSocial - Atendimento](https://www.gov.br/esocial/pt-br/canais_atendimento);

**2.** No quadro **EMPRESAS**, clique na opção **ESOCIAL EMPRESAS (ambiente de produção - com validade jurídica)**;

**3.** Clique no assunto **ERRO 301**, preencha os campos e informe o *hash* e o identificador em sua mensagem;

**Saiba Mais**  
Para saber mais sobre o Erro 301, acesse:  
     • [Erro 301 - Esocial](https://www.gov.br/esocial/pt-br/noticias/erro-301-o-que-fazer)
