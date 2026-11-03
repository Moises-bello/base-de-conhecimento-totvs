---
content_hash: ef31a1e07f3e14e3de464ca6432112dc242fbc050ddb84b4b53ec96bba35c0fe
fetched_at: '2026-06-29T00:08:34.290082+00:00'
page_id: '274659034'
product: rm
source: tdn-rm
title: RMFIN000018_FIN_0005_Controlar Concorrência na baixa de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274659034
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | RM - TOTVS Gestão Financeira |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | Controlar Concorrência na baixa de Lançamentos |
| **Ambiente:** | Padrão |

## **Introdução**

O parâmetro "Controlar Concorrência na baixa de Lançamentos" foi implementado com o objetivo de garantir que não seja gerado item de baixa duplicado quando mais de um usuário executar simultaneamente os seguintes processos:

* Baixa Manual;
* Importação de Baixas;
* Retorno Cobrança;
* Retorno Débito automático;
* Retorno de Pagamento;
* Acordo;
* Emissão de Cheque;
* Recebimento via Cheque;
* Borderô;
* Desconto Duplicata;
* Integrações com:

* + Incorporação;
  + Gestão de Estoque, Compras e Faturamento;
  + Educacional;

**Parametrização**

Para controlar a concorrência na baixa é necessário habilitar o parâmetro: "Controlar Concorrência na baixa de Lançamentos" disponível em Ambiente | Parâmetros | TOTVS Gestão Financeira | 02.01 - Contas a Pagar / Receber | 02.01.02 - Baixa | 02.01.02.01 - Manutenção de baixa | Baixa 2/5.

**Funcionalidade**

Quando dois os mais usuários executarem simultaneamente algum dos processos citados acima, somente um dos usuários conseguirá realizar a baixa com sucesso. A baixa será bloqueada por concorrência para os demais usuários.

Ao final do processo que está sendo executado pelo usuário o(s) lançamento(s) baixado(s) será(ão) desbloqueado(s). Caso por algum motivo inesperado na execução do serviço o(s) lançamento(s) fique(m) bloqueado(s), será necessário utilizar o processo "Corrigir Lançamentos Bloqueado por concorrência" localizado na aba Utilitários | Ajuste na Base para que o mesmo seja desbloqueado.

Para executar o processo "Corrigir Lançamentos Bloqueado por concorrência" é necessário permitir acesso ao Perfil de usuário .
