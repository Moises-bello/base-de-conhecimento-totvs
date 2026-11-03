---
content_hash: 34ed8931d2b90d8ee0c3e94acccf5db42f2aa06b8c2922be8193034650d8fefd
fetched_at: '2026-06-29T00:09:49.525758+00:00'
page_id: '435105313'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Renegociação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105313
version: 6
---

**Renegociação**

---

**Descrição**  
Esta funcionalidade permite o comprador realizar ou sugerir uma renegociação de parcelas vencidas de sua venda, gerando um novo plano com novas parcelas.

|  |  |
| --- | --- |
|  | Como Fazer |

---

**Gestão**  
   
Não foi desenvolvido nenhum módulo de gestão no Portal do Cliente. Toda a funcionalidade foi desenvolvida utilizando a estrutura já existente para aditivos. Quando o comprador gera uma renegociação no portal um aditivo do tipo Renegociação de Contrato é criado para a venda.  
   
Na descrição do aditivo vem o nome "PDC-Renegociação do Contrato". Porém o administrador pode alterar esta descrição quando o aditivo estiver em preparação. A data do aditivo é a data corrente que o aditivo foi solicitado pelo comprador. Para a execução da funcionalidade da renegociação no Portal o executável RM disponibiliza os seguintes parâmetros:

* **Permite efetivação automática da renegociação de contrato:** Informa se a renegociação elaborada pelo comprador será efetivada de forma automática pelo sistema ou se o novo plano será efetivado pelo setor responsável. Caso este parâmetro esteja marcado, a aprovação automática estará condicionada aos dois próximos parâmetros abaixo, que estarão habilitados para edição:
  + **Valor máximo para renegociação:** Valor máximo permitido a ser renegociado, ou seja, a soma das parcelas vencidas.
  + **Número máximo de parcelas:** Quantidade máxima de parcelas permitidas para o novo plano.
* **Número de dias corridos para o primeiro vencimento:** Informa a quantidade de dias corridos que o sistema utilizará para calcular o vencimento da primeira parcela do novo plano. Portanto a data do primeiro vencimento será igual a data que o aditivo foi criado mais o número de dias definido nos parâmetros.
* **E-mail do(s) responsáveis pela aprovação:** Informa quais e-mails devem ser comunicados quando o comprador executa determinadas ações no Portal. Os seguintes cenários geram e-mail:
  + Comprador gera uma nova renegociação e a mesma foi efetivada de forma automática.
  + Comprador gera uma nova renegociação e a mesma aguarda análise e aprovação.
  + Comprador cancelou uma renegociação que estava na situação em preparação.

**Cliente**   
   
No Portal existem duas formas do comprador solicitar a renegociação do seu contrato. A primeira maneira é dentro da Situação Financeira da venda através do botão Renegociar. Quando a venda não possui parcelas vencidas este botão não estará visível para o usuário.  
   
A segunda forma é utilizando o menu Renegociação. Nesta tela o Portal exibe uma lista com todas as renegociações já solicitadas separadas por venda. Cada renegociação possui a sua situação (cancelado, efetivado ou em análise), a data em que foi criado, o seu número de identificação e um botão para visualizar mais detalhes.  
O Portal também apresenta a quantidade de parcelas vencidas para a venda e um botão para iniciar o processo de renegociação. Quando não houver parcelas em atraso, o sistema exibe uma mensagem informando da pontualidade dos pagamentos. Abaixo um exemplo de duas vendas com situações diferentes.  
   
Ao clicar sobre o botão Renegociar, o Portal encaminha o usuário para uma nova página, onde as parcelas passíveis de renegociação são exibidas.  
   
São parcelas passíveis de renegociação:

* Parcelas em aberto e vencidas
* Parcelas com o componente do tipo Entrada ou Principal
* Parcelas do tipo a Receber

