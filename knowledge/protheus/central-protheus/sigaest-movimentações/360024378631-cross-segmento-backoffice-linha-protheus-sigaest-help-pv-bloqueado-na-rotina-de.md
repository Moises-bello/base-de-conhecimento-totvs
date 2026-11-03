---
article_id: 360024378631
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5b5014cd3c8d1941d2ebdf57bc9bd7ba7382d5e7926586e5eeb045d3e05e3f52
fetched_at: '2026-06-28T22:38:55.590137+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Help PV BLOQUEADO
  na rotina de Transferência entre Filiais (MATA310 e MATA311)
type: support-article
updated_at: '2025-08-05T19:00:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024378631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-PV-BLOQUEADO-na-rotina-de-Transfer%C3%AAncia-entre-Filiais-MATA310-e-MATA311
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23217982821143)* Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**  
Ao efetivar uma solicitação de transferência através rotina de **Transferência entre Filiais** (**MATA310** e **MATA311**) está apresentando a mensagem: "**PV BLOQUEADO**". O que fazer para resolver o Help?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001297601)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Existem algumas validações que acionam esse HELP.

Mantenha os pacotes acumulados de Estoque/Custos e Faturamento atualizados.   
[- Acumulado BackOffice conforme sua versão](https://tdn.totvs.com/x/2hgdHw)  
**Obs:** sempre aplicar pacotes de atualização primeiramente em ambiente de homologação.

1. Avalie se o saldo que está tentando transferir não está em poder de terceiros.
2. Ajuste o parâmetro **MV\_VEBLQRG** para **.T.** (**T*****rue***).
3. Caso tenha configurado Regra de Negocio (FATA100), deletar as informações.
4. Avaliar como está o parâmetro **MV\_AVALEST**. Ele serve para definir como ocorrerá a liberação de crédito, sendo:  
   **1 =** Considerar quantidade Liberada;  
   **2 =** Considerar a quantidade em Estoque;  
   **3 =** Bloqueia o estoque.
5. Incluir o campo [**NNT\_NUMPED**](https://tdn.totvs.com/display/public/PROT/12323727+DMANMAT01-32758+DT+MATA311+-+PV+BLOQUEADO)no dicionário de dados, o campo será responsável por armazenar o número do pedido de venda quando a solicitação de transferência for encerrada com bloqueio, conforme documentação do link abaixo:  
   <https://tdn.totvs.com/display/public/PROT/12323727+DMANMAT01-32758+DT+MATA311+-+PV+BLOQUEADO>

Após efetuada a criação do campo indicado acima, o **Help PV Bloqueado inclui a opção de "Continuar"** onde criar o Pedido de Venda Bloqueado aguardando a Liberação. **Sendo necessário continuar o processo manual pelas rotinas do Faturamento.**

Também, podendo Cancelar a transferência e reavaliar os saldos como desejar.

**HELP ATUALIZADO COM AS OPÇÕES**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12807361136535)

* Revise o Saldo do Produto se consta com **Saldo de Terceiro em Nosso Poder (B2\_QTNP)** ***igual ou** **superior*** *ao saldo disponível no Armazém*. Veja exemplo abaixo, nesse cenário as rotinas MATA310 e MATA311 não permitem utilizar o Saldo de Terceiro para movimentar para outras Filiais.

***Dica.*****:** É possível transferir o saldo pela rotina MATA261 para um Armazém que **não tenha Saldo de Poder de Terceiro** e dessa forma concluir a Transferência entre as Filiais sem que apresente o Help PV Bloqueado. No exemplo abaixo transferir para o Armazém 02.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12807998449047)

* Revise no **Cadastro do Cliente (Filial Origem)** se o campo **Risco** esta *diferente* de **Vazio ou A**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13491700589207)

### **Ao efetivar uma Solicitação de Transferência o campo NNT\_NUMPED deveria vim preenchido?**

O processo de transferencia de filiais MATA310 e também a  MATA311, é um facilitador de todo um processo que pode ser feito manualmente, compreendido com a inclusão de um pedido de vendas necessario para a emissão de nota fiscal, e assim como no processo manual, na transferencia de filiais MATA310 e a MATA311, o pedido pode ser bloqueado e não aprovado, seja bloqueio de estoque ou outros.

No caso manual, o pedido é inserido e havendo um bloqueio entra na agenda de liberação, podendo ser liberação de estoque ou credito, ou por regras de bloqueio.

Já no MATA310 o pedido é inserido e havendo um bloqueio, a etapa seguinte da emissão da nota deverá ser efetuada manualmente, e na agenda de transferencias MATA311, havendo um bloqueio no pedido, é dado diversas mensagens, que o pedido foi bloqueado podendo visualizar o item com bloqueio, ou continuar, e se continuar é encerrada a solicitação, gerando o pedido bloqueado, e a nota não será gerada automaticamente.

Somente nesta exceção, o campo do pedido é atualizado para o usuario saiba qual é o pedido, permitindo que ele resolva o motivo do bloqueio e possa seguir com a emissão da nota fora da rotina.

Portanto, esta atualização foi concebida em carater de exceção e não como um identificador do pedido gerado no processo efetivado, não caracterizando assim um erro ou não conformidade, porem a sugestão de atualização com o numero do pedido na efetivação pode ser uma sugestão de melhoria via [Central Colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)

Como alternativa, caso a melhoria seja validada, aceita pelo time de produto TOTVS e deseje a implementação da funcionalidade na versão atual ou em curto prazo, podemos direcionar essa solicitação para a nossa área de Central de Soluções que providenciará uma proposta de customização para sua empresa para atender a funcionalidade sugerida.

***Saiba mais:***  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)  
[*SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-)  
[*SIGAEST - MATA310/MATA311 - Transferência entre Filiais utilizando o parâmetro MV\_FILTRF*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF)  
[*SIGAEST - MATA310 e MATA311 é possível utilizar com a TES controlando Poder de Terceiros?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12052291346583-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-e-MATA311-%C3%A9-poss%C3%ADvel-utilizar-com-a-TES-controlando-Poder-de-Terceiros-)
