---
content_hash: af26aadd1fcfaf170ad6c9275bbcb3ce543aaf737481613a6884a0eb338b620b
fetched_at: '2026-06-29T00:11:50.718825+00:00'
page_id: '84541588'
product: rm
source: tdn-rm
title: RMFIS00025_Geração Bloco P
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=84541588
version: 35
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52 |
| **Processo** | **:** | EFD Contribuições |
| **Subprocesso** | **:** | Geração do Registro P |
| **Data da publicação** | **:** | 18/09/2013 |

**Introdução:**

Este documento tem por objetivo auxiliar o usuário na parametrização e geração do registro **“P”** **(Apuração da Contribuição previdenciária sobre a Receita Bruta).**

Entendendo o **Bloco “P”:**

Até 31/12/2014, as empresas relacionadas pela Lei 12.546/2011 (basicamente TI e vestuário) deixam de recolher a contribuição para a Seguridade Social apurada com base na remuneração paga e passam a recolher a Contribuição Social sobre Receita Bruta, pelas alíquotas de 2,5% ou 1,5%.

Essas empresas precisam informar na EFD Contribuições, os registros:

**• 0145 – Para identificar a obrigatoriedade de escrituração do Bloco P**

**• P001 – Para indicar se há valores no Bloco P**

**• P010 – Para identificar o estabelecimento da empresa que obteve receitas sujeitas à Contribuição Social**  
**sobre Receita Bruta**

**• P100 – Para indicar os valores da apuração da Contribuição Social sobre Receita Bruta**

**• P110 – Para detalhar os valores acumulados do P100**

**• P199 – Caso tenha processos para o tratamento diferenciado da Contribuição Social sobre Receita Bruta**

**• P200 – Para totalizar a Contribuição Social sobre Receita Bruta devida pela empresa**

**• P210 – Para informar valores de ajustes na apuração da Contribuição Social sobre Receita Bruta**

**• P990 – Para fechamento do Bloco P**

O bloco **“P”** só deve ser exigido no **EFD** **Contribuições** da pessoa jurídica, caso tenha sido gerado no mínimo 01 (um) registro “0145”, indicando a sujeição da pessoa jurídica à nova contribuição, no período da escrituração. A inexistência de registro **“0145”** no Bloco **"0"** , deve dispensar a necessidade de gerar o **Bloco “P”**, inclusive em relação a registros de abertura e de encerramento deste.

**IMPORTANTE!**

As empresas no regime de **Lucro Real** já entregam a **EFD Contribuições** contendo a escrituração do **PIS** e **COFINS** nos Blocos **A**, **C**, **D** e **F**. Já as empresas do **Lucro Presumido** só passarão a informar a escrituração de **PIS** e **COFINS** a partir da competência julho/2012.

Entretanto, para os dois regimes, **Real** e **Presumido**, a obrigação para a escrituração da apuração da contribuição previdência sobre receita é a partir de março/2012.

As empresas do **Lucro Real** devem informar o **Bloco** **P** juntamente com os demais Blocos. As empresas do **Lucro Presumido** devem informar, até a competência junho/2012, apenas os dados dos **Blocos 0**, **P** e **9** e o restante dos blocos **A, C, D, F, 1, M** vazios.

Para identificarmos as empresas optantes pelo **Lucro Presumido**, será apresentado na tela de geração da rotina, campo para informação do Regime adotado pela empresa de **Lucro Presumido**:

• **Não se aplica;**

• **Regime de Caixa**;

• **Regime de Competência**.

Caso seja selecionada a opção**“Não se aplica”**, a geração seguirá o modelo padrão, já gerado atualmente, mais o **Bloco P**, de acordo com as regras constantes no Item 5 desta especificação. Se for selecionada a opção **Regime de Caixa ou Regime de Competência** e o período selecionado por anterior a Julho/2012, serão gerados apenas os **Blocos 0, P** e **9**. A partir da competência Julho/2012 segue regra para o Lucro Presumido ainda a ser definida.

