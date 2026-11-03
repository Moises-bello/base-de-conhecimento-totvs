---
content_hash: 9544488f5db8a53a324de2de5d08ffd472167f330ef8d2164fcd046ac7283183
fetched_at: '2026-06-29T00:09:21.396075+00:00'
page_id: '422545879'
product: rm
source: tdn-rm
title: Copiar Naturezas de Operação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545879
version: 11
---

Este processo possibilita os seguintes tipos de cópia:

* Entre coligadas (Naturezas globais)
* Entre filiais de coligadas diferentes (Naturezas não globais)
* Entre filiais de uma mesma coligada (Naturezas não globais)
* De uma filial de uma coligada (Naturezas não globais) para uma coligada (Naturezas globais)
* De uma coligada (Naturezas globais) para uma filial de outra coligada (Naturezas não globais)

false0lefttrue1Regras de interface da cópia1true1Origem

Informe a coligada da qual se deseja copiar. Se esta coligada trabalhar com naturezas globais o checkbox FILIAL GLOBAL será desabilitado.   
Se esta coligada trabalhar com naturezas não globais deverá ser selecionada a filial da qual deseja copiar as naturezas. Neste caso o checkbox FILIAL GLOBAL não necessita ser marcado. Caso seja na lista de naturezas a copiar serão apresentadas naturezas que tenham sido incluídas como global. Se não existirem a lista para cópia não será apresentada.  
Deverão ser selecionados os exercícios de origem e as naturezas que se deseja copiar. Quando forem copiadas somente naturezas analíticas seus níveis sintéticos deverão ser previamente incluídos ou copiados.

2Destino

Informe a coligada para a qual se deseja copiar as naturezas. Se esta coligada trabalhar com naturezas globais o campo para a escolha da filial será desabilitado. Caso contrário uma filial deverá ser selecionada obrigatoriamente. Como na origem o campo exercício é obrigatório. Se deseja informar novos códigos e descrições para as naturezas no destino marque o checkbox INFORMAR NOVOS CÓDIGOS.

2Informações sobre o processo2

O sistema consistirá somente Naturezas de nível analítico.  
Caso haja Naturezas fiscais com as mesmas regras tributárias, o sistema fará o controle de consistência de Naturezas Fiscais com mesmas regras tributárias caso os parâmetros Consiste CFOP Regras Duplicadas e Permite CFOP Regras Duplicadas estiverem habilitados. Se apenas o primeiro parâmetro estiver marcado, o sistema consistirá a existência de CFOP com mesma regra tributária e irá barrar a duplicação da mesma. Caso o segundo parâmetro também estiver marcado, será exibida apenas uma mensagem informando sobre a existência de CFOP com mesma regra tributária, permitindo duplicar a natureza. Nas duas situações o sistema estará emitindo informações em um arquivo de LOG.  
Será consistido Naturezas com mesmas regras tributárias cujo código da natureza, até o nível anterior ao analítico, seja igual ao que se deseja incluir, exemplo:

5
complete
Existe uma natureza 1.501.01 e estamos tentando incluir a 1.501.02 com mesmas regras tributárias. Neste caso o sistema consistirá. Se incluirmos a 1.502.02, o sistema não consistirá, pois o nível sintético (1.501.) é diferente do nível sintético (1.502) que se deseja incluir. Como o processo de cópia também é uma inclusão de registro estará sujeito às mesmas regras de inclusão de natureza fiscal. Naturezas que já existam no destino (pelo campo Código) não serão copiadas.
true1Regra de ICMS e IPI

Se Coligada Origem e Destino são as mesmas:

* Natureza global, ou não global e a regra é global: a natureza no destino ficará vinculada à mesma regra da origem.
* Natureza não global e regra de origem não global: busca regra de mesmo código, filial e mesmas informações fiscais.

Se Coligada Origem e Destino são diferente:

* Natureza global, ou não global e a regra é global: busca regra de mesmo código e mesmas informações fiscais.
* Natureza não global e regra de origem não global: busca regra de mesmo código, filial e mesmas informações fiscais.
2Regras Tributárias

Serão analisados os seguintes campos para a consistência das Naturezas com mesmas regras tributárias:

* Código da Coligada (Regras Tributárias não serão copiadas entre Coligadas diferentes)
* Código da Filial (se o parâmetro Natureza Global estiver desmarcado);
* Exercício;
* Código da Natureza (neste caso o sistema considera até o nível anterior ao analítico);
* Nível Classificação Fiscal; Regras de Dependência por Estado/Região, Cliente/Fornecedor, Tipo Cli/For; Empresa; Produto / Tipo de Produto;
* Regra de ICMS
* Regra de IPI
3Configuração dos Campos

Para que a cópia entre as coligadas ocorra com sucesso, os seguintes passos devem estar configurados:

* Máscara da Tabela das duas Coligadas sejam iguais, se negativo, a cópia não será processada.
* Consistirá se a mascara do Exercício Fiscal Origem e Destino são iguais, se negativo, a cópia não será processada.
* Os campos referentes às tabelas relacionadas com a tabela de natureza somente serão gravados na cópia de naturezas caso na coligada destino existam os registros constantes na coligada origem (emite aviso caso não exista).

**Campos/Tabelas copiadas:**Além dos campos da tabela de natureza serão copiados os tributos, defaults contábeis, regras de dependência e histórico.

**Erros e Avisos:**Erros Graves: Impede que o registro seja duplicado. Porém, o processo de cópia continuará, ou seja, o sistema estará tentando inserir a próxima Natureza Fiscal ou o próximo Tributo ou a próxima Conta Contábil ou Gerencial.

3Configuração dos Campos

***Atenção aos avisos***: Trata-se apenas de um aviso ao usuário, não impedindo que os registros sejam duplicados no Banco de Dados.

4Configuração dos Campos

***Atenção aos avisos***:

Deve-se utilizar o processo de cópia de natureza, este processo cópia todos os vínculos da natureza.

Não é possível usar o processo de copiar e colar com o botão direito pois ele não copia os vínculos   
necessários da operação original.
