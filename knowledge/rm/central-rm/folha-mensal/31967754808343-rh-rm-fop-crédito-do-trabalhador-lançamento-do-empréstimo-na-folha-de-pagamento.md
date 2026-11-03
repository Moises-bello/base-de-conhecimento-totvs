---
article_id: 31967754808343
category: Folha Mensal
content_hash: f609eb88ffea56264d5bc4ff14277c5e159da713956041bb3daba7c80c1aa115
fetched_at: '2026-06-28T22:46:58.122048+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador -  Lançamento do Empréstimo na Folha
  de Pagamento
type: support-article
updated_at: '2026-05-26T18:31:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31967754808343-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Lan%C3%A7amento-do-Empr%C3%A9stimo-na-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31967754798359) Tempo aproximado para leitura: **00:03:58 min**  
  
**Dúvida**

Com a implementação do novo modelo de Crédito do Trabalhador, tornou-se necessário adequar os procedimentos de lançamento dos empréstimos na folha de pagamento. Esta documentação tem como objetivo orientar os usuários do sistema RM quanto aos passos necessários para registrar corretamente os novos empréstimos, garantindo o correto desconto em folha e a conformidade com as novas regras estabelecidas pelas instituições financeiras envolvidas. Diante disso, como será o lançamento do empréstimo na folha de pagamento?

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

* 12.1.2406.277
* 12.1.2410.229
* 12.1.2502.145
* 12.1.2506 e superiores

**Solução**

O lançamento do valor referente ao empréstimo Crédito Trabalhador no movimento do funcionário deverá ser realizado por meio do lançamento via Grupo de Eventos, acessado pelo menu **Folha Mensal | Lançamentos | Grupo de Eventos:**

**IMPORTANTE:***É importante destacar que não haverá controle automático caso o valor seja inserido manualmente, seja via Entrada de Dados ou diretamente no envelope do funcionário. Nesses casos, o usuário será responsável por realizar todas as atualizações necessárias de forma manual.*

Caso o usuário queira lançar o provisionamento do valor do empréstimo no adiantamento, será necessário marcar o parâmetro: **“Lançar Provisionamento do Empréstimo do Crédito do Trabalhador eSocial”**, no momento do  lançamento do adiantamento via Grupos de Eventos.

No momento do lançamento da folha de pagamento via Grupos de Eventos, o usuário deverá selecionar os seguintes parâmetros para lançar o empréstimo importado anteriormente:

* **Lançar Empréstimos:** *Todos*
* **Tipo de Empréstimo:***Selecionar o tipo cadastrado correspondente ao Crédito do Trabalhador.*  
    
  *Não há necessidade de informar os eventos de empréstimo na aba "Eventos do Grupo" do Grupo de Eventos.*

Após o lançamento do valor no movimento do funcionário, a alteração poderá ser consultada em dois locais:

* **Funcionário | Anexos | Folha de Pagamento | Empréstimos | Aba Empréstimos** - Detalhes em: [Empréstimos Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=452719572)
* **Funcionário | Anexos | Folha de Pagamento | Empréstimos | Aba Descontos de Empréstimos** - Detalhes em: [Empréstimos de Funcionários - Descontos de Empréstimos](https://tdn.totvs.com/pages/viewpage.action?pageId=937695241)

**IMPORTANTE:**

O cálculo da margem consignável do funcionário será sobre o líquido do movimento, ou seja, todos os proventos menos os descontos, mas o usuário poderá informar quais eventos quer considerar para a margem consignável do desconto do empréstimo da modalidade "Crédito do Trabalhador eSocial" usando o anexo Eventos Remuneração Crédito do Trabalhador do cadastro de funcionários ou o Eventos do Crédito do Trabalhador em folha normal no parametrizador.

**ATENÇÃO:** Os eventos inseridos nesses cadastros têm prioridade sobre o líquido do movimento, por exemplo, se inserir o evento de dias trabalhados no Eventos do Crédito do Trabalhador em folha normal no parametrizador então em**todos os funcionários que tiverem o empréstimo da modalidade "Crédito do Trabalhador eSocial"** será considerado na base consignável como dias trabalhados menos INSS e IRRF.

**DICA:** Para exemplos de utilização do novo empréstimo, veja a documentação: [RH - RM - FOP - Crédito do Trabalhador - Exemplos de Utilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31969117356439-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Exemplos-de-Utiliza%C3%A7%C3%A3o)

* [RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
* [FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
