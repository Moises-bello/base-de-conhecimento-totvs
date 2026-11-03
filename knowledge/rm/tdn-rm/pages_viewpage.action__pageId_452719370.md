---
content_hash: 5233f98eb501a60505a9f453be2b1ec834411b4d7d4964190c10ad9a51b55b2f
fetched_at: '2026-06-29T00:10:07.174352+00:00'
page_id: '452719370'
product: rm
source: tdn-rm
title: Informações Contratuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719370
version: 33
---

As informações contratuais são obrigatórias para todos os empregadores, podendo ser registradas em livro, ficha ou sistema eletrônico, conforme orientação do Ministério do Trabalho.

**REGISTRO**  
Devem constar dados relativos à admissão do empregado, tais como: Número da Ficha de Registro, Tipo de Admissão, Data de Admissão, Data Base, Contrato com Prazo, Função, Salário, entre outros.

O campo **Data Base** atualmente não é utilizado por nenhum processo ou rotina nativa do produto TOTVS Folha de Pagamento. Trata-se de uma informação cadastral que pode ser usada na construção de Fórmulas, Consulta SQL, Relatórios, dentre outros.

Ao cadastrar um novo funcionário, o sistema preenche automaticamente, no momento do salvamento, o campo **Data Base** com a mesma data informada no campo **Data de Admissão**.

Possui Função de Confiança/Cargo em Comissão  
Será habilitado na tela a aba "Função de Confiança", onde poderá ser vinculado ao funcionário uma função de confiança/cargo em comissão. 

**Atenção:**

1. 1. 1. Para o eSocial a função de confiança/cargo em comissão representa uma posição diferenciada atribuída ao empregado na hierarquia da organização, superior ao cargo para o qual ele foi contratado, acompanhada de gratificação para o seu exercício.
      2. Apenas serão listadas as funções que estiverem com o parâmetro "Função de Confiança/Cargo em comissão" marcado no cadastro de função.
      3. Caso o Parâmetro "Possui Função de Confiança/Cargo em Comissão" seja desmarcado ,  o usuário deverá informar a "Data final da mudança"  e será gerado um gatilho para o evento S-2206 .

Reintegração  
Deverão ser preenchidos com as informações da reintegração do trabalhador previamente desligado da empresa, para atender o leiaute "S-2298 -Reintegração" do eSocial.

Os campos da aba "Reintegração" serão habilitados quando o campo "Tipo de admissão" for "I-Reintegração".

Os tipos de Reintegração são:

* **1-Reintegração por Determinação Judicial:** será habilitado o campo "Nro. Processo Jurídico".
* **2- Reintegração por Anistia Legal:** será habilitado o campo "Nro. da Lei de Anistia".

Na "Data da Reintegração" deverá preencher com a data a partir da qual o trabalhador deverá ser considerado como reintegrado. Devendo ser posterior a data de desligamento.  
Na "Data de Retorno Efetivo" informar a data do efetivo retorno ao trabalho, devendo ser igual ou posterior a "Data da Reintegração".

**Importante:** Os dados de Reintegração serão enviados ao eSocial no evento S-2298 -Reintegração. Se for realizada uma nova alteração de forma que o "Tipo de Admissão" deixe de ser Reintegração, será gerado um gatilho para o Evento de Exclusão (S-3000), excluindo o registro da Reintegração.

**Observações:**  
Somente funcionários que possuem rescisão efetivamente calculada podem ter a reintegração efetuada.

A reintegração pode ser efetuada de duas formas:

Utilizando o mesmo cadastro  
Informar "I" no campo "Tipo de admissão", retornar o funcionário para Situação A, ou seja, mantendo a matricula e data de admissão originais. Ao confirmar a reintegração o sistema exclui as rescisões existentes para o funcionário, retornando-o a situação normal.

Cadastrando um novo funcionário

Define que o funcionário será reintegrado utilizando matrícula e data de admissão novas e o campo "Tipo de admissão" igual a I.

Ao confirmar a Reintegração o sistema abre a tela do cadastro do funcionário com todos os campos preenchidos conforme sua matricula anterior, onde deve –se apenas informar a data de admissão e efetuar os ajustes desejados.  
 

O tipo de admissão dos autônomos deverá ser preenchido com 'O - Outros Casos' para emissão da folha analítica. Mesmo não sendo obrigatório preencher no cadastro de autônomos, o campo é necessário para emissão da folha analítica.

