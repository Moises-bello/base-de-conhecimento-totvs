---
content_hash: d610246dd993ebd8648b706b53ab739c81d28ceabee7421185bafffb81755256
fetched_at: '2026-06-29T00:05:57.728239+00:00'
page_id: '181964393'
product: rm
source: tdn-rm
title: Dicas e Soluções - DIRF, Informe de Rendimentos e RAIS 2022 (Ano Base 2021)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=181964393
version: 14
---

**A partir das versões:**

12.1.32.xxx ou superior  
12.1.33.xxx ou superior  
12.1.34.xxx ou superior

# Objetivo:

---

Este documento contém os principais incidentes que poderão ocorrer na geração dos relatórios anuais obrigatórios (DIRF/INFORME DE RENDIMENTOS e RAIS). O objetivo principal é apresentar as possíveis soluções de forma clara e resumida para auxiliar nas correções ou sanar as principais dúvidas que geralmente ocorrem ao gerar os arquivos.

---

**INCIDENTE 01**

**QUESTÃO:** Ao validar o arquivo no programa da DIRF, o parâmetro "Efetuou pagamentos a plano privado de assistência à saúde - coletivo empresarial" não está sendo marcado automaticamente. Como faço para que ele venha marcado?

**POSSÍVEL SOLUÇÃO:**

1- Para que esse parâmetro seja marcado, é preciso conter a seguinte parametrização no labore no ato da geração da DIRF: Acesse relatórios/dirf/ vá em "opções de emissão", aba "declarante" e no campo " Indicador assistência saúde coletivo empresarial" deve estar com a opção 2 selecionada, ou seja, "existe pagamento de valor pelo titular/dependente do plano de saúde". Marque essa informação, gere novamente a DIRF e verifique que o parâmetro será marcado.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 02**

**QUESTÃO:** Os valores de Assistência Médica não saem na DIRF.

**POSSÍVEL SOLUÇÃO:**

1- Para que as informações de Assistência Médica sejam levadas, ao gerar a "DIRF em arquivo", é preciso acessar "Anuais | Dirf/Informe de Rendimentos", selecionar a opção "DIRF em Arquivo" e na tela "Parâmetros da coligada", aba "Geral | DIRF em Arquivo | Declarante",  no campo "Indicador assistência saúde coletivo empresarial" deve estar com a opção “2 -Existe pagamento de valor pelo titular/dependente do plano de saúde” selecionada, conforme figura abaixo.

2- Informar os eventos de Assistência médica na aba “Operadora de Assistência a Saúde“. Esta é a última aba existente nos Parâmetros da Coligada. Caso não a visualize, caminhe através das setas disponíveis na parte superior do menu. Ao acessar a aba, siga os passos conforme apresentado na figura abaixo, para cadastrar os eventos;

3- Para visualizar os valores no programa da DIRF, certifique-se que está selecionando a operadora e os dados do titular. O aplicativo importa os valores e, na visualização, ele apresenta um registro sem informações. Neste caso, é necessário clicar em “Operadora Anterior” e/ou “Titular anterior” para visualizar as operadoras e titulares que tiveram o desconto, conforme apresentado nas figuras abaixo:

                 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 03**

**QUESTÃO:** Ao gerar a DIRF é apresentada a mensagem a seguir: “Erro ao gerar DIRF em arquivo. Não é possível um controle desabilitado ou invisível ganhar foco.“

**POSSÍVEL SOLUÇÃO:**

1- Este erro pode ocorrer quando o CPF do Responsável pelo CNPJ não está preenchido (vide figura abaixo). Para correção selecione o menu “Anuais | Dirf/Informe de Rendimentos”, clique na aba “Geral | DIRF em Arquivo | Pessoa Jurídica” e preencha no campo “CPF do Responsável pelo CNPJ” a informação correspondente.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 04**

**QUESTÃO:** Ao gerar a DIRF/INFORME DE RENDIMENTOS pode ocorrer a seguinte mensagem: “Aviso: O(s) seguinte(s) funcionário(s) não foram relacionado(s) pois possuem valor de rendimentos abaixo de R$ 28.559,70 e não tiveram retenção de IRRF:"

**POSSÍVEL SOLUÇÃO:**

1- Trata-se apenas de um aviso. O sistema vai gerar um log contendo uma listagem dos funcionários que se enquadraram na mensagem de aviso apresentada. Verifique se os funcionários que serão listados realmente tiveram total de rendimentos abaixo do valor apresentado. Geralmente, referem-se a funcionários que ficaram afastados no ano base selecionado ou que foram demitidos em anos anteriores e receberam verbas de diferenças ou de rescisões complementares no ano base da DIRF. Basta verificar se estes funcionários deverão realmente constar no arquivo.  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 05**

