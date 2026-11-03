---
content_hash: e2efc8b4af37afcf7acdf90dedc78040789f83fafa1bc58f634da8d71d7911b4
fetched_at: '2026-06-29T00:08:57.087975+00:00'
page_id: '353272953'
product: rm
source: tdn-rm
title: Controle de Procurações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353272953
version: 3
---

**Objetivo**

Este recurso deverá permitir associar procurações a um imóvel ou a um contrato de locação. Este documento representa qual pessoa será a responsável por atender ao registro em nome do Locador ou do locatário.

**Regra de Negócio**

Serão necessárias as seguinte informações:

* Criação do cadastro de Procuração. Este cadastro pode estar associado a um imóvel ou a vários. Há ainda casos onde a procuração não está vinculada a nenhum imóvel e neste caso a identificação do objeto deve ser feita na descrição.
* Instrumento (Publica ou Particular) campo com valores pre-determinados e informativos.
* Situação
  + Fase (cadastro aberto)
    - Código
    - Descrição
  + Tipo de procuração (cadastro aberto)  
    - Código
    - Descrição  
      Ex: para alterar titularidade, para controlar contas de consumo, etc.
  + Imóvel (tabela) (vínculo com um ou vários imóveis)
  + Procuração: número ou codificação de controle da Procução
  + Solicitante: cliente/ fornecedor que represente o solicitante
  + Outorgante (Tabela): aquele que concede ou transfere alguma coisa a alguém.
    - Podem ser indicados 1 ou vários outorgantes. Deve ser relacionado o Cliente/ Fornecedor.
  + Outorgado(Tabela): pessoa a favor de quem se outorgam poderes, um mandato etc.
    - Podem ser indicados 1 ou vários outorgados. Deve ser relacionado o Cliente/ Fornecedor.
  + Há procuração anterior (sim ou não): campo de controle para informar se permite a transferência de poder para outra pessoa
  + Permite substabelecimento (sim ou não)
  + Cartório (cadastro já existente)
  + Cidade (cadastro já existente)
  + Data de início da vigência
  + Data de fim da vigência
  + Data da procuração anterior
  + Revogada (sim ou não)
    - Data de Revogação: quando a procuração perde o poder. Só deve ser indicado se for informado Revogado = Sim.
  + Poderes: campo longo que descreve os poderes que estão sendo concedidos
  + Livro atual (campo aberto)
  + Folha atual (campo aberto)
  + Observação
* Relatório padrão para controle de vencimento de procurações. O layout será definido em tempo de projeto.
* Processo para alterar o status automaticamente conforme data fim da vigência que permita agendamento.
