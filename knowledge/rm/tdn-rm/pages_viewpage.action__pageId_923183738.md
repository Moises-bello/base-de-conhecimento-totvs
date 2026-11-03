---
content_hash: 59151141d4fe1a0e157cea79a53a705a209daf9a0758708b1d6367ac22cc2ff7
fetched_at: '2026-06-29T00:12:07.327708+00:00'
page_id: '923183738'
product: rm
source: tdn-rm
title: Possíveis divergências e erros no Lançamento Financeiro "25 - Total Guia INSS
  DCTFWeb" e no Relatório de Conferência de INSS Patronal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=923183738
version: 37
---

## Objetivo:

---

Este documento tem como objetivo auxiliar o usuário na identificação e resolução de diferenças entre o **lançamento financeiro 25 - Total Guia INSS DCTFWeb** e o **Relatório de Conferência de INSS Patronal**, além de outras situações que possam gerar erros ou divergências.

Para isso, é necessário analisar as seguintes informações:

---

**01.** Verificar sempre as parametrizações abaixo:

No menu Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Encargos Sociais é necessário esta com o parâmetro ”**Trunca valores de FGTS/INSS**” marcado, conforme demonstrado no print abaixo:

No menu Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Encargos Sociais é necessário esta com os parâmetros ”**Habilita Histórico de INSS no Cadastro de Seção**" e "**Discrimina Percentual de Terceiro**" marcados, conforme demonstrado no print abaixo:

No menu Cadastros | Seções a seção centralizadora precisa ter o anexo “**Histórico de Percentuais para INSS**” preenchido com as informações dos percentuais discriminados de terceiros conforme abaixo:

**02.**Caso no cadastro do lançamento financeiro a opção "**Desconsiderar Autônomo TOTVS Gestão Financeira**" esteja desmarcada, os eventos/verbas informados no menu Configurações | Parametrizador | eSocial | Autônomos e Externos precisam estar configurados com o código de cálculo 3, conforme demonstrado no print abaixo:

**03.** Caso no cadastro do lançamento financeiro a opção "**Desconsiderar Autônomo TOTVS Gestão Financeira**" esteja marcada, o sistema fará o seguinte cálculo:

Cálculo para geração do lançamento financeiro:

* + Busca o valor “Total Folha” do **Relatório de Conferência de INSS** **Patronal** e abate o valor de autônomos, esse valor poderá ser obtido no **Relatório de Conferência de INSS** usando filtro avançado para selecionar as categorias de autônomos.

Lembrando que, ao marcar o parâmetro **"Desconsiderar Autônomos TOTVS Gestão Financeira"**, o lançamento financeiro **ficará divergente do governo**, conforme descrito no **TDN**. <https://tdn.totvs.com/display/LRM/Cadastros+Financeiros>

**04.** Quando existir diferença de centavos, possíveis causas:

**04.1.** **Considera Autônomo TOTVS Gestão Financeira**

Quando os valores de BASE INSS e desconto INSS são extraídos do produto TOTVS Gestão Financeira, identificamos que, ao calcular o desconto de INSS, o módulo TOTVS Gestão Financeira arredonda o valor, enquanto o eSocial trunca. Caso seja necessário que os valores sejam truncados de forma semelhante ao eSocial, será necessário abrir uma demanda para a equipe responsável pelo TOTVS Gestão Financeira.

Exemplo do cálculo no TOTVS Gestão Financeira: Base INSS: R$556,64.

* + - Alíquota: 20%
    - Cálculo: R$556,64 × 20% = R$111,3**28**

O TOTVS Gestão Financeira arredonda o valor para **R$111,33**, enquanto o governo sempre **trunca**, considerando **R$111,32**. Isso gera uma diferença de **R$0,01**, conforme demonstrado na tela abaixo:

**04.2.** **Diferença de cálculo de arredondamento no Governo nas tags <vrCpSeg> e <vrDescSeg>**

