---
content_hash: 0aa087fb182647a40c23397ed87d890915de1abd842e55e06cfd2057efa76fea
fetched_at: '2026-06-29T00:05:54.416475+00:00'
page_id: '1079786815'
product: rm
source: tdn-rm
title: Visão Geral de Planilhas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1079786815
version: 1
---

Foi desenvolvida uma **v****isão geral** contendo as informações das três planilhas: Orçamento, Meta e Executiva.

A base dessa visão é a **Planilha de Atividades (Executiva)**, a partir da qual será apresentada o vínculo com a Planilha de Serviços e com a Meta, conforme configuração definida:

* Vínculo pelo **Código da Tarefa**ou

* Vínculo por **Tabela de Relacionamento**

A **Planilha de Orçamento** se baseia na estrutura de **Serviços**, enquanto a **Planilha de Atividades** será representada como a visão **Executiva**.

Foram criados novos parâmetros de projeto que permitirão ao usuário definir as descrições de todas essas planilhas, as quais serão exibidas no sistema, de acordo com a necessidade de cada empresa.

A **Planilha de Meta** é composta por campos de recurso (composição, insumo ou verba), criados diretamente na estrutura da planilha. O usuário poderá definir se o projeto utilizará ou não a **Planilha de Meta**, permitindo também configurar a descrição que será atribuída a essa planilha e parametrizar onde será realizada a manutenção das informações de Meta, definindo se essa gestão ocorrerá na planilha de **Atividades** ou na planilha de **Serviços**.

### **Informações exibidas na visão geral**

**Identificação** 

* Código da Tarefa
* Código Auxiliar
* Descrição da Tarefa

 

**Valores (para Orçamento, Meta e Executivo)** 

* Quantidade
* Preço Unitário
* Valor Total
* Unidade

**Campos de Acompanhamento** 

* **Valor em Solicitação de Compra**   
  Soma dos itens vinculados a solicitações de compra no Backoffice.   
  (Obtido com base na nova configuração do tipo de apropriação que será implementada para controle do saldo da tarefa)

* **Valor em Ordem de Compra**   
  Soma dos itens em Ordens de Compra (geradas por cotação ou diretamente, como pedidos de regularização).   
  (Obtido com base na nova configuração do tipo de apropriação)

* **Valor Efetivo (Nota Fiscal)**Soma dos itens em notal fiscal.  
  (Obtido com base na nova configuração do tipo de apropriação)

* **Valor Contratado  (Total de Contrato) - Informativo**

 

* **Saldo A Medir**  Somatório dos contratos, considerando aditivos em aprovação (valor não medido)
* **Valor Medido (Liberado)**   
  Obtido com base na nova configuração do tipo de apropriação para controle do saldo da tarefa

 **Campos Calculados** 

* **Valor Total Comprometido**   
  = Valor em Solicitação de Compra + Valor em Ordem de Compra  **Saldo A Medir**  **Valor Medido (Liberado) +** **Valor em Nota Fiscal**

 

* **Saldo a Pedir**   
  = Valor do Executivo - (Valor Total Comprometido  + Valor Recebido por Transferência - Valor Cedido por Transferência)

 

**Transferências** 

* **Valor Recebido por Transferência**   
  (Orçamento e Executivo)

* **Valor Cedido por Transferência**   
  (Orçamento e Executivo)

 

**Indicador de Desvio** 

**Desvio do Executivo**   
 

* Valor

* Percentual

Cálculo: 

Desvio = Valor Total da Meta – Valor Total do Executivo 

 

**Informações complementares (Anexos)**  

 

São apresentados dados adicionais vinculados às planilhas, disponibilizados em formato de anexos, conforme abaixo:

* Recursos (composição ou insumo) da Planilha de Orçamento (Serviços)

* Recursos (composição ou insumo) da Planilha de Meta (nova planilha)

* Recursos (composição ou insumo) da Planilha Executiva (Atividades)

* Transferências
* Visualização

* Criação de novas transferências  
  (Aplicável tanto para a Planilha de Orçamento quanto para a Planilha Executiva)

* Visão dos insumos da Planilha Executiva (Atividades)  
  Dados da Curva S, incluindo:

* Insumo

* Preço Unitário
* Preço Unitário Médio (Preço médio utilizado nos contratos)

* Quantidade

* Quantidade Pedida

* Quantidade Medida

* Saldo (em valor e quantidade)

* Cronograma da Planilha Executiva (Atividades)

* Histórico de Alterações das planilhas

* Contratos vinculados à tarefa, contendo:

* Valor Contratado

* Valor Medido
* Saldo
* Visão das Apropriações  
  Nesta visão, o usuário poderá acompanhar, por tarefa, os valores que estão em:

* Solicitação de Compra

* Ordem de Compra

* Recebido
