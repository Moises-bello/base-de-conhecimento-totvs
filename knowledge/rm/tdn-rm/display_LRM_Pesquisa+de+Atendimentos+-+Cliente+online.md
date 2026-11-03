---
content_hash: 4859cbcff22de8c1f6efaabcb45dbb065bddb8a28f03d34797a528507ec49717
fetched_at: '2026-06-29T00:09:30.331590+00:00'
page_id: '425458431'
product: rm
source: tdn-rm
title: Pesquisa de Atendimentos - Cliente online
type: documentation
url: https://tdn.totvs.com/display/LRM/Pesquisa+de+Atendimentos+-+Cliente+online
version: 2
---

**Pesquisa de Atendimentos**   
 A pesquisa de atendimentos no Módulo de Cliente On Line é um recurso que permite buscar os atendimentos que atendam os critérios preenchidos, entre eles estão:

* Código do atendimento

O código do atendimento só aceita valores numéricos e pode buscar mais de um registro de uma só vez, mas os códigos devem estar separados por vírgula.

* Status

O sistema apresenta uma lista de status para escolha, dentre eles estão: Em andamento, Concluído a responder , Concluído respondido , Concluído confirmado , Concluído automático (pelo sistema), Avaliado, Agendado a responder , Agendado respondido , Aguardando terceiros , Cancelado , Despertado. No caso das opções "Aguardando Retorno" e "Em minha responsabilidade" não são considerados como status, mas a escolha dessas opções irão retornar os atendimentos que foram abertos pelo cliente e estão aguardando alguma ação de terceiros (Aguardando Retorno) ,  já o caso de (Em minha responsabilidade) serão retornados os atendimentos que necessitam de atuação do cliente.

* Data de Abertura

Período da data de criação do atendimento (início e fim).

* Data de Fechamento

Período da data de encerramento do atendimento (início e fim).

* Assunto

Busca todos os registros que satisfaçam o texto digitado. Com a utilização do like (LIKE%%) não será necessário digitar o texto completo , basta apenas uma parte para que o registro seja encontrado.  
    
 **Observação.:**  
    
 Caso nenhum critério seja preenchido, o sistema apresenta uma mensagem de alerta "É necessário que você estabeleça algum critério para a pesquisa" para dar andamento na busca dos registros.   
 Toda a pesquisa efetuada na base de dados sempre levará em conta apenas os atendimentos do cliente corrente, ou seja,  o cliente não irá conseguir fazer buscas de atendimentos de outros clientes, apenas do usuário que estiver logado naquele momento.
