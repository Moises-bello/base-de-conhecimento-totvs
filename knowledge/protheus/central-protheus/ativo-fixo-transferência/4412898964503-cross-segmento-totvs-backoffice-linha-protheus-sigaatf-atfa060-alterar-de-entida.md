---
article_id: 4412898964503
category: Ativo Fixo - Transferência
content_hash: 166aa7a80174630a3c7d8b14cebd44ff7197672a51d41a8cd18a6d9788c250d4
fetched_at: '2026-06-28T22:41:52.247890+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - ATFA060 - Alterar
  de entidades contábeis de bens
type: support-article
updated_at: '2026-04-30T12:51:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412898964503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-ATFA060-Alterar-de-entidades-cont%C3%A1beis-de-bens
---

A alteração das entidades contábeis de bens cadastrados e depreciados no Protheus deve ser feita pela rotina de Transferência (ATFA060), selecionando o tipo Contábil e informando as novas entidades (Conta Contábil, Centro de Custo, Item Contábil e Classe de Valor). As mudanças são refletidas na tabela SN3 e confirmadas no cadastro do bem (ATFA012).

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26124342477207) Tempo aproximado para leitura: **5 min**  
  
**Dúvida**  
Como realizar alteração de entidades contábeis (Conta contábil, centro de custo, item contábil e classe de valor) de bens já cadastrados e depreciados.

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – a partir da versão 12  
  
  
**Solução**  
A alteração no cadastro do ativo (bem) referente às entidades contábeis (Conta Contábil, Centro de Custo, Item Contábil e Classe de Valor) deve ser realizada por meio da rotina de Transferência (ATFA060).

Esta rotina possibilita efetuar dois tipos de transferências:

* **Física:** destinada à movimentação de um bem para um local físico diferente de sua alocação atual.
* **Contábil:** destinada à transferência do saldo contábil de um bem para outras entidades contábeis.

Para efetivar a modificação, é necessário realizar a transferência do tipo Contábil e informar as novas entidades de destino nos respectivos campos apresentados pela rotina (Conta Destino, Centro de Custo Destino, Item Contábil Destino e Classe de Valor Destino). As alterações efetuadas refletirão diretamente nos campos de amarração contábil da tabela SN3 (Saldos e Valores).  
  
  
**Passos**

1. Acesse a rotina de transferência (ATFA060) no caminho: Atualizações -> Movimentos -> Transferências.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40126431661079)
2. Localize o bem que deseja alterar a entidade contábil e clique na opção **"Transferir"**.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40126447930775)

   Caso deseje realizar a alteração em lote (mais de um bem), selecione a opção **"Automático"** e aplique os filtros para identificar os bens que deseja alterar.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40126431664023)
3. Clique sobre a aba das entidades que deseja alterar: Conta contábil, centro de custo, item contábil e classe de valor.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40126431665175)
4. Preencha os campos das entidades de destino que deseja realizar a alteração, como, por exemplo, **"Ct Bem Dest"** e verifique que o sistema irá alimentar os campos na aba **"Tipo de ativo"** com as novas entidades.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40126431666071)

   OBS.: Não é obrigatório o preenchimento de todos os campos, somente das entidades que deseja alterar.
5. Clique em **"Confirmar"** e verifique no cadastro do bem (ATFA012) se a entidade foi alterada com sucesso.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40126431667095)

**Saiba mais:**  
[ATFA060 - Como funciona a rotina de Transferência de ativo entre filiais e contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015091671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-Como-funciona-a-rotina-de-Transfer%C3%AAncia-de-ativo-entre-filiais-e-cont%C3%A1bil?source=search)
