---
content_hash: cb39c9a1f3aeca1bc9c5f7544e718739de35bc1d0d4f8fc5caa1794c78e249e7
fetched_at: '2026-06-29T00:08:57.066362+00:00'
page_id: '353272950'
product: rm
source: tdn-rm
title: Controle de Documentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353272950
version: 2
---

Para o controle de Documentação será criado um novo recurso.  
 O controle de documentação deve permitir a gestão e consultas de documentos relacionados ao imóvel e ao contrato de locação.   
 Macro Escopo

* Criar cadastro de Controle de Documentação. Este cadastro poderá ser acessado em menu especifico que apresentará todos os documentos cadastrados ou através do cadastro do imóvel e do contrato de locação, onde nestes dois últimos recursos serão apresentados apenas os documentos associados a cada uma das entidades.
* Criar cadastro de tipo de Documento Tipo de Documento. Através deste cadastro será possível que identificar documentos de grupos similares como registros, contratos, licenças, etc.
* Ao incluir um documento serão necessárias as seguintes informações:
  + Tipo de documento;
  + **Descrição**: identificação do documento e/ ou referência.
  + **Período de Vigência**: composto por data inicial e final. A data de validade final não será obrigatória para documentos que não expiram. Exemplo: Escritura do Imóvel.
  + **Órgão responsável**: associado ao cadastro de Cliente/ Fornecedor onde será informada a instituição responsável pela emissão e/ou renovação do documento. Exemplo: Receita Federal;
  + **Status**: este campo terá opções pré determinadas que serão estabelecidas em tempo de projeto. Exemplo: Ativo, Inativo, em preparação, etc.
  + **Responsável**: indica quem é o usuário responsável pela renovação do documento.
  + **Tempo de regularização**: determinar com quanto tempo de antecedência deve ser avisado para renovar.
  + **Observações**: campo livre
* Permitir associar arquivos como Imagens, PDFs, etc. (definir em tempo de projeto se será feito no Fluig ou em outro recurso)
* Criação de Relatório padrão para identificar documentos a vencer em período indicado pelo usuário. O layout deve ser definido em tempo de projeto.
  + Tipo de documento
  + Data final de vigência
  + Imóvel
  + Órgão
  + Tempo de regularização