Para apuração da **Contribuição Previdenciária** sobre a receita e a geração dos registros equivalentes na **EFD Contribuições,** realizamos as seguintes implementações.

**1. Para a correta geração do bloco P deve-se:**

1.1 Criar o Tributo **Contribuições Previdenciárias** cujo tipo será **Contribuição Previdenciária**. Para isto acesse o Menu: **Cadastros | Tributos:**

       Ao Cadastrar o Tributo na aba **Identificação**, atentar para o preenchimento dos seguintes campos:

**•** Tipo de Alíquota: **Variável**

• Tipo Tributo: **Contribuição Previdenciária**

• Abrangência do Tributo: **Federal**

• Periodicidade: **Mensal**

Em seguida na aba **Outros Dados**, atentar para o preenchimento dos seguintes campos:

• Incidência: **Ambos**

• Procurar Alíquota no: **Produto**

**2. Códigos de Receitas**

Os Códigos de Receitas aplicáveis na apuração da Contribuição Previdenciária devem ser inseridos no Cadastro de **"Código da Receita"**, para acessá-lo existem dois caminhos disponíveis:

1-  Acessando o módulo Gestão Financeira (menu **Cadastros | Fiscais | Mais | Códigos de Receita**)

2-  Pesquisando pelo Cadastro de **"Código da Receita"** no módulo Gestão Fiscal por meio do ícone **Executar,**localizado no canto superior direito da tela. Ao acessá-lo será apresentado um campo de busca, no qual deve-se inserir o texto correspondente ao que se deseja pesquisar.

Na tela  **Código da Receita**deve ser informado o Código de Receita Oficial. O Anexo **"Variações do Código de Receita"** também deve ser preenchido para correta geração da **DCTF**.

**Observação**: Mesmo que o campo "Alíquota" seja preenchido no Cadastro de **"Código da Receita"**, esta não será utilizada no processo. Isso porque a alíquota, de acordo com a Tabela 5.1.1 da **EFD Contribuições**, é definida por produto.

**Segue trecho retirado do Guia Pratico com os códigos da receita que devem ser utilizados no Bloco P:**

**3. Cadastro de Produtos**

O Tributo criado no item 1 **(CONTRIB PR)** deve ser inserido no cadastro do produto, juntamente com a alíquota e o Código de Receita previamente cadastrado em:  Produto → Anexos → Tributos do Produto

Deve ser preenchido, também o campo **“Código de Atividade Econômica”**de acordo com a Tabela 5.1.1 do Guia Prático da **EFD Contribuições**. Este campo apesar de visível a partir da versão 12.0,  é necessária a criação de um **Campo Complementar**com as seguintes configurações:

• Alteração feita para gerar o campo 05 do **Registro P100** da **EFD Contribuições**.

**Campo 05 - COD\_ATIV\_ECON:**  Será preenchido através do campo complementar no cadastro de produtos conforme observação abaixo.

**Nome do campo: CODATIVECONOMIC**  
**Tipo: Alfanumérico**  
**Tamanho: 8 posições**

                    3.1 - Acessando o módulo Gestão Fiscal (menu **Cadastros | Produto | clique duplo no produto | Campos Complementares**)

3.2 - Acessando o módulo Gestão de Estoque, Compras e Faturamento (menu **Cadastros | Mais | Campos Complementares | Produtos**)

Para gerar o evento R 2060 da REINF é necessário preencher o campo complementar e o campo Código Atividade Econômica (conforme tabela 9 - Código de Atividades, Produtos e Serviços Sujeitos à CPRB)

**IMPORTANTE:**  A partir da versão 12.1.33 a rotina verificará em Produto | Anexo | Dados Fiscais do Produto | Identificação, código de atividade Econômica esta preenchido caso esteja em branco ele buscará o código do campo complementar.

**4. Lançamentos / Movimentos**

