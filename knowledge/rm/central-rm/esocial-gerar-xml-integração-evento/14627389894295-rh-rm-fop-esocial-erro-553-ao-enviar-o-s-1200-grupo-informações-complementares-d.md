---
article_id: 14627389894295
category: eSocial - Gerar XML/ Integração Evento
content_hash: 26d2a905abe8ff376f58d77bd5ea4d1a03368cf414ac98a1bb513e48d184aca2
fetched_at: '2026-06-28T22:47:12.139203+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 553 ao enviar o S-1200: Grupo Informações complementares
  de identificação do trabalhador não deve ser preenchido'
type: support-article
updated_at: '2026-01-09T11:51:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14627389894295-RH-RM-FOP-eSocial-Erro-553-ao-enviar-o-S-1200-Grupo-Informa%C3%A7%C3%B5es-complementares-de-identifica%C3%A7%C3%A3o-do-trabalhador-n%C3%A3o-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18491373671959) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao transmitir o evento **S-1200** de um autônomo é retornado o erro **553**: **Grupo #39;Informações complementares de identificação do trabalhador#39; não deve ser preenchido**. **Verifique as condições de preenchimento no leiaute. Localização: /eSocial/evtRemin/ideTrabalhador.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14626122484759)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Conforme *Layout* do eSocial, a tag **infoComplem** deve ser  preenchida quando o evento de remuneração se referir a trabalhador cuja categoria não estiver obrigada ao evento de início de trabalhador sem vínculo empregatício, e se não houver evento S-2300 correspondente ao trabalhador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14626408170903)

Sendo assim, o sistema valida se existe ou não o S-2300 na fila de eventos. Encontrando o S-2300, a tag **infoComplem** não é gerada no XML.

**Solução**

•  Verifique se o S-2300 do autônomo foi encaminhado para a **Fila de Eventos Complementar**

1. Acesse **Folha de Pagamento | Fila de Eventos Complementar** aplique um filtro para a chapa do funcionário;  
2. Localize o S-2300 correspondente e copie o identificador do evento;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18491373673751)

3. Acesse **Folha de Pagamento | Fila de Eventos Complementar | Restauração da Fila de Eventos do eSocial,** insira o **Identificador** que foi copiado no passo 2 e execute a rotina;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18491373674775)

4. Gere novamente o XML **S-1200** integre e transmita ao governo.

•  **Caso o XML S-2300 não seja identificado** na Fila de Eventos Complementar, pois pode ter sido inserido diretamente no governo, ou excluído do sistema por algum motivo.

1. Crie manualmente na **Fila de Eventos não Periódicos** um S-2300 para o autônomo desejado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14626766662807)

2. Não é necessário enviar o S-2300 para o governo, visto que o evento já consta no portal;

3. Gere novamente o XML S-1200 integre e transmita ao governo.

**Importante**  
Caso seja necessário alterar o *Status* do evento S-2300 criado manualmente e inserir o número do Recibo do eSocial:

* Para os usuários usuários que utilizam *Middleware*: Poderá inserir manualmente o número do Recibo no campo de referência e alterar o *Status* via *UPDATE* no banco de dados. Lembrando que qualquer alteração via banco de dados não faz parte do escopo de atendimento do Suporte Padrão;
* Para os usuários que utilizam TAF: Poderá realizar o Ajuste de Recibo [CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-TAF-FUNCIONALIDADES-Como-realizar-ajuste-de-recibo-do-e-Social-no-TAF).

**Saiba mais**  
Para mais informações sobre **Fila de Eventos Complementar** acesse:  
      • [RH - RM - FOP - eSocial - Restaurar fila de eventos complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036243133-RM-eSocial-Restaurar-fila-de-eventos-complementar?source=search)
