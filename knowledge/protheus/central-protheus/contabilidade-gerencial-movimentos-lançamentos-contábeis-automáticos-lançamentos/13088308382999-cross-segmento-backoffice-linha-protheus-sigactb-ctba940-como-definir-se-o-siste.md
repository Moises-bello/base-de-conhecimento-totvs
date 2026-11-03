---
article_id: 13088308382999
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 3fceb04139a9dcb539ff5f3b8d676f373f317f628f815590d8bbc262e497dca1
fetched_at: '2026-06-28T22:40:32.504795+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA940 - Como definir
  se o sistema permite excluir/alterar um lançamento já conciliado pela rotina CTBA940.
type: support-article
updated_at: '2024-11-27T15:35:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13088308382999-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Como-definir-se-o-sistema-permite-excluir-alterar-um-lan%C3%A7amento-j%C3%A1-conciliado-pela-rotina-CTBA940
---

**Dúvida:**

Como configurar o sistema que permita ou não excluir um lançamento já conciliado pela rotina **CTBA940**.

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.1.33

**Solução:**

Para que o sistema permita ou não excluir/alterar um lançamento já conciliado pela rotina **CTBA940** deve-se configurar o parâmetro MV\_CTBVLDC, que foi criado para o controle da exclusão de um registro já contabilizado que já foi conciliado pela rotina CTBA940.

* Caso o parâmetro esteja como**"1"** o sistema permite a exclusão de um registro contabilizado normalmente, conforme o padrão do sistema.
* Caso o parâmetro esteja como **"2"** o sistema valida se o registro posicionado já foi conciliado, através do campo **MSUIDT**, caso este **ID** existe na tabela **QLD** (campo **QLD\_ITEM**), a exclusão do registro é bloqueada e é exibida a mensagem: **"Este lançamento já esta conciliado. Não será possível excluir este registro."**
* Caso o parâmetro esteja como **"3"** o sistema valida se o registro posicionado já foi conciliado, através do campo **MSUIDT**, caso este ID existe na tabela **QLD** (campo **QLD\_ITEM**), a exclusão do registro é interrompida e é exibida a mensagem:  **"Este lançamento já esta conciliado. Deseja excluir a conciliação deste registro?"**Caso seja selecionado a opção "Sim", o sistema irá excluir o lançamento contábil e a conciliação do registro.

Ao realizar a exclusão em lote, as mensagens serão apresentadas uma única vez e replicadas a todos os registros.

Para facilitar o entendimento, abaixo há um mapa mental para exemplificar melhor.

![MV_CTBVLDC.png](https://tdn.totvs.com/download/attachments/721015538/MV_CTBVLDC.png?version=1&modificationDate=1667927760137&api=v2)

Atualmente e por default o sistema permite a exclusão de um registro contabilizado e conciliado, após a validação desse parâmetro será possível ao cliente parametrizar como ele deseja que o sistema valide o registro.

**Conteúdo do parâmetro:**

 **"1"** - Permite exclusão.

        "**2"** - Não permite exclusão.

**"3"** - Pergunta se permite ou não a exclusão da conciliação.

**Importante**

Avalie com critério a configuração deste parâmetro, uma vez que, se o registro já está conciliado qualquer alteração de lançamento pode impactar nos resultados de fechamento contábil.

**CONFIGURAÇÃO DO PARÂMETRO MV\_CTBVLDC**

Nome MV\_CTBVLDC  
Tipo 1-Caracter  
Descrição   
Define se permite excluir/alterar um lançamento já conciliado pela rotina CTBA940.

Conteúdo Padrão "1"

**Saiba Mais:**

**[MV\_CTBVLDC - Define se permite excluir/alterar um lançamento já conciliado pela rotina CTBA940](https://tdn.totvs.com/pages/releaseview.action?pageId=721015538)**