O tributo criado no item 1 deve ser informado nos Itens dos Lançamentos Fiscais com base de cálculo, alíquota, valor do imposto e código de receita, para correta apuração do tributo e geração da EFD Contribuições.

**4.1 - Tipo de Movimento**

A parametrização do Tipo de Movimento é realizada no sistema de  Gestão  Estoque, Compras e Faturamento, onde o tributo da Contribuição Previdenciária sobre a Receita Bruta deve ser inserido no Item do Movimento (**Etapa 64 - Fis/Tributação Item**) informando no campo "Buscar alíquota em" a opção "Produto".

Na inclusão de movimentos que possuem o tributo Contribuição Previdenciária sobre a Receita Bruta parametrizado, o sistema irá buscar o Código de Receita e a alíquota do tributo no Anexo "Tributos do Produto" do Cadastro do Produto, conforme parametrizado no item 1.3.

Essas informações serão escrituradas para a Gestão Fiscal. Será criado campo na tabela **DTRBITEM** (pasta Outros Tributos do Item) para receber o Código de Receita do Tributo do Movimento a partir da versão 11.90, nas versões inferiores como, por exemplo, 11.52, 11.81 e 11.82, deverá ser criado o campo complementar nos itens do lançamento fiscal conforme dados abaixo:

**Nome do campo: CODRECEITA**  
**Tipo: Alfanumérico**  
**Tamanho: 6 posições**

**5. Cadastro de Outros Débitos/Créditos – Lançamentos de ajustes**

O Cadastro de Outros Débitos/Créditos deve ser evoluído para permitir lançamentos para o tributo “Contr. Previdenciária”. Devem ser considerados apenas lançamentos dos Tipos “Débito” e “Crédito”, com Subtipo “Não se aplica”, tanto na apuração do tributo, como na geração do **Registro P210**.

Para a correta geração do **Registro P200/P210**, o código da receita equivalente ao lançamento de ajuste que está sendo feito deve ser informado no campo **Classificação** do lançamento de Outros Débitos/Créditos, com a variação do Código da Receita (*Exemplo: 298501*).

O Código de ajuste deverá ser cadastrado no campo **Código Ajuste SPED.** Os valores possíveis para este campo são encontrados na tabela 4.3.8 do guia da EFD Contribuições.

Os lançamentos de Outros Débitos serão considerados como **ajustes de acréscimo** (**P210 – Campo 02 INS\_AJ = ‘1’**). Os lançamentos de Outros Créditos serão considerados como **ajustes de redução (P210 – Campo 02 INS\_AJ = ‘0’**).

**6. Período de Apuração**

Cada Filial que realizar atividades sujeitas à Contribuição Social sobre Receita Bruta deve ter seu Período de Apuração criado. Isso é necessário porque a **EFD Contribuições** pede as informações da apuração por Estabelecimento da empresa. No entanto, o valor a recolher da contribuição deve ser consolidado pela Filial Matriz.

Para correta apuração da Contribuição Previdenciária deve ser preenchido, manualmente, no Período de Apuração, o campo **“Valor total do Faturamento”**. Esse valor será utilizado no cálculo da proporção das receitas desoneradas e não desoneradas, conforme determina a **Lei nº 12.715/2012**.

**Observação:** O preenchimento do campo deve ocorrer ANTES do encerramento do período.   
  
Esse campo será utilizado para geração do **Campo 03 VL\_REC\_TOT** no Registro 0145 e, também, do Campo **04 VL\_REC\_TOT\_EST** no Registro P100. O valor será replicado em cada um dos Registros gerados para cada estabelecimento da empresa.

Após o encerramento do período, os lançamentos de Outros Créditos/Débitos serão considerados na aba "Contribuição Previdenciária" do período de apuração.  
  
**7. Apuração**   
  
Apesar de cada Filial ter que cadastrar um período de apuração para a Contribuição Previdenciária, o processo de encerramento do período de apuração deve ocorrer, tão somente, pela **Filial Matriz.**   
  