Os valores calculados pelo governo para alguns funcionários **ficam maiores** do que os valores processados na folha, conforme explicação abaixo:

* + No evento **S-5001**, o eSocial retorna os valores calculados para o INSS do funcionário por meio de duas tags:

**vrCpSeg**: Valor da contribuição do segurado, devida à Previdência Social, calculada segundo as regras da legislação em vigor, por CR.

**vrDescSeg:** Valor efetivamente descontado do segurado, correspondente a tpValor = [21] do correspondente infoCpCalc/tpCR.

* + No **Relatório de Conferência do INSS**, na parte **analítica**, utilizamos a tag <**vrCpSeg**>, pois trata-se do detalhamento por funcionário. Já na parte **sintética**, utilizamos a tag <**vrDescSeg**>, que representa o total por CPF. Esses valores podem divergir quando o funcionário possui **múltiplos vínculos**, caso contrário o valor será o mesmo.

Identificamos que o eSocial está realizando cálculos diferentes para esses dois campos, sendo que o correto seria retornar o mesmo valor: em um deles, o valor é **truncado**, enquanto no outro, é **arredondado** na terceira casa decimal.

Diante disso, como o problema ocorre no **eSocial**, recomendamos a abertura de uma demanda junto ao governo.

No entanto, é importante ressaltar que não haverá impacto na **DCTFWeb** gerada pelo governo nem na geração do financeiro, pois ambos consideram a tag <**vrDescSeg**>.

****05.**** Na gera lançamento do financeiro financeiro está sendo apresentado o erro "Column 'CODCOLIGADA, IDLAN' is constrained to be unique.".

Verifique se há configurações incorretas nas seções, como:

1. Seções do mesmo CNPJ apontando para uma filial diferente da centralizadora.
2. Outras seções centralizadoras apontando para uma filial já vinculada a outro CNPJ.

**06.** Quando na geração do lançamento financeiro é apresentado erro na finalização e não gera o lote financeiro.

Isso pode ocorrer quando o histórico da categoria eSocial esta incorreto.

****07.**** Quando o percentual de Aposentadoria Especial informado na seção do funcionário não for considerado.

Para calcular corretamente o percentual de aposentadoria especial, é imprescindível que as informações sejam inseridas na seção centralizadora. Este é um comportamento padrão no produto garantindo que os valores sejam exibidos de forma adequada na verificação junto ao e-Social. É importante destacar que tanto o lançamento financeiro quanto o relatório patronal são fundamentados no arquivo XML de retorno do evento S-5011, que é disponibilizado por estabelecimento (filial).

****08.**** Quando o lançamento gerado não bate com o valor da rastreabilidade do lançamento.

A diferença na rastreabilidade do lançamento financeiro pode ocorreu devido à presença de autônomos do TOTVS Gestão Financeira. A rastreabilidade existente foi desenvolvida exclusivamente para funcionários cadastrados na folha de pagamento, sendo a chapa o identificador utilizado. Inclusive a antiga GPS - Guia de INSS também não contemplava esse cenário. Diante disso, caso a rastreabilidade dos autônomos seja realmente necessária, será preciso abrir uma solicitação de melhoria em nossa central colaborativa, para que seja feita uma análise de viabilidade de implementação.

****09.**** Quando está ocorrendo a geração do lançamento financeiro para os autônomos da folha e não deveria.

O lançamento financeiro considera a soma do valor de segurados mais a soma da parte empresa dos autônomos.

Verificar se o campo "**% Autônomo**" existente em Cadastros | Seções | Anexo Histórico de Percentuais para o INSS está correto. Caso o cliente entenda que a base de autônomos não tem parte empresa ele deverá zerar este campo para que o lançamento financeiro seja gerado somente com o valor de segurados.

****10.**** Ao gerar o lançamento financeiro para um funcionário autônomo de uma organização 100% filantrópica, o sistema está considerando 20% da base, em vez de apenas o valor do segurado, conforme a DCTFWeb.

