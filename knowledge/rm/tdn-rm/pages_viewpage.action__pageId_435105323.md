---
content_hash: 0f56b617f01437f3ed839cbfddbf6bfef6e0aa6c6aa996746a3e6a8b4fe3c7cd
fetched_at: '2026-06-29T00:09:49.575664+00:00'
page_id: '435105323'
product: rm
source: tdn-rm
title: Parcela de Reembolso - Processo - Gerar Lançamentos de Reembolso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105323
version: 8
---

Esse processo é o responsável por gerar os lançamentos a receber das parcelas de reembolso da despesa.   
   
**Pré-requisitos:**

* A despesa deve estar da seguinte forma:

* + Parâmetro "Permite reembolso" marcado;
  + Uma ou mais parcelas de reembolso vinculadas;
  + Parâmetro de reembolso vinculado;
  + Parâmetro de integração financeira vinculado;
  + Deve estar na situação "Integrada";

**Como executar:**

* Acesse a visão de Despesas através do caminho: TOTVS Incorporação >> Aluguel>> Despesa;
* O processo pode ser executado de 2 formas, são elas:

* + **Através da visão da despesa ou da edição da despesa:** Ao executar dessa forma, será exibido uma tela permitindo inserir o período que se deseja gerar os lançamentos. Caso não seja informado nenhum período será gerado os lançamentos financeiros a receber de todas as parcelas de reembolso vinculadas as despesas selecionadas;
  + **Através da visão da parcela de reembolso ou da edição da parcela reembolso:** Ao executar dessa forma, será gerado os lançamentos financeiros a receber de todas as parcelas de reembolso selecionadas;

**Observações:**

* Os lançamentos serão gerado para um  responsável financeiro de acordo com a regra de reembolso vinculada a despesa. Segue abaixo uma tabela com  o comportamento do sistema de acordo com a parametrização da regra de reembolso e do imóvel da despesa:

  **Tabela 1 - Comportamento do sistema de acordo com a regra de reembolso e situação do imóvel**

* Quando um imóvel possui mais de um locatário principal, sendo assim do tipo "Áreas Fracionadas" ou "Áreas Unificadas" e possuindo mais de um Contrato de Locação efetivado em um mesmo período. Será gerado um lançamento a receber para cada locatário, tendo o seu valor de reembolso rateado conforme o somatório de área locada por um locatário em relação a área total do imóvel. Segue abaixo um exemplo:
  + Imóvel com 2 áreas:
    - Área 1 - 100 metros total;
    - Área 2 - 100 metros total;
  + Possui 2 locatários:
    - José locou 50 metros da Área 1;
    - João locou 100 metros da Área 2;
  + Despesa no valor de R$ 2.000,00;
  + Ao gerar os lançamentos de reembolso, irá realizar a seguinte conta:
    - (Somatório das áreas locada do locatário/área total do imóvel) \* Valor da Despesa;
    - Cálculo locatário José: 50/200 \* 2000,00 = R$ 500,00
    - Cálculo locatário João: 100/200 \* 2000,00 = R$ 1.000,00
  + Podemos observar que faltou R$ 500,00 reais para que a despesa fosse totalmente reembolsada, só que não foi possível, pois o imóvel possui 50 metros de vacância. Nesse caso a administradora do imóvel irá assumir essa parte da despesa.
* Os lançamentos serão gerados somente para o locador ou locatário principal, dos contratos de Administração e Locação respectivamente;
* Será buscado somente o locador ou locatário vigente conforme a data de competência cadastrada na Despesa;

Importante: Na geração de lançamentos de reembolso, caso o parâmetro integração financeira não estiver configurado com algum valor para o campo "Centro de Custo" o sistema irá automaticamente buscar o centro de custo cadastrado no imóvel associado a despesa.

Veja Também

---
