---
article_id: 22515207808919
category: Originação de Grãos (OG)
content_hash: f36c8f7b864e73c9021264d1ae1c2e4b2affc085b3525191a01a7c8494296be5
fetched_at: '2026-06-28T22:45:39.473971+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Exemplo de Utilização na Nova Comercialização
type: support-article
updated_at: '2025-06-24T19:19:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22515207808919-Agro-Linha-Protheus-AGR-Exemplo-de-Utiliza%C3%A7%C3%A3o-na-Nova-Comercializa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22515207788823) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como são descritos uma estrutura de **Exemplo de Utilização** **na Nova Comercialização**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos para incluir uma nova negociação na nova comercialização. O exemplo é de uma operação de venda, mas é similar para operação de compra:

**1.** Verifique, os parâmetros **MV\_AGRO002** habilitados. Os parâmetros devem ser alterados no módulo Configurador;

**2.** Acesse em **Gestão de Agronegócio - SIGAAGR**, acessando **Atualizações > Comercialização > Negociação > Controle de Negócios > Registro de Negócios**;

**3.** Clique em **Incluir**;

**4.** Informe os campos iniciais que são apresentados:

* Safra;
* Produto;
* Moeda;
* Operação de Negócio (1 - Compra; 2 - Vendas).

**5.** Informe os campos obrigatórios:

* Na pasta Principal: (Entidade, Filial de Origem, Tipo Preço);
* Na pasta Precificação (Data inicial e final, Quantidade e Filial de Origem. Para negociação a fixar, os campos Data Limite Fixação, Mês Bolsa, Índice de Negócio são obrigatórios). O índice de negócio representa o índice futuro na bolsa. Na tabela inferior são apresentados os componentes que estão vinculados ao produto informado na negociação. Informe um valor para os componentes e no componente do tipo resultado será apresentado o valor final. Quando a negociação é a fixar, os componentes podem ser fixados, mas o preço final não é fechado.

**6.** Clique em **Confirmar**;

**7.** Clique em **Outras Ações > Aprovar**. Caso algum componente fixado possua *hedge*, a próxima situação do registro de negócio é trabalhando. Portanto, é necessário acessar a opção de aprovação novamente após ter feito o *hedge* em Sistema de terceiro. A aprovação também pode ocorrer automaticamente em todas as etapas, conforme configurado nos parâmetros **MV\_AGRO003 - Necessidade de Aprovação de negócios** e **MV\_AGRO006 - Aprovação de banking no cadastro de novos negócios**.

**8.** Clique em **Outras Ações > Aceite Cliente > Aprovar**;

**9.** Analise em **Gestão de Agronegócio - SIGAAGR**, acessando **Atualizações > Comercialização > Negociação > Contrato de Venda > Contrato de Venda**;

**10.** Selecione o contrato que foi gerado por meio do processo de aprovação do **Registro de Negócio**;

**11.** Clique em **Alterar**;

**12.** Informe os campos obrigatórios:

* Na pasta **Principal (TES)**;
* Na pasta Financeiro (Ref. Contrato, Tipo Valor, Quantidade ou Percentual);

**13.** Clique em **Confirmar**;

**14.** Clique em **Outras Ações > Confirmar**.
