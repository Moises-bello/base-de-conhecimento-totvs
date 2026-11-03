---
content_hash: 42a722beff5061953bf7c249d2f60dc6f2cf7e4a1a4e6684393318c08f39c990
fetched_at: '2026-06-29T00:09:29.803109+00:00'
page_id: '425458289'
product: rm
source: tdn-rm
title: Alteração de status das opções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458289
version: 7
---

Este serviço irá permitir que o usuário visualize todas as alterações de status das opções de área de interesse dos candidatos. Os registros de alteração de status apenas serão gerados se no cadastro do processo seletivo for marcada a opção "Gerar log de alteração de status". Será possível que o usuário rastreie qual usuário e serviço responsável e quando foi realizada a alteração.

Sempre que uma inscrição for incluída seja via sistema ou portal será incluído o registro inicial de alteração de status. Quando uma opção for removida da lista de opções de um candidato o log de alterações de opção para esta área de interesse será removido.

Segue a lista dos serviços que alteram status de opção e que irão gerar registros de log:

* Serviço Inscrição Web.
* Serviço Inscrição Secretaria.
* .
* Processo Cancelar área ofertada.
* Processo Classificar Candidatos.
* Processo Cancelar classificação de candidato.
* Processo Chamada de candidato aprovado.
* Processo Cancelar chamada de candidato aprovado.
* Processo Registrar chamada de candidato
* Processo Cancelar Inscrição
* Processo Excluir Inscrição
* Processo Matrícula de candidatos (RM Classis)
* Processo Desfazer matrícula de candidatos (RM Classis).

Importante

Caso o candidato esteja com status de inscrição "Inscrito (pendente de confirmação de pagamento)", "Excedente" (para processos seletivos que utilizem controle de vagas) ou "Cancelado", o campo do novo status ficará bloqueado, ou seja, só será possível alterar o status de opção de um candidato que esteja com status de inscrição "Candidato (inscrição confirmada)".

Informações

Á partir das versões 12.1.27.300, 12.1.28.211 e 12.1.29.136 foi implementado um ajuste para que se o candidato por ventura tiver sido "Desclassificado por insuficiência de nota" e a área de interesse que o candidato se inscreveu tiver somente uma única etapa, o processo permitirá que o status deste candidato seja alterado para "Inscrito para seleção" e caso o candidato tenha nota nesta etapa, o sistema irá informar que a nota será alterada para o valor 0 e assim o candidato poderá novamente passar por uma etapa de classificação.
