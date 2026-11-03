---
content_hash: 3d99952c52b9cabc68f4d221253bc24236b9701155e423d94ae59a9f6e11441f
fetched_at: '2026-06-29T00:09:22.166662+00:00'
page_id: '422545982'
product: rm
source: tdn-rm
title: Natureza de Operação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545982
version: 63
---

No sistema de Gestão Fiscal as regras de tributação do ICMS e do IPI são definidas no cadastro de Naturezas de Operação.   
Neste cadastro, devem ser registradas as operações realizadas pela empresa, com suas características, os tributos incidentes, as situações tributárias relacionadas, etc.   
Este é um dos cadastros mais importantes do TOTVS Gestão Fiscal.

Para os contribuintes do ICMS e do IPI, devem ser cadastrados códigos de Naturezas de Operação que atendam as exigências do Regulamento do ICMS (RICMS).   
Como esta codificação pode sofrer alteração pelo Fisco, o sistema trabalha com o conceito de vigência para o cadastro de naturezas. Esta vigência é controlada pelo cadastro de Exercícios através do menu Cadastros | Tabelas Auxiliares | Exercícios.

Para cada exercício deve ser definida uma máscara para o cadastro de naturezas de operação.   
Antes de se iniciar o uso desse cadastro, é necessário que as parametrizações relacionadas já tenham sido feitas pelo menu Ambiente | Parâmetros | TOTVS Gestão Fiscal | 03.02 - Apuração de Tributos | 03.02.01 - ICMS | etapa 16 - Natureza de Operação 1/2.

Dentre os parâmetros de naturezas de operação, destacam-se:

false1true1Identificação

**Identificação:**Nesta pasta serão informados os campos que identificarão a natureza fiscal.

**Tipo Natureza:**Determina se a natureza é de Entrada ou Saída

**Fiscal:**Habilitando este campo, as informações dos lançamentos efetuados com esta natureza serão levadas para as rotinas fiscais do ICMS e do IPI e também para os livros fiscais de entrada e saída. Havendo informações que não deverão constar nem nas rotinas de ICMS/IPI e nem nos livros fiscais, deverá ser utilizada uma natureza com este campo desmarcado.

***Importante!!!***Para naturezas que não são fiscais, não estará disponível a opção de vincular Regras de ICMS e de IPI.

**Origem/Destino:**

* **Dentro**: Indica as operações realizadas com emitente/destinatário situado dentro do estado da empresa (filial);
* **Fora do Estado**: Indica as operações realizadas com emitente/destinatário situado fora do estado da empresa (filial);
* **Exterior**: Indica operações com emitente/destinatário situado no exterior.

**Natureza Global:**Ao habilitar este parâmetro, irão ser definidas as naturezas de operação para todas as filiais de uma coligada, caso todas as filiais estejam estabelecidas no mesmo estado. Com o parâmetro desabilitado, as naturezas de operação passarão a ser definidas para cada filial. Para as naturezas não globais, será necessário definir os exercícios e as respectivas máscaras para cada filial.

* **Consiste Regras CFOP Duplicado:**Com este parâmetro habilitado, não será permitida a inclusão de mais de uma natureza de operação com as mesmas características tributárias.
* **Permite Regras CFOP Duplicado:**Neste caso, o sistema irá emitir uma mensagem de aviso quando for incluída uma natureza de operação com as mesmas características tributárias de outra já existente, e permitirá sua gravação no sistema.

***Importante!!!***O sistema consiste apenas naturezas de nível analítico. O sistema consiste naturezas com as mesmas regras tributárias cujo código, até o nível anterior ao analítico, seja igual ao que se esteja tentando incluir, exemplo:

Já existe a natureza 1.501.01 e estamos incluindo a natureza 1.501.02, com as mesmas regras tributárias. Neste caso, o sistema consistirá. Já se incluirmos a natureza 1.502.02, o sistema não fará a consistência, uma vez que o nível sintético (1.501) e diferente do nível sintético (1.502) que se deseja incluir.

Alguns dos campos considerados nessa consistência: Código da Natureza, Regras de Tributação, Tipo Tributação ICMS, Tipo Tributação IPI, Base Red. ICMS (%), Base Red. ICMS (ST), dentre outros.

2Regras de Tributação

**Regras de Tributação**

Nesta pasta serão definidos os critérios de dependência para as naturezas de operação. Estão disponíveis no sistema os seguintes grupos:

