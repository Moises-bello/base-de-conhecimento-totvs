---
article_id: 35794394372887
category: Materiais - Compras (SIGACOM)
content_hash: 3d095d911a6d14935661f2d9222f55b0890335fc6a381416ad1a2b8af8901d3d
fetched_at: '2026-06-28T22:41:21.753293+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como o sistema
  preenche as Informações de Entrega no formulário do Workflow quando as filais são
  diferentes?
type: support-article
updated_at: '2025-10-22T10:11:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35794394372887-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-o-sistema-preenche-as-Informa%C3%A7%C3%B5es-de-Entrega-no-formul%C3%A1rio-do-Workflow-quando-as-filais-s%C3%A3o-diferentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35794394360215) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Quando a Filial de Inclusão (**C1\_FILIAL**) da Solicitação de Compra for diferente da Filial de Entrega (**C1\_FILENT**),  como o sistema preenche as **Informações de Entrega** no formulário do Workflow que é enviado ao Fornecedor?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
Ao gerar a Cotação no Novo Fluxo de Compras, temos a possibilidade de disparar um email via Workflow para os Fornecedores que selecionamos na Cotação. Uma das informações que devem ser preenchidas é a Informação de Entrega.

No campo **Informações de entrega**, temos um campo do tipo Memo (sem formatação), onde é exibido por extenso a descrição da **Razão Social** e **CNPJ/CPF** e **Endereço de Entrega** da organização (definido no cadastro de empresas do sistema, tabela **SM0**).

A ordem da apresentação do endereço é: **Endereço de Entrega** (**M0\_ENDENT**) - **Bairro**(**M0\_BAIRENT**) - **Cidade**(**M0\_CIDENT**) e **Estado**(**M0\_ESTENT**). Essas informações **sempre serão correspondentes à filial na qual está logado no Protheus** do disparar o Workflow do NFC, ou seja, por mais que a filial de entrega seja diferente da filial de inclusão da Solicitação (tenha endereço de entrega diferente), essas informações sempre serão preenchidas referente a filial logada.

Exemplificando, fica da seguinte forma no campo Informações de Entrega: ***RAZÃO SOCIAL: TOTVS SP - CNPJ: 56.809.338/0001-43 - Endereço de entrega: AV. BRAZ LEME, 1631 - SANTANA - SAO PAULO/SP - CEP: 02013-050***.

Esse é o padrão do sistema - ao preencher o campo de Informação de Entrega - mas caso o comprador queira alterar algum dado, basta editar essas informações, visto que é um campo editável pelo usuário, conforme imagem abaixo:

![](https://tdn.totvs.com.br/download/attachments/680260500/eNDERE%C3%87O.gif?version=1&modificationDate=1743789696433&api=v2)

Abaixo, podemos ver como essas informações serão apresentadas no formulário encaminhado via Workflow ao fornecedor.

![](https://tdn.totvs.com.br/download/attachments/680260500/endere%C3%A7o_email3.png?version=2&modificationDate=1743788696163&api=v2)

***Saiba Mais:***

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19823527070871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
