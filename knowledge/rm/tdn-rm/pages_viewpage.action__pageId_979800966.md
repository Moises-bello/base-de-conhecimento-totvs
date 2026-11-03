---
content_hash: bfe7ab679abe8fc60a40c65554f5106d2d0832e6d0140ce39c5f059a60e9a1c6
fetched_at: '2026-06-29T00:12:15.466650+00:00'
page_id: '979800966'
product: rm
source: tdn-rm
title: Pré-Venda - Pessoas - Fluxograma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=979800966
version: 3
---

O processo de criação e gerenciamento de clientes acontece em **três grandes momentos** dentro do sistema:

1. **Cadastro inicial (no PI)**
2. **Geração de proposta**
3. **Efetivação da proposta (integração com Gestão de Imóveis)**

## 1. Cadastro Inicial (PI)

- Inserção: O cadastro é feito apenas no PI (tabela XPIPESSOA), sem integração imediata com a Gestão de Imóveis (tabela FCFO).  
- Alteração: Permitida somente no PI.  
- Visualização: Disponível apenas no PI.  
- Deleção: Permitida apenas no PI.

➡️ Nesta etapa, o cliente é apenas um **lead/proponente**, sem vínculo com a Gestão de Imóveis.

## 2. Geração de Proposta

- Inserção: O cadastro passa a existir no PI (XPIPESSOA) e na Gestão de Imóveis (FCFO).  
- Alteração: Somente no PI. Após inserção no Gestão de Imóveis, alterações no PI não são refletidas.  
- Visualização: Disponível tanto no PI quanto na Gestão de Imóveis, podendo haver diferenças.  
- Deleção: Não permitida nesta etapa.

➡️ Nesta etapa, temos **duplicidade controlada**: o cliente existe em PI e Gestão de Imóveis, mas só é atualizado no PI.

## 3. Efetivação da Proposta (Backoffice)

- O processo de efetivação da proposta atualiza os dados do cliente na Gestão de Imóveis (FCFO).  
- Neste momento, todos os clientes envolvidos na proposta passam a ter seus dados idênticos entre PI (XPIPESSOA) e Gestão de Imóveis.  
  
➡️ Aqui acontece a sincronização final, garantindo consistência entre os dois sistemas.

**Fluxo Resumido**

* **PI (pré-proposta):** cliente só existe no PI → livre para inserir, alterar, visualizar, excluir.
* **PI + Gestão de Imóveis (proposta):** cliente passa a existir na Gestão de Imóveis, mas só é atualizado no PI → Gestão de Imóveis pode ficar desatualizada.
* **Efetivação (backoffice):** cliente é atualizado na Gestão de Imóveis → dados ficam iguais entre PI e Gestão de Imóveis.

## Conclusão

O processo garante que:  
- O PI é sempre a base principal de atualização de dados.  
- A Gestão de Imóveis é atualizada apenas na inclusão inicial e na efetivação da proposta.  
- Diferenças de dados podem existir durante a fase de proposta, mas são eliminadas na efetivação.