Grupos

|  |  |
| --- | --- |
| **Grupo A** | Região |
| Estado |
| Municípios |
| Grupo de Municípios |
| **Grupo B** | Empresa |
| Cliente / Fornecedor |
| Tipo Cliente / Fornecedor |
| **Grupo C** | Produto |
| Tipo de Produto |
| Procedência |
| **Grupo D** | Tipo de Operação |

***Observações*:**

* Elementos do Grupo A, exceto Estado, se relacionam com quaisquer elemento dos Grupos B, C e D.
* Quando for incluída uma regra com Cliente / Fornecedor, automaticamente será incluída também a regra Cliente Fornecedor Contribuinte, com a opção Não Depende selecionada.

3leftRegião

**Região**

A regra de Região irá afetar na seleção da Natureza do movimento e do lançamento.

ExemploEstado

**Estado**

A regra de Estado irá afetar na seleção da Natureza do movimento e do lançamento.

ExemploGrupo de Município

**Grupo de Município**

A regra de Grupo de Município irá afetar na seleção da Natureza do movimento e do lançamento.

ExemploEmpresa

**Empresa**

A regra de Empresa irá afetar na seleção da Natureza do movimento e do lançamento.

ExemploCliente/Fornecedor

**Cliente/Fornecedor**

A regra de Cliente/Fornecedor irá afetar na seleção da Natureza do movimento e do lançamento.

ExemploTipo Cliente/Fornecedor

**Tipo Cliente/Fornecedor**

A regra de Tipo Cliente/Fornecedor irá afetar na seleção da Natureza do movimento e do lançamento.

ExemploProduto

**Produto**

A regra de Produto irá afetar na seleção da natureza do item do movimento.

ExemploTipo de Produto

**Tipo Produto**

A regra de Tipo Produto irá afetar na seleção da natureza do item do movimento e no lançamento.

OBS: No lançamento, a regra de seleção de natureza pelo Tipo de Produto, só funciona se os campos Tipo de Produto e Produto estiverem parametrizados para ser editados no Lançamento Fiscal.

Caminho: Gestão Fiscal |Parametros| TOTVS Gestão Fiscal | Escrituração | Dados Gerais 2/2 | Edita Produto

ExemploRegra Procedência

**Procedência**

A regra de Procedência não afeta na inclusão de outra regra de tributação de mesmo grupo, ou seja, pode-se incluir uma procedência independente do Produto e do Tipo de Produto.

A regra de Procedência irá afetar na seleção da natureza do item do movimento. De acordo com opção de procedência selecionada no item (movimento), irá filtrar a Natureza que possui essa Regra de Tributação Procedência vinculada.

Exemplo

         

Vídeo How To

648432

Tipo de Operação

**Tipo de Operação**

A regra Tipo de Operação irá afetar na seleção da natureza do item do movimento. De acordo com opção de Tipo de Operação selecionada na tabela do item (movimento), irá filtrar a Natureza que possui essa Regra de Tributação Tipo Operação vinculada.

Mas caso exista regra de Tipo de Tributação informada no cadastro do produto que está sendo utilizado no movimento,  
o sistema irá selecionar a CFOP que possua o Tipo de Operação conforme classificação do produto e não a CFOP que tem a classificação do item do movimento.

O campo Tipo de Tributação do cadastro do produto/serviço está localizado no Modulo Cadastro| Produto | Detalhes| Classificação.

ExemploVídeo How To

648432

  
Peso dos Grupos

Cada Regra de Tributação possui um peso associado, ou seja, para cada regra selecionada na natureza, esta se tornará mais ou menos seletiva.   
No momento da inclusão do lançamento fiscal, dependendo da regra de seleção de naturezas parametrizada, o sistema irá listar as naturezas de maior peso, ou seja, as mais seletivas.

| Grupo | Dependência | Peso |
| --- | --- | --- |
| **A** | Região | 10 |
| Estado | 100 |
| Grupo de Municípios | 100 |
| **B** | Empresa | 100 |
| Cliente/Fornecedor | 100 |
| Tipo | 10 |
| **C** | Produto | 100 |
| Tipo de Produto | 10 |
| Procedência | 10 |
| **D** | Tipo de Operação | 10 |

**Regra de Tributação utilizando dados de Coleta e Entrega**

