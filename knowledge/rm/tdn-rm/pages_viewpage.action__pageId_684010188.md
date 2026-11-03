---
content_hash: 84fe4dc3fb9df07a60d78888e58122cbc0143487e75f1ad7f32846408ed29702
fetched_at: '2026-06-29T00:11:18.192771+00:00'
page_id: '684010188'
product: rm
source: tdn-rm
title: Integração TOTVS RH | Performance & Metas (P&M)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684010188
version: 53
---

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2205.130
* ou superiores.

## **02. VISÃO GERAL**

Ter de forma nativa no produto a possibilidade de carga e integração dos dados pessoais dos funcionários para nossa solução Performance & Metas (P&M). Assim, o sincronismo dos funcionários será de forma automatizada e irá otimizar o esforço que antes era necessário para sequência do processo de avaliação, PDI e demais rotinas dentro no P&M.

## **03. EXEMPLO DE UTILIZAÇÃO**

Será possível realizar a carga e integração de forma online dos dados contratuais e movimentações dos funcionários que estão no ERP e que são necessárias para a apuração do pagamento de PLR.

## **04. PARAMETRIZAÇÃO**

 

11ParametrizaçãoParametrização

Acesse o menu Serviços Globais | Segurança | Perfis, selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 01.05.01 - TOTVS RH | Avaliação e Desempenho

Acesse RH | Folha de pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.10 - TOTVS RH | Avaliação e Desempenho  selecione a opção "Performance e Metas" e cadastre os dados para a integração.

