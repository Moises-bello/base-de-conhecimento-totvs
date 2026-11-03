---
content_hash: 40d0e3812749389bdc06d174707679d9ec5c2c8dd5b44cf269e64178613c1cb3
fetched_at: '2026-06-29T00:10:18.552500+00:00'
page_id: '4812518'
product: rm
source: tdn-rm
title: Como Fazer - MANAD
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+Fazer+-+MANAD
version: 9
---

BLOCK

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.0 |

Aqui se encontram as etapas pelas quais o usuário do TOTVS Folha de Pagamento (RM Labore) passará para a correta geração dos arquivos do MANAD. O objetivo desse material é auxiliar o cliente na verificação dos dados presentes na base de dados para a confecção de um arquivo com informações mais consistentes.

Antes de executar o procedimento aqui descrito, recomendamos a leitura do manual explicativo do MANAD, presente no site da Receita Federal, bem como o download, instalação e a leitura do manual do aplicativo SVA, que é o programa validador do arquivo (também disponível no site da Receita).

**MANAD é o Manual Normativo de Arquivos Digitais no qual consta todas as informações para gerar o arquivo digital a ser apresentado à fiscalização da Secretaria da Receita Previdenciária quando a empresa for intimada por Auditor Fiscal da Previdência Social (AFPS).**

Abaixo segue um breve resumo dos principais blocos que contém as informações mais relevantes para o entendimento daquilo que está sendo levado para o arquivo gerado.

**Os blocos que começam com 0 (zero) são o cabeçalho do arquivo. O restante dos blocos gerados pelo Labore começam com K, exceto o Bloco I050 (que leva o cadastro de Plano de Contas Contábeis) e o bloco I100 (que leva o cadastro de Centros de Custos).**

**Deve ser gerado também um arquivo do MANAD com informações do sistema de contabilidade da empresa.**

**Detalhes das informações de cada bloco podem ser verificados pelo manual do MANAD que contém o layout do arquivo.**

**Bloco 0000** – Contém os dados das filiais ou das seções (de acordo com o parâmetro escolhido na geração do relatório).

**Bloco 0050** – Dados do contabilista informados na geração.

**Bloco 0100** – Dados do responsável pela geração do arquivo, informado na geração.

**Bloco I050** – Cadastro do Plano de contas contábil.

**Bloco I100** – Cadastro dos Centro de Custos.

**Bloco K050** – Cadastro dos funcionários.

**Bloco K100** – Cadastro de lotações (Seções).

**Bloco K150 –** Cadastro de Rubricas (Eventos).

**Bloco K200 –** Parametrização da contabilização. Eventos, seções ou centros de custos e suas contas.

**Bloco K250 –** Mestre da folha de pagamento. Leva uma linha para cada tipo de folha do funcionário, com a base de INSS e IRRF total do mês competência.

**Bloco K300 –** Itens da folha de pagamento. Leva os eventos da ficha financeira e a indicação de incidência em INSS e IRRF. O total desses eventos deve corresponder à base total informada no Bloco K250.

**Procedimentos a serem feitos antes da geração do arquivo:**

**Passo 01:** **Verificar a parametrização da contabilidade.**

A execução desse passo dependerá diretamente do requerimento do Auditor Fiscal ou do órgão que solicitou o arquivo do MANAD. Na solicitação, geralmente, é explícita a necessidade de geração do bloco K200 (Dados Contábeis). Quando não há nenhuma citação sobre esse tipo de geração, recomendamos o envio do arquivo contendo os dados contábeis da folha de pagamento (com o bloco K200).

Caso a contabilização não tenha sido parametrizada, ou caso ache importante fazer uma revisão dos processos hoje inseridos no RM Labore, é necessária a leitura e execução dos procedimentos presentes no Roteiro de Contabilização.

Além da parametrização citada acima, existe um dado que não era utilizado pelo RM Labore em nenhum processo contábil e que, por isso, não é citado em nenhum outro documento de parametrização da parte contábil: **Natureza da conta para a emissão do SPED**. No registro I050 (Plano de Contas) essa informação é utilizada para o preenchimento do campo Indicador da Natureza. Portanto, é de extrema importância que essa informação seja preenchida em todas as contas do plano de contas contábeis.

