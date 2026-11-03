---
content_hash: e5a543f007ab531e962cb4bc7c8cd93f9fce650a91a7efc2b4a1f28776517fcc
fetched_at: '2026-06-29T00:09:47.146076+00:00'
page_id: '435104947'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Alteração da regra de vencimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104947
version: 4
---

**Pré-condições**

* Ter habilitado a permissão [02.03.01.27 e 28] para Efetivar / Desfazer aditivo de Alteração da regra de vencimento, do perfil do TOTVS Gestão de Imóveis, localizada em *Serviços Globais / Segurança / Perfis.*
* Ter efetivado o Contrato de Locação
* Ter incluído um Motivo do Aditivo

**Incluindo um Aditivo de Alteração de regra de vencimento**

* Selecione o Contrato de Locação e acesse: Anexo/Aditivo/Alteração da regra de vencimento.
* Clique em Incluir Aditivo de Prorrogação do Contrato de Locação. Preencha os campos:

* + Código do Aditivo: Campo de preenchimento automático
  + Data do Aditivo
  + Tipo do Aditivo: Campo de preenchimento automático
  + Situação do Aditivo: Preparação (este campo não é editável, seu status é alterado após a efetivação do aditivo)
  + Motivo do Aditivo: Informar um Motivo do Aditivo
  + Código regra vencimento: Neste campo o usuário informa qual será a nova regra de vencimento para o contrato de locação.

* + - **Observações:**
      * Caso o usuário queira alterar para uma Regra de Vencimento com **Contagem** e **Ação divergência vencimento** com tipos diferentes da atual no contrato, será necessário que o campo **Fim primeiro período** localizado na aba **Identificação** do **Contrato de Locação** esteja preenchido.
      * Caso o campo **Fim primeiro período** esteja em branco, ao tentar fazer uma alteração de vencimento com tipos diferentes, será exibida uma mensagem informando ao usuário que este processo não pode ser realizado.

* Salvar
* Verifique que o status do Aditivo foi alterado para Efetivado.
* Selecione o Aditivo e clique em Editar Aditivo de Alteração de regra de vencimento.
* Acesse a aba Histórico. Será exibida a informação  do campo Observação preenchido ao efetivar o Aditivo
