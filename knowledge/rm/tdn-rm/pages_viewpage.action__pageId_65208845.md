---
content_hash: de7546e4b2a0b6a38e477a514e5ee5e025ac2e045bfac5b463364b5d9345fdb4
fetched_at: '2026-06-29T00:11:12.258933+00:00'
page_id: '65208845'
product: rm
source: tdn-rm
title: NF-e - Parametrizar movimento de saída para emissão de NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=65208845
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.20* |
| **Processo** | **:** | Parametrizar o movimento de saída para emissão de NF-e |
| **Subprocesso** | **:** | Parametrizar o movimento de saída para emissão de NF-e |
| **Data da publicação** | **:** | 05/07/2013 |

**Introdução:**

Este documento tem como objetivo orientar os parâmetros específicos do movimento para correta emissão de NF-e, caso deseje criar um novo movimento entre em contato com o suporte do RM Nucleus e após a criação siga este Como Fazer.

**Procedimentos:** 

Acesse o RM Nucleus no seguinte menu: Opções | Parâmetros | RMNucleus | Outras Movimentações ou Vendas (dependendo da classificação do movimento) | Selecione o Tipo de movimento e clique em Parametrizar.

**Observação: Para emissão de NF-e de Saída é obrigatório que o código do tipo de movimento seja iniciado por 2.2.xx**

**Etapa Mov – Identificação:**

Nesta Etapa Selecione a Serie para emissão de NF-e, lembrando que a serie obrigatoriamente deve ser numérica, maiores informações sobre o [cadastro da serie](http://totvsconnect.blogspot.com/2011/11/como-fazer-verificar-cadastros-para.html).

**Etapa Mov – Emitente/Destinatário 1/2:**

Nesta Etapa o Emitente deverá ser “Empresa” e o destinatário “Cliente” ou “Fornecedor”.

**Mov – Datas 1/2:**

Nesta etapa deverá ser selecionado “Edita” no campo “Edição da Data de Emissão”.

**Etapa Mov – Datas 2/2:**

Nesta etapa deverá ser selecionado “Edita” no campo “Edição da Data de Saída”.

**Etapa Mov – Transporte 2/3:**

Nesta Etapa deverá ser selecionado o tipo de frete que será praticado no movimento.O campo é obrigatório pela SEFAZ e não poderá ficar como “Não Edita”.

**Etapa Mov – Campos Livres 2/2:**

Nesta Etapa pode ser selecionado a Edição do Histórico para Edita, este campo ira preencher a TAG infCpl do XML da NF-e com as informações preenchidas no movimento.

**Etapa Item – Campos Livres 2/2:**

Nesta Etapa pode ser selecionado a Editar Histórico para Edita, este campo ira preencher a TAG infAdProd do XML da NF-e com as informações preenchidas no movimento.

**Etapa Fis – Natureza:**

No Campo “Edição” do grupo “Natureza” deve ser selecionado “Edita”, no campo “Seleção Automática de Natureza” deve ser selecionado “Seleciona por Item”.

**Etapa Fis – Escrituração 1/2:**

Nesta Etapa deverá ser marcada a opção “Gerar Escrituração” e no campo “Tipo Documento Escrituração” deverá ser selecionado o tipo de documento cadastrado para emissão de NF-e, maiores informações sobre o cadastro do tipo de documento.

**Etapa Fis – Tributação – Item:**

Nesta Etapa deverão ser selecionados os tributos incidentes em cada item do movimento. Exemplo: ICMS, PIS, COFINS, ISS etc.

**Etapa Fis – Tributação – Movimento:**

Nesta Etapa deverão ser selecionados os tributos retidos incidentes na NF-e. Exemplo: COFINS RF, CONTRIBUIÇÃO SOCIAL RF, CSLLRF, IRPF, IRPJ, IRRFPJ etc.

**Etapa Fis - NF-e:**

Nesta Etapa deverá ser selecionado o Tipo de Envio da NF-e Manual ou Automático.Nos Campos DANFE e DANFE.net deverão ser selecionados os respectivos relatórios DANFE, caso não os tenha entre em contato com nosso Help Desk.

[Clique aqui para o campo Envio de email](http://totvsconnect.blogspot.com/2011/08/nf-e-novo-processo-de-envio-de-xml-por.html).

**Para maiores informações:**

 **[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