Mais informações acesse: [Chaves de Integração](https://tdn.totvs.com/pages/viewpage.action?pageId=686464694)

true2Avaliação e Desempenho Avaliação e Desempenho

Acessando Administração de Pessoal | TOTVS RH | Avaliação e Desempenho, podemos fazer a integração filtrando por funcionário, por período de admissão ou por período dos históricos selecionados, conforme tela abaixo:

  Após a execução será apresentado um log de erros ou de execução.

**ATENÇÃO:**

* Não é permitido a mesma descrição de seção, mesmo que o código seja diferente. Regra estabelecida pela P&M.
* Múltiplos Vínculos: a P&M permite apenas um cadastro por pessoa, sendo assim, ao integrar mais de um funcionário com o mesmo código de pessoa, o P&M irá sobrepor e prevalecerá o ultimo cadastro integrado para o mesmo código de pessoa, sendo que, na Folha de Pagamento a ordem de envio é a data de admissão para o mesmo código pessoa, e caso a data de admissão seja igual, dependerá da ordem do banco de dados.

   Mais informações acesse: [Integração de cadastros básicos de pessoas](https://tdn.totvs.com/pages/viewpage.action?pageId=676047532)

3De/ParaDe/Para3De/ParaDe/Para

**1 - PESSOAS**

**1.1 - DADOS ENVIADOS NO ENDPOINT DE PESSOAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFUNC.CODCOLIGADA |
| name | Nome | PPESSOA.NOME |
| socialName | Nome de preferência (apelido) | PPESSOA.NOMESOCIAL |
| email | Email | PPESSOA.EMAIL |
| admissionDate | Data de admissão | PFUNC.DATAADMISSAO |
| lastRaiseDate | Data de último aumento | PFHSTSAL.DATAMUDANCA |
| birthDate | Data de aniversário | PPESSOA.DTNASCIMENTO |
| demissionDate | Data de demissão | PFUNC.DATADEMISSAO |
| experienceEndDate | Data do fim do período de experiência | PFUNC.FIMPRAZOCONTR |
| dismissalType | Tipo de demissão: 1 - Pedido de desligamento 2 - Sem justa causa 3 - Com justa causa  DE/PARA:  Caso o tipo de demissão seja  "3 - Inic. Empregado com justa causa" ou  "4 - Inic. Empregado sem justa causa", retorna "1 - Pedido de desligamento".  Caso o tipo de demissão "2 - Inic.Empregador sem justa causa" retorna "2 - Sem justa causa".  Caso o tipo de demissão "1 - Inic.Empregador com justa causa", retorna "3 - Com justa causa".  Valores diferentes dos citados acima, retorna  "2 - Sem justa causa". | PFUNC.TIPODEMISSAO |
| hiringTypeIntegrationId | Identificador único de integração do regime de contratação | PFUNC.CODTIPO |
| departmentIntegrationId | Identificador único de integração da área da pessoa | PFUNC.CODSECAO |
| positionIntegrationId | Identificador único de integração do cargo da pessoa | PFUNC.CODFUNCAO |
| positionLevelIntegrationId | Identificador único de integração do nível cargo da pessoa | PFUNC.CODNIVELSAL |
| facilityIntegrationId | Identificador único de integração da unidade da pessoa | PFUNC.CODFILIAL |
| managerIntegrationId | Identificador único de integração do líder imediato da pessoa | Código da Pessoa do chefe imediato, verificando a estrutura de Chefe/Supervisor  ou Hierarquia por Posição (quando ativada). |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.1 - DADOS ENVIADOS NO ENDPOINT DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFUNCAO.CODIGO |
| name | Nome | PFUNCAO.NOME |
| positionGroupIntegrationId | Identificador único de integração do grupo de cargo do cargo | PFUNCAO.CARGO |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.2 - DADOS ENVIADOS NO ENDPOINT DE NÍVEIS DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | VNIVELFUNCAO.CODNIVEL |
| name | Nome | VNIVELFUNCAO.NOMENIVEL |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.3 - DADOS ENVIADOS NO ENDPOINT DE GRUPOS DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PCARGO.CODIGO |
| name | Nome | PCARGO.NOME |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.4 - DADOS ENVIADOS NO ENDPOINT DE UNIDADES**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | GFILIAL.CODFILIAL |
| name | Nome | GFILIAL.NOME |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.5 - DADOS ENVIADOS NO ENDPOINT DE ÁREAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PSECAO.CODIGO |
| name | Nome | PSECAO.DESCRICAO |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**2 - REGISTROS AUXILIARES**

**2.6 - DADOS ENVIADOS NO ENDPOINT DE REGIMES DE CONTRATAÇÕES**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PTPFUNC.CODCLIENTE |
| name | Nome | PTPFUNC.DESCRICAO |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**3 - HISTÓRICO DE REGISTROS AUXILIARES POR PESSOAS**

**3.1 - DADOS ENVIADOS NO ENDPOINT DE MOVIMENTAÇÃO DE PESSOAS PARA CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTFCO.CODCOLIGADA |
| positionIntegrationId | Identificador único de integração do cargo da pessoa | PFHSTFCO.CODFUNCAO |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| changeDate | Data de alteração da pessoa para o cargo | PFHSTFCO.DTMUDANCA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**3.2 - DADOS ENVIADOS NO ENDPOINT DE MOVIMENTAÇÃO DE PESSOAS PARA NÍVEIS DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTFCO.CODCOLIGADA |
| positionLevelIntegrationId | Identificador único de integração do nível de cargo da pessoa | PFHSTFCO.CODNIVEL |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| changeDate | Data de alteração da pessoa para o nível de cargo | PFHSTFCO.DTMUDANCA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**3.3 - DADOS ENVIADOS NO ENDPOINT DE MOVIMENTAÇÃO DE PESSOAS PARA GRUPOS DE CARGOS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTFCO.CODCOLIGADA |
| positionGroupIntegrationId | Identificador único de integração do grupo de cargo da pessoa | VGRUPOOCUPACIONAL.CODGRUPOOCUP |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| changeDate | Data de alteração da pessoa para o grupo de cargo | PFHSTFCO.DTMUDANCA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**3.4 - DADOS ENVIADOS NO ENDPOINT DE MOVIMENTAÇÃO DE PESSOAS PARA UNIDADES**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTSEC.CODCOLIGADA |
| facilityIntegrationId | Identificador único de integração da unidade da pessoa | GFILIAL.CODFILIAL |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| changeDate | Data de alteração da pessoa para a unidade | PFHSTSEC.DTMUDANCA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**3.5 - DADOS ENVIADOS NO ENDPOINT DE MOVIMENTAÇÃO DE PESSOAS PARA ÁREAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTSEC.CODCOLIGADA |
| departmentIntegrationId | Identificador único de integração da área da pessoa | PFHSTSEC.CODSECAO |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| changeDate | Data de alteração da pessoa para a área | PFHSTSEC.DTMUDANCA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**4 - AFASTAMENTOS POR PESSOAS**

**4.1 - DADOS ENVIADOS NO ENDPOINT DE AFASTAMENTOS POR PESSOAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTAFT.CODCOLIGADA |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| type | Tipo do afastamento, podendo ser:   * Acidente de trabalho = 1 * Doença ocupacional = 2 * Doença = 3 * Licença maternidade = 4 * Licença paternidade = 5 * Licença não remunerada = 6   DE/PARA:  Caso o tipo de afastamento seja   T-Af.Ac.Trabalho, retorna Acidente de trabalho = 1.  Caso o tipo de afastamento seja  O - Doença Ocupacional, retorna Doença ocupacional = 2.  Caso o tipo de afastamento seja  P - Af.Previdência, retorna Doença = 3.  Caso o tipo de afastamento seja  E - Licença Mater. ou  W - Licença Mater. Compl. 180 dias, retorna  Licença maternidade = 4.    Caso o tipo de afastamento seja  Y - Licença Paternidade, retorna Licença paternidade = 5.  Caso o tipo de afastamento seja   L - Licença s/venc, retorna Licença não remunerada = 6.   Valores diferentes dos citados acima, retorna tipoAfastamento = 0. | PFHSTAFT.TIPO |
| startDate | Data de início do afastamento | PFHSTAFT.DTINICIO |
| endDate | Data de término do afastamento | PFHSTAFT.DTFINAL |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |

**5 - FALTAS POR PESSOAS**

**5.1 - DADOS ENVIADOS NO ENDPOINT DE FALTAS POR PESSOAS**

| Campo | Descrição | Campo RM |
| --- | --- | --- |
| integrationId | Identificador único de integração do objeto no sistema de origem com o P&M | PFHSTFALTA. CODCOLIGADA |
| personIntegrationId | Identificador único de integração da pessoa | PFUNC.CODPESSOA |
| year | Ano de ocorrência da falta | PFHSTFALTA.ANOCOMPFALTA |
| month | Mês de ocorrência da falta | PFHSTFALTA.MESCOMPFALTA |
| daysNotWorked | Total de dias não trabalhados para o ano e mês informados | CALCULADO PELO SISTEMA |

Retorno

|  | Descrição |
| --- | --- |
| Valor string | O retorno é uma string que é o identificador do processo que será utilizado no endpoint de consulta para checar o status do processamento do lote |
