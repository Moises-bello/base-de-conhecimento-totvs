---
content_hash: 21ffee0eeeb6d962636d52ce86dd77f3722f87f7426a91016f25aeaae79e3fe5
fetched_at: '2026-06-29T00:10:02.479482+00:00'
page_id: '452718920'
product: rm
source: tdn-rm
title: Rotinas Mensais / Anuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718920
version: 3
---

As rotinas mensais e anuais da empresa são relatórios que são necessários serem gerados ou dados atualizados de acordo com instruções do Ministério do Trabalho (MTE), Caixa Econômica Federal (CEF) e outros.  
   
**FGTS /SEFIP**  
FGTS: Fundo de Garantia por Tempo de Serviço  
SEFIP: Sistema de Recolhimento de FGTS e Informações à Previdência Social  
   
A atualização do saldo de FGTS será processada pelo sistema a partir da data do último saldo de FGTS informada. Na admissão, este campo deve ser preenchido com a data de admissão e será utilizado na atualização do saldo de FGTS a partir do mês subseqüente.  
   
A informação do saldo de FGTS incluída em 'Saldo FTGS na CEF' é disponibilizada de acordo com o último saldo disponível quando ocorrer a atualização através do módulo de Atualização de Saldo de FGTS.  
   
**Manutenção do Extrato**  
É o campo onde pode se realizar manutenções no saldo do FGTS, de acordo com mudanças, podendo ser elas por:

* Correção monetária
* Deposito mensal
* Saldo inicial
* Ajuste de saldo
* Debito/resgate/saque

poderá ser incluído no mesmo a 'data do lançamento da mudança', 'o tipo de lançamento' e o 'valor a alterar'.   
   
A informação da ocorrência do funcionários indica exposição ou não a agentes nocivos de acordo com o manual do SEFIP da Caixa Econômica Federal (CEF).  
**Atenção:**  
1. Não deverão preencher a **Ocorrência** as empresas cujas as atividades não exponham seus empregados a agentes nocivos.   
2. Para o campo ocorrência das categorias 02, 22 e 23 será permitido apenas branco, 01, 02, 03 e 04.  
3. O código 1 somente deve ser utilizado para o empregado que esteve e deixou de estar exposto a agente nocivo.  
   
Informação que indica a Categoria do Funcionário deve ser de acordo com as tabelas existentes no manual do SEFIP (fornecido pela C.E.F.).  
**Atenção:**  
1. Para a categoria 17 – Cooperado da cooperativa de trabalho deverá também criar o evento "Pagamentos para Contribuinte Individual Cooperados" com o código de cálculo 164, e lançar em sua movimentação.  
   
2. Para as Categorias 14 e 16 será necessário, também, informar a Classe de Contribuição. Observe que estas categorias somente podem ser utilizadas para recolhimentos até a competência 03/2000.  
   
3. Para as Categorias 14 e 16 será necessário, também, informar a Classe de Contribuição. Já para as categorias 11, 13, 14, 15, 16 será habilitado automaticamente pelo sistema o campo "Cadastro Contribuinte Individual".  
   
O Código de Contribuinte Individual é para prestadores de serviço pertencentes às categorias citadas no parágrafo anterior, ou seja, autônomos que não possuem vínculo empregatício. Este campo só é disponibilizado quando for selecionado funcionários com categorias 11,13,14,15 e 16 para SEFIP.   
**Observação:**  
Anteriormente, o valor do campo "Código de Contribuinte Individual" era cadastrado no campo "PIS", haja vista, que nestas categorias o PIS perde a sua função, porém agora é necessário que se cadastre o número neste campo para ser considerado no arquivo do SEFIP.  
  
**RAIS**  
Relação Anual de Informações Sociais. Informa dados para controle governamental com determinados objetivos como: controle de atividade trabalhista no País, estatísticas do trabalho e informações do mercado de trabalho às entidades governamentais. O site www.rais.gov.br disponibiliza estas e outras informações sobre esta relação.  
   
Os vínculos relacionados na tabela dinâmica referente a este campo estão com os códigos do Folha de Pagamento e serão mapeados internamente para os códigos de vínculos aceitos pelo validador do arquivo de RAIS.  
   
Os itens da tabela cor/raça (PCORRACA) estão incluídos nas tabelas dinâmicas em Cadastro de Tabelas Dinâmicas, sendo que os códigos relacionados abaixo serão mapeados internamente para os códigos aceitos pelos validadores dos arquivos de RAIS e CAGED:  
Ø  Cor/Raça 0 - Indigena para 1 - Indigena Ø  Cor Raça em branco para 9 - Não informado.   
   
