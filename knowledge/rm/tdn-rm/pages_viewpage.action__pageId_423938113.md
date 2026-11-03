---
content_hash: d6848ea691bc53e6e15a7d4e5700efda739607aea3fedd46df871ff62785b8e5
fetched_at: '2026-06-29T00:09:25.308222+00:00'
page_id: '423938113'
product: rm
source: tdn-rm
title: Movimentos (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938113
version: 16
---

**Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

O TOTVS Gestão de Estoques, Compras e Faturamento trabalha com o conceito de Movimentos para identificar todas as movimentações fiscais e não fiscais da empresa, ou seja, todos os processos que envolvem as rotinas de compras, vendas, transferências, devoluções de compra/venda de mercadorias e/ou serviços, implantação de saldos, estes processos são todos cadastrados através dos Movimentos.   
Por sua vez, estes dados, previamente cadastrados, otimizam as operações e rotinas de uma empresa, proporcionando correta apuração e veracidade das informações cadastradas.   
É através do Movimento que são realizadas todas as integrações com os demais aplicativos TOTVS – uma grande vantagem no processo de rastreabilidade da operação principalmente para atender a área contábil, financeira e fiscal da empresa.   
Os movimentos do TOTVS Gestão de Estoques, Compras e Faturamento trabalha com a seguinte divisão em grupos:

* Grupo 1.1 – Corresponde aos movimentos de Solicitação de Compras e Ordem de Compra; os mesmos podem gerar movimentos para o Grupo 1.1. e 1.2;
* Grupo 1.2 – Corresponde aos movimentos de Compras e Devolução de Vendas;
* Grupo 2.1 – Corresponde aos movimentos de Pedido de Venda; os mesmos podem gerar movimentos para o Grupo 2.1, 2.2 e 3.1;
* Grupo 2.2 – Corresponde aos movimentos de Vendas e Devolução de Compras;
* Grupo 3.1 – Corresponde aos movimentos de Transferência;
* Grupo 4.1 – Corresponde aos movimentos referentes ao processo de ajuste de estoque.

Lembramos que esta iteração entre os grupos de movimentos dependem de parametrizações específicas existentes em cada movimento.   
E ao faturar/receber algum movimento o status do mesmo irá ser alterado de acordo com o processo em questão.   
O TOTVS Gestão de Estoque, Compras e Faturamento divide os Tipos de Movimentos nos seguintes Menus:

1. Estoque;
2. Compras;
3. Vendas;
4. Outras Movimentações.

Para que um Tipo de Movimento fique na aba Compras, por exemplo, é necessário que ele tenha uma certa Classificação de Movimento, que pode ser definida na aba Mov – Identificação dos parâmetros do Tipo de Movimento.   
E em algumas dessas classificações, existem parametrizações preliminares que devem ser feitas.  
Chamamos de Tipo de Movimento o agrupamento de regras que define as atividades que compõem um determinado processo de negócio.   
O Tipo de Movimento define as regras fiscais, contábeis, financeiras, de estocagem e gerenciais, indicando ainda se a operação é de entrada ou saída.  
Todos os processos de negócio tratados no módulo TOTVS Gestão de Estoque, Compras e Faturamento, utilizam o Tipo de Movimento para inclusão das informações, como podemos mostrar através da figura abaixo: Principais Processos Existentes no TOTVS Gestão de Estoques, Compras e Faturamento.

**Gestão de Compras**  
  
**Gestão de Vendas**  
 

**Observação:**

Antes de iniciar a inclusão de movimentos, certifique-se de que já determinou todos os parâmetros para cada tipo de movimento que será utilizado.   
Estes são informados através do menu Opções-Parâmetros/Tipos de Movimentos.   
É de suma importância a parametrização correta do tipo de movimento, pois dependendo de sua parametrização em sua execução o movimento pode retornar diferentes resultados induzindo a análises incorretas quanto as suas informações.   
Se a opção do saldo está parametrizada para barrar saldo menor que saldo zero, ao tentar excluir um movimento que tenha afetado o saldo tornando-o negativo, o sistema irá consistir e não permitirá excluir a movimentação.  
***Atenção!*** Abaixo citamos todas as funcionalidades, anexos e processos, que regem o cadastro de Movimentos. Ressaltamos que nem todas estas funcionalidades estarão presentes em alguns grupos de movimentos mencionados anteriormente, pois são processos específicos pertinentes em cada grupo dos mesmos.

**Divisão do Movimento por Abas**

Para facilitar o preenchimento e identificação das informações dentro do movimento o mesmo foi dividido em abas. Dentro de cada aba são agrupadas as informações relativas a algum processo do sistema como por exemplo: na aba integração opção Financeira são exibidas informações relativas a geração de informações no processo Financeiro. Estas opções, também, são apresentadas de acordo com as parametrizações específicas de cada movimento.

### Repositório de Arquivos

A partir da versão 12.1.2402 a visão de Movimento passa a exibir a nova funcionalidade [Repositório de Arquivos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=784778828).

---