Quando o tipo de demissão for '5 - Transferência Sem Ônus p/ Cedente', o sistema irá preencher automaticamente o campo 'Tipo de Admissão' do registro ativo com 'T - Ent. Transf. Sem Ônus p/ Cedente' e o Motivo da Transferência informado no processo de transferência através do processo de Rescisão, podendo ser 'Sucessão, incorporação, cisão ou fusão', 'Empresa do mesmo grupo econômico' ou 'Estabelecimentos da própria empresa'. Quando o Motivo da Transferência é 'Sucessão, incorporação, cisão ou fusão', o sistema habilita a aba Sucessão de Vínculos.  
 

Dados do Contrato  
Nesta aba é possível informar se o funcionário possui contrato com prazo determinado ou de experiência.  
 

**Tipo de contrato -** Se o contrato possui prazo determinado ou se é de experiência.  
   
**Tipo de contrato por prazo determinado -** Caso seja selecionado no campo anterior "Contrato com prazo determinado" esse campo será habilitado, onde será informado se o contrato é "definido em dias" ou "vinculado à ocorrência de um fato".  
   
**Motivo da contratação por prazo determinado -** Em caso de contrato com prazo determinado vinculado à ocorrência de um fato, será necessário descrever qual o motivo que se deu a essa contratação.

Trabalhador Temporário  
O campo  "**Hipótese legal para Contratação Trabalhador Temporário"** tem as opções**:**

* Demanda Complementar de Serviços
* Necessidade de substituição transitória de pessoal permanente

Sendo um funcionário do tipo **B –**Temporário com redução de encargos**, F –**Temporário / Comissionista ou**P –**Temporário**,**quando na aba Trabalhador Temporárioo campo**Hipótese legal para Contratação Trabalhador Temporário**for preenchido com ainformação**Necessidade de substituição transitória de pessoal permanente,**o campo **CPF do Funcionário Substituído**será habilitado**,** neste, selecionar o funcionário que foi substituído temporariamente, caso o funcionário ao qual realizou a substituição esteja na situação demitido será necessário marcar a flag "Exibir funcionários demitidos" (**observação:** nos casos de cadastro retroativo).   
**Justificativa para prorrogação do Contrato** O usuário deverá informar a Justificativa de prorrogação de contrato de trabalho necessária para atender ao leiaute "S-2206 -Alteração de Contrato de Trabalho" do eSocial . **Tipo de Inclusão de contrato** Informar o tipo de inclusão de contrato: 1 - Locais sem filiais; 2 - Estudo de mercado; 3 - Contratação superior a 3 meses.   
 

Sucessão de Vínculos  
Os campos da aba 'Sucessão de Vínculo' serão habilitados, quando o campo 'Tipo de Admissão' for 'T - Ent.Transf sem ônus p/Cedente'. Deverão ser preenchidas as informações de Sucessão de vínculo do trabalhado para atender o leiaute S-2200- Admissão /Ingresso de Trabalhador. Os campos CPF/CNPJ Empregador Anterior, Matricula Anterior e Data início do Vínculo, são preenchidos automaticamente para a chapa ativa quando é feito o processo de Transferência sem Ônus p/ Cedente (tipo 5) através do processo de demissão. Caso seja feito uma admissão nova, a informação pode ser incluída manualmente.  
   
Caso o tipo de demissão seja '6 - Transferência com Ônus p/ Cedente', será preenchido com 'E - Ent. Transf. Com Ônus p/ Cedente'.  
Para maior agilidade na admissão do funcionário, o sistema dispõe do recurso em gerar o nº da ficha de registro automaticamente. Para isso, deverá marcar o parâmetro 'Número da Ficha de Registro gerado pelo sistema' existente em Parametrizador | Funcionário | Configuração de Registro.

**Observações:**

* + O sistema apresentará uma mensagem de alerta caso o usuário informe um número de ficha de registro zero ou deixe em branco.
  + Não será permitido trocar a chapa de um funcionário que tenha o número de ficha de registro zero ou em branco, com exceção de funcionários do tipo Estagiário ou Autônomo, quando estiver marcado o parâmetro 'Não cadastrar número de Ficha de Registro para Estagiários e Autônomos' existente em Parametrizador | Funcionário | Configuração de Registro.

Dados do beneficiário Órgão Público

Serão cadastrados nesta aba os dados do beneficiário que terão direito a receber os benefícios pagos pelos órgãos públicos. Esta aba será habilitada quando o parâmetro 'Beneficiário entes Públicos' existente no cadastro do funcionário estiver marcado ou o tipo de funcionário for "W-Beneficiário".

**ATENÇÃO:**

