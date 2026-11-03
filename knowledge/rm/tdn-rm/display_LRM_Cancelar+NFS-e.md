---
content_hash: b6710de493923acc322d47b65d2cd2ae0ede4f20b24c14b20ce29242c82669ff
fetched_at: '2026-06-29T00:09:22.099310+00:00'
page_id: '422545968'
product: rm
source: tdn-rm
title: Cancelar NFS-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelar+NFS-e
version: 9
---

Através deste processo é possível cancelar uma NFS-e que por algum motivo não deveria ter sito emitida. Devem ser observadas as condições da prefeitura para o cancelamento das NFS-e.

Antes de executar o cancelamento crie antes um filtro para se certificar de que está cancelamento a NFS-e correta. Na visão, selecione o registro e nos processos clique em Cancelar NFS-e. Pode-se executar o processo para um ou mais registros.

Ao selecionar mais de um registro, será apresentado a tela de "Verificar pendência(s) para cancelar a(s) nota(s) fiscal(is)". Nesta tela o usuário tem a opção de verificar ou não se o movimento da NFS-e poderá ser cancelado, antes de fazer a solicitação de cancelamento na prefeitura.

Ao optar por "Verificar Movimentos", o processo é executado e ao término informa quais movimentos não podem ser cancelados (automaticamente) e motivo de não poder ser cancelado. Contudo, isso não impede o processo de cancelamento da NFS-e. Desta forma, fica a cargo do usuário decidir continuar ou não com o processo.

***Atenção!*** Este processo pode ser demorado, uma vez, que verifica todas as integrações que o movimento possui.

 O processo de "Consultar autorização/Cancelamento", sempre realiza esta verificação, fazendo com que a execução possa ser opcional no momento do envio do cancelamento.

Devem ser informados o motivo do cancelamento e o código do motivo do cancelamento. O texto do motivo do cancelamento é livre mas pode ser utilizado o texto padrão se for marcada a opção: Justificativa Padrão.

O cancelamento só pode ser executado em NFS-e que possua o status Autorizada. Ao ser enviado o pedido de cancelamento a NFS-e terá seu status alterado temporariamente para Cancelamento Pendente. Após a consulta, se o cancelamento for autorizado a NFS-e terá seu status atualizado para Cancelado. Se por algum motivo este cancelamento não for autorizado a NFS-e terá seu status retornado para Autorizado.

Verifique com a prefeitura os motivos da rejeição do cancelamento e ser for realmente necessária esta ação e a mesma não puder ser feita por cancelamento utilize o processo de [Substituição de NFS-](http://tdn.totvs.com/pages/viewpage.action?pageId=422546166)e se a prefeitura permitir.

Se nenhuma das duas ações for possível a prefeitura deverá procurada e solicitadas instruções sobre o procedimento.

**Município NÃO Disponibiliza Integração Eletrônica para o Cancelamento da NFS-e**

O Processo "Cancelar NFS-e" foi evoluído para tratar municípios que não disponibilizam integração eletrônica para o cancelamento da NFS-e fazendo que a NFS-e nesta situação fique com o Status "Cancelamento Pendente".  
Disponibilizado o processo "Confirmação de Cancelamento OffLine", este processo altera o Status da NFS-e para "Cancelado" e também cancela o movimento.

**Como Fazer**  
(1) O usuário selecionar a NFS-e TXT\XML Autorizado que não possui integração eletrônica para o cancelamento da NFS-e.

(2) Executar o processo "Cancelar NFS-e". Após a execução do passo (2) a NFS-e deverá passar a apresentar o status "Cancelamento Pendente".

(3) Neste momento o usuário deve acessar a prefeitura para fazer o cancelamento da NFS-e

(4) Após ter certeza que a NFS-e está cancelada na prefeitura então executar o processo "Confirmação do Cancelamento OffLine".

(5) Alguns municípios necessitam de uma justificativa referente ao Motivo do Cancelamento.

Mais sobre [Motivo de Cancelamento NFS-e](https://tdn.totvs.com/x/BuryIw)

***Atenção!*** Este processo cancelará também o movimento e é irreversível no ERP.
