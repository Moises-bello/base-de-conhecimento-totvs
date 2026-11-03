---
content_hash: 1c1b095d64f5e832b8fae3eb13e32d34925b76e34d2550db67377051349ee773
fetched_at: '2026-06-29T00:09:33.853638+00:00'
page_id: '425459066'
product: rm
source: tdn-rm
title: Cancelamento de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459066
version: 3
---

---

O Cancelamento de Lançamentos é um recurso disponibilizado pelo TOTVS Gestão Financeira, porem alguns processos disponibilizados no TOTVS Educacional utilizam este recurso.

 Para que o cancelamento de um lançamento financeiro possa ser realizado, o sistema deverá antes fazer uma série de validações, como as seguintes: 

**1 - Boletos remetidos/registrados:**Se os lançamentos já possuírem boletos remetidos e/ou registrados nos bancos, o cancelamento destes lançamentos não será permitido.

Para que o cancelamento de lançamentos como estes, cujos boletos possuem status de remessa igual à '*Remetido*' ou '*Registrado*' possa ser realizado, é necessário que o parâmetro do sistema  esteja marcado, assim, ao cancelar os lançamentos, as remessas serão automaticamente canceladas.

Ressaltamos que estas remessas ficarão pendentes no módulo *TOTVS Gestão Financeira*, sendo necessário enviar para o banco a remessa de cancelamento dos boletos afetados. Este parâmetro se encontra em Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin-Geral 3/4.  
    
 **2 - Laçamentos de bolsa de crédito:**Lançamentos provenientes do TOTVS Educacional e originados a partir de uma bolsa de crédito não podem ser cancelados.

Caso o lançamento selecionado para o cancelamento possua lançamentos vinculados a ele, oriundos de bolsa crédito, será executado o cancelamento tanto dos lançamentos de bolsa de crédito quanto do lançamento selecionado no processo.  
    
 **3 - Lançamentos financeiros cujos boletos já possuem movimentos gerados por regime de caixa:**Lançamentos financeiros cujos boletos já possuem movimentos gerados por regime de caixa não poderão ser cancelados.

Para cancelar tais lançamentos é necessário primeiramente excluir os movimentos gerados e somente depois prosseguir com o cancelamento.  
    
 **4 - Lançamentos originados pelo processo de Bolsa Retroativa-Novo Modelo:**Lançamentos que foram originados pelo processo de Bolsa Retroativa-Novo Modelo, não poderão ser cancelados, para estes casos é necessário executar o processo de *Desfazer* bolsa retroativa.
