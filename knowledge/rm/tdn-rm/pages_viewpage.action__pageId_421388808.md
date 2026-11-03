---
content_hash: ee498868a108b087900f2108b72dc11ad91bd27133a2f0364266e6c7b47511bf
fetched_at: '2026-06-29T00:09:19.176154+00:00'
page_id: '421388808'
product: rm
source: tdn-rm
title: Regerar Contabilização de Extrato de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388808
version: 2
---

O processo Regerar Contabilização das operações manuais do extrato de Caixa tem o objetivo de regerar a Contabilização nos casos:

* Contabilização esteja integrada ao Lote Zero Contábil.
* Contabilização não esteja integrada ao Lote Zero Contábil.
* Contabilização esteja no Modelo Antigo.

Este processo contempla as mesmas funcionalidade do processo anterior " Estorno da Contabilização".  
Para regerar a contabilização o processo deve ser realizado na visão de Extrato através do seguinte menu: Processos - Regerar Contabilização.   
Ao executar o processo é necessário informar a Data do Estorno, caso não seja informada será considerada a data parametrizada no sistema.

Caso queira solicitar a exclusão da Operação Contábil, utilizar o menu: Processos - Solicitar Exclusão Operação Contábil. Após este processo acessar o TOTVS GESTÃO CONTÁBIL e executar a tarefa de Exclusão de Lançamentos de Estorno e Estornados do Lote Zero, através do Menu Utilitarios  | Tarefas  | Gerenciador.

Ao final do processo para registros Não integrados ao lote zero o sistema irá regerar a contabilização no TOTVS GESTÃO CONTÁBIL.  
Nos casos dos registros integrados o sistema além de regerar a contabilização irá estornar os registros antes contabilizados.   
  
 Será possível visualizar no TOTVS GESTÃO CONTÁBIL na tela de Lançamentos Contábeis que o status *"Tipo Geração"* será alterado para *Estornado* e na tela de Manutenção de Lote será gerado dois lançamentos. O primeiro referente ao *Estorno* (Dentro do Lote de Estorno) e o segundo referente á Contabilização de Inclusão do Novo Extrato (Dentro do Lote de Inclusão).
