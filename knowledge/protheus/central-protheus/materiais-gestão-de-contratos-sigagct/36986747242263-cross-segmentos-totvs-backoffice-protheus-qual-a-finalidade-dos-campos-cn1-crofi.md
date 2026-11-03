---
article_id: 36986747242263
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 7103773ddec6db417261ada6cf31331e347ce5a8b4f6144723b89df1ce1155b5
fetched_at: '2026-06-28T22:37:20.232416+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - Qual a finalidade dos campos  CN1_CROFIS
  /CNL_CROFIS e Cronograma Físico ?
type: support-article
updated_at: '2026-01-23T14:35:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36986747242263-Cross-Segmentos-Totvs-Backoffice-Protheus-Qual-a-finalidade-dos-campos-CN1-CROFIS-CNL-CROFIS-e-Cronograma-F%C3%ADsico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36986747221143) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Qual a finalidade dos campos  CN1\_CROFIS /CNL\_CROFIS ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de contratos - Todas as versões

**Solução**

Realizando a configuração do Tipo de contrato/ Tipo de planilha com o campo Cronograma físico (CN1\_CROFIS /CNL\_CROFIS) igual a "Sim" , é habilitado a inclusão de Cronograma físico por quantidade para cada parcela do cronograma financeiro do contrato, conforme demonstrado no exemplo abaixo:

**1.** Inclusão de um Contrato com Vigência de 12 meses e no campo "Quantidade do Item inclui 24 " conforme imagem abaixo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36986731469335)**

**2.** Ao incluir o Cronograma financeiro/físico.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36986747221527)**

- Será incluso um Cronograma físico com a quantidade prevista de itens que será medido para cada parcela/competência do contrato, conforme imagens abaixo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36986747221655)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36986731474583)**

**Obs:**

No exemplo acima com quantidade total de itens 24 e gerado 12 parcelas no financeiro para cada parcela está previsto amedição de 2  quantidades por parcela.

**Obs2:**

Tem algum impacto ajustar campo Cronograma físico de "Sim" para "Não" na planilha do contrato?

R:Não é possível ajustar o campo Cronograma Físico , o campo fica bloqueado para alteração.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36986731475479)**

**Obs3:**

Uma possibilidade para alteração da planilha do contrato para utilização de uma nova planilha com o campo Cronograma Físico igual a Não é :

-Em contratos já possui movimentações , nesse caso é recomendado ,primeiro zerar o saldo da planilha conforme artigo - [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como Excluir ou Zerar o Saldo de um Produto / Item do contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021322032-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-Excluir-ou-Zerar-o-Saldo-de-um-Produto-Item-do-contrato)  
-Depois Incluir uma nova revisão para adição de uma nova planilha ,com o campo Cronograma Físico(CNL\_CROFIS) igual a "Não" e posteriormente incluir as informações da planilha conforme a necessidade.

Veja mais detalhes sobre como realizar revisão no artigo abaixo:  
[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Revisão de Renovação de Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025659713-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Revis%C3%A3o-de-Renova%C3%A7%C3%A3o-de-Contrato)

**Obs4:**

Como o sistema calcula o valor do campo CNS\_SLDQTD (saldo)?

**R:**O Cálculo do campo **CNS\_SLDQTD** é:  **CNS\_SLDQTD - CNE\_QUANT(Quantidade medida)**da medição realizada corresponde competência medida do contrato.

**Exemplo:**

**Competência 12/2025**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37883686305431)

Saldo do cronograma físico **CNS\_SLDQTD = 2** correspondente a **Competência 12/2025**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37883686306583)

Medição Realizada com a "Quantidade**(CNE\_QUANT)**"  = **1,50**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37883702424983)

Saldo( **CNS\_SLDQTD) = 0,50 após Medição realizada**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37883686314903)

**Obs5:**

O que fazer quando tiver registros/ valores negativos no Cronograma Físico?

**R:**No padrão do sistema não há como os valores do Crograma físico ficarem negativo, uma possibilidade disso ter acontecedido é o ajuste manual de valores via base ou outra possibilidade pode ser customização.

Caso o valor das medições realizadas estejam corretos conforme o previsto do Contrato e não tenha sido realizado nenhuma manipulação de base uma possibilidade é utilizar a rotina de ajuste de saldos para acerto dos valores nos contratos e cronogramas.

Segue artigo com as orientaçoes: [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o Ajuste de Saldos em Contratos, Planilhas e Cronograma Financeiro ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020124591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-o-Ajuste-de-Saldos-em-Contratos-Planilhas-e-Cronograma-Financeiro)

Verificar o artigo abaixo com informações mais detalhadas sobre sua execução.

[GCT0130 - Ajustes de Saldos](https://tdn.totvs.com/pages/viewpage.action?pageId=968132056)

***Saiba Mais:***

[*Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os tipos de Revisão disponíveis no Gestão de Contratos ?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-tipos-de-Revis%C3%A3o-dispon%C3%ADveis-no-Gest%C3%A3o-de-Contratos)

[*Artigos Materiais - Gestão de Contratos - (SIGAGCT)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