Isso é necessário porque, apesar do detalhamento da receita ser por estabelecimento, por ser um tributo de administração da Receita Federal do Brasil, ele deve ser apurado e recolhido pelo estabelecimento Matriz.   
  
**7.1 Apuração das Filiais**   
  
No encerramento dos Períodos de Apuração das Filiais serão selecionados os Lançamentos de Saída (receita) e os Lançamentos de Entrada (devoluções/vendas canceladas) que possuam o tributo **“Contribuição Previdenciária”** informado no Tributo do Item.

Os lançamentos selecionados serão agrupados e detalhados por (i) Código da Atividade Econômica, (ii) Alíquota e (iii) Código da Receita, totalizando os seguintes valores:   
  
**• Valor da Receita** correspondente à atividade (Lançamentos de Saída);   
**• Valor de Exclusões da Receita** (Lançamentos de Entrada);   
**• Base de cálculo** (Receita – Exclusões);   
**• Valor das Contribuições** (Base de cálculo x Alíquota).

Serão selecionados, também, os lançamentos de **Outros Débitos/Créditos.** 

**Observação:** O Saldo devedor não será calculado nas Filiais, apenas na Matriz.   
  
**7.2 Apuração da Matriz**   
  
Os valores do detalhamento apurados nas demais Filiais devem ser acrescentados ao detalhamento da própria Filial Matriz que foram apurados seguindo os mesmos critérios descritos no item 7.1.   
  
Seguindo o exemplo anterior, teríamos o seguinte detalhamento:

Para calcular o Saldo Devedor do Tributo, o sistema deve fazer as seguintes verificações:   
  
**7.2.1 Proporção das Receitas Desoneradas**   
  
O cálculo da proporção será realizada através do campo **“Valor Total do Faturamento”** informado no Período de Apuração, **ANTES** do encerramento do período, em relação ao somatório das   
receitas correspondente a cada Código de Atividade gerado no Detalhamento do período.   
  
De posse desse fator, o sistema terá dois comportamentos distintos**¹**:  
  
**I.** Se o total da **Receita Desonerada for maior ou igual a 95%** do total das receitas:

**a.**Caso o total da Receita Desonerada não seja 100% do total do faturamento informado no Período de cada Filial, será inserido automaticamente um registro de detalhamento com código de atividade  “999900XX”  com o valor da diferença entre o total das receitas desoneradas e o valor total do faturamento informado no Período de Apuração, este detalhamento será inserido com o Código de Receita informado no Cadastro do Tributo e alíquota informada no período de apuração \ Aba Apuração\ Campo “Alíquota Apuração”.

**b.** O valor do **Saldo Devedor** do Tributo no Período deve corresponder ao somatório da **Contribuição Previdenciária**, mais **ajustes de acréscimos**, menos **ajustes de redução**, consolidados no detalhamento da Filial Matriz. No Exemplo acima, o saldo devedor retornaria o valor de **$ 716,00** (431,00 + 300,00 – 15,00).

**II.** Se a **Receita Desonerada for inferior a 5%** do total da receita:

**a.** O Saldo Devedor do Tributo é zero.   
  
*Nota Explicativa:**¹** Comportamento necessário para tratar as alterações da Lei nº 12.715/2012 que retira, totalmente, a aplicação da desoneração da folha para as empresas que se dediquem a outras atividades, além das previstas no Anexo da Lei 12.546/2011, cuja receita bruta decorrente dessas outras atividades seja igual ou superior a 95% da receita bruta total. TOTVS Gestão Fiscal*

**8. Geração das Guias DARF**   
  
O processo de geração automática das guias DARF só deve ser executado se o Saldo Devedor do Período for maior que zero.   
  
O Sistema irá gerar uma guia para cada **Código de Receita** gerado no detalhamento da Filial Matriz, utilizando o mesmo critério da apuração, ou seja, o valor da Contribuição Previdenciária, mais ajustes de acréscimos, menos ajustes de redução, apurados no detalhamento.   
  