* + O campo "**Matrícula****Benefício**" deverá ser igual a matrícula do servidor/militar (campo **Matrícula eSocial**) constante na base do TOTVS Folha de Pagamento do órgão cujo vínculo deu ensejo ao benefício. No caso de pensão por morte, informar a matrícula do instituidor da pensão.
  + Em caso onde o benefício é não oriundo de um vínculo laboral e/ou bem como os concedidos antes da obrigatoriedade dos eventos não periódicos, o cadastro desse campo fica opcional.
  + No caso dos benefícios concedidos por órgão diverso do declarante do vínculo laboral, o cadastro desse campo não possui uma  mascara pré determinada.

Estatutário/ Mandato Eletivo

Serão cadastrados neste aba os dados do estatutário ou mandato eletivo. Os campos Estatutário nessa aba serão habilitados quando o tipo de funcionário for "E - Estatutário" e código de categoria do eSocial for  301, 302, 303, 306, 307, 309, 310, 312. Os campos Mandato Eletivo nessa aba serão habilitados quando o tipo de funcionário for "E - Estatutário" e código de categoria do eSocial for  304. 

Ahgora

Na aba "Ahgora", estará disponível a opção para o uso do **Ponto Web Ahgora**. Os funcionários poderão marcar ou desmarcar a utilização do cartão de ponto, o que permitirá que sejam incluídos em todo o processo de coleta e verificação das marcações de ponto Ahgora.

Dados do aprendiz

Serão cadastrados nesta aba os dados do funcionário aprendiz. Esta aba será habilitada quando o funcionário possuir código de categoria do eSocial igual a  '103 - Empregado - Aprendiz'.

**ATENÇÃO:**

* + O campo Modalidade de Contratação pode receber dois valores Direta ou Indireta, sendo:

a) Contratação direta: contratação do aprendiz efetivada pelo estabelecimento cumpridor da cota de aprendizagem

b) Contratação indireta: contratação do aprendiz efetivada por entidades sem fins lucrativos ou por entidades de prática desportiva a serviço do estabelecimento cumpridor da cota 

* + O campo CNPJ do estabelecimento onde estão sendo realizadas as atividades práticas, quando ocorrer uma das situações abaixo:

a) Modalidade alternativa de cumprimento de cota de aprendizagem (neste caso, informar o CNPJ da entidade concedente da parte prática);  
b) Realização das atividades práticas na empresa contratante do serviço terceirizado;  
c) Centralização das atividades práticas em estabelecimento da própria empresa, diverso do estabelecimento responsável pelo cumprimento da cota. 

* + O campo CNPJ da Entidade Qualificadora(no caso de contratação direta) ou CPF/CNPJ do empregador cotista (no caso de contratação indireta)

**Indicativo de Admissão**  
Corresponde ao motivo da admissão, serão listados os indicativos disponibilizados leiaute S-2200- Admissão /Ingresso de Trabalhador do eSocial.  
   
**Código da Categoria eSocial**  
Preencher com o código da categoria do trabalhador conforme tabela 1 do eSocial.

**Tipo de Funcionário**  
Quando o campo Tipo de Funcionário for preenchido com **B – Temporário com redução de encargos, F – Temporário / Comissionista ou P – Temporário** será habilitada a aba **Trabalhador Temporário** para devido preenchimento das informações.

 **Tipo de Regime trabalhista**

Identifica o regime trabalhista do funcionário para envio dos eventos do eSocial.  
   
**Salário / Jornada**  
Constam as informações cadastrais básicas para cálculo da folha de pagamento do funcionário. A fixação do salário e da jornada deve estar prevista no contrato de trabalho celebrado não podendo ultrapassar os limites estabelecidos na legislação vigente.

**Contrato de trabalho em regime de tempo parcial:**  
Contrato de trabalho em regime de tempo parcial, ou seja, aquele cuja jornada semanal não exceda:

* Limitado a 25 horas semanais;
* Limitado a 26 horas semanais;
* Limitado a 30 horas semanais;
* Não é um contrato em tempo parcial.

**Atenção:** São informações referentes ao contrato de trabalho necessárias para atender aos leiautes   S-2200- Cadastramento Inicial do Vínculo e Admissão /Ingresso de Trabalhador  e  "S-2206 -Alteração de Contrato de Trabalho".  
**Tipo de regime da jornada:**  
Identifica o regime de jornada do funcionário.   
**Atenção:** **Este campo é utilizado na geração do eSocial  leiautes**S-2200- Cadastramento Inicial do Vínculo e Admissão /Ingresso de Trabalhador **e**  "S-2206 -Alteração de Contrato de Trabalho".

**Descrição do Salário Variável**  
Registrar a **descrição do  Salário Variável,** que será habilitado quando, o tipo de funcionário for **F –** Temporário/Comissionista**, M –** Misto ou **O –** Comissionista .