**QUESTÃO:** Ao gerar RAIS ocorre o erro: “O registro não possui o tamanho esperado.“

**POSSÍVEL SOLUÇÃO:**

1- Esse erro pode ocorrer, pois o flag "Gera RAIS Genérica" está marcado. Para desmarcá-lo acesse o menu "Anuais | RAIS", tela "Parâmetros".

Obs: Com o parâmetro “Gera RAIS Genérica" marcado, o arquivo será gerado conforme layout do programa GDRAIS Genérico que permite informar os anos base 1976 a 2005. Para maiores informações, consulte o site [www.rais.gov.br](http://www.rais.gov.br).  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 06**

**QUESTÃO:** Ao gerar a Rais ocorre o erro: “Indicador de Atividade no ano-base inválido.”

**POSSÍVEL SOLUÇÃO:**

Esse erro ocorre quando, nas seções centralizadoras, o campo "ano base" e o parâmetro "exerceu atividade no ano base" não estão preenchidos/marcados. Sendo assim, acesse o cadastro das seções centralizadoras dos seus funcionários em Anexos/Dados Anuais da Rais e verifique essas informações. Caso seja necessário, preencha os campos citados acima e gere a RAIS novamente. Veja as figuras abaixo.

 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 07**

**QUESTÃO:** Ao validar a RAIS ocorre o erro: “Valor de contribuição Associativa só dever ser informado para funcionários sindicalizados."

**POSSÍVEL SOLUÇÃO:**

1- Esse erro acontece quando o sistema encontra valor de contribuição associativa ou confederativa para o funcionário e o mesmo não é sindicalizado, esses tipos de contribuições são permitidas apenas para funcionários sindicalizados. Normalmente ocorre porque foi informado valor de contribuição, mas o sistema não está parametrizado para verificar qual funcionário é sindicalizado. Para parametrizá-lo será necessário criar um campo complementar em “Cadastros/campos complementares/funcionários”, do tipo alfanumérico, tamanho 1, valor default S ou N. Este campo será utilizado para informar se o funcionário é sindicalizado ou não.

Em seguida, deverá informar o campo complementar criado acima, em RELATÓRIOS / RAIS / Avance até a tela de Seleção de coligadas, clique em "Adicionar Parâmetros a Coligada"/ CAMPOS COMPLEMENTARES/ INDICADOR DE SINDICALIZADO.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 08**

**QUESTÃO:** Ao validar a RAIS ocorre o erro: “A importação não poderá ser realizada. O arquivo não atende as especificações definidas para o ano-base.“

**POSSÍVEL SOLUÇÃO:**

A versão da Biblioteca e/ou Aplicativo utilizados podem não estar compatíveis com a rotina do ano vigente. Para obter mais informações em relação as versões que atendem as especificações para a geração da RAIS, entre em contato com o suporte da totvs.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 09**

**QUESTÃO:** Os valores de Assistência Médica para os dependentes não foram levados para DIRF.

**POSSÍVEIS SOLUÇÕES:**  
1- Verifique o Incidente 02 deste documento;

2- Para que o valor de Assistência Médica por dependente seja informado na DIRF, o sistema utilizará as informações cadastradas no Histórico de Assistência à Saúde. Este Histórico fica disponível no cadastro de funcionários, aba Registro, sub aba “Histórico Assistência à Saúde”.

Os valores poderão ser informados manualmente ou a fórmula de cálculo dos eventos de desconto de Assistência Médica deverão ser adequadas para o preenchimento automático dos históricos.

Nos links abaixo, é possível obter maiores informações referentes aos valores de Assistência Médica.

**Como Fazer – Histórico de Assistência à Saúde:**

**Como Fazer – Preenchimento Histórico de Assistência à Saúde – Método por Backups:**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**INCIDENTE 10**

**QUESTÃO:** Como enviar comprovante de Rendimentos por email.

**POSSÍVEIS SOLUÇÕES:**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 11**

**QUESTÃO:** Alguns valores da Ficha Financeira não foram considerados na DIRF.

**POSSÍVEL SOLUÇÃO:**

1- Seguir os passos abaixo:

**1º Passo:** Conferir a data de admissão do funcionário;

**2º Passo:** Verificar se existe movimentação na ficha financeira referente à data que está sendo gerado o Informe de rendimentos/Dirf do funcionário (verifique a data de pagamento e o caixa);

