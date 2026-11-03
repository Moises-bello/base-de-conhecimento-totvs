---
content_hash: 0e83c1333f0fc2601ad00c4e17df6e0500628d903d12fff800b7e2a17c345a8d
fetched_at: '2026-06-29T00:11:36.863425+00:00'
page_id: '773518793'
product: rm
source: tdn-rm
title: TCGI - Comissão - Integrar/Cancelar Parcelas Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773518793
version: 4
---

### **Processo de Integrar/Cancelar Parcelas de Comissão**

O Processo de Gerar/cancelar Integração da Comissão no RM enviará as informações das parcelas da comissão, de acordo com cada regra.  
A comissão pode ser integrada com o uso da Fórmula de validação ou sem o uso.  
Somente parcela com status de calculada que será integrada.  
O cancelamento da integração pode ser feito de todas as parcelas ou de uma competência.

Os tipos de integração disponível são **TOTVS Gestão de Estoque Compras e Faturamento,**  **TOTVS Gestão Financeira e TOTVS Folha de Pagamento**.

Liberar Perfil do Usuário para utilizar o processo de Integração das Parcelas da Comissão

Novidade!

A partir do Release 12.1.2310.160 e superiores, o processo para Integrar as Parcelas da Comissão permite as seguintes parametrizações de execução:

* **Competências do Vencimento:**
  + **Todas:** este processo será executado para todas as parcelas de comissão com situação calculada, independentemente da sua competência;
  + **Mês Corrente:** este processo será executado somente para as parcelas de comissão com situação calculada, cuja competência de vencimento seja no mês atual;
  + **Mês Anterior:**  este processo será executado somente para as parcelas de comissão com situação calculada, cuja competência de vencimento seja no mês anterior ao da execução do processo; ou
  + **Específica:**  este processo será executado somente para as parcelas de comissão com situação calculada, cuja competência de vencimento seja a especificada;

Este processo permite ainda que sejam selecionadas as seguintes opções de Tipos de Parcelas de Comissão:

