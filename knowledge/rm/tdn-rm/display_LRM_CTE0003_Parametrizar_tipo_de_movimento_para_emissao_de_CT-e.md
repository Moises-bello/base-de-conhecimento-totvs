---
content_hash: bb60f724086299668f5bbe56cc23295ac133c6341eca695cdcb5a05a01429d85
fetched_at: '2026-06-29T00:08:12.684950+00:00'
page_id: '243646176'
product: rm
source: tdn-rm
title: CTE0003_Parametrizar_tipo_de_movimento_para_emissao_de_CT-e
type: documentation
url: https://tdn.totvs.com/display/LRM/CTE0003_Parametrizar_tipo_de_movimento_para_emissao_de_CT-e
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | CT-e - Conhecimento de Transporte Eletrônico |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Parametrizar o tipo de movimento para emissão de CT-e |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar os parâmetros específicos do movimento para correta emissão de CT-e, caso deseje criar um novo tipo de movimento entre em contato com o suporte do RM Nucleus e após a criação siga este Como Fazer.  **Procedimentos:**  Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento |Outras Movimentações/Vendas (dependendo da classificação do tipo movimento desejado) | Selecione o Tipo de movimento e clique em Parametrizar  **Observação: Para emissão de CT-e  é obrigatório que o código do tipo de movimento seja iniciado por 2.2.xx**  **Etapa Mov – Identificação:**  Campo "máscara do número", deve ser parametrizado com 9 dígitos.  Campo "Série", deve ser informado a série estabelecida pela SEFAZ.      **Etapa Mov - Emitente / Destinatário 1/2:** Campo "Emitente" deve ser igual a **Empresa** e o campo "Destinatário"  deve  ser igual a **Cliente**.    **Etapa Mov - Datas 1/2:** Campo "Data Entrega" deve estar como edita ou mostra.    **Etapa Mov - Transporte 1/3:** Marcar os "Flags" campo "Editar Transportadora 1", "Editar quantidade", "Editar Marcar", "Editar Via de Transporte" e "Editar Especie".    **Etapa Mov - Transporte 2/3:**  Habilitar campo "Tipo de Frete            Marcar os "flags" dos campos "Editar dados de Cálculo do Frete da Mercadoria" e "Editar Dados da Placa do Veículo;    **Mov – Transporte 3/3:** Marcar os "Flags " dos campos "Editar Peso Bruto" e "Editar Peso Liquido".  **Item - Identificação 1/2 :** Campo "Tipo dos Itens", selecionar entre serviço, produto ou Ambos.  **Fis - Natureza:**  Campo "Edição", definir como edita ou mostra.  Campo "Seleção Automática da Natureza", definir de acordo com a regra de negocio da empresa, selecionando por item ou movimento.    **Fis - Escrituração 1/2:**  Marcar o "Flag" Gerar Escrituração.  Campo "Tipo Documento Escrituração", selecionar tipo de documento cujo campo CODMODDOC = 57.  **Fis - Tributação - Item:** Verificar regra de negocio da empresa.  **Fis - Tributação - Movimento:** Verificar regra de negocio da empresa.  **Fis - Conhecimento de Transporte (etapa NOVA):**  Campo "Tipo de Operação do Conhecimento de de Transporte": Definir como "Emitir CT-e".  Campo "Modal": Definir a modalidade que será utilizada.  Campo "DACTE": informar o relatório default para impressão do DACTE.  Campo "Formato de Impressão", definir o formato que o relatório DACTE será impresso. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
