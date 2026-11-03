---
content_hash: 748f45236e5c99e4c80fcf862046197da8d1dff1a9324e234b4f5ebe5c526216
fetched_at: '2026-06-29T00:05:48.813375+00:00'
page_id: '1028947938'
product: rm
source: tdn-rm
title: Middleware - Relatório de Conferência IRRF S-5002
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1028947938
version: 69
---

false

**A partir das Versões:**




* [Mapeamento dos Campos e Orientações](https://tdn.totvs.com/pages/viewpage.action?pageId=1040994699)

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Este relatório foi desenvolvido para otimizar a conferência dos dados complementares declarados no evento **S-1210**. De forma intuitiva, ela permite a conciliação entre as bases e valores de IRRF registrados no sistema TOTVS Folha de Pagamento e as informações processadas pelo governo no evento totalizador **S-5002**.

**Itens disponíveis para conferência:**

* Bases de cálculo segmentadas por Código de Receita;
* Valores de Pensão Alimentícia;
* Previdência Complementar;
* Assistência Médica e Odontológica (Plano de Saúde);
* Reembolsos de despesas com saúde.

## **02. EXEMPLO DE UTILIZAÇÃO**

11ParametrizaçãoParametrização

1 - Acesse o menu Serviços Globais | Segurança | Perfis. Em seguida, selecione o sistema **Folha de Pagamento**, edite o perfil desejado, acesse a aba **Menus** e conceda acesso à **tag 09.06.01**.

2 - Acesse o menu Configurações | Parametrizador | eSocial | Configurações Gerais | Integração com Middleware | Outros parâmetros.

Para utilização dos relatórios de conferência, é necessário informar o servidor e porta que serão utilizados para execução desses serviços.

ATENÇÃO:

**É necessária a execução do sistema RM.Atualizador.exe para a criação da nova tabela utilizada no processo.**

true2Relatório de Conferência IRRF S-5002Relatório de Conferência dos Dados Complementares de IRRF

Acesse o menu eSocial |Conferência INSS/IRRF/FGTS/S-5002, e clique em "Conferência IRRF S-5002".

1 - Filtros e Filtros Avançados.

Lista de campos apresentados na tela para utilização como filtro das informações a ser processadas:

|  |  |  |
| --- | --- | --- |
| **Período** | Obrigatório | Período ao qual o relatório se refere. |
| **Código de receita** | Opcional | Pesquisa por código de receita específico. |
| **Nome** | Opcional | Nome do colaborador para o qual se deseja buscar os valores. |
| **CPF** | Opcional | CPF do colaborador para o qual se deseja buscar os valores. |
| **Somente Divergências** | Opcional | Parâmetro que permite listar apenas os casos que apresentam divergência de valores entre as colunas RH e Governo.  **Opções:**   * **Sim:** lista somente os colaboradores com divergência de valores. * **Não:** lista as informações de todos os colaboradores. |
| **Conferência de valores IRRF** | Opcional | O sistema permite alternar a exibição principal entre os dados do **Governo** e da **Folha**, utilizando o Governo como padrão caso não haja uma seleção específica. |

2 - Exibição dos dados

2.1. Visão geral do relatório:   
  
   → Comparação dos valores presentes no sistema, com os valores retornados pelo governo (RET):

       a) Valores divergentes serão exibidos na cor vermelho:

 b) Valores corretos serão exibidos na cor verde:

3 - Parametrização das colunas do relatório (campos que serão exibidos na tela) -   
Clicar na engrenagem ao lado esquerdo do campo pesquisar:

4 - Visualização das informações por código de receita:

5 - Detalhes do IRRF por pessoa colaboradora:

6 - Exportação das informações do relatório em Excel:

true2AutônomosAutônomos

O **Relatório de Conferência (IRRF) – Informações Complementares**, disponível no menu eSocial | Conferência INSS/IRRF/FGTS/S-5002, considera dados provenientes dos autônomos de diferentes origens. Além dos **Autônomos cadastrados na folha de pagamento**, o relatório também busca informações dos A**utônomos cadastrados no TOTVS Gestão Financeira** e dos **Autônomos Externos**.

**AUTÔNOMO EXTERNO**

As informações são buscadas no menu Encargos | Autônomos Externos, nas abas **Identificação** e **Dependentes**.

