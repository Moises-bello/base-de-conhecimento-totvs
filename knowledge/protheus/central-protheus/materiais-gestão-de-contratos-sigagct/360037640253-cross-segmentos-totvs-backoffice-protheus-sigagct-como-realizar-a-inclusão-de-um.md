---
article_id: 360037640253
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: e62a1c4330641a53bc561a08f418d4d652b0539f1c0e134c2c5469b296d99e33
fetched_at: '2026-06-28T22:37:21.616933+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a inclusão
  de um Contrato Flexível ?
type: support-article
updated_at: '2025-11-24T20:28:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037640253-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-inclus%C3%A3o-de-um-Contrato-Flex%C3%ADvel
---

**Dúvida**  
Como realizar a inclusão de um Contrato Flexível ?  
  
**Ambiente**  
Microsiga Protheus  – Gestão de Contratos – A partir da versão 12

**Solução**

Consulte o nosso video:

[How To | MP-SIGAGCT - Contrato Flexível](https://youtu.be/Q1whNSaOuyE)

O Conceito de Contrato Flexível é quando não é possível estimar o que vou vender ou que vou comprar.

Neste tipo de Contrato não há informação de Itens na Planilha do Contrato, sendo estas informações com Produto, Quantidade e Valores inseridas no momento da medição.

Para incluir um Contrato do Tipo Flexível, deverá ter as seguintes configurações no cadastro de Tipo de Contrato:

**MEDIÇÃO EVENTUAL** = SIM → Não possui Cronograma, ou seja, não é possível prever os valores do contrato.

**CONTRATO FIXO** = NÃO → Não possui Estrutura de uma Planilha, ou seja, será um contrato flexível.

**PREVISÃO FINANCEIRA** = SIM→ Contrato sem itens na planilha, mas você sabe que gastará um certo valor naquele contrato, caso passe deste valor, terá que rever através de revisão o contrato).

O campo Previsão Financeira (**CN1\_VLRPRV**) é habilitado somente quando Ctr. Fixo como **NÃO** e serve para indicar se haverá controle financeiro no contrato mesmo não havendo itens na planilha (Planilha Flexível). Em caso positivo, ao incluir o contrato o valor total negociado pelo contrato deverá ser informado manualmente e a soma dos valores medidos não poderá ultrapassar o previsto no contrato.

Previsão Financeira (**CN1\_VLRPRV**) - Indica se serão informados valores para a previsão financeira do contrato, independente do uso de planilhas.  
Pode-se configurá-lo com:

**SIM** → O usuário deverá informar o valor do contrato no campo Valor Total da Planilha (***CNA\_VLTOT***)  
**NÃO** → O valor do contrato é atualizado de acordo com as medições executadas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403897564695)

Para atender ao conceito dos contratos flexíveis, no momento da medição, o Sistema solicita a informação dos produtos e quantidades envolvidas.

Para os contratos flexíveis **com previsão financeira**, ao encerrar a medição, o Sistema atualiza o saldo e controla os valores totais.

Para os contratos flexíveis **sem previsão financeira**, os valores previstos serão atualizados conforme as medições efetuadas e o saldo será sempre zero (0).

Para o controle dos contratos flexíveis, foram disponibilizados dois campos: Ctr. Fixo (**CN1\_CTRFIX**) - Informa se o contrato possui estrutura **fixa** ou **não**. Pode-se configurá-lo com:

**SIM** → O contrato deve possuir itens nas planilhas que formarão o seu valor financeiro.  
**NÃO** → O contrato não possui itens nas planilhas (Contratos Flexíveis), e seus valores serão informados manualmente e por meio das medições.

**Observações:**

Ao incluir a medição, caso os campos  CNE\_PRODUT e CNE\_QUANT não estejam habilitados,  verifique se os mesmos encontram-se em **Propriedade = 1 Alterar.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9478849838871)

Este tipo de Contrato **não**gera Títulos Provisórios no Financeiro. O campo de ***Previsão Financeira*** no tipo de contrato não tem este conceito, este serve para sinalizar se o contrato terá controle financeiro, ou seja, se o usuário irá informar o valor do contrato no campo Valor Total da planilha do contrato se o campo estiver com o conteúdo = **SIM**, caso contrário com conteúdo = **NÃO** o valor do contrato será atualizado de acordo com as medições inclusas.

***Obs1**:*

Caso queira poderá realizar a configuração no Tipo de Planilha (CNL) rotina

CNTA230 conforme exemplo abaixo:

Exemplo de Planilha Flexível de Compras

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10847626987415)

Na inclusão do Contrato quando tiver preenchido os campos conforme exemplo acima  o sistema irá  ignorar as configurações do Tipo de Contrato (CN1) e considerar as configurações do Tipo de Planilha (CNL) para inclusão do contrato Flexível.

O Tipo de Planilha normalmente é utilizado em casos em que há mais de uma planilha com configurações diferentes no contrato para que cada Planilha tenha sua respectiva configuração.

***Obs2:***

Caso queira considerar as configurações da rotina CNTA021 Tipos de Contratos configure o Tipo de Planilha com os campos preenchidos conforme o contrato segue exemplo abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10847957665047)

***Obs3:***

A "Previsão Financeira", quando configurada como "Sim", pode ser considerada como um "Valor Limite Máximo"  ou "Teto Contratual" do Contrato Flexível.

***Saiba Mais:***

[Tipos de Contratos - CNTA021 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=274323782)

[Tipos de Planilhas - CNTA230 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=233734412)

[GCT0027\_Como\_incluir\_um\_Tipo\_de\_Contrato Flexível - CN1\_CTRFIX](https://tdn.totvs.com/pages/viewpage.action?pageId=239023109)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