Seguindo o exemplo dado, seriam geradas duas guias DARF: uma para o Código de Receita **2991.01** no valor de **$ 2.025,01**; outra no valor de **$ 3.345,00** para o Código de Receita**2985.01**.   
  
O sistema só deve permitir a geração das guias através da Filial Matriz

**9. Geração da EFD Contribuições**   
  
**Menu:** Obrigações Acessórias | Gerador de Saídas | Layouts do Gerador de Saída | EFD\_CONTRIBUIÇÕES\_B  
  
Na tela de geração da rotina, no parâmetro "Contribuição Previdenciária Indicador da Incidência" deverá ser   
informando com uma das opções:   
  
  
  
Onde o código indicador da incidência tributária no período pode ser:   
  
**1 –** Contribuição Previdenciária apurada no período, exclusivamente com base na Receita Bruta;   
  
**2 –** Contribuição Previdenciária apurada no período, com base na Receita Bruta e com base nas Remunerações pagas, na forma dos nos incisos I e III do art. 22 da Lei no 8.212, de 1991.   
  
No Período de Apuração deverá ser informado o total da receita bruta,manualmente, para a geração do registro 0145 e registro P100.   
  
**9.1 REGISTRO 0145: REGIME DE APURAÇÃO DA CONTRIBUIÇÃO PREVIDENCIÁRIA SOBRE A RECEITA BRUTA**   
  
Esse registro indica a obrigatoriedade do Bloco P no arquivo. Esse registro só deve ser gerado se o valor do Campo 04 for maior que zero, ou seja, a empresa realizou atividades sujeitas à Contribuição Social   
sobre Receita Bruta.

Este registro só será gerado pelo sistema se o **Saldo Devedor** da Contribuição Previdenciária na Filial Matriz for maior que zero. Se o Saldo Devedor for zero, indica que o total das receitas desoneradas é   
menor que 5% do total da receita da empresa, neste caso, não se sujeitando à contribuição previdenciária.

Com relação aos demais campos deste Registro, seguem observações:   
  
**• Campo 02 – COD\_INC\_TRIB:** Serão apresentadas as opções na tela de geração da rotina como parâmetro para que o usuário selecione no momento da geração da rotina:

1 – Contribuição Previdenciária apurada no período, exclusivamente com base na Receita Bruta;   
2 – Contribuição Previdenciária apurada no período, com base na Receita Bruta e com base nas Remunerações pagas, na forma dos nos incisos I e III do art. 22 da Lei no 8.212, de   
1991.

**• Campo 03 – VL\_REC\_TOT:** Será preenchido com o valor informado no campo Valor Total do Faturamento no Período de Apuração.   
  
• **Campo 04 – VL\_REC\_ATIV:** Será gerado com a totalização dos Itens que possuem o Tributo “Contr. Previdenciária” informado:

a) A informação no Lançamento de Saída indica valor a pagar.   
b) No Lançamento de Entrada indica valor a estornar (devolução de vendas, vendas   
canceladas).   
  
**• Campo 05 – VL\_REC\_DEMAIS\_ATIV**: Será gerado com a diferença entre o total da receita e o total de receita sujeita à Contribuição Social sobre Receita Bruta (Campo 03 – Campo 04). Este campo   
será gerado com valor zero se a opção do campo COD\_INC\_TRIB for igual 1.   
  
**• Campo 06 – INFO\_COMPL**: Não será gerado.   
  
  
**9.2 BLOCO P: APURAÇÃO DA CONTRIBUIÇÃO PREVIDENCIÁRIA SOBRE A RECEITA BRUTA**

Os Registros deste bloco só devem ser gerados se o Registro 0145 foi gerado. O Bloco deve ser gerado por Estabelecimento que realizou atividades sujeitas à Contribuição Social sobre Receita Bruta,   
informando no Registro P010 o CNPJ da Filial.

**9.3 REGISTRO P100: CONTRIBUIÇÃO PREVIDENCIÁRIA SOBRE A RECEITA BRUTA**

