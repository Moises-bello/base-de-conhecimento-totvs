---
content_hash: 981b18baf87eaf75924e78ce58abbcabd784f97967e420fc40e3e10a9a5579c4
fetched_at: '2026-06-29T00:09:19.544025+00:00'
page_id: '422545606'
product: rm
source: tdn-rm
title: Grupo GA (CNPJ/CPF - TAG autXML)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545606
version: 4
---

Implementação para atender a NT 2015/002 permitindo informar mais de um CNPJ/CPF na tag **autXML**.

**Cadastros**

Podem ser criados até 05 (cinco) campos complementares para indicação do CNPJ/CPF  na tag autXML de acordo com a necessidade do cliente.   
 O cadastro dos campos complementares devem efetuados no movimento do [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com.br/pages/viewpage.action?pageId=198948835) do através do menu Cadastro | Mais... |  [Campos Complementares](http://tdn.totvs.com.br/pages/viewpage.action?pageId=423938235).  
Deve ser seguidas as orientações abaixo em relação ao Nome da Coluna dos campos complementares:

|  |  |
| --- | --- |
| **NOME DA COLUNA** | **DESCRIÇÃO** |
| CNPJCPF1 | CNPJ\CPF Para Acesso 1 |
| CNPJCPF2 | CNPJ\CPF Para Acesso 2 |
| CNPJCPF3 | CNPJ\CPF Para Acesso 3 |
| CNPJCPF4 | CNPJ\CPF Para Acesso 4 |
| CNPJCPF5 | CNPJ\CPF Para Acesso 5 |

**Tipo**: Alfanumérico  
 **Tamanho**: 20 (vinte)

**Observação:**  Serão levados os dados da transportadora quando a mesma possuir CNPJ/CPF igual ao do Cliente/Fornecedor.

Os Campos Complementares criados deverão ser colocados visíveis no movimento.  
Na geração do XML da NF-e o CNPJ ou CPF será gerado no Grupo GA - Autorização para obter XML:

TAG G51 <<**autXML**>> - CNPJ Autorizador  
 TAG G52 <<**autXML**>> - CPF Autorizador

Lembrando que estes campos seguirão as regras de tamanho e quantidade definidos no Manual do Contribuinte.
