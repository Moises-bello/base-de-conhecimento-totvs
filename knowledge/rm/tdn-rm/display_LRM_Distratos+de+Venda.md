---
content_hash: 8e9c63be213252d681d1126b9b955ba93836f836b203dba2525e308f09f99f6f
fetched_at: '2026-06-29T00:09:47.693961+00:00'
page_id: '435105048'
product: rm
source: tdn-rm
title: Distratos de Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/Distratos+de+Venda
version: 9
---

**Distratos de Venda**   
Nesta tela é possível visualizar todos os Distratos das vendas. Possibilitando executar os seus processos sem a necessidade de abrir o cadastro de Vendas.   
   
São exibidos os seguintes campos nessa tela:   
   
**Coligada:** Exibe o número da Coligada;  
**Venda/Aluguel:** Exibe o número do Contrato;   
**Situação Distrato:** Exibe a situação do Distrato;  
**Código Tipo Distrato:** Exibe o Tipo de Distrato;   
**Descrição Motivo Distrato:** Exibe a Descrição do Motivo Distrato;   
**Data Base do Distrato:** Exibe a data base do Distrato;   
**Valor do Distrato: Exibe o Valor do Distrato;**   
**Coligada operação contábil:** Exibe a Coligada de Operação Contábil;   
**Total de Parcelas do Contrato:  Exibe o total de parcelas do contrato;**   
**ID Operação:** Exibe o código da Operação Contábil;   
**Usuário Criação:** Exibe o usuário que criou o Distrato;   
**Data Criação:** Exibe a data de criação do Distrato;   
**Usuário Alteração:** Exibe o Usuário que alterou o Distrato;   
**Data Alteração:** Exibe a Data de Alteração do Distrato;

Informações:

* Se o parâmetro **Cancelar parcelas da venda ao efetivar distrato**(Ambiente/Parâmetros/Gestão de Imóveis/Contrato/Plano de Financiamento/Plano de Financiamento), estiver habilitado será feito uma validação do sistema se os lançamentos podem ser cancelados, caso seja encontrado algum impedimento será necessário ajustar os lançamentos listados no log, para posteriormente efetivar o Distrato.
* Quando **não** existir parcelas de devolução, para que ocorra a quitação do plano de devolução, o sistema irá efetuar o cancelamento do plano de financiamento existentes oriundos do contrato de venda no momento da efetivação do distrato. caso seja encontrado algum impedimento será necessário ajustar os lançamentos listados no log, para posteriormente efetivar o Distrato.
* Ao baixar a última parcela do distrato o sistema irá quitar o distrato cancelando todas as parcelas do plano de financiamento da venda/aditivo. Caso seja cancelada a baixa da última parcela do distrato, o sistema **não** alterará a situação deste Distrato, ou seja ele será mantido com situação quitada.

Guardar Informações sobre Distrato

### **Reversão do Distrato com Reprocessamento de Parcelas   VERSÃO 12.1.2602 em Diante.**

Para possibilitar a contabilização correta das parcelas anteriores ao aditivo, é necessário realizar a **reversão do distrato**.

Com esse objetivo, foi implementado o controle de estado das parcelas (**quitadas e em aberto**), permitindo restaurar parcelas que tenham sido canceladas durante o processo de distrato.

Durante a reversão:

* As parcelas são **recalculadas em memória** para sincronização dos valores;
* A **efetivação do distrato efetivará o reajuste** na base para a data do distrato e caso esteja fechado a competência contábil, o sistema contabilizará na data atual.

---

### **Parâmetro de Cancelamento de Parcelas**

O comportamento do processo depende da configuração do parâmetro:

**“Cancelar parcelas da Venda ao efetivar distrato”**

📍 **Localização:**  
Contrato de Venda > Plano de Financiamento > Plano de Financiamento

|  |  |
| --- | --- |
|  | Veja Também |

---

Distrato