O parâmetro "Determinação da Origem/Destino de CTRC" no TOTVS Gestão Fiscal. Ele definirá quais campos da nota fiscal serão considerados para determinação da Origem/Destino da Operação nos casos de CTRC. O parâmetro pode ser encontrado na tela de parâmetros do sistema através do caminho "03.01 - Identificação de Regras de Apuração | ICMS | Lançamento Fiscal 5/7" e apresentará ao usuário as seguintes opções:

1. Coleta/Entrega
2. Remetente/Destinatário

**Exemplo:**Para Lançamento Fiscal do tipo CTRC, o sistema irá selecionar as Naturezas de Operação da seguinte forma:

**Lançamentos de Entrada**:

* O sistema verifica o estado da Filial declarante e a UF da Coleta/Remetente
* Se forem iguais, a natureza será 1.xxx. se forem diferentes a natureza será 2.xxx.

**Lançamentos de Saída**:

* Se a UF da Coleta/remetente= UF da Entrega/Destinatário => Natureza Interna 5.xxx
* Se a UF da Coleta/remetente <> UF da Entrega/Destinatário => Natureza Inter Estadual 6.xxx
* Se apenas o campo UF Entrega estiver preenchido o sistema usará a seguinte regra de seleção da Natureza:

1. Se a UF de Entrega tiver sido informado, considera o estado da UF da Entrega/Destinatário (Lançamentos de Saída).
2. Caso a UF de Entrega não tiver sido informado, considera a UF do C.F Origem/Destino.
3. Caso o C.F Origem/Destino não tiver sido informado, considera a UF do Emitente/ Destinatário da Nota Fiscal.

Baseando-se neste parâmetro e nas regras aplicadas a ele serão exibidas as naturezas que poderão compor os lançamentos de entrada e saída do módulo TOTVS Gestão fiscal.   
Vale ressaltar que as regras mencionadas acima  também são consideração durante a seleção de natureza existente no cadastro de movimentos do TOTVS Gestão de Estoques, Compras e Faturamento.

**Tabelas de Classificação**

