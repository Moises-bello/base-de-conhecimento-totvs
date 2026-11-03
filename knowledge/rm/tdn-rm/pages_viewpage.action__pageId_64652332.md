---
content_hash: 35ec689baddceb21bdc5b1e799fd8cc0e2f2668728c78b4497e370368b4221cf
fetched_at: '2026-06-29T00:11:11.408996+00:00'
page_id: '64652332'
product: rm
source: tdn-rm
title: NF-e - Parametrizar movimento de entrada para emissão de NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=64652332
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.40* |
| **Processo** | **:** | Movimento de entrada para emissão de NF-e |
| **Subprocesso** | **:** | Movimento de entrada para emissão de NF-e |
| **Data da publicação** | **:** | 03/07/2013 |

**Introdução:**

Este documento tem como objetivo orientar os parâmetros específicos do movimento para correta emissão de NF-e, caso deseje criar um novo movimento entre em contato com o suporte do RM Nucleus e após a criação siga este Como Fazer.

**Observação: Para emissão de NF-e de Entrada é obrigatório que o código do tipo de movimento seja iniciado por 1.2.xx**

**Procedimentos**

Acesse o RM Nucleus no seguinte menu: Opções | Parâmetros | RMNucleus | Outras Movimentações ou Gestão Compras (dependendo da classificação do movimento) | Selecione o Tipo de movimento e de um duplo click sobre o mesmo.

**Etapa Mov – Identificação:**

Nesta Etapa Selecione a Serie para emissão de NF-e, lembrando que a serie obrigatoriamente deve ser numérica.

 

**Etapa Mov – Emitente/Destinatário 1/2:**

Nesta Etapa o Emitente deverá ser “Empresa” e o destinatário também “Empresa”.

**Mov – Datas 1/2:**

Nesta etapa deverá ser selecionado “Edita” no campo “Edição da Data de Emissão”.

**Etapa Mov – Datas 2/2:**

Nesta etapa deverá ser selecionado “Edita” no campo “Edição da Data de Saída”.

**Etapa Mov – Transporte 2/3:**

Nesta Etapa deverá ser selecionado o tipo de frete que será praticado no movimento.O campo é obrigatório pela SEFAZ e não poderá ficar como “Não Edita”.

**Etapa Mov – Campos Livres 2/2:**

Nesta Etapa pode ser selecionado a Edição do Histórico para Edita, este campo ira preencher a TAG infCpl do XML da NF-e com as informações preenchidas no movimento.

**Etapa Item – Identificação 2/2:**

Nesta Etapa **DESMARQUE** a opção “Cadastrar Cliente/Fornecedor do Produto automaticamente” conforme figura abaixo:

**Etapa Item – Campos Livres 2/2:**

Nesta Etapa pode ser selecionado a Editar Histórico para Edita, este campo ira preencher a TAG infAdProd do XML da NF-e com as informações preenchidas no movimento.

**Etapa Fis – Natureza:**

 No Campo “Edição” do grupo “Natureza” deve ser selecionado “Edita”, no campo “Seleção Automática de Natureza” deve ser selecionado “Seleciona por Item” e a opção “Edita Cliente/Fornecedor Origem/Destino” deve ser marcada.

**Etapa Fis – Escrituração 1/2:**

Nesta Etapa deverá ser marcada a opção “Gerar Escrituração” e no campo “Tipo Documento Escrituração” deverá ser selecionado o tipo de documento cadastrado para emissão de NF-e, onde o mesmo tem que possuir o CodModDoc (código modelo documento) = 55.

**Etapa Fis – Tributação – Item:**

Nesta Etapa deverão ser selecionados os tributos incidentes em cada item do movimento. Exemplo: ICMS, PIS, COFINS, ISS etc.

**Etapa Fis – Tributação – Movimento:**

Nesta Etapa deverão ser selecionados os tributos retidos incidentes na NF-e. Exemplo: COFINS RF, CONTRIBUIÇÃO SOCIAL RF, CSLLRF, IRPF, IRPJ, IRRFPJ etc.

**Etapa Fis - NF-e:**

Nesta Etapa deverá ser selecionado o Tipo de Envio da NF-e Manual ou Automático.Nos Campos DANFE e DANFE.net deverão ser selecionados os respectivos relatórios DANFE.

**Observação: Ao gerar um movimento de entrada, observe que na aba identificação do mesmo será selecionado a filial que esta recebendo a mercadoria e o cliente deverá ser preenchido na aba Integrações | Fiscal | campo “Código cliente / Fornecedor RM Fluxus:”. Estas parametrizações se aplicam a qualquer movimento de entrada que irá emitir NF-e para a SEFAZ (Devolução de venda, importação, compra de produtor rural etc.).**

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
