---
article_id: 360017979312
category: eSocial - Gerar XML/ Integração Evento
content_hash: c128b464a822e32288e6a7613740986a09daa2a6a98525b23908415a2a9ded86
fetched_at: '2026-06-28T22:47:11.998227+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao transmitir S-2230 ocorre o erro 174: A data de
  ocorrência do evento #39;XX/XX/XXXX#39; deve ser igual ou posterior ao início da
  obrigatoriedade deste evento #39;XX/XX/XXXX#39; para o empregador ao eSocial'
type: support-article
updated_at: '2026-01-09T12:03:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017979312-RH-RM-FOP-eSocial-Ao-transmitir-S-2230-ocorre-o-erro-174-A-data-de-ocorr%C3%AAncia-do-evento-39-XX-XX-XXXX-39-deve-ser-igual-ou-posterior-ao-in%C3%ADcio-da-obrigatoriedade-deste-evento-39-XX-XX-XXXX-39-para-o-empregador-ao-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24503492372503)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**  
Ao transmitir S-2230 ocorre o erro 174: A data de ocorrência do evento #39;XX/XX/XXXX#39; deve ser igual ou posterior ao início da obrigatoriedade deste evento #39;XX/XX/XXXX#39; para o empregador ao eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24505747389079)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  - Todas as versões   
  
**Causa**  
A mensagem apresentada pelo RET é uma validação que o evento enviado não corresponde ao período da data de obrigatoriedade do empregador.  
  
**Solução**  
1. Na mensagem do erro identifique a data do evento e qual a data da obrigatoriedade do empregador;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24505776779415)

No exemplo supracitado, consta que a obrigatoriedade do empregador no governo é 10/04/2019 e, está sendo enviado um S-2230 com data 01/01/2011, ou seja, anterior à data de obrigatoriedade;

2. Identifique no XML a data com o erro;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24505776785431)

3. Caso a data esteja incorreta, realize a correção e regere o XML S-2230, após integre com o governo;

4. Caso a data esteja correta e o funcionário tenha iniciado o eSocial afastado, é necessário enviar o S-2200 com o grupo afastamento com a data início preenchida;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24505776793751)

4.1. Verifique a necessidade de [**retificação do S-2200**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005056141-RH-RM-FOP-eSocial-Retifica%C3%A7%C3%A3o-dos-eventos-de-funcion%C3%A1rios-S-2200-S-2205-S-2206-S2300-e-S-2306), caso o afastamento não tenha sido enviado;  
4.2. Para os casos onde o afastamento foi informado a data início no S-2200, é necessário envio posterior somente da data fim do afastamento no S-2230. Para isto, acesse **eSocial | Outros processos | Gerar gatilho afastamento / férias eSocial** e execute o processo selecionando o parâmetro **Gerar gatilho de término para funcionários afastados na carga inicial**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24505747420439)

**Importante**  
Lembrando que as datas da obrigatoriedade podem ser alteradas no parametrizador do RM em **Configurações | Parametrizador | eSocial | Configurações Gerais 1/7**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24505747430167)

**Saiba mais**  
Para mais informações, acesse:  
-  [Parametrização das datas do início de obrigatoriedade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004814832-RH-RM-FOP-eSocial-Parametriza%C3%A7%C3%A3o-das-datas-do-in%C3%ADcio-de-obrigatoriedade) ;  
- [Erro ao transmitir S-2230: Só é permitido enviar fim de afastamento para trabalhadores que iniciaram o eSocial afastados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024675814-RH-RM-FOP-eSocial-Erro-ao-transmitir-S-2230-S%C3%B3-%C3%A9-permitido-enviar-fim-de-afastamento-para-trabalhadores-que-iniciaram-o-eSocial-afastados)