**3º Passo:** Verificar no módulo, AMBIENTE| PARÂMETROS|FOLHA DE PAGAMENTO, Módulo Folha normal / Ficha financeira, o número de meses constantes no campo "Meses a manter na ficha financeira".

Se o período da geração do relatório for maior do que o número de meses guardados, deverá então efetuar a restauração da ficha financeira complementar, através do módulo "ROTINAS -> RESTAURAÇÃO DA FICHA FINANCEIRA COMPLEMENTAR".

OBS: após a liberação de competência, os meses restaurados voltarão para as tabelas complementares.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 12**

**QUESTÃO:**Clientes que tem base Oracle podem se deparar com o erro:

"General SQL error ORA-01410 invalid ROWID"

**Possível Solução:**

Para solucionar, altere o BDE em: CONFIGURATION | DRIVERS | NATIVE | ORACLE, os campos abaixo:

* DLL32 = SQLORA8.DLL
* VENDOR INIT = OCI.DLL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 13**

**QUESTÃO:**

Pode ocorrer de que funcionários que recebem pró-labore sejam levados na DIRF com a natureza do rendimento definida como "Rendimentos do trabalho sem vínculo empregatício" sendo que o correto seria "Rendimento trabalho assalariado".

**Possível Solução:**

O sistema considera o código de retenção 0588 (IRRF - Rendimento do trabalho sem vínculo empregatício) para Diretores com categoria 5 (Diretor não empregado com FGTS) ou categoria 11 (Diretor não empregado sem FGTS) do SEFIP. Para que o código de retenção seja 0561 (IRRF - Rendimentos do trabalho assalariado no País/Ausente no exterior a serviço do País) o funcionário tem que estar na categoria 1 (Empregado).

Para localizar a informação no sistema acesse: **Cadastro | Funcionários**; edite o registro do funcionário e acesse **FGTS/SEFIP**.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 14**

**Causas**

Pode ocorrer situações em que o valor do 13º Salário não esteja sendo levado para o campo “**RENDIMENTOS SUJEITOS A TRIBUTAÇÃO EXCLUSIVA (RENDIMENTO LÍQUIDO)**”.

**Solução**

É fundamental que a data de pagamento do 13º Salário esteja no **caixa 12 do ano da geração** e preferencialmente o dia do pagamento igual a 20 (20/12/xxxx), o fato do valor não sair neste campo pode ocorrer devido a um lançamento realizado com data de pagamento incorreta como,por exemplo em Janeiro (05/01/xxxx).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 15**

**Causas**

Algumas vezes durante a geração da DIRF algumas pessoas podem se deparar com os seguintes erros :

"Arquivo para informações Debug inválido Tfile info. Creatre: Erro 32 ao abrir o arquivo "LogDirf.txt"

"Erro ao gerar a Dirf em disquete. Erro de Erro de Entrada / Saída nº **XXX**."

***Obs****.: O **XXX** informado acima pode variar.*

**Solução**

Devemos avaliar duas situações:

**1ª** – O arquivo está sendo gravado na rede e não na máquina local.

**R** – Para essa situação faz-se necessário que o arquivo seja salvo em um local onde tenha permissão para criação de arquivos.

**2ª** – O arquivo está sendo gravado na própria máquina (local).

**R** – Para essa situação devemos alterar o diretório onde o arquivo está sendo salvo para um local da máquina onde tenha permissão para criação de arquivos.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**INCIDENTE 16**

**Causas**

Acontece em alguns clientes situações como por exemplo, em que funcionários não são importados na DIRF.

**Solução**

Com essa situação listamos algumas informações que devem ser analisadas:

* Grade de seleção de funcionários para a geração.
* Filtros de seleção.
* As Opções de Seleção.
* Período de Referência.
* Código de Quebra (Sempre deve ser informado “?”, pois o arquivo deve ser consolidado no CNPJ principal da empresa e não por filial).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

 **INCIDENTE 17**

**Causas**

Podem ocorrer situações com erro de caracteres inválidos.

**Solução**

Para esse tipo erro, primeiramente temos que avaliar onde a mensagem está informando a origem do erro, por exemplo, caracteres inválidos no nome/nome empresarial.

Com isso retirar acentos, apóstrofos, etc...

**INFORMAÇÕES ADICIONAIS:**

**Para melhor conferência dos valores do informe de rendimentos utilize o log da DIRF. Essa opção fica disponível ao selecionar para emitir "DIRF Para Conferência".**
