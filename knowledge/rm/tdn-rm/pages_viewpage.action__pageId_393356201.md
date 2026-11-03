---
content_hash: 4163e16ddb0c4c38ff9230efa0818033350aa98f9c8c98d88fa2c9916efb20e5
fetched_at: '2026-06-29T00:09:09.262962+00:00'
page_id: '393356201'
product: rm
source: tdn-rm
title: DT Integração bancária SIACC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393356201
version: 24
---

# Integração bancária com padrão SIACC da Caixa Econômica Federal

## Características do Requisito

1535629720490\_-1180659154

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Backoffice |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Integração Bancária | Integração Bancária |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Remessa Bancária | Remessa Bancária | | Retorno Bancário | Retorno Bancário | |
| **Cadastros Iniciais:** | Convênio, Boleto, Lançamento, Conta/Caixa, Agência, Conta Corrente, Banco. |
| **Parâmetro(s):** | Parâmetros do Convênio |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7062> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Tabelas Utilizadas:** | FLAN, FBORDERO, FCONVENIO, GBANCO, FPARAMCONV, GBANCO, GAGENCIA, FCONTA |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.21;12.1.22 |

## Descrição

Integração com o padrão de comunicação entre arquivos (remessa e retorno) SIACC, adotado pela Caixa Econômica Federal, onde se utiliza uma padronização diferente, com menos caracteres na chave do lançamento do que o padrão da FEBRABAN.

INTRODUCAOINTIntrodução

## Procedimento para Implantação

O sistema provém de parametrizações de permissões de perfil do usuário, desta forma é preciso dar permissão em um processo para atualizar o sequencial que será utilizado na remessa bancária.

Ao habilitar a opção acima será preciso executar o login no sistema para recarregar as opções do perfil.

## Procedimento para Utilização

* Para utilização do padrão SIACC deverá ser acessado o cadastro de Convênio na aba Movimentações Bancárias:

* Lembrando que essa opção é apenas para Convênios que possuem na conta/caixa, a Caixa Econômica Federal, que deve ser cadastrada com o número oficial 104, que representa seu código Febraban.

  

* Editar o Convênio que deseja utilizar e acessar a aba Dados Adicionais e marcar a opção "Usa padrão SIACC".

* Após marcar a opção será necessário atualizar o próximo sequencial que deverá ser gerado na remessa bancária. Acesse a opção de processos e clique em "Atualizar próximo sequencial SIACC".

* No processo de remessa de pagamento o campo "SEQSIACC" do lançamento será atualizado com o próximo sequencial, onde o convênio estiver marcado "Usa padrão SIACC".
RempagRemessa de Pagamentos

Nesta etapa será possível remeter borderôs, gerando arquivos de remessa no padrão SIACC.

### Procedimento para Implantação

* Para a correta criação dos arquivos de remessa no padrão SIACC é necessária a importação do layout bancário "FINLAY0056 - Pag. CEF Padrão CNAB240 SIACC" disponível na pasta objetos gerenciais.
* O layout deve ser importado via gerador de saídas em Gestão / Gerador de Saída:

* Após a importação do layout, o usuário deverá associá-lo ao convênio parametrizado como "Padrão SIACC".

* Ao gerar a remessa, o sistema irá preencher o sequencial SIACC nos lançamentos e também no arquivo de remessa gerado. É importante frisar que o sistema somente irá gerar os sequenciais caso o convênio esteja marcado como "Padrão SIACC".
* A geração irá obedecer o sequencial cadastrado no convênio via processo.
RetpagRetorno de Pagamentos

No retorno bancário de pagamento quando o banco for 104 e a flag "Padrão SIACC CEF" estiver marcada, o sistema irá encontrar a coligada e a referência dos lançamentos através do campo sequencial devolvido no retorno.

## Procedimento para utilização

* Ao importar um arquivo de retorno CEF usando a opção Retorno de pagamento – Padrão Febraban (CNAB240), deve-se marcar a flag “Padrão SIACC CEF".

* Caso seja encontrado mais de um lançamento em aberto com o mesmo número sequencial (FLAN.SEQSIACC), o sistema não irá conseguir baixar os lançamentos.

**Importante**: para cada convênio distinto com o banco deve existir um registro no cadastrado diferente, assim, dois convênios com mesmo número de convênio, banco e agência não devem ser cadastrados. O controle de sequencial SIACC é único por convênio.
