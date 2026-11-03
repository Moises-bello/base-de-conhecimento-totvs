---
content_hash: db670350da55fc1e9613be571e07d74fbb9f9eaf19ea42798dfa9dbd6b7579f1
fetched_at: '2026-06-29T00:10:06.598235+00:00'
page_id: '452719319'
product: rm
source: tdn-rm
title: Histórico de Afastamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719319
version: 13
---

Em caso de afastamento do empregado ao longo do vínculo empregatício a empresa deve guardar um histórico de afastamentos para ser utilizado em cálculos futuros ou mesmo para controles gerenciais. O histórico de afastamentos guardará as informações relativas a ocorrências de afastamento do empregado.   
   
O início do afastamento deve ser sempre o primeiro dia de afastamento. No caso do afastamento ser do tipo P ( Afastamento Previdência), T( Afastamento por Acidente de Trabalho) ou O ( Doença Ocupacional) haverá uma projeção dos 15 dias que devem ser pagos para empresa.

A data do requerimento do benefício pode ser cadastrada, não é obrigatória, mas caso a data de requerimento fique nula, o sistema considerará a data do efetivo afastamento.  
   
A quantidade de dias que o funcionário estiver afastado será calculada em conformidade com a data início e fim, observando que se o funcionário ainda se encontrar afastado (sem data final), o retorno será sempre valor nulo.

Não Gerar Gatilho de Término da Cessão

Parâmetro será apresentado ao cadastrar a Data Fim Afastamento para o tipo de afastamento K - Cessão / Requisição, ao marcar o parâmetro o sistema não irá gerar o gatilho de termíno do evento S-2231 para o eSocial.  
   
O tipo de afastamento será cadastrado na tabela dinâmica.   
   
**Observação para tipos de afastamentos:**  
Os tipos de afastamentos que estão sujeitos à redução de avos para o cálculo do 13º salário durante o afastamento no ano corrente são: **P** (Afast.Previdência), **L** (Licença s/venc ), **M** (Serv.Militar), **I**(Apos. Invalidez), **S** (Mandato Sindical Ônus do Sindicato), **C-**Contrato de Trabalho Suspenso e **U** (Outros).Os funcionários afastados por **T** (Af.Ac.Trabalho), só terão avos reduzidos caso o parâmetro "Meses de afastamentos por acidente de trabalho reduz avos de 13º" esteja marcado nos parâmetros de 13º salário.  
   
Mesmo mantendo o empregado na situação "**A**" (Ativo), pode-se fazer o tratamento de seu afastamento. Nesse caso a situação do empregado será "**A**", porém no anexo o usuário lançará os dados do afastamento.  
   
**Observações para afastamentos por licença maternidade:**  
1.   O afastamento por licença maternidade poderá ser prorrogado e por se tratar de prorrogação não poderá haver dias trabalhados entre o atestado normal de 120 dias e a prorrogação deste atestado. Esta prorrogação do afastamento deverá ser cadastrada devendo também ser cadastrada, obrigatoriamente, a data final do afastamento.

**Exemplo:**  
O médico emitirá um primeiro atestado para licença maternidade de 120 dias a partir de 02/01/XXXX que terminará em 01/05/XXXX e emitirá outro prorrogando por 15 dias a partir de 02/05/XXXX que terminará em 16/05/XXXX.  
2.   Quando o tipo do afastamento for E, o motivo for igual ao selecionado pelo usuário e o parâmetro "Salário maternidade pago pela previdência" estiver marcado, o sistema lançará a licença pela previdência, independente do inicio ou data de requerimento do afastamento.  
3.   Há um cadastramento de um novo motivo de afastamento para licença maternidade por adoção e deverá ser incluso nos parâmetros de afastamentos o motivo de afastamento: "Motivo de afastamento ref. a licença maternidade por adoção".  
O relatório do SEFIP trata os seguintes casos:

* Quando for afastamento tipo E e o motivo for igual ao selecionado pelo usuário no parâmetro acima citado:
* 1 a 30 dias de afastamento: Q6 - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança de 4 (quatro) até 8 (oito) anos de idade (30 dias)
* 31 a 60: Q5 - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança a partir de 1(um) ano até 4(quatro) anos de idade (60 dias)
* 61 a 120: Q4 - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança até (um) ano de idade (120 dias)
* Os demais casos permanecem como Q1 - Afastamento temporário por motivo de licença-maternidade (120 dias)

