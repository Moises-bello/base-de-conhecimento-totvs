---
content_hash: 860e1ec8bf8c0ca7958626f501daacb3f717856061ba4c49197d900ad815afe0
fetched_at: '2026-06-29T00:09:23.819603+00:00'
page_id: '422546137'
product: rm
source: tdn-rm
title: Adequações Gerais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546137
version: 6
---

**Cadastro de Outros Débitos/Créditos**

No cadastro de Outros Débitos/Créditos, aba Identificação, foi incluído um campo para a identificação da Sub-Apuração a qual o Lançamento está vinculado.  
Tabela  DLDC, Campo IDSUBAPURACAO, tipo Inteiro, Descrição - Identificador Sub-Apuração.  
   
**Regras Gerais:**Este campo e apenas visível na tela, não podendo ser alterado pelo usuário, o preenchimento será realizado através do processo de "Apuração ICMS Prodepe".  
*****Observações*:****Campo apenas visível caso o Parâmetro HABILITAPRODEPE na tabela DPARAMETROSEMPRESA esteja marcado.

**Cadastro de Lançamento Fiscal**

No cadastro de Lançamento fiscal, dados da situação tributaria, aba ICMS e IPI foi incluído um campo para o preenchimento do Valor do ICMS Diferido.  
Tabela DLAF, campo ICMSDIFERIDO, tipo numérico, Descrição Valor ICMS Diferido.  
Cálculo deste campo será realizado através do recálculo do Lançamento fiscal que e realizado automaticamente, pelo resultado do valor de outros ICMS multiplicado pelo valor da alíquota do ICMS informada na Natureza de Operação.  
Foi Habilitado no Cadastro de Natureza de Operação – Regra de ICMS o campo alíquota quando o Tipo de Tributação da Natureza for "Diferido", para que este cálculo possa ser possível.

**Cadastro de Natureza da Operação**

No cadastro de Natureza da Operação, aba Outros Dados, foi criado um campo "Valor adicionado/PE" para informar o Detalhe da Operação. Disponíveis as opções:

1-Prestação de serviço de transporte intermunicipal ou interestadual   
2-Prestação de serviço oneroso de comunicação   
3-Substituição pelas entradas, nas operações não documentadas por nota avulsa   
4-Substituição pelas saídas, nas operações com não-inscrito   
5-Distribuição de mercadoria de fornecimento continuado   
6-Escrituração centralizada, autorizada por regime especial  
7-Escrituração centralizada, vinculada a estabelecimento sem inscrição  
8-Informação das revendas por autônomos (contribuinte localizado no Estado)   
9-Informação das revendas por autônomos (contribuinte localizado fora do Estado

*****Observações*:****Tabela DCFOP, Campo IDDETALHEOPERACAO, tipo Inteiro, Descrição Detalhamento Operação.

**Cadastro/Processos do Período de Apuração**

No cadastro de [Período de Apuração](http://tdn.totvs.com/pages/viewpage.action?pageId=431677780), aba Apuração, foi incluído um campo para guardar o valor do Saldo Credor/Devedor antes da execução do processo de "Apuração ICMS Prodepe", isto é necessário pois este processo irá alterar o valor do campo "SALDOTRBATUAL" Saldo Credor/Devedor e é preciso manter o valor antigo.  
 Tabela DPERIODO, Campo SALDOTRBANTPRODEPE, tipo Numérico, Descrição Saldo Credor/Devedor do ICMS antes das deduções do Prodepe.  
   
**Regras Gerais:**Campo apenas visível caso o Parâmetro HABILITAPRODEPE na tabela DPARAMETROSEMPRESA esteja marcado.  
Campo apenas para visualização, não sendo possível alterações manuais.  
Este campo será preenchido no processo de encerramento do Período de ICMS.
