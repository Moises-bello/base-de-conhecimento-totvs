---
content_hash: bfa2bc0e76ef579fdc2e28cae4536a6f7433de4ac13f1b53427d22d8e34b3d77
fetched_at: '2026-06-29T00:05:47.873984+00:00'
page_id: '1018586945'
product: rm
source: tdn-rm
title: Retificação Informações Complementares Períodos Anteriores - S-1210
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1018586945
version: 20
---

false

**A partir das Versões:**

* [Vídeo How Too](https://www.youtube.com/watch?v=EHNbbG6LOck)

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A partir de **Janeiro de 2026**, em atendimento às novas regras do eSocial (previstas no Leiaute S-1.3), foi liberado um novo processo para gerenciar a retificação de informações complementares do evento **S-1210 (Pagamentos de Rendimentos do Trabalho)**.

Este novo processo foi desenvolvido para permitir a **retificação exclusiva** de informações complementares transmitidos em anos anteriores, tais como:

* Dedução de Dependente
* Pensão Alimentícia
* Previdência Privada Complementar
* Despesas Médicas e Reembolsos

O processo utiliza o parâmetro **Ano Retificação** para delimitar o escopo da correção. Ao informar o ano em que a retificação será enviada (ex: **2026**), o sistema identifica e lista os funcionários que, no ano imediatamente anterior (**2025**), possuíam eventos S-1210 transmitidos com status 10 na fila de eventos (caso possua eventos na tabela de eventos complementares é necessária a restauração dos eventos) passíveis de ajustes.

É fundamental notar que esta ferramenta é destinada **apenas** à correção dos informações complementares. Caso haja necessidade de alteração de valores de rubricas principais da folha de pagamento, o procedimento padrão de **reabertura da folha** e reenvio dos eventos na competência original deve ser utilizado.

Este processo visa garantir a conformidade com as exigências fiscais, oferecendo uma forma direcionada e eficiente de ajustar dados complementares sem a necessidade de reprocessamento completo das folhas de pagamento anteriores.

## **02. EXEMPLO DE UTILIZAÇÃO**

11ParametrizaçãoParametrização

1) Acesse o menu Serviços Globais | Segurança | Perfis, selecione o sistema Folha de pagamento, edite o perfil desejado, acesse Menus e permita o acesso ao cadastro **09.05.15 - Retificação Informações Complementares Períodos Anteriores - S-1210**

Atenção

**É necessario a excecução do sistema RM.Atualizador.exe para a criação da nova tabela utilizada no processo.**

true2Cadastro Retificação Informações Complementares Períodos Anteriores - S-1210Cadastro Retificação Informações Complementares Períodos Anteriores - S-1210

Acesse o menu eSocial | Outros Processos | Retificação Informações Complementares Períodos Anteriores - S-1210

Este menu é responsável por **vincular o período que será retificado**.

Na tela, serão exibidos **todos os funcionários** que tiveram o evento **S-1210** transmitido ao Governo no ano imediatamente anterior ao ano definido no parâmetro **Ano Retificação**.

O comportamento da tela depende diretamente do preenchimento do parâmetro **Ano Retificação**:

# 1 - Filtros

### 1.1 Parâmetro: Ano Retificação

O **Ano Retificação** deve ser informado no formato de **4 dígitos** e com um valor **maior ou igual a 2026**.

* Ele indica o **ano em que o evento S-1210 será gerado** contendo a retificação de períodos anteriores.
* **Exemplo Prático:** Ao informar **Ano Retificação 2026**, a tela exibirá funcionários que:

  + Tiveram o evento **S-1210** transmitido ao Governo (status 10- Aceito RET) no **ano de 2025**.

### 1.2 Parâmetro: CPF

* O parâmetro **CPF** é de preenchimento **opcional**. Caso seja adicionado apresentará somente o CPF digitado.

# 2- Filtros Avançados

### 2.1 Estabelecimento

O parâmetro **Estabelecimento** é de preenchimento **opcional**.

Serão listados os estabelecimentos de acordo com o envio do evento S-1005. Poderá selecionar mais de um estabelecimento.

Caso não selecione nenhum estabelecimento, será considerada todos.

### 2.2 Parâmetro: Ano Retificação

O **Ano Retificação** deve ser informado no formato de **4 dígitos** e com um valor **maior ou igual a 2026**.

* Ele indica o **ano em que o evento S-1210 será gerado** contendo a retificação de períodos anteriores.
* **Exemplo Prático:** Ao informar **Ano Retificação 2026**, a tela exibirá funcionários que:

  + Tiveram o evento **S-1210** transmitido ao Governo (status 10- Aceito RET) no **ano de 2025**.

### 2.3 Parâmetro: CPF