**Contrato de trabalho em regime de tempo parcial:**  
Contrato de trabalho em regime de tempo parcial, ou seja, aquele cuja jornada semanal não exceda 25 horas semanais. Valores Válidos: S, N.  
   
**Observações:**  
Quando tiver integração com o Gestão de Pessoas:  
1. Ao fazer a inclusão de um funcionário, e o usuário cadastrar os campos de Função, Faixa salarial, Nível salarial e Seção, o sistema trará o valor do salário conforme tabela salarial do Gestão de Pessoas.   
Neste caso, no momento da inclusão o salário estará zerado para que o sistema possa incluir o salário da tabela salarial.   
   
2. Caso o Gestão de Pessoas esteja parametrizado para trabalhar com Tabela Salarial ao alterar a Função, Nível ou Faixa Salarial do funcionário, o campo 'Salário' será automaticamente atualizado, e a alteração será registrada nos respectivos históricos.  
   
3. Ao alterar o salário do funcionário acima ou abaixo do valor estipulado na tabela salarial do Gestão de Pessoas, será apresentada a mensagem de alerta no momento de salvar a alteração no Folha de pagamento, apenas informando que a alteração foi feita para um valor diferente do nível e faixa da tabela do Gestão de Pessoas e esta alteração será processada normalmente.   
   
4. Quando o usuário possuir licença para Gestão de Pessoas, a alteração salarial não será realizada se o mesmo estiver parametrizado para trabalhar com Controle de Lotação por Verba caso o limite de verba determinada venha a exceder, sendo considerado também a verba disponível.  
   
Definir a natureza do vínculo do empregado com a empresa, informando o 'Tipo de Funcionário' e 'Tipo de Recebimento'.  
   
**Observações:**  
1. Os tipos de funcionários: 'F-Temporário/Comissionista', 'O-Comissionista' e 'P-Temporário', tem as mesmas características;  
   
2. Para funcionários do tipo 'B-Temporário com redução de encargo' existem parametrizações para atender a legislação - Lei número 9.601, de 21 de janeiro de 1.998 - (DOU 22.1.98).  
   
**Atenções:**  
1. No cálculo da guia de INSS apenas as alíquotas das contribuições sociais destinadas ao serviço social das indústrias (SEST, SENAT, SESI, SENAI, SENAC, SEBRAE e INCRA) e acidente de trabalho serão reduzidas a 50%  
   
2. A alíquota de recolhimento de FGTS será de 2% (dois por cento).  
   
3. No cálculo da rescisão, o funcionário não terá direito a aviso prévio e a indenização dos 40% de FGTS.  
   
4. Em conformidade com o disposto no artigo 2º da Lei 10.097/00, onde altera o artigo 15º da Lei 8036/90, que determina que os contratos de aprendizagem com admissão a partir de 20/12/2000 tenham sua alíquota do FGTS reduzida, o funcionário do tipo 'Z-Aprendiz' terá o recolhimento de FGTS de 2% (dois por cento) ou invés de 8% (oito por cento).  
   
5. Para o código de recebimento 'P-Horista (Professor)' o sistema permitirá digitar o salário hora, quando o parâmetro 'Edita salário mensal para horistas/tarefeiros" existente em Parametrizador | Folha Normal | Horistas e Tarefeiroestiver desmarcado.  
   
**Atenção:**  
O tratamento do cálculo para o código de recebimento 'P-Horista (Professor)' será o mesmo do mensalista, porém nos relatórios (RAIS, DIRF, CAGED, SEFIP, etc) será tratado como horista.  
Para o código de recebimento 'H-Horista', quando utilizar o cadastro de funcionário .NET e o parâmetro 'Permite salário hora com mais de duas casas decimais' existente em Parametrizador | Folha Normal | Horistas e Tarefeiroestiver marcado, tanto o salário hora do cadastro do funcionário como o salário hora do histórico salarial, terão as casas decimais limitadas a 5 dígitos.   
No DELPHI é limitado a 13 dígitos.  
   
**Dados do Estágio**  
Este cadastro somente será disponibilizado quando o campo 'Tipo de Funcionário' for  'T – Estagiário'  
   
São informações, sobre o estágio, necessárias para atender ao leiaute S-2300 - Trabalhados sem vinculo de emprego/Estatutário-inicio.  
   
A entidade apresentada nos campos 'Instituição de Ensino do Estágio' e 'Agente de Integração do Estágio' poderá ser previamente cadastrada em Gestão de Pessoas | Desenvolvimento | Entidade ou por meio do ícone de inclusão na tela de localização de '**Entidades'**.   
   
   
   
   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