* **Todos:** este processo será executado para todos os tipos de parcelas de comissão, desde que elas estejam em situação calculada;
* **Comissão:** este processo será executado somente para as parcelas de comissão do tipo Comissão, ou seja, as que que tem origem direta na criação da comissão;
* **Prêmio:** este processo será executado somente para as parcelas de comissão do tipo [Prêmio](https://tdn.totvs.com/pages/viewpage.action?pageId=772038893);
* **Apuração Mensal Meta:** este processo será executado somente para as parcelas de comissão do tipo [Apuração Mensal Meta](https://tdn.totvs.com/pages/viewpage.action?pageId=773885389); ou
* **Comissão Complementar:** este processo será executado somente para as parcelas de comissão do tipo Comissão Complementar, ou seja, as que que tem origem pelo processo de [Recálculo de Comissão por Competência](https://tdn.totvs.com/pages/viewpage.action?pageId=821184753).

O processo para Cancelar a Integração das Parcelas de Comissão, também passa a permitir a seleção do Tipo de comissão:

### **Tipos de Processos da Integração e Cancelamento da Integração das Parcelas**

Tipos de IntegraçãoTOTVS Gestão de Estoque Compras e FaturamentoTOTVS Gestão de Estoque Compras e Faturamento e Gestão Financeira |

Regra de Comissão se encontra com a seguinte configuração:

* Corretor Padrão  ( TOTVS GESTÃO FINANCEIRA )
* Imobiliária ( TOTVS GESTÃO FINANCEIRA )
* SDR ( TOTVS GESTÃO DE ESTOQUE COMPRAS E FATURAMENTO )

Modalidade da Comissão configurada nos Parâmetros de Integração com :

* TOTVS Gestão de Estoque Compras e Faturamento
* TOTVS Gestão Financeira

Comissão Gerada e Status dos itens ( **Calculada** )

Selecionar a Comissão e em seguida : Processo | Integrar as Parcelas da Comissão

Após processar ( Integrar as Parcelas da Comissão )

As parcelas passam a ficar com o Status de ( **EM INTEGRAÇÃO** ) , Lembrando que a parcela de CLIENTE não é integrada.

Após a execução do processo de Integração

Gerada a Integração com TOTVS Gestão Financeira

Gerada Integração com TOTVS Gestão de Estoque Compras e Faturamento.

TOTVS Folha de PagamentoTOTVS Folha de Pagamento |

### TOTVS Folha de Pagamento

O Portal de Imóveis hoje trabalha com o CPF do corretor (ou CNPJ da imobiliária). Essa informação é automaticamente associada ao fornecedor no RM. Para facilitar a integração e não obrigar uma configuração de chapa relacionada ao funcionário no portal, iremos trabalhar sempre com fornecedores na comissão do TCGI. Para facilitar a integração da comissão com a Folha de Pagamento, foi criado um processo para esse vínculo.

Funcionário cadastrado no TOTVS Folha de Pagamento

Vínculo pode ser como antes , no cadastro do Fornecedor em :

Integrações | Dados Complementares ( TCGI )

Ocupação Profissional

Em Tipo de Integração : Receberá a Comissão por :

Informar a Integração com o TOTVS Folha de Pagamento e em seguida selecionar a Chapa do Funcionário.

**Pelo Processo de Comissão:**

Selecionar Comissão e em seguida : Associar Chapa ao Fornecedor da Comissão

Associação já encontra o Funcionário com mesmo CPF e faz a associação com Fornecedor.

Chapa do funcionário associada ao Fornecedor.

**Integrando Comissão Folha de Pagamento**

O Processo de Gerar/cancelar Integração da Comissão no RM enviará as informações das parcelas da comissão, de acordo com cada regra.   
A comissão pode ser integrada sem o uso da ´formula de validação ou com o uso dela.  
Somente parcela com status de calculada que será integrada;  
O cancelamento da integração pode ser feito de todas as parcelas ou de uma competência

Regra de Modalidade cadastrada com Tipo de Integração ( **Folha de Pagamento** ) e Comissionado e sua Chapa informada.

Comissão gerada e Integrada.

Id da Folha de Pagamento na Parcela de Comissão

TOTVS Folha de Pagamento - Em grupo de eventos - Identificação ( Marcar : Lançar eventos da Integração com outros aplicativos ) Subsituir.

Integração com outros Aplicativos ( Marcar : TOTVS Incorporação - Comissão Mensal ).

Por fim : Clicar em ( Lançar ).

Envelope Gerado!

Cancelar Integração das ParcelasCancelar Integração das Parcelas |

Se quiser **Cancelar** a Integração das Parcelas , basta Selecionar a Comissão e em seguida : Processos | Cancelar Integrações das Parcelas da Comissão

Podendo cancelar todas parcelas ou apenas uma determinada Competência.

Integrar Parcela via FórmulaIntegrar Parcela via Fórmula |

**Exemplo de Integrar Parcela via Fórmula**

**1 -**Modelo de Cálculo da Comissão - Parametrizado para Utilizar Fórmula.

Neste Exemplo , modelo de Cálculo esta parametrizado para gerar ( 4 PARCELAS ) e utiliza Fórmula que valida para INTEGRAR apenas a Parcela 1 , parcela 2 , 3 e 4 não irão Integrar.

Se a Parcela for 1 ( **Integrar** ) se for diferente ( **Não Integrar** ).

Exemplo de Fórmula:

Se TABCOMISSOESITEMPARCELA ('NUMPARC','I')=1 Entao   1 Senao   0 FimSe

Cadastrada em seguida uma Regra da Comissão ( Neste exemplo comissão para Corretor da Proposta e utilizando a Modalidade de Cálculo parametrizada com a **Fórmula**.

Cadastrada Modalidade da Comissão com os dados:

* Regras x Modalidades da Comissão
* Parâmetros de Integração
* Imóveis x Modalidades da Comissão

**Gerando a Comissão**

Comissão Gerada com 4 Parcelas e calculada (Conforme parametrizado Modelo de Cálculo da comissão ).

Selecionar a Comissão e em seguida : Processos | Integrar as Parcelas da Comissão

Apenas **Parcela 1** encontra-se Integrada , as **parcelas 2 , 3 e 4 não se encontram Integradas**.

Pois a Fórmula criada para esse exemplo , irá validar apenas a **Parcela = 1**
