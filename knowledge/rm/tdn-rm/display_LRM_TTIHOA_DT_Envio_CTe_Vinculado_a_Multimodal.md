---
content_hash: 353ff50b17b30e4565532a8a5b0f040b2811cf64ce1b369256c90463c1684278
fetched_at: '2026-06-29T00:06:10.966769+00:00'
page_id: '203766276'
product: rm
source: tdn-rm
title: TTIHOA_DT_Envio_CTe_Vinculado_a_Multimodal
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIHOA_DT_Envio_CTe_Vinculado_a_Multimodal
version: 1
---

# ENVIO DE CT-e VINCULADO A MULTIMODAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque Compras Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *FIS.451630* | *CT-e Envio* | | *CTE.002* | *CT-e Inconsistencia* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **MOV.001** | *INCLUSAO DE MOVIMENTO* | | **MOV.013** | *COPIA A PARTIR DE OUTRO MOVIMENTO* | | **Mov.321412** | *COPIA DE MOVIMENTO A PARTIR DE MOVIMENTO SELECIONADO* | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *Não se aplica.* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server / Oracle* |
| **Tabelas utilizadas:** | *TMov, TItmMov, TCTe, TCTeHistorico* |
| **Sistema(s) operacional(is):** | *Não se aplica.* |
| **Versões/Release:** | *11.82.40.117 ou superior* |

## Descrição

Envio de CT-e com informação do Tipo de Serviço igual a "4-Vinculado a Multimodal".

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.82.40.117* deste chamado.

## Procedimento para Utilização

       1.            No TOTVS Gestão de Estoque Compras e Faturamento, acesse opção para emissão de movimentação (Vendas / Faturamento - Movimentação, por exemplo) e informe o tipo de movimento que possui integração para CT-e .

O sistema apresenta a janela de movimentos cadastrados.

       2.            Clicar no botão para "Incluir" movimento ou selecionar um registro existente e solicitar o processo para gerar "Cópia de Movimento a Partir de Outro Movimento".

       3.            Na aba "Transporte / Identificação" clicar no campo do Tipo de Serviço.

Selecionar o item "Vinculado a Multimodal".

       4.            Acessar a aba "CTRC / CTRC Saída" e incluir registro com os dados:

Tipo de Vínculo Documento: "Documentos Transportados";

Tipo de Documento: CT-e (selecionar o registro correspondente a este tipo de documento);

Data de Emissão: data de emissão do documento transportado;

Documento Auxiliar Eletrônico: informar a Chave de Acesso do CT-e autorizado pelo OTM (Operador de Transporte Multimodal).

       5.            Preencher os demais campos que se fizerem necessários e salvar o movimento.

Observação: Na emissão de CT-e vinculado a Multimodal o Tomador de Serviço deverá ser o mesmo emitente da Chave de Acesso vinculada no CTRC Saída, verificando-se pelo CNPJ.

       6.            Acessar opção de "Vendas / Faturamento", "Conhecimentos de Transporte Eletrônico (CT-e)" e selecionar o filtro desejado.

       7.            Solicitar o processo para "Enviar CT-e", preencher os campos e confirmar o processo.

O sistema deverá montar o XML do CT-e com a tag "tpServ" igual a "4" (Serviço Vinculado a Multimodal) e conter a tag "refCTe" (Chave de Acesso do CT-e autorizado pelo OTM).
