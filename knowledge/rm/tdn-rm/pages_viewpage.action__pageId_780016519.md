---
content_hash: 6b0f9adae58a1161e8f254ff8dbf54014588cfaa540bad2e256e8d182645c63b
fetched_at: '2026-06-29T00:11:37.919305+00:00'
page_id: '780016519'
product: rm
source: tdn-rm
title: Cadastro Global Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=780016519
version: 12
---

## 

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Rescisão Global**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizada**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2310 e Superiores

## **02. VISÃO GERAL**

Cadastrar os dados da rescisão individual de um grupo de funcionários de acordo com a seleção do usuário.

Continua com a mesma validação do cadastro para rescisão no futuro, ou seja, somente pode cadastrar no mês e no próximo mês.

Situação do funcionário: 

* Mudança de A para D se a data de demissão for no mesmo mês de competência
* Continua na situação A se a data de demissão for para o próximo mês - sendo que não pode recalcular o envelope de pagamento do mês atual após o cálculo da rescisão para o próximo mês.

**OBSERVAÇÕES:**

**01 -** Somente será possível informar o valor do Saldo do FGTS via cadastro de funcionários ou no cadastro de rescisão individual.

**02 -** Não haverá sobreposição para funcionários que já tenham rescisão cadastrada. Quando o funcionário estiver na situação “D - Demitido” ou em casos de demissão para o próximo mês onde a situação do funcionário está “A - Ativo” não será processado no cadastro de rescisão global.

**03 -** Somente será cadastrado dados da rescisão com datas na competência atual ou posterior. Não haverá cadastro retroativo.

**04 -** Quando a rescisão é com aviso prévio indenizado e altera a data de demissão após avançar no wizard, é alterada automaticamente a data de aviso prévio indenizado para manter a compatibilidade.

**05 -** Funcionário com afastamento pode ser demitido a partir do último dia do afastamento, sendo que será validado a condição de estabilidade por acidente de trabalho. Somente no caso de funcionário afastado que será demitido pelos motivos 8, F e P são permitidos os cadastros das rescisões e funcionários dentro do período de afastamento.

**06 -**Como na rescisão coletiva, haverá a sobreposição de tipo de demissão quando houver aviso prévio cadastrado e a seleção do tipo de demissão for diferente no cadastro da rescisão global. Por exemplo, quando tem aviso prévio cadastrado com o tipo de demissão 2 - sem justa causa e cadastro uma rescisão global com tipo de demissão tipo T - Término de contrato modificará o tipo de demissão no cadastro da rescisão. Portanto deve ser feita a seleção considerando o tipo de demissão para o grupo de funcionários que será feito o cadastro global.

O parâmetro “Gravar rescisão com férias a lançar ou a finalizar” será utilizado para gravar o cadastro da rescisão mesmo existindo pendências em relação ao processo de férias. Sendo validado a interseção de datas para que não haja cadastro de rescisão enquanto o funcionário estiver de férias.

**Atenção:** Esse parâmetro não executa as pendências de processos de férias como calcular, lançar e finalizar férias que estejam no cadastro de férias do funcionário.

**Exemplo com datas:**

1Exemplo com datas1Datas

Dados para execução do exemplo:

Funcionário 00036 com férias pagas em 28/07/2023 e cadastradas para o período de 01/08/2023 a 30/08/2023 - Calculadas

Funcionário 00043 com férias pagas em 13/07/2023 e cadastradas para o período de  17/07/2023 a 31/07/2023 - Pagas

Funcionário 00048 com férias pagas em 13/07/2023 e cadastradas para o período de  17/07/2023 a 26/07/2023 - Finalizadas

Data de demissão registrada no cadastro global de rescisão = 31/07/2023 - Ou seja, após pagamento das férias calculadas, dentro do período de férias pagas e após as férias finalizadas.

2Parâmetro Desmarcado

Será apresentado as seguintes mensagens ao final da execução e não grava o cadastro da rescisão:

Funcionário: 00036 Há cadastro de férias com a situação 'Marcadas' e data de pagamento anterior a data de demissão. Verifique a necessidade do lançamento das férias antes de realizar a Demissão do funcionário.

Funcionário: 00043 Há cadastro de férias com a situação 'Marcadas' e data de pagamento anterior a data de demissão. Verifique a necessidade do lançamento das férias antes de realizar a Demissão do funcionário.

Funcionário: 00048 Existem férias a Calcular, Lançar e ou Finalizar na competência atual ou anterior a Demissão. Deve ser concluído as férias, ou no recalculo da rescisão global deverá marcar o parâmetro “Lança e/ou finaliza férias automaticamente” para que seja concluído as férias

3Parâmetro Marcado

Será apresentado as seguintes mensagens ao final da execução e grava o cadastro da rescisão somente do funcionário 00048:

Funcionário: 00036 Há cadastro de férias com a situação 'Marcadas' e data de pagamento anterior a data de demissão. Verifique a necessidade do lançamento das férias antes de realizar a Demissão do funcionário.

