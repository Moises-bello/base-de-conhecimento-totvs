---
content_hash: 0b3e814e20978ad4c156748e039601a24ec4cd084e8d7a2c624955f9667e93da
fetched_at: '2026-06-29T00:10:07.865499+00:00'
page_id: '452719457'
product: rm
source: tdn-rm
title: Batidas
type: documentation
url: https://tdn.totvs.com/display/LRM/Batidas
version: 4
---

**Batidas**   
**Batidas**   
**-Permite alterar batidas digitadas**  
Marcando esta opção o usuário poderá alterar e excluir as batidas digitadas na grid de batidas do RM Portal, ao alterar as batidas o status será salvo de acordo com os parâmetros do agrupamento "Batidas Aprovadas". Se a alteração estiver sendo feita por um gestor para o subordinado o parâmetro "Inclui batidas não aprovadas para subordinados" influenciará no status dessa batida.  
 ***-*Permite alterar e excluir batidas coletadas**  
Marcando esta opção o usuário poderá alterar e excluir as batidas coletadas na grid de batidas do RM Portal, ao alterar as batidas o status será salvo de acordo com os parâmetros do agrupamento "Batidas Aprovadas". Se a alteração estiver sendo feita por um gestor para o subordinado o parâmetro "Inclui batidas não aprovadas para subordinados" influenciará no status dessa batida.  
****Importante:****Todas as batidas excluídas serão desconsideradas pelo sistema. Ao emitir os relatórios ACJEF, AEJ e Espelho do Ponto da Portaria 671, as batidas excluídas serão impressas nos relatórios com a informação de desconsiderada com a devida justificativa informada no processo de cancelamento ou alteração. O fiscal terá a informação da batida oficial registrada no REP via relatório AFD, que é emitido pelo REP para que sejam confrontadas as informações. Este processo está em conformidade com a portaria 671, Art. 84., V - marcações efetuadas no REP e marcações tratadas (incluídas, desconsideradas e pré-assinaladas) no Programa de Tratamento de Registro de Ponto;

**-Inclui batidas não aprovadas para subordinados**  
Marcando esta opção o chefe ou supervisor consegue entrar com batidas para os subordinados, mas as batidas devem ser aprovadas posteriormente para fazer parte do cálculo da movimentação do funcionário. Não marcando esta opção as batidas que o chefe ou supervisor incluir serão aprovadas sem a necessidade de aprovação  
**-Aprovar automaticamente batidas incluídas e editadas na data atual**  
*Marcando esta opção o usuário poderá incluir e editar as batidas na data atual com o status aprovado.*  
   
**Batidas Aprovadas**  
**-Inclui batidas não aprovadas**  
Marcando esta opção todas as batidas incluídas via RM Portal serão não aprovadas necessitando posteriormente serem aprovadas pelo chefe ou supervisor para fazer parte da movimentação do funcionário.  
   
***-*Inclui batidas aprovadas**  
Habilitando este parâmetro o chefe e o supervisor poderão entrar com suas batidas e as mesmas serão automaticamente aprovadas já fazendo parte do cálculo da movimentação.  
   
**Observação:**  
Marcando o parâmetro "Somente na data atual" juntamente com o parâmetro "Permite incluir batidas aprovadas", qualquer funcionário poderá entrar com suas batidas sem a necessidade de aprovação do supervisor ou chefe.  
   
**-Inclui batidas aprovadas para gestores apenas na data atual**  
   
Este parâmetro deve ser utilizado com o parâmetro "Somente na data atual" marcado. Com estes dois parâmetros marcados os chefes e supervisores entrarão com suas batidas já aprovadas apenas na data atual.  
Em datas diferentes da data atual as batidas necessitarão de serem aprovadas para fazer parte da movimentação. Qualquer batida que os chefes ou supervisores entrarem para seus subordinados com estes parâmetros marcados já serão  
**Período de inserção de batidas**  
**-Somente no período atual**  
Marcando esta opção os funcionários poderão entrar com as batidas apenas no período mensal que está determinado no menu Configurações| Períodos.  
   
***-*Todos os períodos:**  
   
Marcando esta opção os funcionários poderão entrar com batidas em qualquer data, dentro do período atual ou não.  
**-Ate a data atual:**  
Marcando esta opção os funcionários poderão entrar com as batidas a partir da data do início do período atual determinado no menu Configurações|Períodos até a data atual do servidor da base de dados.  
**-Somente na data atual:**  
Marcando esta opção os funcionários poderão entrar com as batidas apenas na data atual do servidor da base dados. Para entrar com a batida na data atual via RM Portal basta abrir a página do grid de batidas no espelho do cartão de ponto e marcar a opção Incluir Batida.  
**Observação:**  
Marcando o parâmetro "Somente na data atual" juntamente com o parâmetro "Permite incluir batidas aprovadas", qualquer funcionário poderá entrar com suas batidas sem a necessidade de aprovação do supervisor ou chefe. Mesmo com os dois parâmetros marcados posso entrar com batidas em datas anteriores a atual pelo módulo de Espelho do funcionário. Estas batidas deverão ser aprovadas pelo chefe ou supervisor para fazerem parte do cálculo da movimentação do funcionário.
