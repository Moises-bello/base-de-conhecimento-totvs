---
content_hash: afbe646996a9d051e8b776133089d042db0bd8719811c1025e828559c834d1fd
fetched_at: '2026-06-29T00:12:09.342538+00:00'
page_id: '945393365'
product: rm
source: tdn-rm
title: DT - Contabilização - Evolução no Log
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=945393365
version: 26
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Contabilização - Evolução no Log |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11426](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11426) |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir dos patches:

* 12.1.2502.155
* 12.1.2506 e superiores

## **03. SITUAÇÃO/REQUISITO**

Evoluir o log gerado pela contabilização do produto TOTVS Folha de Pagamento, proporcionando aos usuários mais autonomia na conferência e identificação de inconsistências, tanto relacionadas a eventos quanto a encargos.

## **04. SOLUÇÃO**

O log gerado pela Contabilização da Folha de Pagamento evoluiu. Agora, os usuários contam com mais informações e visibilidade sobre os lançamentos, facilitando a identificação de possíveis inconsistências em eventos e encargos, com muito mais autonomia.

1true1Log Antes da EvoluçãoLog Antes da Evolução

Demonstração do Log de Contabilidade antes da inovação:

3Log Após a EvoluçãoLog Após a Evolução

Demonstração do Log de Contabilidade após a inovação:

4Cenários de InconsistênciasCenários de Inconsistências

Segue a demonstração de alguns cenários de inconsistências apresentadas durante a geração do lote:

**01. Conta débito igual a crédito**

A mensagem está relacionada ao parâmetro “Permite Contas iguais a débito e Credito**”** existente em Parametrizações | Folha Normal | Contabilização, conforme demonstrado abaixo:

**02. Conta crédito e débito não podem ser nulas**

Esta mensagem será apresentada quando o evento possuir contas associadas no cadastro do evento e o flag “Tem integração contábil” estiver desmarcado.

Para análise, acessar o menu Administração de Pessoal | Eventos | Aba Dados Contábeis, conforme demonstrado abaixo:

**03. Contabilização com inconsistência no cadastro de encargos**

Para inconsistências relacionadas ao cadastro,  foi inserido o código do encargo.

**04. Contabilização com inconsistência no cadastro de eventos.**

Para inconsistências relacionadas ao cadastro, foi inserido o código do encargo.

**05. Ao gerar o lançamento foi apresentada a mensagem de inconsistência abaixo.**

Neste cenário, foi criado um novo item na tabela dinâmica de código CODINTCONT, menu Administração de Pessoal | Cadastros Globais | Tabelas Dinâmicas, e associado ao cadastro da seção de lotação do funcionário na aba “Dados contábeis” no campo “Integração contábil” , menu Administração de Pessoal | Seções, porém este não foi associado a nenhum grupo de contas em “Agrupamento de Contas contábeis”, menu Encargos | Cadastros | Cadastros Contábeis | Agrupamentos de Contas Contábeis (Folha de Pagamento).

Verificar o motivo deste novo registro ter sido criado na tabela dinâmica citada e a necessidade de criar/associar este código no Agrupamento de Contas Contábeis (Folha de Pagamento) correto. Conforme tela abaixo:

true4Dicas para a geração do lote com sucessoDicas para a geração do lote com sucesso

Para garantir a geração bem-sucedida do lote contábil, é essencial verificar as configurações dos eventos (contas de débito e crédito), encargos (contas de débito e crédito), filial contábil configurada, código da integração contábil configurada, centro de custo e Agrupamento de Contas Contábeis (Folha de Pagamento). É necessário que esses registros tenham seus relacionamentos interligados de forma correta.

Ao criar um novo item na tabela dinâmica de código CODINTCONT, meu Administração de Pessoal | Cadastros Globais | Tabelas Dinâmicas, e vinculá-lo ao cadastro da seção de lotação do funcionário na aba “Dados contábeis”, é necessário que esse item tenha um registro de relacionamento no cadastro de Agrupamento de Contas Contábeis (Folha de Pagamento).

Para a geração de lotes com a flag “Gerar lote separado por filial” (tela de processo da geração do lote), no cadastro do Agrupamento de Contas Contábeis (Folha de Pagamento) o campo “Código da Filial” não deve ser preenchido.

## **05. DEMAIS INFORMAÇÕES**
