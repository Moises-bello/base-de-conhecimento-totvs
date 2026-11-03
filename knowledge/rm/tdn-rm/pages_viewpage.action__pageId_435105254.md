---
content_hash: 92c54436f0bd597501456c107841dc21bb6c56cb7a96768b1bb2a373dfd92442
fetched_at: '2026-06-29T00:09:49.209173+00:00'
page_id: '435105254'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Aluguel - Contratos de Administração -
  Contrato de Administração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105254
version: 16
---

A administradora de imóvel oferece a seus clientes uma gama de serviços para facilitar e descomplicar a vida de quem precisa locar, vender um imóvel ou administrar um condomínio.   
A administradora de imóvel em troca de uma porcentagem do valor combinado na intermediação, tanto para venda como para a locação do imóvel, trabalha a sua divulgação imóvel através de anúncios em mídias especializadas, colocação de placas, visita dos interessados com acompanhamento de profissionais especializados.   
No fechamento do negócio, conta com profissionais que acompanham a negociação, orientando as partes e conferindo toda a documentação necessária.   
A administradora de imóvel tem a obrigação de fazer as vistorias, o levantamento cadastral do imóvel e dos interessados em sua aquisição, venda ou administração de condomínios, elaboração dos contratos concernentes a transação em conformidade com a legislação vigente.   
No caso de locação a administradora de imóvel tem a incumbência de receber o valor da transação, cobrança e acordo com inadimplentes, faz a ponte entre locador e locatário.   
De acordo com o Departamento de Proteção e Defesa do Consumidor, do Ministério da Justiça, as administradoras de imóveis tem como deveres:

* Informar claramente o consumidor sobre os diferentes serviços que se propõe a prestar e o preço exato que será cobrado pela sua prestação.
* Não podem fazer anúncios utilizando palavras que podem ser interpretadas como publicidade enganosa ou abusiva.
* Não podem cobrar muito mais do que o preço de mercado nem alterar o contrato feito com seus consumidores, objetivando forçá-los a cumprir obrigações que não estejam de acordo com o preço justo.

**Incluindo um Contrato de Administração**  
**Pré-Condições:**

* Incluir Imóvel.
* Ter incluído um Fornecedor ou Ambos (Cliente-Fornecedor).
* Incluir Locador (Proprietário do Imóvel).

**Passos:**

1. Acesse: Gestão de Projetos/ TOTVS Incorporação/ Aluguel/ Contrato de Administração;
2. Clique no ícone Incluir novo Contrato de Administração;
3. Preencha os campos descritos abaixo conforme desejado.
4. Clique em Salvar;
5. Vincule um Imóvel ao Contrato de Administração;
6. Vincule um Locador ao Contrato de Administração;
7. Efetive o Contrato de Administração.

Os campos apresentados no formulário são:

**Contrato de Administração**

* **Contrato de Administração**: Id do Contrato de Administração. Gerado automaticamente pelo Sistema;
* **Número do Contrato**: Número que identifica o contrato. Campo Alfanumérico;
* **Data de Assinatura do Contrato**: Data em que o contrato foi assinado pela Administradora e o Locador do imóvel.

**Prazo de Duração do Contrato**

* **Data de Início do Contrato**: Data qual o contrato passa a vigorar;
* **Periodicidade**: Tipo de Cálculo que o sistema utilizará para calcular a Data de Vencimento do Contrato de Administração;
* **Período**: Valor que complementa a Periodicidade no cálculo da Data de Vencimento do Contrato de Administração;
* **Data de Vencimento do Contrato**: Campo calculado de acordo com os valores informados para os campos de Data de Início, Periodicidade e Período.

**Taxas do Contrato**

* **% de Taxa de Administração**: Percentual que será abatido nos Lançamentos gerados através do Contrato de Locação de Imóvel;
* **Carência**: Número de Períodos que o sistema não abaterá o % de Taxa de Administração dos Lançamentos a Pagar;
* **%Taxa de Intermediação**: Percentual que será abatido nos Lançamentos gerados através do Contrato de Locação de Imóvel;
* **Recorrência**: Número de parcelas que terão o %Taxa de Intermediação deduzidos nos seus lançamentos a pagar.
* **Base de Cálculo da Taxa de Administração**: Define qual montante será utilizado como base para o cálculo da taxa de administração:

  + **Bruta**: O percentual incide sobre o valor total do aluguel.
  + **Líquida**: O percentual incide sobre o valor do aluguel subtraído o valor da taxa de intermediação.

