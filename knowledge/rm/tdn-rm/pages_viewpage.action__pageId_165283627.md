---
content_hash: 0245cfa5a17cf9fa7bd6ec6224d932496598e192ae361f79068dbcd69407a470
fetched_at: '2026-06-29T00:05:57.223149+00:00'
page_id: '165283627'
product: rm
source: tdn-rm
title: CT-e - Parametrizar o tipo de movimento para emissão de CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=165283627
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | CT-e                        **Versão:***a partir 11.52* |
| **Processo** | **:** | Parametrizar o tipo de movimento para emissão de CT-e |
| **Subprocesso** | **:** | Parametrizar o tipo de movimento para emissão de CT-e |
| **Data da publicação** | **:** | 03/10/2014 |

**Introdução:**

Este documento tem como objetivo orientar os parâmetros específicos do movimento para correta emissão de CT-e, caso deseje criar um novo tipo de movimento entre em contato com o suporte do RM Nucleus e após a criação siga este Como Fazer.

**Procedimentos:**

Acesse o RM Nucleus no seguinte menu: Opções | Parâmetros | RMNucleus | Selecione o Tipo de movimento e clique em Parametrizar. Para selecionar o tipo de movimento deve se atentar a classificação do mesmo (Outras movimentações, vendas e etc).

MDI: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento.

**Observação: Para emissão de CT-e  é obrigatório que o código do tipo de movimento seja iniciado por 2.2.xx**

**Etapa Mov – Identificação:**

Campo "máscara do número", deve ser parametrizado com 6 dígitos.

Campo "Série", deve ser informado a série estabelecida pela SEFAZ.

**Etapa Mov - Emitente / Destinatário 1/2:**Campo "Emitente" deve ser igual a **Empresa** e o campo "Destinatário" deve ser igual a **Cliente**.

**Etapa Mov - Datas 1/2:** Campo "Data Entrega" deve estar como edita ou mostra.

**Etapa Mov - Transporte 1/3:**

Marcar os "Flags" campo "Editar Transportadora 1", "Editar quantidade", "Editar Marcar", "Editar Via de Transporte" e "Editar Especie".

**Etapa Mov - Transporte 2/3:**

Habilitar campo "Tipo de Frete"

                                Marcar os "flags" dos campos "Editar dados de Cálculo do Frete da Mercadoria" e "Editar Dados da Placa do Veículo;

**Mov – Transporte 3/3:** Marcar os "Flags " dos campos "Editar Peso Bruto" e "Editar Peso Liquido".

**Item - Identificação 1/2 :** Campo "Tipo dos Itens", selecionar entre serviço, produto ou Ambos.

**Fis - Natureza:**

Campo "Edição", definir como edita ou mostra.

Campo "Seleção Automática da Natureza", definir de acordo com a regra de negocio da empresa, selecionando por item ou movimento.

**Fis - Escrituração 1/2:**

Marcar o "Flag" Gerar Escrituração.

Campo "Tipo Documento Escrituração", selecionar tipo de documento cujo campo CODMODDOC = 57.

**Fis - Tributação - Item:** Verificar regra de negocio da empresa.

**Fis - Tributação - Movimento:** Verificar regra de negocio da empresa.

**Fis - Conhecimento de Transporte (etapa NOVA):**

Campo "Tipo de Operação do Conhecimento de de Transporte": Definir como "Emitir CT-e".

Campo "Modal": Definir a modalidade que será utilizada.

Campo "DACTE": informar o relatório default para impressão do DACTE.

Campo "Formato de Impressão", definir o formato que o relatório DACTE será impresso.

**Para maiores informações:**

 **[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
