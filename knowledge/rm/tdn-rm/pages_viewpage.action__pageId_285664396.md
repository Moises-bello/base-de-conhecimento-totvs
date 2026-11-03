---
content_hash: da461d11666d9deb94d30954923a4fe521fcd0c6b0640f50937c6f3e4d6d516a
fetched_at: '2026-06-29T00:08:38.544627+00:00'
page_id: '285664396'
product: rm
source: tdn-rm
title: DT Remessa de Boletos Cancelados, Inativos, Baixados ou Baixados Parcialmente.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285664396
version: 110
---

# Remessa de Boletos Cancelados, Inativos, Baixados ou Baixados Parcialmente.

## Remessa de Cobrança Eletrônica

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Remessa de Cobrança Eletrônica* | *Remessa de Cobrança Eletrônica* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Boleto* | *Remessa Cobrança Eletrônica* | |
| **Cadastros Iniciais:** | *Lançamentos, Boleto, Convênio.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produçãokey,summary,type,created,updated,due,assignee,reporter,priority,status,resolution0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-1136 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL, Oracle* |
| **Tabelas Utilizadas:** | *FBOLETO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Permitir gerar remessa de cobrança para os lançamentos que possuam boletos com STATUS "Cancelado, Inativo, Baixado e Baixado Parcialmente", ou seja,  realizar a comunicação eletrônica com o banco. A remessa de cobrança para esses status visa efetuar o cancelamento do registro do boleto junto ao banco, levando em consideração a instrução do campo “comando” do “Boleto”.  Um exemplo de quando essa situação ocorre, é quando faz o registro do boleto, mas o pagamento dele ocorre através de baixa manual ao invés de retorno bancário. Para evitar que esse boleto seja pago novamente é solicitado junto ao banco o seu cancelamento.

## Procedimento para Implantação

* A implementação estará disponível após atualização para versão do RM 12.1.18.1

|  |  |
| --- | --- |
| **Nome da Variável:** | Cancelados, Baixado, Baixado Parcialmente e Inativos |
| **Tipo:** | Parâmetro |
| **Descrição:** | Define os status que serão reconhecidos na geração da remessa. |
| **Valor Padrão:** | False |

## Procedimento para Utilização

Acessar a visão de boletos em Contas à Pagar/Receber | Operações financeiras | Boletos.

Selecionar o Boleto para gerar a remessa e em Processos | Remessa Cobrança Eletrônica | marcar as opções desejadas "Baixados/ Baixados Parcialmente", "Cancelados" ou "Inativos".

Após a geração da remessa para os boletos com os STATUS "Baixados/ Baixados Parcialmente", "Cancelados" ou "Inativos" terão o STATUS DA REMESSA atualizados para REMETIDO.

OBS.:

* O campo COMANDO está disponível no processo de alteração Global de Boleto.
* Ao selecionar as opções de "Baixados/Baixados Parcialmente", "Cancelados" ou "Inativos" o sistema busca o status da coluna STATUS do Boleto.

**Atenção: Para gerar a remessa do boleto com os novos status, verifique a regra junto ao banco para o correto preenchimento do campo COMANDO.**

## Vídeo

600400

divs
