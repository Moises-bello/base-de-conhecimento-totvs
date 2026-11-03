---
content_hash: 40de0b8b271092dca315928fdfbf668f5be1e0f417ecff669bc63f2598f9dbfb
fetched_at: '2026-06-29T00:09:48.769281+00:00'
page_id: '435105227'
product: rm
source: tdn-rm
title: Aditivo de Alteração de Valor de Parcela Global (Revitalização)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105227
version: 3
---

Com a **Revitalização** do TCGI, agora é possível de se utilizar a funcionalidade do **Aditivo de Alteração de Valor de Parcela Global**, para se aditivar várias vendas que atendam a uma determinada condição, de uma só vez.

Esta funcionalidade permite inserir, alterar ou remover valores/componentes nas parcelas de mais de uma venda, simultaneamente. Permitindo, por exemplo a inserção de valores de Taxa de Limpeza, Taxa de IPTU, Seguro, aplicação de Descontos, entre outros, que sejam comuns a um determinado grupo de vendas, de forma ágil e simples.

**Tela Inicial:**  
Na tela inicial deste **Aditivo de Alteração de Valor de Parcela Global** são exibidos os seguintes campos:  
   
**Descrição Aditivo:** Assim como na tela de aditivos padrão, informe um texto para descrever a finalidade do aditivo. Este campo é obrigatório.

**Usar Data Agendamento:** Quando o Ambiente do RM estiver configurado em **[3 camadas](https://tdn.totvs.com/display/LRM/Ambiente+3+Camadas)** será possível utilizar o [*Agendamento de Processos*](https://tdn.totvs.com/pages/viewpage.action?pageId=270085915#Configura%C3%A7%C3%A3odoJobservernaLinhaRM-1.1AgendamentodeProcessos)  para executar o aditivo. Esse campo é prioritário ao campo *Data Aditivo*. Os parâmetros que definem o [congelamento das parcelas](https://tdn.totvs.com/pages/viewpage.action?pageId=435105213) também podem ser utilizados por esse aditivo.

**Data Aditivo:** Define qual a Data Base da efetivação do aditivo. Esta data tem importância para definir qual a data do [Reajuste das Parcelas das Vendas](https://tdn.totvs.com/pages/viewpage.action?pageId=546260610), caso o [Reajuste Online](https://tdn.totvs.com/pages/viewpage.action?pageId=633072776) esteja ativo.

**Ação do Componente na Parcela:** Este campo define o comportamento do Novo Componente inserido na parcela quando o processo de aditivo verificar que já existe um Componente deste mesmo Tipo nas parcelas selecionadas. Atualmente existem as seguintes ações:

* **Manter o valor existente** - Existindo o Novo Componente nas parcelas, o valor do componente já existente será mantido, ou seja não será alterado. Caso não exista, o Novo Componente será incluído com o valor definido no aditivo;
* **Sobrepor o  valor existente** - Ao verificar as parcelas aditivadas, caso exista Componente selecionado nelas, o valor desse Componente será substituído pelo novo valor definido para este Componente, informado no aditivo. Caso não exista, o Novo Componente será incluído na parcela com o valor definido;
* **Somar ao valor existente** - Caso o Novo Componente já esteja presente em alguma das parcelas selecionadas, os valores deles, será somado. Caso não exista, o Novo Componente será acrescentado à composição da parcela.
* **Remover o componente** - Neste caso, o sistema irá zerar o valor do Componente selecionado no campo Componente, descrito abaixo, mantendo este componente na composição da parcela (mesmo com o valor zerado);

Importante:

As **Regras de Negócios** do *TOTVS Gestão Financeira* e do TCGI definem que o Componente removido, pela ação acima, na verdade tem o seu valor zerado, continuando na composição da parcela para fins de histórico.

**Componente:** Selecione na listagem exibida o componente que terá seu valor alterado na parcela. Não será possível escolher os Componentes do [Tipo](https://tdn.totvs.com/display/LRM/Plano+-+Tipos+de+Componentes) Principal, ou seja, componentes que geram parcela (como Sinal, Mensal, Anual, etc.). Também não poderá escolher componentes de Juros e Correção Monetária exceto os do T[ipo](https://tdn.totvs.com/display/LRM/Plano+-+Tipos+de+Componentes) Antes Aditivo.  
   
**Valor:** Este será o valor que será incluído na parcela para o Componente escolhido.  
   
**Fórmula de Cálculo:** Caso desejar, será possível escolher uma fórmula para calcular o valor do componente da parcela, esse campo é prioritário ao campo valor.   
   
  
  
   
**Seleção de vendas:**  
Nessa mesma tela será possível escolher quais vendas receberão o novo valor de componente. Essa visão é idêntica à tela de contrato de vendas, sendo possível realizar filtros e processos da venda. A diferença é que nessa visão aparecerão as vendas de **todas as coligadas**.  
   
**Seleção de parcelas:**  
Nessa tela aparecerão todas as parcelas em aberto ou parcialmente baixadas de todas as vendas que foram selecionadas na tela anterior.  
   
**Agendamento (Ambiente 3 Camadas):**  
Nessa tela será possível realizar o [agendamento do processo](https://tdn.totvs.com/pages/viewpage.action?pageId=270085915#Configura%C3%A7%C3%A3odoJobservernaLinhaRM-1.1AgendamentodeProcessos), informando a data, o horário da execução e a recorrência do processo.  
   
   
Após a execução do processo, será exibido um log com a descrição de todas as vendas e parcelas afetadas pelo processo.

Para maiores informações, acesse a página a seguir:  
   
Aditivos
