---
article_id: 22182266219159
category: Originação de Grãos (OG)
content_hash: 911672789b598ffbe727f31692d4cf7d70488c6b56c82e1a4dbd2decad493cf5
fetched_at: '2026-06-28T22:45:39.495949+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Fixação de Componente na Nova Comercialização
type: support-article
updated_at: '2024-07-03T21:18:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22182266219159-Agro-Linha-Protheus-AGR-Fixa%C3%A7%C3%A3o-de-Componente-na-Nova-Comercializa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22182278887959) Tempo aproximado para leitura: **00:03:30 min****Dúvida**  
Como realizar uma Fixação de Componente na Nova Comercialização?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**Fixação de Componente:**

**1.** Analise em **Gestão de Agronegócio - SIGAAGR**, acessando **Atualizações > Comercialização > Gestor Comercial > Painel de Fixações** para realizar fixações. Esse processo também pode ser realizado pelo **Registro de Negócio**;

**2.** Informe os campos iniciais para filtrar a consulta;

**3.** Selecione o contrato e cadência e em seguida clique em **Fixar**;

**4.** Selecione o tipo de fixação **2-Componente**. Quando optado por fixar apenas componente, deve-se informar a quantidade e valor para cada componente a ser fixado. Somente será permitido informar um volume para componentes que possuam saldos a serem fixados;

**5.** Clique em **Confirmar**;

**6.** Clique em **Outras Ações > Aprovar**.  Caso algum componente fixado possua *hedge*, a próxima situação do registro de negócio é Trabalhando. Portanto, é necessário acessar a opção de aprovação novamente após ter feito o *hedge* em Sistema de terceiro. A aprovação também pode ocorrer automaticamente conforme estiver configurado no parâmetro **[MV\_AGRO006 - Aprovação de banking no cadastro de novos negócios](https://tdn.totvs.com/pages/viewpage.action?pageId=370618885).**

**Fixação de Preço:**

**1.** Analise em **Gestão de Agronegócio - SIGAAGR**, acessando **Atualizações > Comercialização > Gestor Comercial > Painel de Fixações** para realizar fixações. Esse processo também pode ser realizado pelo **Registro de Negócio**;

**2.** Informe os campos iniciais para filtrar a consulta;

**3.** Selecione o contrato e cadência e em seguida clique em **Fixar**;

**4.** Selecione o tipo de fixação **1-Preço**. Quando optado por fixar preço deve-se informar a quantidade na cadência e a mesma é replicada para os componentes. É deduzido volumes já fixados anteriormente por componente. A **fixação de preço** define que foi fechado um valor para um volume. Esse valor será utilizado para gerar a **previsão financeira e faturamento**;

**5.** Clique em **Confirmar**;

**6.** Clique em **Outras Ações > Aprovar**. Caso algum componente fixado possua *hedge*, a próxima situação do registro de negócio é Trabalhando. Portanto, é necessário acessar a opção de aprovação novamente após ter feito o *hedge* em Sistema de terceiro. A aprovação também pode ocorrer automaticamente conforme estiver configurado no parâmetro **[MV\_AGRO006 - Aprovação de banking no cadastro de novos negócios](https://tdn.totvs.com/pages/viewpage.action?pageId=370618885).**

**Consulta de valores financeiros, de faturamento e fixados:**

**1.** Analise em **Gestão de Agronegócio - SIGAAGR**, acessando **Atualizações > Comercialização > Negociação > Contrato de Venda > Contrato de Venda**;

***2.*** Posicione no contrato de venda que deseja consultar;

**3.** Clique em **Visualizar**;

**4.** Clique na pasta **Previsão de Entrega**;

**5.** Verifique na tabela superior da pasta **Previsão de Entrega** selecione a cadência que deseja consultar os valores;

**6.** Verifique na tabela inferior da pasta **Previsão de Entrega** são exibidas **regras fiscais**. Para cada regra fiscal é possível ter acessos aos **valores do contrato** nos campos **Vlr. Tot. Fin**, **Vlr. Tot. Fat** e **Vlr. Tot. Fix**. **NOTA**: Na nova comercialização existe o conceito de regra fiscal que é similar a um pedido. Uma previsão de entrega pode ter uma ou mais **regras fiscais**.

**Gerando um relatório com os dados financeiro de faturamento e fixação:**

**1.** Verifique em **Gestão de Agronegócio - SIGAAGR**, acessando **Atualizações > Comercialização > Negociação > Contrato de Venda > Contrato de Venda**;

**2.** Posicione no **contrato de venda** que deseja gerar o relatório;

**3.** Clique em **Outras Ações > Mais Ações > Extrato Contrato**;

**4.** Clique em **Imprimir.**