**Observações para afastamento por Licença Paternidade**  
Quando o funcionário é afastado por Licença Paternidade, ao realizar o afastamento alterando a situação do funcionário para Y, o sistema automaticamente calcula a data fim e a quantidade de dias, fazendo a projeção para 15 dias contados a partir do primeiro dia de inicio do afastamento, em virtude do programa "Empresa Cidadã" sobre a qual terá incentivo fiscal relativo.   
Neste caso, o afastamento não considera os 5 dias de abono que o funcionário tem por direito e que são pagos pela empresa e não fazem parte do programa Empresa Cidadã. Quando o usuário for cadastrar o afastamento deve desconsiderar estes 5 dias abonados e a data inicial deve ser a partir do sexto dia de licença paternidade (que no total deve ser 20 dias -  5 dias pagos pela empresa e 15 de afastamento).  
Os dias de afastamento serão lançados no evento de código de cálculo 353.  
Exemplo:  
Funcionário tem o período de Licença paternidade do dia 01/06/2017 a 20/06/2017. O afastamento deve ser cadastrado com data inicial 06/06/2017. O período 01/06 a 05/06 não fazem parte do programa Empresa Cidadã.  
   
Dt. Inicial da Continuidade de Aft.  
Esse componente, do tipo "lookup", pode ser usado para ligar registros relacionados que terão continuidade em um período de Atestado Médico. Na lista para seleção apresentada por esse componente são exibidos todos os registros de afastamento com tipos P (Previdência), T (Acidente de Trabalho) e O (Doença Ocupacional) que não estejam associados a outros registros. Dessa forma, somente os afastamentos que iniciam uma sequência, chamados de registro Pai, podem ser usados para criar uma continuidade. É importante lembrar que não é permitido a exclusão de períodos de afastamento que foram selecionados em outros registros como o afastamento inicial de uma sequência. Para isso, o usuário deverá acessar todos os registros Filhos e limpar o campo de relacionamento ("Dt. Inicial da Continuidade de Aft."), para então excluir o registro Pai.

**Observação**  
O parametrizador conta com um parâmetro global para controle manual da continuidade de afastamento: "Habilita controle manual de continuidade de afastamentos com atestado médico". Dessa forma, para habilitar a continuidade de afastamento manualmente, é necessário que o parâmetro anterior esteja devidamente habilitado no parametrizador. Caso o mesmo não esteja marcado, não será considerado a informação do campo 'DT. Inicial da Continuidade de aft.' para cálculo de atestado médico.  Mais informações são fornecidas na página relativa ao parametrizador.

Afastamento pela previdência social

