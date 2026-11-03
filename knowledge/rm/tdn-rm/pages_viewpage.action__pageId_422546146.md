---
content_hash: 874f54400c9dc38ff4ca3c46441c619d668f04fc331ff1365d8475775022f0ed
fetched_at: '2026-06-29T00:09:23.871559+00:00'
page_id: '422546146'
product: rm
source: tdn-rm
title: Requisitos Necessários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546146
version: 13
---

**Cadastro do Produto**

Para a correta geração do arquivo, deverão ser informados nos anexos do [Produto](http://tdn.totvs.com/pages/viewpage.action?pageId=423938817) no campo FCI's do Produto os seguintes os campos:

* Unidade de medida
* Valor da Parcela importada no Exterior
* Valor da saída interestadual
* Conteúdo de Importação

***Observação***. Após a segunda fase de Implementação da Rotina, onde o sistema fará o cálculo automaticamente, os campos acima serão calculados automaticamente.  
Após a importação da FCI os campos abaixo serão preenchidos automaticamente

* Número da FCI Gerada

Mensagem de Validação da FCI retornada pela SEFAZ.

**Parametrização do Processo**

No TOTVS Gestão Fiscal, acesse Cadastros | Parâmetros de Processos |

Faça o cadastro de um novo processo  especificando **FCI - Ficha de Conteúdo de Importação** no campo **Processo,** conforme imagem abaixo

Neste processo devem ser informados os produtos submetidos a processo de industrialização (que serão utilizados nos movimento de Venda).

Para cadastrar os produtos, acesse o menu Anexos | Filtro Produto

Além disso o usuário poderá informar quais itens são passíveis de recálculo ( Quando o cálculo for otimizado) e alíquota do ICMS praticada.