Na geração do relatório, as informações são preenchidas nos **campos destacados abaixo**.

 Exemplo do retorno do evento  S-1210

**AUTÔNOMO TOTVS GESTÃO FINANCEIRA**

As informações são buscadas no menu Administração de Pessoal  | Cliente e Fornecedor Anexo (eSocial e Lançamento)

Aba (Tributos)

Na geração do relatório, as informações são preenchidas nos campos destacados abaixo.

Exemplo do retorno do evento  S-1210

**AUTÔNOMO FOLHA DE PAGAMENTO**

Administração de Pessoal | Funcionário Pasta Registro

        Envelope de Pagamento

Na geração do relatório, as informações são preenchidas nos campos destacados abaixo.

Exemplo do retorno do evento  S-1210

3Exemplos de UtilizaçãoExemplos de Utilização21Plano de saúdePlano de saúde

### Exemplo de conferência – Plano de Saúde (sem divergência)

Abaixo, exemplo de conferência de valor referente a **Plano de Saúde**, sem identificação de divergências.

O valor apresentado no relatório corresponde à verba de desconto de Plano de Saúde lançada no envelope do colaborador, refletindo corretamente o valor descontado na folha de pagamento.

Retorno do governo no evento S-5002.

Geração do Relatório de Conferência de IRRF do S-5002.

Detalhamento dos valores do IRRF por Colaborador.

### Exemplo de conferência – Plano de Saúde (com divergência)

Abaixo, exemplo de conferência de valor referente a **Plano de Saúde**, com identificação de divergência.

O valor apresentado no relatório não corresponde à verba de desconto de Plano de Saúde lançada no envelope do colaborador, sendo necessário validar:

* Se a verba está parametrizada corretamente para dedução de IRRF;
* Se houve recálculo ou alteração na competência;
* Se os valores enviados ao eSocial estão consistentes com os valores apurados na folha;
* Se houve lançamento manual ou ajuste posterior no envelope.

Retorno do governo no evento S-5002.

Geração do Relatório de Conferência de IRRF do S-5002.

Detalhamento dos valores do IRRF por Colaborador.

2Pensão AlimentíciaPensão Alimentícia

### Exemplo de conferência – Pensão Alimentícia (sem divergência)

Abaixo, exemplo de conferência de valor referente à **Pensão Alimentícia**, sem identificação de divergências.

O valor considerado no relatório corresponde à verba de desconto de Pensão Alimentícia lançada no envelope do colaborador, refletindo corretamente o valor descontado na folha de pagamento.

Movimentação de Pensão do Dependente.

Retorno do governo no evento S-5002.

Geração do Relatório de Conferência de IRRF do S-5002.

Detalhamento dos valores do IRRF por Colaborador.

### Exemplo de conferência – Pensão Alimentícia (com divergência)

Abaixo, exemplo de conferência de valor referente à **Pensão Alimentícia**, com identificação de divergência.

O valor demonstrado no relatório não corresponde ao valor da verba de desconto de Pensão Alimentícia lançada no envelope do colaborador, sendo necessário validar:

* Se a verba está com a incidência correta para IRRF;
* Se houve alteração de cálculo ou recálculo na competência;
* Se os valores considerados no eSocial (S-1210/S-5002) estão consistentes com a folha.

Movimentação de Pensão do Dependente.

Retorno do governo no evento S-5002.

Geração do Relatório de Conferência de IRRF do S-5002.

Detalhamento dos valores do IRRF por Colaborador evidenciando a divergência.

## **03. TABELAS UTILIZADAS**

* PIRRFCOMPLRECEITAFUNCTOTAIS
* PIRRFCOMPLRECEITAFUNCDETALHE
* PIRRFCOMPLFUNCDETALHE
* PIRRFCOMPLRECEITATOTAIS
* PIRRFCOMPLTOTAIS
* PESOCIALEVENTOS

## **04. DEMAIS INFORMAÇÕES**

* [[Relatório IRRF - DIRF] Pacote Final (API RH + TAF)](https://tdn.totvs.com/pages/viewpage.action?pageId=1042914771)
* [Painel do evento S-5002 Imposto de Renda Retido na Fonte por Trabalhador](https://tdn.totvs.com/display/TAF/Painel+do+evento+S-5002+Imposto+de+Renda+Retido+na+Fonte+por+Trabalhador)