Funcionário: 00043 A data da demissão está em interseção com o período de férias. A rescisão não poderá ser processada.

**Observação:** Para o funcionário 00048 a finalização das férias poderá ser feita no momento do recálculo da rescisão marcando o parâmetro "Lança e/ou finaliza férias automaticamente" que está no Recálculo das rescisões em Parâmetros da Rescisão.

Para informações sobre o parâmetro “Reposição de vaga” consulte o TDN da rescisão individual em: [Rescisão - RHU](https://tdn.totvs.com/pages/releaseview.action?pageId=452719347)

Se o parâmetro “Desativa usuários associados aos funcionários demitidos” estiver marcado e no cadastro de funcionários tenha um usuário associado, será inserido a data de demissão no cadastro do usuário desse funcionário.

## **03. EXEMPLO DE UTILIZAÇÃO**

Em uma simulação de demissão da seção 01.02 na base exemplo:

Selecionar rescisão tipo 2 - Sem justa causa, informar data de aviso prévio indenizado 31/07/2023 e 30 dias de aviso prévio indenizado:

Informar a data de demissão 31/07/2023, data de pagamento 01/08/2023, motivo de demissão 03 - Sem razão específica, Quebra de seção 01.02 e o motivo mudança de situação 5 - Demissão:

Na finalização foi apresentado exceção que impede o cadastro da rescisão:

E exceção que não impede o cadastro da rescisão:

Foi cadastrada a rescisão para todos os funcionários que estavam em situação A - Ativo exceto o funcionário que tinha pendência com patrimônio.

## **04.** **TELA Rescisão Global**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Tipo de Demissão | Informe aqui o tipo de demissão para o grupo de funcionários que será selecionado |
| Demissão de aprendiz por desempenho insuficiente ou inadaptação | Marque esse parâmetro para selecionar entre Desempenho insuficiente ou inadaptação e Ausência injustificada do aprendiz à escola que implique perda do ano letivo |
| Desconta Aviso Prévio | Marque para descontar o valor do aviso prévio na rescisão |
| Tem Aviso Prévio Indenizado | Marque para pagar o aviso prévio indenizado na rescisão |
| Data de Inicio do Aviso | Informar da data de inicio do aviso prévio caso seja indenizado ou descontado |
| Dias de Aviso | Informar a quantidade de dias de aviso prévio a ser indenizado ou descontado |
| Executa Fórmula de Aviso Prévio | Executará a "Fórmula de número de dias aviso prévio" registrada no [cadastro de sindicato](https://tdn.totvs.com.br/display/public/LRM/Sindicatos) |
| Indicador de Cumprimento Parcial de Aviso Prévio | Selecione o indicador para ser informado no eSocial |
| Tem Aviso Misto | Marque esse parâmetro quando o aviso prévio for misto |
| Data de Inicio do Aviso Trabalhado | Será apresentada a data de inicio do aviso prévio trabalhado |
| Tipo Redução do Aviso | Selecione se a redução será por Dias ou Jornadas |
| Forma Redução do Aviso | Selecione se a redução será no Início ou Fim do aviso |
| Filtro Período Aviso Prévio Trabalhado | Informe a data inicial e final para filtrar o aviso prévio trabalhado |
| Considerar data de demissão prevista informada no aviso prévio trabalhado | Marque esse parâmetro caso queira que o processo considere automaticamente a data de desligamento cadastrada dentro do aviso prévio |
| Data Demissão / Cálculo | Informar a data que será considerada para todos os funcionários da seleção |
| Data Desligamento | Informar a data que será considerada para todos os funcionários da seleção |
| Data Pagamento | Informar a data que será considerada para todos os funcionários da seleção |
| Data último Movimento | Informar a data que será considerada para todos os funcionários da seleção |
| Período | Período será atual, mas quando for para o próximo mês informar a data que será considerada para todos os funcionários da seleção |
| Código de Saque | Selecionar o código de saque |
| Motivo de Demissão | Selecionar o motivo de demissão |
| Dados Homolognet | Selecione entre Cumpriu Jornada Semana, Sábado Compensado e Tem Novo Emprego quais informações serão consideradas na geração do Homolognet |
| Gravar rescisão com férias a lançar ou a finalizar | Marque para gravar rescisão para funcionários com férias a lançar ou a finalizar |
| Reposição de vaga | Marque para gravar no banco que esse funcionário terá reposição de vaga para informar no Registro de Recolhimento Rescisório do Trabalhador |
| Desativa usuários associados aos funcionários demitidos | Marque para desativar os usuários associados aos funcionários demitidos |
| Quebra de Seção | Selecione a quebra de seção |
| Seleção de funcionários | Selecione os funcionários para o cadastro da rescisão |
| Situação - Motivo Mudança | Selecione o motivo da mudança da situação para registrar no histórico de situação do funcionário |
| Situação - Data Mudança | Selecione a data da mudança da situação para registrar no histórico de situação do funcionário |

## **05. TABELAS UTILIZADAS**

* PFUNC
* PDADOSRESCISAO
* PFHSTSIT