Esse Registro será gerado a partir dos valores apurados no detalhamento do Período para o tributo “Contr. Previdenciária”. Deve ser gerado um Registro para cada combinação dos campos “05 COD\_ATIV\_ECON” e “09 ALIQ\_CONT”.

**• Campo 03 – VL\_REC\_TOT:** do Registro 0145.

**• Campo 04 – VL\_REC\_TOT\_EST:** Deve receber o mesmo valor informado no TOTVS Gestão Fiscal

**• Campo 05 - COD\_ATIV\_ECON:** Em versões anteriores a 11.90 será preenchido através do campo complementar no cadastro de produtos conforme observação abaixo. A partir da versão 11.90 será preenchido através do campo “Código Atividade Econômica” a ser disponibilizado nos dados fiscais do cadastro de produto.

**OBS: Para geração deste campo em versões anteriores a 11.90 é necessário criar o campo na tabela complementar de produtos.**   
  
**Vide Item 3.**   
  
**• Campo 06 - VL\_REC\_ATIV\_ESTAB:** Será preenchido com o somatório dos Itens (Valor Mercadoria) que possuem o Tributo Contr. Previdenciária, nos Lançamentos Fiscais de Saída,   
deduzindo o somatório dos Itens (Valor Mercadoria) que possuem o Tributo Contr. Previdenciária, nos Lançamentos Fiscais de Entrada.   
**• Campo 07 – VL\_EXC:** Valor das exclusões da receita bruta informadas no campo 06.

**Os campos “11 - COD\_CTA” e “12 - INFO\_COMPL” não serão gerados.**  
**Observação:** Só devem ser selecionados os detalhamentos cujo Código de Atividade seja diferente de nulo. Isso é necessário para que sejam desprezados os valores de ajustes que devem ser informados   
apenas nos Registros P200/P210.

**9.4 REGISTRO P110: COMPLEMENTO DA ESCRITURAÇÃO – DETALHAMENTO DA APURAÇÃO DA CONTRIBUIÇÃO**

Hoje esse Registro é opcional, portanto, não será gerado neste primeiro momento, pois foram muitas as dúvidas sobre a regra de sua geração.

**9.5 REGISTRO P199: PROCESSO REFERENCIADO**

Não será gerado, visto que, atualmente, não é possível referenciar Processo no Período de Apuração.

**9.6 REGISTRO P200: CONSOLIDAÇÃO DA CONTRIBUIÇÃO PREVIDENCIÁRIA SOBRE A RECEITA BRUTA**

Esse Registro consolida a Contribuição Previdenciária sobre a Receita Bruta devida pela empresa no período. Os dados para sua geração serão obtidos do Período de Apuração.   
Será gerado um Registro P200 para cada **Código de Receita** apurado no detalhamento do Período de Apuração, totalizando os valores da **Contribuição Previdenciária**, **Ajustes de Redução**, **Ajustes de**  
**Acréscimo** e valor total da **Contribuição a recolher**.

**9.7 REGISTRO P210: AJUSTE DA CONTRIBUIÇÃO PREVIDENCIÁRIA APURADA SOBRE A RECEITA BRUTA**

Esse registro será gerado pelos lançamentos de Outros Débitos/Créditos para o tributo “Contribuição Previdenciária”.

**• Campo 02 - IND\_AJ:** Se o lançamento for de Crédito, recebe valor “0”. Se for do Tipo Débito recebe valor “1”.   
**• Campo 03 - VL\_AJ:** Recebe o valor do lançamento de ajuste.   
**• Campo 04 - COD\_AJ:** Recebe o valor do campo “Código Ajuste SPED”.   
**• Campo 05 - NUM\_DOC:** Recebe o valor do campo “Processo Judicial ou Administrativo”.   
**• Campo 06 - DESCR\_AJ:** Recebe o valor do campo “Histórico”.   
**• Campo 07 - DT\_REF:** não aderência.

**Para maiores informações:**

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