Para empresas filantrópicas, é necessário que os valores estejam zerados em Cadastros | Seções | Anexo Histórico de Percentuais para o INSS.

**11.** Quando existir diferença entre o lançamento financeiro e a DCTFWeb gerada pela Receita.

A diferença pode ocorrer porque o valor da parte empresa é **truncado** quando o parâmetro **"Trunca valores de FGTS/INSS"** está ativado. Esse parâmetro pode ser encontrado no menu:  
Configurações | Parametrizador | Encargos Sociais.

**12.** Quando na geração do lançamento financeiro, o sistema está realizando o rateio de 50% para a seção centralizadora e 50% para a seção do funcionário. No entanto, o comportamento correto é que o valor seja rateado integralmente apenas para a seção do funcionário.

Para que o lançamento financeiro utilize exclusivamente o centro de custo da seção do funcionário, é necessário **deixar desmarcado** o parâmetro abaixo no momento da geração:

Com esse parâmetro desmarcado, o lançamento será gerado corretamente, utilizando apenas o centro de custo da seção do funcionário.

**13.** Quando está ocorrendo diferença na geração do Relatório de INSS Patronal.

Verificar se foi gerada sua distribuição no mês da rescisão, caso não tenha sido, será necessário realizar a distribuição conforme demonstrado abaixo através do menu Encargos | FGTS | Distribuir Tomador: 

**14.** Quando existir diferença entre os campos Total FOLHA e Total DCTFWEB Relatório de Conferência INSS Patronal.

Verificar no menu Cadastros | Seções | Anexo Histórico de Percentuais para o INSS, na seção centralizadora, se:

1. A vigência não está vencida.
2. O campo "%Autônomos" não está zerado.

**15.** Quando existir divergência de base entre os Relatórios de Conferência Patronal X eSocial no campo empresa.

Verificar no menu Administração de Pessoal| Funcionários | Anexos | Histórico Ocorrência SEFIP, se a ocorrência informada e a data de mudança estão corretas e compatíveis com o cadastro do funcionário.

**16.**Lançamento financeiro por filial X dedução da licença maternidade

Atualmente, a dedução da licença maternidade na DCTFWeb ocorre no nível da estrutura da empresa, sendo aplicada exclusivamente sobre a parte previdenciária.

Quando o lançamento financeiro está parametrizado por filial e o valor da licença maternidade excede o total da contribuição previdenciária, pode haver divergência no valor líquido. Isso acontece porque a dedução é aplicada apenas sobre a parte previdenciária, mantendo inalterado o valor referente aos terceiros.

➡️ **Saiba mais:**  
 

**17.** Valores negativos da Contribuição Previdenciária (CP) Patronal no Relatório de Conferência de INSS Patronal

Verificar os percentuais da empresa e de autônomos definidos nas seções.  
Se houver **quebra de FPAS**, é necessário garantir que os percentuais estejam corretamente cadastrados em todas as quebras existentes. A ausência dessa configuração pode gerar inconsistências nos cálculos apresentados.

**18.**Ao gerar oRelatório de Conferência Patronal, os valores referentes aos autônomos, como base de INSS e desconto patronal, não são apresentados.

Ao acessar o job de cálculo do relatório através do menu Ambiente | Gerenciamento de Jobs, é exibida a seguinte inconsistência:

> “Autônomo código 19394808001443 não lançado. Tipo do tomador diferente da parametrização.”

É necessário acessar o menu Administração de Pessoal | Cliente e Fornecedor, editar o autônomo listado e ajustar o campo **Tipo de Tomador,** na aba Tributos, de acordo com a classificação do tipo de tomador utilizada pela empresa.

---

**OUTROS LINKS**

[Perguntas DCTFWeb](https://tdn.totvs.com/display/public/LRM/Perguntas+DCTFWeb)
