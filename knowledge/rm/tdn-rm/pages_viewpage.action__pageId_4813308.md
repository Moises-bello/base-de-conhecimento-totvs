---
content_hash: 168c00b789346d4cd9620cd4cefc223af73a6603304d998ac4933c7e2cea80b9
fetched_at: '2026-06-29T00:10:19.317843+00:00'
page_id: '4813308'
product: rm
source: tdn-rm
title: Movimento Extemporâneo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813308
version: 4
---

BLOCK

Movimento Extemporâneo

FAQ: **Movimento Extemporâneo**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

**Produto:** TOTVS Gestão de Estoque, Compras e Faturamento **Versão 11.20**

**Processo do Sistema**: Compras  
**SubProcesso**: Movimentação

**Como Fazer**

Tem como finalidade apresentar a correta parametrização da utilização do recurso “Extemporâneo” no registro das notas de entradas.

**Definição do Processo**

O recurso de 'Extemporâneo' é utilizado para identificar a nota fiscal de entrada de mercadorias ou prestação de serviço registrada fora do prazo regulamentar.  
Será utilizado para realizar escrituração de movimentações com data retroativa. Desta maneira ao incluir um movimento com data superior a data utilizada para escrituração (data lançamento), o sistema apresentará na aba 'Integração' o campo 'Extemporâneo', ou seja, o movimento será escriturado com data retroativa.

Solução

**Parametrizações Necessárias**

Acessar os parâmetros do tipo de movimento em questão e definir as seguintes parametrizações:

* **Etapa Movimentos - Datas**

Data Lançamento:Informar “Edita” para permitir que o usuário preencha ou “Mostra” se quiser deixar um default preenchido.   
Data Entrada:Se editar o movimento de entrada: “Edita” para permitir que o usuário preencha ou “Mostra” se quiser deixar um default preenchido.  
Data Saída:Se editar o movimento de entrada: “Edita” para permitir que o usuário preencha ou “Mostra” se quiser deixar um default preenchido.

**Registro da Nota e Escrituração**

O registro da nota fiscal será incluído como de costuma, mas o campo ‘Extemporâneo’ será apresentado na aba Integração apenas quanto cumprirem as seguintes regras:  
- Nos movimentos do tipo 1 e 3 quando a data de lançamento for diferente da data de entrada/saída.  
- Nos demais movimentos quando a data de lançamento for diferente da data do movimento.

No processo de escrituração do movimento “Extemporâneo” o campo data do lançamento será considera para a criação do lançamento fiscal e a geração da guia de pagamento do tributo será sobre o mês desta data, porem o sistema irá considerar que a data da nota é do período definido na data de entrada do movimento.Para melhor entendimento sobre a utilização deste recurso, será dado um exemplo dentro de uma situação cotidiana.

Exemplo: O contribuinte recebe uma NF de um fornecedor em out/20XX, guarda esta NF na gaveta e lembra-se de registrá-la somente em nov/20XX. Esta nota deverá ser registrada nos livros fiscais de nov/20XX e nas rotinas fiscais de novembro, deverá constar como débito extemporâneo.

Neste exemplo a data de entrada da nota será out/20XX e a data de lançamento será nov/20XX.