Exemplo de Cálculo (Base Líquida)

Para facilitar o entendimento:

* **Aluguel**: R$ 1.000,00
* **Taxa Intermediação**: 10% (R$ 100,00)
* **Base de Cálculo**: R$ 900,00 (Líquida)
* **Taxa Adm (10%)**: R$ 90,00
Importante

Para entender melhor como o sistema se comporta com deduções de taxa de intermediação em cenários pro-rata, veja a documentação abaixo:

**Taxa de Repasse dos Encargos Financeiros**

* **% de Juros**: Percentual de juros que o sistema incrementará ao Lançamento Financeiro de um Contrato de Locação se a regra para sua cobrança for atendida;
* **% de Multa**: Percentual que o sistema incrementará ao Lançamento Financeiro de um Contrato de Locação se a regra para sua cobrança for atendida;
* **% de Desconto**: Percentual que o sistema decrementará ao Lançamento Financeiro de um Contrato de Locação se a regra para sua dedução for atendida;

**Importante:** Para que na baixa dos lançamentos de repasse sejam calculados, é necessário que, nos parâmetros financeiros, estejam configuradas corretamente as fórmulas para tal calculo. As sugestões das fórmulas básicas podem ser encontradas .

* **Aceita Negociar Taxas**:
  + Selecionando: Ao vincular um Contrato de Administração a um Contrato de Locação através do Imóvel, o sistema habilitará para alteração os campos de taxa no Contrato de Locação;
  + Não Selecionado: Por padrão o sistema apresenta este checkBox desmarcado e os respectivos campos no Contrato de Locação estão desabilitados para edição.

**Repasse**

* **Modelo de Repasse do Contrato de Administração:**
  + **Modelo de Repasse Condicional**: Ao selecionar o Repasse Condicional, automaticamente o sistema selecionará o valor "Variável a partir da data de pagamento" para o comboBox Data de Referência para Repasse com Dia Variável. O repasse condicional altera a data de vencimento de um Lançamento Financeiro a Pagar para a data qual o lançamento a receber foi baixado e incrementa a data de vencimento deste lançamento um número de dias igual ao valor estabelecido para o campo Dias Base para Repasse;
  + **Modelo de Repasse Garantido**: Estabelece a regra para repasse do Lançamento Financeiro a Pagar de acordo com a seleção feita no comboBox Data de Referência para Repasse com Dia Variável;
* **Dias Base para Repasse**: Número de dias que o sistema ajustará o vencimento do Lançamento Financeiro a Pagar, de acordo com a seleção feita no comboBox Data de Referência para Repasse com Dia Variável.
* **Data de Referência para Repasse com Dia Variável:**
  + **Variável a partir da data de pagamento**: O sistema altera a data de Vencimento do Lançamento Financeiro a Pagar para a data de baixa do lançamento financeiro a receber e incrementa um número de dias igual ao valor informado ao campo Dias Base para Repasse;
  + **Variável a partir da data de Vencimento**:O sistema estabelece a data de Vencimento do Lançamento Financeiro a Pagar , um número de dias igual ao valor informado ao campo Dias Base para Repasse após a data de vencimento do lançamento financeiro a receber;
  + **Fixo**: O sistema estabelece uma data de Vencimento fixa para o dia igual ao valor informado ao campo Dias Base para Repasse do Lançamento Financeiro a Pagar.
* **Cobrança do Imposto sobre o Repasse do Contrato de Administração:**De acordo com a Legislação Municipal  a cobrança de imposto sobre o repasse do contrato de administração pode ser feita pelo proprietário e não recolhido pela administradora. Sendo assim esta opção define se o imposto será recolhido pela Administradora ou será realizada pelo Proprietário.
* **Valor Total do Contrato:**
* **Situação do Contrato:**
  + **Em Preparação**
  + **Vigente**
  + **Cancelado**
  + **Encerrado**
  + **Suspenso**

Informações Complementares

---



Recursos Adicionais

---
