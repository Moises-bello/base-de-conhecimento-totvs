---
article_id: 1500005817402
category: Integrações Nativas
content_hash: 9980a482eb7c5ff6bb0f093655c1a49150c789e66d723eeda27f2cda93248710
fetched_at: '2026-06-28T22:42:35.539924+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Reporte de insumos aplicados pelo Estoque/Custos
  - SIGAEST
type: support-article
updated_at: '2026-01-30T21:12:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005817402-Manufatura-Linha-Protheus-MNT-Reporte-de-insumos-aplicados-pelo-Estoque-Custos-SIGAEST
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37988186370071)** Tempo aproximado para leitura: **00:01:40 min**  
  
**Dúvida**  
Quais são os processos de aplicação de insumos em **Ordem de Serviço - O.S** por meio das rotinas do **Estoque/Custos - SIGAEST**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Solução**  
O processo de reporte de insumos do tipo produto para **Ordens de Serviço**, pode ser realizado somente por meio de algumas rotinas do módulo **Estoque/Custo - SIGAEST**. Sendo estas apresentadas a seguir:  
  
**Baixa Pré-Requisição - MATA185**  
Primeiramente deve-se **Gerar Pré-Requisição - MATA106** referente a solicitação de armazém, esta que pode ser inclusa diretamente pela rotina **Solicitar - MATA105**ou por meio da [inclusão de insumos previstos em uma ordem de serviço](https://tdn.totvs.com/x/XKBqIQ).  
Após a pré-requisição gerada, deve-se realizar o processo de **Baixa da Pré-Requisição - MATA185**. Para este preencher além de todos os campos obrigatórios, deve-se informar o campo **Ordem de Serviço - D3\_ORDEM**para efetivação da aplicação do produto diretamente na ordem de serviço**.**   
  
**Movimentação Múltipla - MATA241**  
Acessar o módulo **Estoque/Custos - SIGAEST** no menu do módulo ir em: **Atualizações / Movimentações / Internas / Movimentação Múltipla - MATA241**. Preencher além de todos os campos obrigatórios, deve-se informar o campo **Ordem de Serviço - D3\_ORDEM** para efetivação da aplicação do produto diretamente na **O.S**.  
  
**Importante**  
De forma a facilitar o processo, o parâmetro**MV\_NGMNTNO** **- Permite vincular ou não a****Ordem de Serviço****automaticamente aos pedidos informados****precisa** estar igual a **1 - Sim** para permitir o preenchimento automático do campo **Ordem de Serviço - D3\_ORDEM**.  
  
**Saiba mais**  
Para ter acesso a documentação deste processo, acesse o *link* [Reporte de insumos pelo SIGAEST](https://tdn.totvs.com/pages/viewpage.action?pageId=560639677)