A informação do deficiente utilizada pela RAIS e CAGED será mapeado conforme abaixo:  
   
RAIS e CAGED  
   
O funcionário não é Portador de Deficiência quando, no Folha de Pagamento **não** for marcada nenhuma deficiência.  
1 - Física   
2 - Auditiva   
3-  Fala   
4 - Visual   
5 - Mental   
6 – Reabilitado (BR)  
7-  Intelectual   
8-  Preenche cota de PCD  
**Atenção:**  
O campo "Preenche cota" é utilizado na geração do eSocial leiaute S-2100, S-2200 e S-2205.   
   
   
**Atenção:**  
O item Reabilitado é prioritário, uma vez marcado não são verificadas as outras deficiências levando '6 - reabilitado' para os relatórios.   
Para adicionar observações quanto à deficiência e reabilitação, estas observações precisam ser feitas no "Cadastro de Pessoas/Informações adicionais.  
   
**Número do Processo Judicial**  
Preencher quando na data de admissão a idade for menor que 14 anos, ou se idade for maior que 14 e menor que 16 e 'Tipo de Funcionário' diferente de 'Aprendiz'.  
Este campo é utilizado na geração do eSocial leiaute S-2100 e S-2206.  
   
   
**Dados Contábeis**   
São informações primordiais para a contabilização, quando se usa a integração contábil por funcionário.  
Os Códigos de integração contábil ou agrupadores devem ser criados (*veja abaixo onde cadastrá-los)* de acordo com o nível de detalhamento que a contabilidade exige. Uma vez criado, deve-se atribuir a cada funcionário o seu código. Se a contabilidade precisar de um nível de detalhamento tal que não seja possível determinar pelos agrupamentos em seção ou centro de custo, então provavelmente faz-se necessário utilizar a integração contábil por funcionário. Vale lembrar que, a contabilização por funcionário pode diminuir um pouco a performance do sistema no momento da contabilização. Esta integração só será realizada se os campos *integração contábil por funcionário* para conta contábil estiverem marcados no *cadastro de eventos* e/ou no *cadastro de encargos.*  
   
**Referência:**  
Tabela  
PFUNC  
Campo  
INTEGRCONTABIL  
Onde cadastrar  
Cadastro de Tabelas Dinâmicas - Código INTCONTFUN   
   
Os dados da integração gerencial indicam um agrupador de funcionários utilizado na *Contabilização por funcionário*, para a visão gerencial. Deve ser utilizado em casos onde a empresa necessita contabilizar por funcionário e faz contabilização separada entre contábil e gerencial. Os Códigos de integração gerencial ou agrupadores devem ser criados (*veja abaixo onde cadastrá-los)* de acordo com o nível de detalhamento que a visão gerencial exige. Uma vez criado, deve-se atribuir a cada funcionário o seu código. Da mesma forma que a integração contábil, deve-se avaliar primeiramente se a contabilização por seção ou centro de custo é mais apropriada. Esta integração só será realizada se os campos *integração contábil por funcionário* para conta gerencial estiverem marcados no *cadastro de eventos* e/ou no *cadastro de encargos.*  
   
**Referência:**  
Tabela  
PFUNC  
Campo  
INTEGRGERENCIAL  
Onde cadastrar  
Cadastro de Tabelas Dinâmicas - Código INTGERFUNC   
**Exemplo:**  
Supondo que a contabilidade queira contabilizar a folha de pagamento por cargo, sendo para efeitos contábeis o cargo de coordenador é idêntico ao dos engenheiros e supervisores, enquanto que na visão gerencial os cargos de coordenadores são idênticos aos dos chefes, gerentes e diretores. Os códigos de integração seriam assim:  
   
FUNCIONÁRIOS COM CARGOS DE:  
INTEGRAÇÃO CONTÁBIL  
INTEGRAÇÃO GERENCIAL  
Assistentes, Auxiliares, Técnicos, Operadores  
01  
15  
Engenheiros, Supervisores  
02  
18  
Coordenadores  
02  
20  
Chefes, Gerentes, Diretores  
03  
20  
   
   
   
   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários   
 [www.caged.gov.br](http://www.caged.gov.br/)  
 [www.caixa.gov.br](http://www.caixa.gov.br/)  
 [www.mte.gov.br](http://www.mte.gov.br/)  
 [www.rais.gov.br](http://www.rais.gov.br/)

|  |  |
| --- | --- |
|  | Veja Também |

---

Veja também um exemplo sobre categoria 15 Exemplo