Para fazer uma verificação mais rápida das contas que necessitam ser atualizadas execute a seguinte consulta no banco de dados:

**SELECT CODCONTA,NATSPED**

**FROM CCONTA WHERE NATSPED IS NULL OR NATSPED ='00'**

Caso essa consulta não discrimine nenhuma conta é porque as todas elas estão preenchidas corretamente.

**Passo 02:** **Verificar cadastro de funcionários.**

Como são utilizados dados de funcionários na confecção de vários blocos, é extremamente importante que os dados cadastrais estejam corretos e completos.

Para a geração do MANAD uma das informações mais importantes é o Histórico de Seção do funcionário. Existe uma obrigatoriedade quanto ao histórico de seção do funcionário: nesse histórico deve haver o registro com a seção na qual o funcionário foi lotado no momento de sua admissão ou de sua entrada por transferência, ou seja, deve haver um registro cuja data de mudança é igual à data de admissão ou de entrada por transferência do funcionário. Geralmente, empresas que possuem grandes números de transferências ou que tiveram as informações importadas de outros sistemas podem encontrar mais problemas quanto a esse tipo de informação.

Para facilitar a verificação das informações citadas acima é possível executar uma consulta que indica quais as chapas estão com o histórico de seção sem o registro da admissão ou de transferência.

**Exemplo SQL SERVER** (Alterar o código da coligada para a desejada):

**SELECT CHAPA,NOME,DATAADMISSAO,DTTRANSFERENCIA FROM PFUNC P WHERE CHAPA NOT IN**

**(**

**SELECT CHAPA FROM PFUNC WHERE EXISTS**

**(**

**SELECT 1 FROM PFHSTSEC WHERE CODCOLIGADA=PFUNC.CODCOLIGADA AND**

**CHAPA=PFUNC.CHAPA AND ((DATEPART(YEAR,DTMUDANCA)=DATEPART(YEAR,DATAADMISSAO) AND**

**DATEPART(MONTH,DTMUDANCA)=DATEPART(MONTH,DATAADMISSAO) AND DATEPART(DAY,DTMUDANCA)=DATEPART(DAY,DATAADMISSAO))**

**OR (DATEPART(YEAR,DTMUDANCA)=DATEPART(YEAR,DTTRANSFERENCIA) AND**

**DATEPART(MONTH,DTMUDANCA)=DATEPART(MONTH,DTTRANSFERENCIA) AND**

**DATEPART(DAY,DTMUDANCA)=DATEPART(DAY,DTTRANSFERENCIA))) AND CODCOLIGADA = '1'**

**)**

**AND CODCOLIGADA = '1'**

**) AND P.CODCOLIGADA=CODCOLIGADA AND P.CHAPA=CHAPA AND CODCOLIGADA='1'**

**Exemplo ORACLE** (Alterar o código da coligada para a desejada):

```
        SELECT        CHAPA, NOME, DATAADMISSAO, DTTRANSFERENCIA  
        FROM          PFUNC P  
        WHERE         CHAPA NOT IN (  
                                    SELECT       CHAPA  
                                    FROM         PFUNC  
                                    WHERE EXISTS (  
                                                    SELECT 1  
                                                    FROM    PFHSTSEC  
                                                    WHERE   CODCOLIGADA=PFUNC.CODCOLIGADA  
                                                    AND     CHAPA=PFUNC.CHAPA  
                                                    AND     (  
                                                             (TO_CHAR(DTMUDANCA, 'YYYY-MM-DD')=TO_CHAR(DATAADMISSAO, 'YYYY-MM-DD'))  
                                                              OR   
                                                             (TO_CHAR(DTMUDANCA, 'YYYY-MM-DD')=TO_CHAR(DTTRANSFERENCIA, 'YYYY-MM-DD'))  
                                                            )  
                                                    AND CODCOLIGADA = '1'  
                                                )  
                                    AND CODCOLIGADA = '1'  
                                )  
        AND P.CODCOLIGADA=CODCOLIGADA  
        AND P.CHAPA=CHAPA  
        AND CODCOLIGADA='1'
```