Os valores das parcelas exibidas já são apresentados com reajuste atualizado. Portanto para o uso adequado desta ferramenta é necessário que o RM esteja configurado para utilizar o Reajuste Online.  
Ao selecionar uma parcela, o sistema exibe no rodapé da página as seguintes informações necessárias para a simulação do novo plano: O valor total a renegociar, que é a soma do valor líquido das parcelas selecionadas; um campo para o usuário definir a quantidade de parcelas do novo plano, que deverá ser entre 1 a 60 parcelas; E por último o valor da parcela do novo plano. Este valor é o resultado da divisão do valor total a renegociar pela quantidade de parcelas do novo plano. A cada alteração no valor total a renegociar e na quantidade de parcelas, o valor da parcela é alterado.  
   
O sistema não permite ao usuário selecionar parcelas de tipos diferentes. Quando a primeira parcela é selecionada, as demais de tipos diferentes ficam desabilitadas. Uma mensagem de texto é informada para o usuário para explicar o motivo.  
Conforme já explicado, as solicitações de renegociação podem ser efetivadas de forma automática ou não dependendo dos parâmetros. Caso a solicitação necessite de uma aprovação do setor responsável, então um alerta será exibido para o usuário. A mensagem do alerta dependerá dos parâmetros. Quando o sistema permite efetivar automaticamente mas os limites de valor máximo a renegociar e/ou a quantidade máxima de parcelas for extrapolado, então a mensagem irá informar o usuário os limites definidos. No exemplo abaixo, a quantidade de parcelas do novo plano passou do limite, então o alerta é exibido explicando que o aditivo passará por análise.  
   
Quando o usuário seleciona parcelas de grupos diferentes o sistema deve gerar o aditivo na situação em preparação, mesmo que a efetivação esteja marcada como automática.  
Quando o usuário seleciona as parcelas, configura o plano conforme desejado e clica no botão Simular, o sistema encaminha o usuário para uma nova tela com as parcelas do novo plano. No canto direito da nova tela, o sistema informa um resumo do plano, exibindo as datas de vencimento do primeiro e do último lançamento, a quantidade de parcelas e o valor de cada parcela. As parcelas utilizam os mesmos componentes do grupo de origem das parcelas selecionadas e o usuário final não poderá alterar ou incluir novos componentes, assim como juros e descontos. Para confirmar a solicitação, o usuário utiliza o botão "Solicitar Plano".

Antes de confirmar a solicitação, o usuário precisa, imprescindivelmente, visualizar o relatório do Termo de Aceite ou confirmar que leu este termo. Este relatório possui informações das novas parcelas geradas, valores atualizados e novos vencimentos. Somente será possível solicitar plano quando o usuário marcar o campo "**Confirmo que li e concordo com o termo de renegociação financeira"**.

Para visualizar o termo, o usuário precisa clicar no link **"Para visualizar o termo clique aqui".** Este relatório deverá ser definido nos **[parâmetros do Portal do Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047).**

Na interface de visualização do Termo de Aceite, ao clicar em "Aceitar" o campo "**Confirmo que li e concordo com o termo de renegociação financeira"** será marcado automaticamente.

Importante: Caso não exista relatório parametrizado, a renegociação prosseguirá com o fluxo anterior, sem a necessidade de clicar no campo "**Confirmo que li e concordo com o termo de renegociação financeira".**

O sistema também permite visualizar as solicitações feitas anteriormente. No menu de Renegociação do Portal, onde os aditivos são exibidos, ao clicar em visualizar de um determinado aditivo, o sistema encaminha o usuário para uma nova tela onde serão exibidos mais detalhes da solicitação feita. Nesta tela não é permitido realizar qualquer alteração no plano. O sistema apenas permite o usuário cancelar aditivos na situação Em Análise. Após este processo, o aditivo passa para o estado Cancelado e nenhuma análise é necessária mais.  
Nesta tela é possível ver detalhes básicos do aditivo como a data em que foi criado, a sua situação e o valor total a renegociar. O sistema também detalha as parcelas que foram selecionadas para a renegociação e o novo plano criado.

|  |  |
| --- | --- |
|  | Veja Também |

---

Aditivos

[Melhoria no Renegociador do Portal - Para usar estrutura do Aditivo existente.](https://tdn.totvs.com/display/LRM/Aditivo+-+Renegociador+Portal)
