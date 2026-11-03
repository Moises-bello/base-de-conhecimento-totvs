---
article_id: 11387150136471
category: Encargos
content_hash: b966ff3da705c9d696571c05a103001555f7ed875687acca694f2477d5e142a2
fetched_at: '2026-06-28T22:46:52.373364+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Lançamento financeiro do total da pensão
type: support-article
updated_at: '2026-05-22T14:56:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11387150136471-RH-RM-FOP-Lan%C3%A7amento-financeiro-do-total-da-pens%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40666231933975) Tempo aproximado para leitura: **00:03:10 min**  
  
**Dúvida**  
No módulo **Folha de Pagamento,** como parametrizar e gerar o lançamento financeiro utilizando o Tipo 14 - Total da Pensão no TOTVS Folha de Pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
O lançamento de Tipo 14 consolida todos os valores de pensão alimentícia calculados no período. Siga as etapas abaixo para configuração e geração:  
  
**1. Parametrização do Lançamento**

Acesse o menu **Encargos | Cadastros Financeiros | Parâmetros Financeiros**.

* Crie ou edite um parâmetro e selecione o **Tipo 14 - Total da Pensão**.
* Defina as contas contábeis e demais campos conforme a regra de negócio da sua organização.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11386074950423)

#### **2. Associação ao Código de Lançamento**

Para que o sistema processe o valor, o parâmetro deve estar vinculado a um **Código de Lançamento** ativo.

* Certifique-se de que o código utilizado na geração financeira esteja corretamente apontado para o parâmetro do Tipo 14 criado no passo anterior.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11386095256727)

#### **Regra de Composição dos Valores**

Este tipo de lançamento não busca valores aleatórios; ele realiza a soma da movimentação constante na pasta de **Movimento da Pensão** **(*****Cadastros | Funcionários | Dependentes | Movimento da Pensão*****)**.

O sistema aglutina automaticamente os eventos vinculados aos seguintes **Códigos de Cálculo (CC)**:

* **CC 13:** Pensão Alimentícia
* **CC 113:** Pensão Alimentícia sobre Férias
* **CC 120:** Pensão Alimentícia sobre 13º Salário
* **CC 121:** Pensão Alimentícia sobre Participação nos Lucros (PLR)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11386169058967)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11386208991127)

**Ponto de Atenção:** Valide sempre se os valores aparecem corretamente no **Envelope de Pagamento** do funcionário antes de iniciar a integração financeira.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11387013838359)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11387034064407)

### **Procedimento de Geração**

1. Acesse a rotina de **Geração de Lançamentos Financeiros**.
2. Selecione o filtro de funcionários desejado e o respectivo **Código de Lançamento**.
3. Execute o processo e valide o log de geração.
4. O lançamento será gerado no **TOTVS Gestão Financeira (RM Fluxus)** consolidando os beneficiários conforme a parametrização.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11387051317655)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11387053782935)

Dessa forma o lançamento será gerado:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11387107817879)

**Importante:**  
Se o valor do lançamento estiver divergente, o primeiro lugar a checar é o histórico em **Dependentes | Movimento da Pensão.** Se o evento estiver no envelope, mas não constar nessa pasta, o Tipo 14 não conseguirá "enxergar" o montante para o envio ao financeiro.