Para ajustar essas informações será necessário acessar o cadastro de cada uma das chapas citadas na consulta acima, corrigindo o histórico de seção do funcionário.

**Passo 03**: **Verificar se existe movimentação na Ficha Financeira ou Ficha Financeira Complementar no o período solicitado.**

Em Opções | Parâmetros | RM Labore | Outros Parâmetros é possível definir por quanto tempo a movimentação será mantida na ficha financeira do funcionário e se a mesma será excluída da base de dados ou mantida na ficha financeira complementar.

Antes que iniciar a geração do MANAD é muito importante fazer essa verificação, pois caso a movimentação tenha sido excluída da base de dados, a geração do arquivo deverá ser feita por meio de um ambiente teste com a restauração de um backup que contenha essas informações.

Caso a movimentação exista na ficha financeira ou na ficha financeira complementar, a geração do arquivo poderá ocorrer com sucesso. A única verificação que deve ser feita, nesse caso, é apurar se essa informação está aparecendo, em duplicidade, tanto na ficha financeira normal quanto na complementar. Se isso ocorrer a movimentação da ficha financeira complementar deverá ser apagada.

**Observação:** Não é necessária a execução da rotina de Restauração da Ficha Financeira Complementar.

Consulta para verificar se os dados estão em duplicidade:

**SELECT \* FROM PFFINANCCOMPL WHERE EXISTS (SELECT \* FROM PFFINANC WHERE**

**PFFINANCCOMPL.CODCOLIGADA=PFFINANC.CODCOLIGADA**

**AND PFFINANCCOMPL.CHAPA=PFFINANC.CHAPA**

**AND PFFINANCCOMPL.ANOCOMP=PFFINANC.ANOCOMP**

**AND PFFINANCCOMPL.MESCOMP=PFFINANC.MESCOMP**

**AND PFFINANCCOMPL.NROPERIODO=PFFINANC.NROPERIODO** **AND PFFINANCCOMPL.CODEVENTO<>PFFINANC.CODEVENTO)**

**Passo 04:** **Verificar cadastro de eventos.**

Esse passo consiste unicamente em verificar as incidências dos eventos. É comum o Auditor Fiscal solicitar a movimentação de um período cujos eventos não são mais utilizados nas movimentações atuais. Portanto, uma verificação criteriosa das incidências pode garantir informações mais consistentes, pois a incidência utilizada é a atual. Com exceção do código de cálculo 62 e 99 que o sistema considera a data informada em Opções | Parâmetros | RM Labore | Parâm. Rescisão.

**Passo 05:** **Verificar cadastro de autônomos no TOTVS Gestão Financeira (RM Fluxus) / TOTVS Gestão de Estoque, Compras e Faturamento (RM Nucleus) caso opte por incluí-los no arquivo. Cadastros | Clientes / Fornecedores.**