Ao marcar esta flag, o sistema irá calcular os dias de atestado médico que antecede ao Afastamento Previdenciário, utilizando o CC445 - ATESTADO MÉDICO COM INCIDÊNCIA SOMENTE SEGURADO.  Para maiores informações, clique em [Folha de Pagamento - Atestado médico com incidência somente segurado (CC445)](https://tdn.totvs.com/pages/viewpage.action?pageId=590618716).

Data Início Continuidade Afast. Cessão  
Esse componente, do tipo "lookup", tem a finalidade de apontar uma continuidade da cessão no afastamento cadastrado. Na lista para seleção apresentada por esse componente são exibidos todos os registros de afastamento com tipo K (Cessão / Requisição) que não estejam associados a outros registros e que estejam em data posterior a obrigatoriedade. Dessa forma, somente os afastamentos que iniciam uma sequência, chamados de registro Pai, podem ser usados para criar uma continuidade. É importante lembrar que não é permitido a exclusão de períodos de afastamento que foram selecionados em outros registros como o afastamento inicial de uma sequência. Para isso, o usuário deverá acessar todos os registros Filhos e limpar o campo de relacionamento ("Data Início Continuidade Afast. Cessão"), para então excluir o registro Pai.  
   
   
**Cálculo de Dias de Atestado**  
O cálculo dos dias de atestado irá somar os dias contidos em todos os registros que compõem uma continuidade de afastamento. Esse processo se inicia com o registro Pai de uma continuidade e considera todos os dias de outros registros Filhos, afastamentos que possuem no campo de relacionamento ("Dt. Inicial da Continuidade de Aft.") a informação do registro inicial (Pai).  A soma dos dias em um afastamento com continuidade será limitada a 15 dias para a definição do período do Atestado Médico a ser pago pela Empresa ao funcionário, respeitando o intervalo informado no Parametrizador, campo "Dias de carência para afastamento com atestado médico".  
Caso o processo, após seguir a sequência de continuidade definida pelo usuário, identifique que o funcionário já tenha afastado pela Previdência para aquela doença, o atestado não será lançado no envelope de pagamento.  
   
   
Tomador de Serviço  
Preencha com o tomador de serviço em que o funcionário teve dias trabalhados no mês de afastamento no campo 'Código do Tomador', assim será considerado também a remuneração do FGTS de afastamento neste tomador, quando ocorrer a geração do SEFIP.   
**Exemplo:**   
O funcionário retornou do afastamento dia 15/06 e do dia 16 ao dia 30/06 trabalhou no tomador de serviço 1. Portanto, ele terá um recolhimento de FGTS de:

* 15 dias (período em que esteve afastado)
* 15 dias (período em que trabalhou no tomador 1)

Para que a remuneração dos dois períodos seja inserida somente no tomador 1, o usuário deverá informar o tomador no Histórico de afastamento do funcionário informando o tomador 1. Assim toda a remuneração de FGTS será considerada neste tomador 1.   
**Atenção:**   
Os campos de tomadores de serviços serão disponibilizados, somente para os tipos de afastamentos abaixo:  
E-Licença Mater.  
M-Serv.Militar  
O-Doença Ocupacional  
T-Af.Ac.Trabalho  
   
**Observações:**  
1.    Havendo dois códigos de Clientes/Fornecedores iguais (coligada corrente e coligada global), ao informar um código será considerado o código do Cliente/Fornecedor da coligada corrente. Caso não seja a informação válida deverá ser selecionado pelo nome.  
   
2.   Para emitir SEFIP de meses anteriores com informações de afastamentos, será considerado o tomador de serviços atual marcado neste campo. Ou seja, se no mês da competência atual estiver marcado tomador 1 e no mês da emissão do SEFIP, que seria em atraso, não existia tomador de serviços neste campo no momento de emitir o SEFIP de mês anterior será considerado o tomador 1 que está no cadastro atual.  
3.   Neste campo só apresentará Clientes/Fornecedores ativos e tomador de serviços folha. Para isto, os campos 'Ativo' e 'Tomador de serviços folha' no cadastro de clientes/fornecedores deverão estar marcados. Se o campo contiver o código do Cliente/Fornecedor, mas não apresentar o nome do mesmo, o Cliente/Fornecedor foi desativado no cadastro de clientes fornecedores.  
4.    Caso a coligada possuir licença de uso do Sistema de Controle Financeiro Gestão Financeira e nos parâmetros do Gestão Financeira, item 'Parâmetros Lançamentos', estiver desmarcado o parâmetro 'Permite Globais', não será possível associar em campos de cadastros do Folha de Pagamento, Cliente/Fornecedor que foram cadastrados como 'Global'.  
   
5.    A partir da versão 4.30 do SEFIP foi possibilitado ao usuário informar movimentação por motivo de licença maternidade também para os códigos de recolhimento 150,155,907 e 908.  
   
6.    O número do CEI vinculado ao tomador de serviço deve ser o cadastrado no Anexo 'CEI do Cliente / Fornecedor' do   cadastro de Cliente/Fornecedor.  
   
O parâmetro 'Estorna Tempo de Serviço' será utilizado para que o período de afastamento seja descontado da contagem do tempo de serviço do empregado.  
**Exemplo:**  
Supondo que a empresa resolva oferecer participação nos lucros apenas para funcionários com um ano ou mais de tempo de serviço.  
Se um funcionário admitido na empresa há 1 (um) ano esteve afastado por 3 (três) meses e o campo 'Estorna Tempo de Serviço' foi habilitado, o sistema descontará o período de afastamento.   
O sistema considerará, então, que o empregado tem 9 (nove) meses de tempo de serviço e, portanto, não terá direito à participação nos lucros.   
   
**Aba eSocial**  
   
Emitente  
Serão listados todos os profissionais de saúde cujo 'Órgão da Classe' tem o parâmetro 'Emite Atestado' marcado.   
Estes profissionais de saúde estão localizados em TOTVS Segurança e Medicina do Trabalho | Cadastros | Profissional da Saúde.  
   
Cód. CID  
Serão listados os códigos cadastrados em TOTVS Segurança e Medicina do Trabalho | PCMSO | CID.  
   
Trabalhador Cedido  
Estes campos "Ônus da Cessão" e "CNPJ do órgão para onde o trabalhador foi cedido" serão habilitados quando o afastamento for do tipo:  
·         K-Cessão / Requisição  
   
Acidente de Trânsito  
Preencher caso haja afastamento do trabalhador em decorrência de acidente.   
Este parâmetro será habilitado quando o afastamento for do tipo:  
·         O-Doença Ocupacional  
·         P-Af.Previdência  
·         T-Af.Ac.Trabalho

Mandato Sindical  
Os campos serão habilitados quando o afastamento for do tipo 'S-Mandato Sindical Ônus do Sindicato' ou 'N-Mandato Sindical Ônus do Empregador':

* CNPJ do Sindicato;

Diferença e/ou complementação salarial paga pelo Sindicato.

**Anexo:**

Histórico de Motivo do Afastamento  
   
Este anexo foi criado para registrar a alteração de motivo de afastamento.  Deve ser utilizado em situações específicas, nos casos em que ocorre, de fato, modificação do motivo do afastamento, atendendo assim o leiaute do eSocial.  
   
O registro de alteração será informado no evento S-2230, sempre que o motivo de afastamento for alterado, o sistema irá gerar um histórico.

|  |  |
| --- | --- |
| **Código do Motivo de Afastamento eSocial** | **Código do Tipo de Afastamento Folha de Pagamento (PCODAFAST)** |
| **01** - Acidente/Doença do trabalho | **T** - Afastamento Acidente de Trabalho  **O** - Doença Ocupacional |
| **03** - Acidente/Doença não relacionada ao trabalho | **P** - Afastamento Previdência |
| **06** - Aposentadoria por invalidez | **I** - Aposentadoria Invalidez |
| **14** - Cessão / Requisição | **K**-Cessão / Requisição |
| **16** - Licença remunerada - Liberalidade da empresa ou Acordo/Convenção Coletiva de Trabalho | **R** - Licença Remunerada |
| **17** - Licença Maternidade - 120 dias | **E** - Licença Mater. |
| **18** - Licença Maternidade - a partir de 120 dias até 180 dias | **W** - Licença Mater. Compl. 180 dias |
| **19** - Licença Maternidade - Afastamento temporário por motivo de aborto não criminoso | **E** - Licença Mater. e PPARAMADICIONAIS.NOMECOLUNA = 'MOTIVOAFASTABORTONAOCRIME' e PPARAMADICIONAIS.VALORSTR = 'Motivo do afastamento' |
| **20** - Licença Maternidade - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança | **E** - Licença Mater. e PPARAMADICIONAIS.NOMECOLUNA = 'MOTIVOAFASTADOCAO' e PPARAMADICIONAIS.VALORSTR = 'Motivo do afastamento' |
| **21** - Licença não remunerada ou Sem Vencimento | **L** - Licença sem vencimento |
| **24** - Mandato Sindical - Afastamento temporário para exercício de mandato sindical | **S** - Mandato Sindical Ônus do Sindicato  **N -** Mandato Sindical Ônus do Empregador |
| **29** - Serviço Militar - Afastamento temporário para prestar serviço militar obrigatório | **M** - Serviço Militar |

   
**Observações:**

* A alteração dos tipos "**T**" para "**O**" ou vice-versa, não habilitará a opção para registro de alteração, pois no eSocial se remetem ao mesmo tipo "**01**".
* Para inclusão dos motivos de alteração será necessário uma alteração válida.
* Os campos "Tipo do Processo" e "Número do Processo" somente serão habilitados se a "Origem da Alteração" for "2 - Revisão Administrativa" ou "3 - Determinação Judicial".

Informações dos Atestados Médicos  
Este anexo foi criado com o intuito de tornar possível a vinculação de vários atestados médicos a um  único afastamento. Neste cadastro será possível informar o médico, CID  e a quantidade de dias do atestado, mas será limitado a inclusão de até 9 atestados.  
Será feita a validação da quantidade de dias informados neste anexo com a quantidade de dias real do afastamento, caso os dias no anexo seja superior, será apresentado uma mensagem de alerta.  
Essas informações serão utilizadas para a geração do evento "S-2230" do eSocial.

**Processos:**

Alterar Data Início do Afastamento

Processo criado para realizar a alteração da data início do afastamento casdatrado.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários  
[Como cadastrar mais de um atestado para o mesmo afastamento?](http://tdn.totvs.com/pages/releaseview.action?pageId=435107039)
