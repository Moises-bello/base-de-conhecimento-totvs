---
article_id: 115010681487
category: Financeiro - Solicitação de Transferência
content_hash: 82507a6c75ea25cb65a3f34e7b6fb8e84ec4e5948f92683fe5eaafedfcd81f6b
fetched_at: '2026-06-28T22:37:37.492178+00:00'
product: protheus
section_id: 35057455051671
source: central-protheus
title: MP - SIGAFIN - FINA620/FINA630 - Como realizo a solicitação de Transferência
  pelo financeiro
type: support-article
updated_at: '2025-11-26T20:04:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010681487-MP-SIGAFIN-FINA620-FINA630-Como-realizo-a-solicita%C3%A7%C3%A3o-de-Transfer%C3%AAncia-pelo-financeiro
---

**Dúvida**  
Como realizo a solicitação de Transferência pelo financeiro?  
  
**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 12  
  
**Solução**  
**Solicitação de transferência- FINA620**

Essa rotina permite que uma empresa corporativa possa transferir os débitos dos clientes (títulos a receber) entre as filiais da empresa e/ou entre outros clientes. Esse recurso atende, principalmente, o ramo de transportes, permitindo que uma empresa (corporativa) possa cadastrar seus débitos entre as filiais que originaram os títulos do **Contas a receber**.  
O sistema disponibiliza um questionário (*checklist*), configurado pela tabela **AA - Checklist para Transferência de Débito**, no módulo **Configurador**, para que a empresa defina se a cobrança deve ser transferida. No entanto, caso seja necessário implementar opções de verificação no *checklist*, a Tabela AA pode ser alterada, por meio do **Configurador**. Dessa forma, somente será permitida a inclusão da solicitação, se todas as questões do *checklist* forem respondidas com **Sim** (marcadas com **X**).  
A Tabela **SE6** - Solicitações de Transferência armazena todas as informações da transferência, e cada solicitação é gravada com um número sequencial no campo **Nº. Solic.**  
O campo **Parc. Dest.** armazena a parcela do título gerado na filial de destino (débito), originado pela rotina **Transferência de títulos a receber entre filiais**, gravando e validando esse código.  
Para que seja efetivada a transferência, a filial de destino pode aceitar ou rejeitar essa solicitação, por meio da rotina **Aprovação/Rejeição solicitação**.

**Dica:**  
O campo **Fil. Débito** permite que seja gravada a filial de débito de título (em customização) ou pelo módulo **Gestão de Transportes** (sistema original). Esse campo é a referência para a seleção das solicitações de transferências, indicando, numa base de Contas a Receber compartilhada, qual é a filial de débito.

**Importante:**  
O sistema não permite a solicitação de transferência nas seguintes situações:

• quando o título não estiver em carteira;  
• quando o título já sofreu algum tipo de baixa;  
• quando já houve solicitação de transferência anterior para esse título.  
  
**Procedimentos:**  
Para efetuar uma solicitação de transferência:  
1. Em **Solic. de Transf.**, selecione o título desejado e clique em **Solicitar.**  
2. O sistema apresenta a tela de Solicitação de Transferência.  
3. Na área superior da tela, são relacionados os dados do título.  
4. Na área central, o sistema apresenta o *checklist*. Todas as questões devem ser assinaladas.  
  
**Importante:**  
Somente será permitida a inclusão de uma solicitação de transferência, se todas as questões do *checklist* forem respondidas com **Sim** (marcadas com **X**).  
5. Na área inferior, selecione a filial de débito (destino) ou o cliente (débito) e informe o histórico da solicitação de transferência, se desejar.  
6.  Confira os dados e confirme.  
7.  Observe que título é sinalizado com a legenda na cor vermelha , aguardando aprovação ou rejeição.   
  
**Aprovação/rejeição da transferência - FINA630**

Esta rotina efetiva ou não a transferência de débito das solicitações pendentes incluídas através da rotina  **Solicitação de transferência**.

O sistema permite aprovar, rejeitar ou excluir as transferências, onde:  
• **Aprovar**  
Efetua a transferência, processando a baixa na filial original e gerando as cobranças na nova filial de débito (destino).  
• **Rejeitar**  
Rejeita a solicitação após a informação do motivo, não efetuando a baixa, apenas registrando a rejeição no arquivo de solicitações (**SA6**).  
• **Excluir**  
Exclui a solicitação de transferência incluída anteriormente.  
Após a efetivação da rotina, será impresso o aceite da transferência.  
A contabilização da rotina é executada pelos lançamentos padronizados de emissão e baixa de títulos e, para o cálculo da comissão, são considerados os títulos em sua filial original.

**Procedimentos:**  
Para efetuar a aprovação ou rejeição da transferência:  
1. Na janela de manutenção de "Aprovação/Rejeição da Transferência", o sistema apresenta a tela de parâmetros, para filtragem da exibição das solicitações em aberto ou de todas as solicitações de transferência.  
2. Selecione e confirme.  
O sistema apresenta os títulos referentes as solicitações, conforme seleção do parâmetro.  
3. Selecione o registro desejado, e em seguida, uma das opções do menu:  
Opção **Aprovar**

Opção **Rejeitar**

Opção **Excluir**