* O parâmetro **CPF** é de preenchimento **opcional**. Caso seja adicionado apresentará somente o CPF digitado.

Atenção

**O botão aplicar filtros só ficará habilitado após informar o parâmetro Ano Retificação que deve ser no formado de 4 dígitos e maior ou igual a 2026. Para autônomo do TOTVS Gestão Financeira ou externo será necessário o filtro pelo CPF.**

# 3 - Apresentação do dados

Após Aplicar Filtros, será exibida as seguintes colunas: 

| Colunas | Campos do sistema |
| --- | --- |
| **CPF** | PPESSOA.CPF / PPAGTOAUTONOMOEXT.CPF / FCFO.CGCCFO |
| **Nome** | PPESSOA.NOME / PPAGTOAUTONOMOEXT.NOMEAUTONOMO/ FCFO.NOME |
| **Tipo** | Funcionário – Funcionários da folha  Funcionário/Prestador – Múltiplos vínculos de funcionário e autônomos (folha, externo ou TOTVS Gestão Financeira)  Prestador – autônomo da folha  Prestador – outros sistemas - autônomo do TOTVS Gestão Financeira ou externo |
| **Meses Retificados/a Retificar em ano** | Ano anterior ao digitado no campo **Ano Retificação** |
| **Editar** | Campo para selecionar o meses a serem retificados |

Para cada registro da lista de funcionários está disponível o botão **Editar**, com ícone de um **lápis**, onde será possível informar quais meses serão retificados. 

Após selecionar basta clicar em confirmar que evento já será gerado com a retificação dos dados complementares do mês selecionado.

Atenção

**O botão correspondente ao mês só ficará habilitado caso tenha o evento com status 10 na fila de eventos caso esteja na fila complementar deverá ser realizada a restauração pelo processo.**

Após a seleção dos meses basta realizar a geração do xml S-1210 pelo processo normalmente, após a execução o xml que estará na fila já terá os dados complementares do mês selecionado.

3Exemplos de UtilizaçãoExemplos de Utilização2Atenção

**A retificação por este processo é exclusiva para os informações complementares (deduções e despesas).  Restrição: Caso haja necessidade de alteração no valor de qualquer rubrica principal da folha, será obrigatório:  A reabertura da folha de pagamento na competência original.  O reenvio dos eventos (S-1200 e S-1210) daquela competência.**

1Plano de saúdePlano de saúde

Foi declarado o valor total do desconto para o funcionário, porém esse valor deveria ter sido rateado com o dependente.

Observe que, no envelope de pagamento, o valor do plano de saúde está apresentado corretamente.

Declaração realizada no mês de setembro de 2025:

No mês de janeiro/2026, foi apurado que o valor do titular deveria ser **R$133,33** e o valor do dependente **R$100,00**.  
Após a verificação, foi acessado o histórico do plano de saúde e incluído o valor correspondente ao dependente em Administração de Pessoal | Funcionários | Anexos | Históricos | Históricos Assistência Saúde.

Ajustado valor do titular e adicionado o dependente:

Acesse o menu eSocial | Outros Processos | Retificação Informações Complementares Períodos Anteriores – S-1210, selecione o **ano 2026** e, em seguida, o **mês de setembro**.

Acesse o menu eSocial | Gerar XML(Eventos Periódicos):

No menu eSocial | Eventos Periódicos, foi validado que o **XML está sendo gerado corretamente**, conforme o ajuste realizado no histórico.

3Troca de CPF do DependenteTroca de CPF do Dependente

Quando for necessário alterar o **CPF do beneficiário da pensão alimentícia**, por exemplo, em situações em que anteriormente era informado o **CPF do responsável.**

No exemplo, em **01/2025** o evento foi enviado com o desconto de pensão vinculado ao CPF **111.111.111-11**.

No mês de **janeiro/2026**, é possível regularizar o CPF identificado como sendo do dependente.  
Para isso, acesse Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Dependentes e realize a alteração do CPF no cadastro do dependente.

Acesse o menu eSocial | Outros Processos | Retificação de Informações Complementares de Períodos Anteriores – S-1210 e selecione o **ano 2026** e o **mês de janeiro**.

Acesse o menu eSocial | Gerar XML(Eventos Periódicos):

Acesse o menu eSocial | Eventos Periódicos. O XML será gerado corretamente, considerando o ajuste do dependente com o novo CPF.

Atenção

**Para alterar o CPF de um dependente do trabalhador, é obrigatório que a modificação cadastral seja primeiramente comunicada ao eSocial pelo evento S-2205 – Alteração de Dados Cadastrais do Trabalhador. Qualquer outro evento dependente só pode ser enviado após a validação do S-2205.**

## **03. TABELAS UTILIZADAS**

* PESOCIALRETIFICPERIODOANTERIOR
