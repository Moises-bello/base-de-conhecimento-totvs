---
content_hash: 696557d7b77691a595fa5a0d7d6a05e66197614f2d9ab1d7bd43aa3378a3de23
fetched_at: '2026-06-29T00:09:24.102712+00:00'
page_id: '423937894'
product: rm
source: tdn-rm
title: Natureza Fiscal e Natureza Inversa
type: documentation
url: https://tdn.totvs.com/display/LRM/Natureza+Fiscal+e+Natureza+Inversa
version: 2
---

Quando uma Nota Fiscal Eletrônica é enviada por um fornecedor, ela contém, para cada um dos seus itens, uma natureza fiscal (CFOP) de saída, que caracteriza a operação desse fornecedor.   
Para a empresa que recebe esse documento, entretanto, deve ser encontrada a natureza fiscal (CFOP) de entrada correspondente. Essa 'Natureza Inversa' é indispensável para a criação automática de um movimento de NF-e

**Regra de Seleção da Natureza (RSN)**

Para cada movimento de NF-e a ser incluído, o sistema irá encontrar a Natureza Inversa da CFOP constante do arquivo XML.   
Para isso, é necessário saber, através das parametrizações vigentes do tipo de movimento, se o movimento a ser criado seleciona a Natureza de Operação somente para o movimento, ou se deve ser selecionada também uma Natureza para o item de movimento.   
Para ambos os casos, será utilizada em primeiro lugar a Regra de Seleção da Natureza (RSN), rotina hoje já existente e, que tem a finalidade de encontrar a Natureza de Operação baseada nas informações do movimento e parametrizações de várias tabelas tais como: Parâmetros do Tipo de Movimento, Produto, Classificação de Produto, Naturezas Fiscais, Regras de ICMS, Regras de IPI, etc..

**Seleção Automática da Natureza por Movimento**

Neste caso, deverá ser encontrada obrigatoriamente uma Natureza de Operação analítica para o movimento.  
Através dos dados do XML e das parametrizações e cadastros do sistema, a Regra de Seleçao da Natureza irá encontrar a(s) natureza(s) possível(eis), de forma que:

* Se a RSN encontrar apenas uma Natureza de Operação (CFOP) possível, o movimento de NF-e será incluído com o CFOP encontrado;
* Se a RSN encontrar mais de uma Natureza de Operação (CFOP) possível, o sistema irá verificar as opções cadastradas como Natureza Inversa da CFOP extraída do XML.

**Seleção Automática da Natureza por Item de Movimento**

Nesta situação, será realizado o mesmo procedimento já explicado anteriormente para encontrar a Natureza de Operação do movimento, com a diferença desta poder ser analítica ou sintética.   
Se for encontrada uma Natureza analítica, sua 'Raiz' (Natureza Sintética) deve ser extraída e considerada como a Natureza do movimento enquanto que a Natureza analítica será atribuída ao item.  
Caso sejam encontradas 2 naturezas sintéticas possíveis, os campos natureza 1 e natureza 2 do movimento (TMOV.IDNAT, TMOV.IDNAT2) serão preenchidos caso ambos estejam parametrizados para o tipo de movimento, mas se existirem mais de 2 naturezas sintéticas possíveis, o sistema não será capaz de resolver o conflito e, neste caso a natureza não será identificada, sendo preenchida a natureza do movimento com um CFOP de primeiro nível, ou seja, 1 ou 2 conforme a UF de origem da NF-e.  
Caso seja encontrada apenas a Natureza sintética, ela será atribuída ao movimento, e o procedimento de busca será realizado novamente para selecionar a Natureza do item.   
Para o item, a Regra de Seleção da Natureza irá considerar os dados do movimento e das demais tabelas citadas anteriormente (Parâmetros do Tipo de Movimento, Produto, Classificação de Produto, Naturezas Fiscais, Regras de ICMS, Regras de IPI, etc.).  
O sistema primeiramente executará as Regras de Seleção da Natureza, mas caso a mesma retorne mais de uma opção de CFOP para os itens do movimento, o sistema utilizará o cadastro das Naturezas Inversas.

**Natureza Inversa**

Cadastros > Natureza Fiscal > Anexos > Natureza Inversa para Importação de XML é onde deverão ser cadastradas as possíveis naturezas de operação inversas para uma determinada natureza sintética.  
Uma natureza de operação sintética, poderá ter a ela vinculada, várias naturezas de operação inversas, sejam elas sintéticas ou analíticas.  
Entre as naturezas inversas cadastradas, o usuário poderá definir 'Defaults', ou seja, registros que devem ser considerados prioritários caso existam várias naturezas possíveis para um determinado movimento.  
Este cadastro será utilizado apenas caso através da aplicação das Regras de Seleção da Natureza tenha sido encontrada mais de uma natureza inversa possível para o item. O sistema procederá da seguinte forma:

* Se apenas uma das naturezas selecionadas estiver cadastrada como 'Default', ela será utilizada para a criação de movimento;
* Se mais de uma das naturezas selecionadas estiver cadastrada como 'Default", o sistema não saberá qual Natureza Inversa escolher e o movimento será criado com o Status Inclusão via arquivo XML como 'Natureza Incompleta';
* Se apenas uma das naturezas selecionadas estiver cadastrada como Natureza Inversa, mesmo não sendo como 'Default', ela será utilizada para a criação do movimento;
* Se mais de uma das naturezas selecionadas estiver cadastrada como Natureza Inversa mas nenhuma delas é 'Default", o sistema não saberá qual Natureza Inversa escolher e o movimento será criado com o Status da Inclusão via arquivo XML como 'Natureza Incompleta';
* Se nenhuma das naturezas selecionadas estiver no cadastro de Natureza inversa, o movimento será criado com o Status da Inclusão via arquivo XML como 'Natureza Incompleta'.

É ***importante*** salientar que, o Status da Inclusão via arquivo XML 'Natureza Incompleta' não influencia no status do movimento que será criado conforme o 'Tipo de Recebimento" utilizado e os parâmetros do Tipo de Movimento gerado, ou seja, mesmo estando com esse Status da Inclusão via arquivo XML o movimento poderá gerar todas as demais integrações (financeira, contábil e de aprovações) se assim estiver parametrizado.   
Os movimentos gerados com o Status da Inclusão via arquivo XML 'Natureza Incompleta' deverão ter seus CFOP informados através de edição manual.   
Uma natureza default pode ser sintética ou analítica, entretanto, poderá haver somente uma natureza analítica default de cada 'raiz' para uma mesma natureza sintética.
