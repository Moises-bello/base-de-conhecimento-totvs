---
article_id: 9802569967639
category: eSocial - Gerar XML/ Integração Evento
content_hash: 868f50a6482208fea6847c4b6a60f4820252a3333ca919b8a61eb88f25cb61e7
fetched_at: '2026-06-28T22:47:12.092858+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 130 na integração com o governo: É necessário
  existir a informação cadastral do empregador para o período'
type: support-article
updated_at: '2025-12-29T14:22:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9802569967639-RH-RM-FOP-eSocial-Erro-130-na-integra%C3%A7%C3%A3o-com-o-governo-%C3%89-necess%C3%A1rio-existir-a-informa%C3%A7%C3%A3o-cadastral-do-empregador-para-o-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24226806602391) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao transmitir eventos para o governo é retornado a inconsistência **Código do erro 130 Descrição: É necessário existir informação cadastral do empregador para o período. Ação Sugerida: Verificar se já foi enviado um evento de cadastramento do empregador.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Essa mensagem de erro na validação ocorre no retorno do evento quando por algum motivo o eSocial entende que o **S-1000** - (Informações do Empregador/Contribuinte/Órgão Público ) da empresa não foi enviado ao eSocial Web ou a vigência está posterior ao período do evento.   
  
**Solução**  
Para correção da ocorrência favor realizar as validações abaixo:  
**• Vigência Inicial  do S-1000 não Enviada**  
1. Primeiramente avalie qual o [grupo que a empresa pertence](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao) e a vigência de início da obrigatoriedade no eSocial ;  
2. Acesse **Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais 1/7.** Deverá preencher com as datas de acordo com o grupo de empresas que se enquadra.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9803202229911)

3. Acesse **eSocial | Fila de eventos** e verifique se existe o evento S-1000 pendente. Se existir, gere o XML e envie ao eSocial;  
4. Caso o evento S-1000 ainda não tenha sido enviado e não exista na Fila de Eventos, faça a [geração dos gatilhos iniciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009056971-RM-eSocial-Como-gerar-os-Gatilhos-Iniciais-por-Evento?source=search) e transmita para o governo.  
  
**• Vigência em desacordo com o Período do Evento**  
1.  Neste caso, consulte a vigência do evento S-1000. A vigência deverá ser menor ou igual ao período do evento que está encaminhando. O início da validade dos eventos podem ser validado no XML como mostra abaixo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9939129529111)

2. Após a correção, gere o XML e envie ao eSocial.  
  
**• S-1000 sem recibo**  
Se o evento S-1000 já estiver no TAF mas não possuir número de recibo, será necessário executar o processo de [ajuste de recibo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-TAF-Ajuste-de-Recibo-Como-inserir-um-n%C3%BAmero-de-recibo-no-TAF-?source=search).  
  
**Saiba mais**  
Para mais informações acesse: 

* [eSocial – O que constitui o evento S-1000 – Informações do Empregador/Contribuinte/Órgão Público.](https://tdn.totvs.com/pages/releaseview.action?pageId=307824222)
