---
content_hash: b5a5aa975f44511d44819fe2d97063d0641cfe2c1ba9c302e9977a016a4d5235
fetched_at: '2026-06-29T00:11:33.391789+00:00'
page_id: '758491949'
product: rm
source: tdn-rm
title: Integração Benefícios com Swile
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=758491949
version: 13
---

**CONTEÚDO**

1. **Versão**
2. **Visão Geral**
3. **Tela Integração Benefício Swile**
4. **Tabelas utilizadas**

## **01.****VERSÃO**

**A partir das versões:**

* **12.1.2302.253**
* **12.1.2306.206**
* **12.1.2310.139**

## **02.****VISÃO GERAL**

Neste módulo, realizaremos a integração de Benefícios com a Swile. Serão enviados os dados do funcionário para integração e/ou pedidos de benefícios da Swile. Veja um exemplo de utilização em**[Integração Benefício com Swile](https://tdn.totvs.com/pages/viewpage.action?pageId=737546308)**.

## 03. **Tela do Processo de Integração Benefício com Swile**

**Principais Campos e Parâmetros**

|  |  |
| --- | --- |
| **Campos** | **Descrição** |
| Enviar Funcionários | Marcar o parâmetro para envio dos funcionários |
| Tipo de Atualização Funcionário - Ignorar | Marcar para não atualizar os dados dos funcionários já existentes, no caso de enviar toda a base. Porém se o funcionário não existir na base da Swile, será inserido. |
| Tipo de Atualização Funcionário - Substituir | Marcar para substituir os dados dos funcionários. Neste caso, além de incluir os funcionários informados e que não estão na base da Swile, será atualizado os dados dos funcionários que já estão na base da Swile. |
| Enviar E-mail de Boas Vindas | Marcar para enviar e-mail de boas-vindas aos funcionários cadastrados no benefício Swile |
| Data do E-mail de Boas Vindas | Informe a data para envio de e-mail de 'Boas Vindas' aos funcionários. Esta data deverá ser posterior a data do envio dos funcionários. |
| Enviar Pedidos de Benefícios | Marcar para enviar o pedido de benefícios dos funcionários para a Swile.  Será enviado todos os benefícios calculados e que estão dentro da data limite. |
| Definir benefício específico | Marcar para enviar um 'benefício específico' para os funcionários. Este campo deve ser marcado caso queira enviar um benefício especifico, sem a necessidade de enviar toda base novamente. Esta opção também pode ser usada para enviar benefícios que são creditados em datas diferentes. |
| Cód. Benef. : | Informe o código de benefício cadastrado no RM e que está associado a um código de benefício da Swile. |
| Data do Crédito | Informe a Data de Crédito dos benefícios Swile para os funcionários. Esta informação é enviada para o Swile disponibilizar os valores na carteira do funcionário, devendo ser maior que a data do dia da execução do processo de envio dos pedidos. |
| Data Limite | Irá verificar a data limite do Benefício no RM para ser considerado para Swile. |

## **04.** **TABELAS UTILIZADAS**

* GCOLIGADA
* PFUNC
* PPESSOA
* VBENEFICIOS
* VBENEFSECAO
* VBENEFVINCFUNC
* VBENEFVINCDEPEND
* VBENEFICODEPARAAPITERCEIRO
