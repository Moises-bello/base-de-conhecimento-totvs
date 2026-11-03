---
content_hash: 487ec69b271275420aded1282b1eb2326a498b93b9dd81e8468b26bdbd06d8ab
fetched_at: '2026-06-29T00:09:34.119238+00:00'
page_id: '425459146'
product: rm
source: tdn-rm
title: Desfazer Inclusão de Bolsas Retroativas – Criando lançamentos de devolução
  / Atualizando a Conta Corrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459146
version: 4
---

---

O processo para *'Desfazer'* a inclusão de Bolsas Retroativas fica disponível no menu *Financeiro/Contábil | Assistentes | Desfazer a inclusão de bolsas retroativas*.  
    
 A inclusão de bolsa pelo processo de Bolsa Retroativa acarreta na criação de lançamentos de devolução com criação de vínculos entre lançamentos ou então na atualização automática da Conta Corrente do aluno com os respectivos valores das bolsas incluídas.  
    
 Este processo é responsável por *'Desfazer'* a inclusão de bolsa incluída retroativamente, assim como todos os registros ocorridos por tal inclusão, possibilitando assim, que a situação original, anterior à inclusão da bolsa pelo processo de Bolsa Retroativa, seja restaurada.

− Caso a opção escolhida previamente nos parâmetros do sistema para se trabalhar com Bolsa Retroativa tenha sido a opção '**Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)**':

O processo para *'Desfazer'* a inclusão somente poderá ser executado se o respectivo crédito gerado pela inclusão da bolsa não tiver sido 'Vinculado' ou se as parcelas dos contratos dos alunos que tiveram seus lançamentos financeiros vinculados aos créditos gerados ainda estiverem com status *'Em aberto'* ou *'Cancelado'*. Neste caso a bolsa será excluída do contrato, os 'Vínculos' criados entre os lançamentos serão cancelados e excluídos, os lançamentos financeiros a pagar criados anteriormente com a inclusão da Bolsa Retroativa serão cancelados e excluídos e, se estiverem *'Desfazendo'* a inclusão de uma *bolsa de crédito*, o lançamento financeiro referente à respectiva bolsa também será cancelado e excluído, removendo assim, todos os registros e informações de rastreabilidade, restaurando então, situação original.  
Caso não seja possível *'Desfazer'* a inclusão, no final do processo será apresentado um LOG com a mensagem de validação. O usuário deverá verificar o motivo apresentado e em seguida realizar os procedimentos necessários afim de que os lançamentos 'Vinculados' voltem para o status 'Em aberto' e, após estes procedimentos, executar novamente o processo para *'Desfazer'* a inclusão.  
**Atenção:**Caso não seja possível realizar tais procedimentos afim de que os lançamentos 'Vinculados' voltem para o status 'Em aberto', o usuário deverá então executar o processo de .

− Caso a opção escolhida previamente nos parâmetros do sistema tenha sido a opção **'Utilizar a movimentação em conta corrente'**:

O processo para *'Desfazer'* a inclusão somente poderá ser executado se os créditos em Conta Corrente gerados pela inclusão da Bolsa Retroativa não tiverem sido utilizados em outro lançamento. Neste caso a bolsa será excluída do contrato e os registros incluídos na Conta Corrente provenientes da inclusão de Bolsa Retroativa serão excluídos.  
**Atenção:**  
 Caso os créditos já tenham sido utilizados em outros lançamentos, o usuário deverá então executar o processo de *.*

Para executar este processo, primeiramente informe o 'Período letivo' e o 'Contrato' para o qual deseja desfazer a inclusão de alguma Bolsa Retroativa. Em seguida informe a bolsa para a qual deseja desfazer a inclusão e clique no botão 'Adicionar', ou se desejar, clique direto no botão 'Adicionar', assim, todas as Bolsas Retroativas deste contrato serão adicionadas para remoção. Se desejar retirar alguma bolsa listada para remoção, selecione-a e clique no botão 'Remover'. Finalmente clique em 'Avançar'.  
  
 No final do processo, será gerado um LOG com informações sobre as bolsas removidas, lançamentos desvinculados e excluídos e atualização realizada em Conta Corrente.