No parâmetro **[Tipo de Operação](https://tdn.totvs.com/x/iTcwJg)** pode ser definida uma tabela para classificar a operação e ser relacionada a RSN (Regra de Seleção de Natureza)

***Observações TOTVS Gestão de Estoque, Compras e Faturamento*:**Quando for informado uma natureza de operação analítica no movimento e este mesmo for escriturado, vai ser preenchida a mesma Natureza na situação tributária do lançamento fiscal, independente da regra de tributação implementada.Desabilita regra de seleção de natureza

Para os tipos de seleção "Completa" e "Avançada" é habilitada a opção [Permite Editar Rsn do Lançamento](https://tdn.totvs.com/pages/releaseview.action?pageId=649997959).

3Tributação ICMS/IPI

**Tributação ICMS/IPI**

Nesta pasta serão associadas regras de ICMS / IPI, que são incluídas no menu Cadastros | Naturezas de Operação | Regras de ICMS e Regras de IPI. O usuário deverá cadastrar as regras de acordo com as operações realizadas pela empresa e associá-las a natureza de operação.

Maiores Informações

* [Regra de ICMS](http://tdn.totvs.com/display/LRM/Regra+de+ICMS)
* [Regra de IPI](http://tdn.totvs.com/display/LRM/Regra+de+IPI)

**Código de Antecipação Tributária**

De acordo com o Decreto nº 44.406, de 16/11/2006, este campo poderá assumir os seguintes valores:

1. Pagamento de substituição tributária efetuada pelo destinatário, quando não efetuada ou efetuada a menor pelo substituto.
2. Antecipação tributária efetuada pelo destinatário apenas como complementação do diferencial de alíquota.
3. Antecipação tributária com MVA (Margem de Valor Agregado), efetuada pelo destinatário, encerrando a fase de tributação.
4. ICMS pago na importação.
5. Branco – Substituição tributária informada pelo substituto ou pelo substituído que não incorra em nenhuma das situações anteriores.
4Outros Dados

**Outros Dados**

**Tipo de Devolução:**Indica se a operação é de devolução, transferência ou normal.

**Tipo de Operação:**Indica se a operação é de Ativo Imobilizado, Consignação ou Outros.

**Tipo da Natureza:**Informe, de acordo com a lista de opções apresentada, qual a característica de cada natureza . Esse campo é utilizado nas seguintes rotinas: DIPI / DAPI / DIEF / GIM RN / Sintegra PR.

**Código da Natureza Inversa:**Deve ser informada a natureza inversa a ser utilizada nas operações de transferência ou devolução.

**Código da Natureza POEB:** Deve ser informada a natureza que será utilizada nas operações com POEB.

**Outros:**

**Detalhe Oper. Não Especificadas:**Informar de acordo com a lista de opções apresentada, qual o detalhamento das Operações Não Especificadas:

Oper. Não Especificadas

| Código | Conteúdo |
| --- | --- |
| 0 | Nenhuma |
| 1 | Não-Incidência do ICMS |
| 2 | Industrialização/Conserto |
| 3 | Demonstração |
| 4 | Exposição ao público/Amostra |
| 5 | Suspensão de ICMS |
| 6 | Armazém Geral/Depósito Fechado |
| 7 | Acondicionamento/Embalagens |
| 8 | Amostra Grátis/Brindes/Doação |
| 9 | Operações não dedutíveis |

Conforme determinação legal, a edição deste campo somente será feita para os Códigos de Naturezas Fiscais a fim de identificar a Operação no que diz respeito a deduções para o cálculo da Receita Bruta ( X.99 / 1.95 / 1.96 / 2.95 e 2.96 / X.99 / 5.96 / 5.97 / 6.96 / 6.97.

Para as Naturezas baseadas na nova codificação fiscal (Ajuste SINIEF 07 de 28/09/2001), este campo será habilitado para as Naturezas cujo 2º nível é igual a #.901; #.902; #.949.

Este campo também será utilização na geração dos registros tipo 13,40 e 92 da DMA estado da Bahia

A informação deste campo é de extrema importância para a correta geração do arquivo DFC-GI00.TXT e DMA - Apuração ICMS da Bahia

**Tipo de Receita:**Para lançamentos/Movimentos que utilizam código de modelo de documento, podendo informar no cadastro da Natureza em outros dados, qual será o tipo de receita ar ser gerado. Essa informação será trazida como padrão para o campo Tipo de Receita no Movimento/Lançamento, podendo ainda ser editado conforme a necessidade.

Relativo a Operação

| Código | Relativo a Operação |
| --- | --- |
| 06 | Conta de Energia Elétrica |
| 21 | Nota Fiscal de Serviço de Comunicação |
| 22 | Nota Fiscal de Serviço de Telecomunicação |
| 28 | Nota Fiscal/Conta de Fornecimento de Gás |
| 29 | Nota Fiscal/Conta de Fornecimento d’água Canalizada |

O campo **Tipo** **Receita** tem as seguintes opções:

Indicadores

|  |  |
| --- | --- |
| **Indicador do Tipo de Receita** | |
| 0 | Receita própria – Serviços Prestados |
| 1 | Receita própria – Cobrança de Débitos |
| 2 | Receita própria – Venda de Mercadorias |
| 3 | Receita própria – Venda de Serviço pré-pago |
| 4 | Outras receitas próprias |
| 5 | Receitas de terceiros (co-faturamento) |
| 9 | Outras receitas de terceiros |

Caso seja selecionado as **opções 5 e 9** será habilitado no movimento (Na Integração Fiscal) /Lançamento (Aba Outros Dados do Item) o campo **Código Terceiro**, campo **obrigatório**, onde pode ser selecionado um Cliente/Fornecedor cadastrado. Essas informações serão utilizadas na geração do SPED Fiscal nos registros C500, C510, C600 (Perfil B), D500, D510, D600 (Perfil B) e sendo obrigados nos campos 1500 e 1510 no convênio 115/03. Ao informar tipo de receita 1, 5 ou 9 não deve haver tributação para os registros D500 e D510, informando uma regra de ICMS de tipo outros.

5Integrações

**Integrações:**Nesta pasta serão definidas as integrações entre os módulos de Gestão Fiscal, Gestão Contábil e Gestão de Estoque e Faturamento.

**Default´s Contábeis:**Serão informadas as contas contábeis que se aplicam a natureza de operação, para integração com o módulo de Gestão Contábil.

**Controla Valor Contábil do Lançamento:**Esta opção permite que no momento da inclusão de lançamentos dessa natureza, o sistema faça a consistência entre os valores de Débito / Crédito da tela de contabilização do lançamento com o valor contábil do mesmo. Havendo divergência entre esses valores, o usuário não poderá sair da tela de contabilização até que a diferença seja acertada.

5Campos Opcionais6Remessa7Dados C. Civil

**Dados da Construção Civil**

Devem ser gravadas nesta aba as informações referentes às notas relacionadas aos materiais e subempreitadas da construção civil. Estas informações são utilizadas para a geração de Rotinas Legais Municipais. Deve ser verificada a necessidade de preenchimento de acordo com o Estado/Município de cada Filial.

***Dica:***Essa informação é de fundamental importância para que o sistema de Gestão Fiscal possa gravar os valores relativos aos Outros Tributos, controlar a incidência destes e ainda contabilizá-los automaticamente, no momento da inclusão dos lançamentos fiscais.

8Dispositivo Legal

**Dispositivo****Legal:**No campo Dispositivo Legal deverá ser informada a Norma Legal relacionada com o tipo de tributação da natureza de operação e que deverá ser impressa no campo de Observação da nota fiscal.

Informações***Dica*:**Ao tentar excluir uma natureza que está vinculada a um movimento ou lançamento fiscal aparecerão às mensagens "A Natureza está vinculada em Movimentos" ou "A Natureza está vinculada em Lançamentos", indicando que estes registros não poderão ser excluídos.false

## **Anexos**

2true1Tributos da Natureza

**Tributos da Natureza:**Nesta opção deverão ser informados os demais tributos incidentes na operação, além do ICMS / IPI, como o ISS, INSS, etc. No momento da inclusão do documento fiscal, o sistema carregará automaticamente esses tributos para a pasta Outros Tributos do lançamento fiscal.

2Norma Referenciada3Mensagens4Associação Natureza de Operação X Código de Ajuste SPED Fiscal5Tributos que afetam Valor Contábil

**Tributos que afetam o Valor Contábil:**Com essa opção é possível incluir os valores de impostos sobre a base de calculo do ICMS, IPI e Valor contábil do lançamento. Esse anexo está disponível no cadastro de naturezas, Regras de ICMS e Regras de IPI e são tratados da seguinte maneira:

* Regras de ICMS – Os valores dos tributos cadastrados nesse anexo irão afetar o valor da base de calculo do tributo ICMS.
* Regras de IPI – Os valores dos tributos cadastrados nesse anexo irão afetar o valor da base de calculo do tributo IPI.
* Cadastro de CFOP – Os valores dos tributos cadastrados nesse anexo irão afetar o valor contábil do lançamento fiscal.

Exemplo:

|  |  |
| --- | --- |
| Valor da Mercadoria | 100,00 |
| Base de Cálculo do ICMS | 100,00 |
| Base de Cálculo do IPI | 100,00 |

Nos anexos da Natureza, da Regra de ICMS e Regra de IPI foram informados os Seguintes Tributos:

* Cadastro de CFOP = Tributo II COFINS e PIS/PASEP
* Regra de ICMS  = Tributo II
* Regra de IPI     = Tributo COFINS

Chegando aos seguintes valores:

|  |  |
| --- | --- |
| Tributo II | 1,00 |
| Tributo PIS | 0,65 |
| Tributo COFINS | 3,00 |

Ao realizar o cálculo do lançamento iremos chegar teremos os valores:

|  |  |
| --- | --- |
| Valor da Mercadoria | 104,65 |
| Base de Cálculo do ICMS | 101,00 |
| Base de Cálculo do IPI | 103,00 |

Para a Integração com TOTVS Gestão Estoque, Compras e Faturamento, deve ser configurado nas formulas do movimento para que esses valores sejam incluídos no conforme exemplo acima.

**Lança Valor Despesa:**Este campo define onde serão lançados os valores informados em Despesa Condicional no Lançamento Fiscal. Os valores de Despesa Condicional continuam sendo somados ao Valor Contábil do Lançamento e o valor informado no campo Despesa Condicional é lançado em "Outros" ou "Isento" conforme parâmetro da natureza. Este novo campo na Natureza é considerado na Escrituração de forma a obedecer a mesma regra da tela de lançamento.

Informações\_ftn1

 Foi criado um novo Tipo de Natureza no cadastro da CFOP, este tipo é referente a Devolução por Recusa.

Se na Natureza o campo Tipo Natureza(Rotinas Legais) for Devolução por Recusa as informações serão geradas no Grupo E, linha 62 de acordo com implementação realizada a partir da versão 12.1.28, onde será possível transmitir NF-e de Devolução por Recusa sem os dados do cliente.

Mais Sobre

Veja como parametrizar e 

---