[![clip_image002](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwsczsHSuI/AAAAAAAAAzQ/lL3gAloKulc/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwsccOC9-I/AAAAAAAAAzM/G7KZJSUXGP0/s1600-h/clip_image002%5B4%5D.jpg)

[![clip_image004](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwsdrfTjlI/AAAAAAAAAzY/0ctYzD4PQ84/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwsdGFnWeI/AAAAAAAAAzU/b18JFE4Udh0/s1600-h/clip_image004%5B4%5D.jpg)

Filial: Nesse campo deve ser utilizada um código de filial que tenha sido associado, pelo menos, a uma seção do RM Labore.

Tipo de Documento: Deve ter classificação Gerar INSS ou Gerar INSS e IRRF para que o desconto previdenciário possa ser calculado.

Datas do Lançamento: Aqui, pelo menos a data de emissão deve estar dentro do período das informações usado na geração do arquivo do MANAD.

Categoria: A categoria utilizada é a do lançamento em questão e não a do cadastro do autônomo.

Valor: O valor do lançamento é o considerado como base para o MANAD.

**Passo 06:** **Gerar arquivo do MANAD.**

Após realizar todas as verificações recomendadas, o arquivo do MANAD está pronto para ser gerado.

**Gerando o arquivo:**

**Tela Inicial:**

[![clip_image006](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwsetvvo3I/AAAAAAAAAzg/D3e7ASzsISk/clip_image006_thumb%5B1%5D.jpg?imgmax=800 "clip_image006")](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwseDh7YXI/AAAAAAAAAzc/jB_d6KA6m6c/s1600-h/clip_image006%5B4%5D.jpg)

Na primeira tela do assistente é possível criar um novo perfil ou selecionar um já criado com as informações já registradas anteriormente.

**Tela de Parâmetros Globais:**

[![clip_image008](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwsfU1M2XI/AAAAAAAAAzo/ZLRYPs9yozk/clip_image008_thumb.jpg?imgmax=800 "clip_image008")](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwse2u8E7I/AAAAAAAAAzk/YWMk7137ZLY/s1600-h/clip_image008%5B3%5D.jpg)

Aqui será definido o período das informações solicitadas pelo auditor fiscal. É obrigatório informar as duas datas sendo que a Data Fim não pode ser menor do que a Data Início e o período deve ser, de no mínimo, um mês.

[![clip_image010](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwsghOy1QI/AAAAAAAAAzw/FOEc6R9Wl7A/clip_image010_thumb.jpg?imgmax=800 "clip_image010")](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwsgOqYRoI/AAAAAAAAAzs/x1IUXKoczQw/s1600-h/clip_image010%5B3%5D.jpg)

Aqui será definido para qual grupo de funcionários será gerado o arquivo. Essa seleção verifica a Situação, Tipo e Código de Recebimento atuais dos funcionários. Filtros só podem ser informados na 6ª tela de geração onde existem parâmetros específicos por coligada.

[![clip_image012](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwsho2h60I/AAAAAAAAAz4/Slx-YpvlPx8/clip_image012_thumb%5B1%5D.jpg?imgmax=800 "clip_image012")](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwshC8Q_nI/AAAAAAAAAz0/7sEqR6GC9BA/s1600-h/clip_image012%5B4%5D.jpg)

Os blocos K250 e K300 do MANAD possuem uma subdivisão quanto ao tipo de folha. Os indicadores do tipo de folha são:

1 – Tipo de Folha Normal

2 – Tipo de Folha de Férias

3 – Tipo de Folha de 13° Salário

Ao escolher a primeira opção a movimentação será dividida conforme informação acima. Caso seja marcada a 2ª Opção, as movimentações de Folha Normal e de Férias serão unificadas e serão ambas informadas com o indicador 1, enquanto o 13º Salário permanece sendo informado no arquivo com o indicador 2.

[![clip_image014](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwsicYr6OI/AAAAAAAAA0A/B06m0NWp6ig/clip_image014_thumb%5B1%5D.jpg?imgmax=800 "clip_image014")](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwsiHJXI9I/AAAAAAAAAz8/Yx8HLKfrkKA/s1600-h/clip_image014%5B4%5D.jpg)

O Auditor Fiscal (ou outro órgão solicitante) poderá exigir as informações da folha de pagamento com ou sem informações contábeis.

Marcando a 1ª Opção os blocos I050, I100 e K200 serão levados para o arquivo do MANAD, enquanto a 2ª Opção, ao ser marcada, fará com que o sistema não considere essas informações na composição do arquivo.

[![clip_image016](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwsjfmJ4lI/AAAAAAAAA0I/69Jx9kj9z2I/clip_image016_thumb%5B1%5D.jpg?imgmax=800 "clip_image016")](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwsizCS66I/AAAAAAAAA0E/dMFSkpQlEHc/s1600-h/clip_image016%5B4%5D.jpg)

Local onde os arquivos serão salvos. A pasta informada deve ter permissão total para todos os usuários. O nome do arquivo gerado tem o seguinte formato:

MANAD\_Código da Coligada\_Data Início (AAAAMMDD)\_Data Fim (AAAAMMDD).txt

**Tela de Opções de Exportação:**

[![clip_image018](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwskFPvfII/AAAAAAAAA0Q/hGHIvn-t8dw/clip_image018_thumb%5B1%5D.jpg?imgmax=800 "clip_image018")](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwsjuNSapI/AAAAAAAAA0M/dy9w3peBiMA/s1600-h/clip_image018%5B4%5D.jpg)

Aqui o sistema verifica as seções para a composição do registro de abertura (0000).

Marcando a 1ª opção, cada filial encontrada dará origem a um registro (uma linha) no bloco de abertura.

Marcando a 2º opção, irá gerar um registro para cada seção.

[![clip_image020](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwskwzy-hI/AAAAAAAAA0Y/rPwDF8FE5_E/clip_image020_thumb%5B1%5D.jpg?imgmax=800 "clip_image020")](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwskTL3pHI/AAAAAAAAA0U/-3JDmQEAwEY/s1600-h/clip_image020%5B4%5D.jpg)

Nesse parâmetro o sistema verifica quais foram os eventos de base de cálculo que foram lançados na movimentação dos funcionários no período informado e os levará para o bloco K300 (itens de folha de pagamento). Nesse bloco existe o campo Indicador de Provento ou Desconto, que pode ser preenchido com:

D – Desconto, P – Provento ou O – Outros

Marcando a 1ª opção, os eventos serão levados para o bloco K300 com o indicador O. Marcando a 2ª opção, os eventos serão levados para o bloco K300 com os indicadores D ou P (de acordo com as incidências e / ou código de cálculo.

[![clip_image022](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwslndvVRI/AAAAAAAAA0g/Rk5jmO6U4HQ/clip_image022_thumb%5B1%5D.jpg?imgmax=800 "clip_image022")](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwslTfRkkI/AAAAAAAAA0c/nSpBy4leA7g/s1600-h/clip_image022%5B4%5D.jpg)

No bloco de abertura do arquivo do MANAD (bloco 0000), existe o campo Indicador de Tipo de Entrada de Dados, cujo preenchimento é feito a partir dos códigos acima. Esse preenchimento será feito de acordo com instruções dadas pelo Auditor Fiscal ou outro órgão solicitante.

[![clip_image024](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwsmiQDQWI/AAAAAAAAA0o/o_80A0ffoaU/clip_image024_thumb%5B1%5D.jpg?imgmax=800 "clip_image024")](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwsmGk1vlI/AAAAAAAAA0k/atPP5wuziNY/s1600-h/clip_image024%5B4%5D.jpg)

Informe a finalidade do arquivo de acordo com o passado pelo fiscal. Normalmente, 61.

**Tela Visão do Contabilista:**

[![clip_image026](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwsntFghCI/AAAAAAAAA0w/utyygtgeT1g/clip_image026_thumb%5B1%5D.jpg?imgmax=800 "clip_image026")](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwsnNYo43I/AAAAAAAAA0s/kjZA-FmYNYc/s1600-h/clip_image026%5B4%5D.jpg)

Inclua quantos contabilistas forem necessários para o período de apuração dos dados. Os campos em negrito são de preenchimento obrigatório.

**Tela Visão do Responsável:**

Informe o funcionário responsável pela geração do arquivo MANAD.

[![clip_image028](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwso-7HryI/AAAAAAAAA04/IXUoXDOHozE/clip_image028_thumb%5B1%5D.jpg?imgmax=800 "clip_image028")](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwsoJ8BcSI/AAAAAAAAA00/z7fHHwyJm1U/s1600-h/clip_image028%5B4%5D.jpg)

Nesta mesma tela é informada a data de início e fim da prestação dos serviços de informática (fornecimento do sistema de geração dos arquivos digitais).

**Tela Seleção de Coligadas:**

Nessa tela é(são) selecionada(s) a(s) coligada(s) para a(s) qual(is) será(ao) gerado(s) o(s) arquivo(s) do MANAD. Lembrando que **NÂO** será gerado um arquivo consolidado com os dados de todas as coligadas e sim um arquivo para cada uma das coligadas selecionadas.

**Parâmetros Específicos por Coligada:**

Alguns parâmetros ficam disponíveis somente ao selecionar uma coligada e clicar em [![clip_image030](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwsprgIc7I/AAAAAAAAA1A/t4kWSgfj2i0/clip_image030_thumb%5B2%5D.jpg?imgmax=800 "clip_image030")](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwspKe6_QI/AAAAAAAAA08/-iwcVfyimCs/s1600-h/clip_image030%5B5%5D.jpg) Adicionar Parâmetros a Coligada.

[![clip_image032](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwsqZ3s8_I/AAAAAAAAA1I/8FdL2mPs-nE/clip_image032_thumb.jpg?imgmax=800 "clip_image032")](http://lh5.ggpht.com/_G7KXZLoZDsY/TGwsp8pBRiI/AAAAAAAAA1E/Fp_6YUfqhvM/s1600-h/clip_image032%5B3%5D.jpg)

Na seleção de funcionários desta tela é possível adicionar um filtro para geração do arquivo e também é possível selecionar apenas uma chapa (em casos de teste).

[![clip_image034](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwsrGPHytI/AAAAAAAAA1Q/pOeuaagbJNI/clip_image034_thumb.jpg?imgmax=800 "clip_image034")](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwsq9voKhI/AAAAAAAAA1M/gl-s1BdmpA4/s1600-h/clip_image034%5B3%5D.jpg)

Aqui é definido se o bloco K200 será montado por centro de custo ou por seção. Para ser montado por centro de custo é necessário que os valores estejam distribuídos na ficha financeira em Movimentação | Centro de Custos.

[![clip_image036](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwssFGJQwI/AAAAAAAAA1Y/8JqsagAzhSw/clip_image036_thumb.jpg?imgmax=800 "clip_image036")](http://lh3.ggpht.com/_G7KXZLoZDsY/TGwsrnws0MI/AAAAAAAAA1U/JLV1Qig3hSQ/s1600-h/clip_image036%5B3%5D.jpg)

Aqui é definido se o sistema irá considerar a movimentação da ficha financeira ou da distribuição por tomadores de serviço para a composição dos blocos K250 e K300.

Obs : Essa caixa só será visível se, em Opções | Parâmetros | RM Labore | Param. Cálculo, o parâmetro **Utiliza Tomadores de Serviço** estiver marcado.

Obs.2: Para a marcação do segundo parâmetro recomenda-se a verificação do parâmetro **Meses de distribuição guardados, para a geração de Sefip em atraso**, presente em Opções | Parâmetros | RM Labore | Param. Cálculo, pois, caso o período das informações seja anterior ao número de meses definido nesse parâmetro, o sistema não terá mais tais informações, sendo necessária a restauração de backup em ambiente de teste para a recuperação das mesmas.

[![clip_image038](http://lh6.ggpht.com/_G7KXZLoZDsY/TGwstJ2FUdI/AAAAAAAAA1g/Xh6qev7Ijuk/clip_image038_thumb%5B1%5D.jpg?imgmax=800 "clip_image038")](http://lh4.ggpht.com/_G7KXZLoZDsY/TGwsstyZKMI/AAAAAAAAA1c/TBnkQfwSLik/s1600-h/clip_image038%5B4%5D.jpg)

Marque a opção caso queira que sejam considerados os autônomos cadastrados no RM Fluxus / RM Nucleus.

Se for necessário DESCONSIDERAR os autônomos cadastrados em uma determinada filial, essas filiais a NÃO serem consideradas, devem ser informadas no campo texto abaixo do parâmetro.

**Informações Adicionais:**

- O sistema salva o arquivo na pasta de instalação do sistema, dentro da pasta RM.Net\Execution Data, e copia após terminar a geração para o caminho informado na segunda tela. Caso ocorra erro ao copiar, esse arquivo pode ser resgatado no caminho original.

- Após a geração, leia o documento de Dicas e Soluções para o MANAD, onde explica como validar no SVA e corrigir os principais erros.

- É importante estar com a versão do sistema e da Biblioteca atualizada para a geração do arquivo.
