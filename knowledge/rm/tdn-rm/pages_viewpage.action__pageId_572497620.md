---
content_hash: 793ba5f6c72159b9c1ae276470eead45190e4072326dadcfeb59c9dfa594d619
fetched_at: '2026-06-29T00:10:52.414752+00:00'
page_id: '572497620'
product: rm
source: tdn-rm
title: DT-Bolsa de Qualificação Profissional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572497620
version: 33
---

**Adequação no módulo TOTVS Folha de****Pagamento**

Importante

**O Layout foi disponibilizado a partir dos patchs abaixo:**

* **12.1.27.302**
* **12.1.28.213**
* **12.1.29.138**

**É necessário importar o Layout no Gerador de Saídas.**

****A geração do arquivo será apenas para os funcionários que tenham no histórico de afastamento o tipo "C-Contrato de trabalho suspenso", devido ao fato dessa informação ser obrigatória para este benefício.****

A Bolsa de Qualificação Profissional é uma das modalidades do benefício Seguro-Desemprego. Ela é concedida quando o contrato de trabalho é suspenso, por dois a cinco meses, para a participação do empregado em curso ou programa de qualificação profissional oferecido pelo empregador. A suspensão contratual deve estar prevista em acordo ou convenção coletiva de trabalho e aprovada formalmente pelo trabalhador.

Excepcionalmente durante o estado de calamidade pública e da emergência de saúde pública decorrente do coronavírus (covid-19), o curso ou o programa de qualificação profissional poderá ser oferecido pelo empregador exclusivamente na modalidade não presencial e terá duração não inferior a um mês e nem superior a três meses, conforme o disposto no art. 17 da Medida Provisória nº 936, de 1º de abril de 2020.

A empresa deve transmitir, por meio do Empregador Web, dados dos trabalhadores que terão o contrato de trabalho suspenso e receberão a Bolsa de Qualificação Profissional.

Para permitir que os empregadores façam a geração desse arquivo pelo sistema RM, foi criado um novo layout de exportação para o gerador de saídas:  FOPLAY0092 Bolsa de Qualificação Profissional.TotvsGen**,** possibilitando que o usuário exporte os dados para o formato compatível para envio pelo Empregador Web.

**Geração do Relatório**

Acesse o menu **RH | Folha de Pagamento | Gestão |** **Gerador de Saídas**, vá em**Processos | importar Layout**, selecione o layout **FOPLAY0092 Bolsa de Qualificação Profissional.TotvsGen** no caminho onde encontram-se os objetos gerenciais. Exemplo: C:\TOTVS\CorporeRM\ObjetosGerenciais\Layout.

Após a importação do layout, selecione o relatório e clique em **Processos | Geração de Saídas**:

Selecione o local para a geração do relatório:

Após avançar será apresentada uma tela com os seguintes parâmetros da geração:

**Obrigatórios****:**

* **Filtro do Usuário:** Neste campo é permitido fazer filtros dos funcionários que serão contemplados na geração do relatório.
* **Número do Processo:** Digite o numero do processo a ser vinculado.
* **Carga horário mínima do curso:** Cadastre o prazo do curso.
* **Percentual de cursos ou laboratórios:**Cadastre o percentual dos cursos.
* ****Fórmula para cálculo do mês do último salário:****Neste campo deve informar o mês da última remuneração do funcionário. O mesmo deve ser retornado através de fórmula. Conforme o layout este campo é de preenchimento obrigatório.
* **Deseja ulilizar os 4 últimos digitos da agência bancaria?:** Quando selecionado "sim" o campo da agência bancária será preenchido com os 4 últimos algarimos.

  **Observação:**

  Caso o campo da conta bancaria tenha dígito verificador, deve-se utilizar o hífen para separa-lo do número da conta.

  Exemplo:

  12345-6. Caso contrario o dígito será preenchido com zero.

  Fórmula - Retorna o Mês Ultima Remuneração
* **Fórmula para cálculo do valor do último salário:**Neste campo deve informar a última remuneração do funcionário. O mesmo deve ser retornado através de fórmula. Conforme o layout este campo é de preenchimento obrigatório.

  Exemplo de Fórmula para informação do último salário. Esta fórmula retorna a soma do salário contratual mais os valores dos eventos pagos referente outras verbas, como hora-extra, gratificação:

  Fórmula - Retorna a Ultima Remuneração 0 ENTAO
  RC + (MV(MES,ANO,'0084')+MV(MES,ANO,'0083')+MV(MES,ANO,'0082'))
  SENAO
  ACUMFF(MES,ANO,'03')
  FIMSE]]>

**Opcionais:**

* **Fórmula para cálculo do mês do penúltimo salário:**Neste campo deve informar o mês da penúltima remuneração do funcionário. O mesmo deve ser retornado através de fórmula. Conforme o layout este campo é de preenchimento obrigatório.

  Fórmula - Retorna o Mês Penúltima Remuneração
* **Fórmula para cálculo do valor do penúltimo salário:**Neste campo deve informar a penúltima remuneração do funcionário. O mesmo deve ser retornado através de fórmula.

  Exemplo de Fórmula para informação do penúltimo salário. Esta fórmula retorna a soma do salário contratual mais os valores dos eventos pagos referente outras verbas, como hora-extra, gratificação:

  Fórmula - Penúltimo Salário 0
  ENTAO SAL
  SENAO SE ACUMFF(MM,AA,'4')> 0
  ENTAO ACUMFF(MM,AA,'4')
  SENAO ''
  FIMSE]]>

* **Fórmula para cálculo do mês do antepenúltimo salário:**Neste campo deve informar o mês da antepenúltima remuneração do funcionário. O mesmo deve ser retornado através de fórmula. 

  Fórmula - Retorna o Mês Antepenúltima Remuneração
* ****Fórmula para cálculo do valor do antepenúltimo salário:****Neste campo deve informar a antepenúltima remuneração do funcionário. O mesmo deve ser retornado através de fórmula.   
    
  Exemplo de Fórmula para informação do antepenúltimo salário. Esta fórmula retorna a soma do salário contratual mais os valores dos eventos pagos referente outras verbas, como hora-extra, gratificação:

  Fórmula - Antepenúltimo Salário 0
  ENTAO SAL
  SENAO
  SE ACUMFF(MM,AA,'4')> 0
  ENTAO ACUMFF(MM,AA,'4')
  SENAO ''
  FIMSE]]>

Após preencher os campos e executar o processo, será gerado o arquivo conforme abaixo:

 

O arquivo é gerado no diretório informado e com o formado .SD:

Após a geração, o arquivo pode ser validado no [Empregador Web](https://sd.mte.gov.br/sdweb/validador/validadorBolsa.html):
