---
content_hash: 7068916f63cc541a159b3084837533b784882f230728d2cc542b746582f933d0
fetched_at: '2026-06-29T00:06:13.467578+00:00'
page_id: '208342024'
product: rm
source: tdn-rm
title: TTJLYB_DT_MDFe_Envio_De_XML_E_Relatorio_Em_PDF_Para_EMail
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJLYB_DT_MDFe_Envio_De_XML_E_Relatorio_Em_PDF_Para_EMail
version: 3
---

# ENVIO DE XML E RELATÓRIO EM PDF DE MDF-E PARA E-MAIL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM** |
| **Segmento:** | ***Construção e Projetos*** |
| **Módulo:** | **Gestão de Estoque, Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | **MDF.004** | **MDF-E - RELATORIO** | | **CLB.013** | **TOTVS COLAB - RELATORIOS MDF-E** | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | **N/A** |
| **Requisito (ISSUE):** | **N/A** |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | **SQL Server e Oracle** |
| **Tabelas utilizadas:** | **TMDFe, TCTeMov, TMovTransp, TCTRC, FCFO, GFilial, TTra** |
| **Sistema(s) operacional(is):** | **N/A** |
| **Versões/Release:** | **12.1.9 ou superior** |

## Descrição

Melhoria no sistema para envio do XML do MDF-e e do respectivo Relatório DAMDFE em PDF por e-mail através de processo.

Através da tela de processo para envio de e-mail do MDF-e o usuário terá disponível:

* Opção para selecionar e-mail principal do(s) destinatário(s) conforme documento(s) fiscal(ais) associado(s) (NF-e: Remetente/Destinatário; CT-e: Remetente/Destinatário/Expedidor/Recebedor/Outros);
* Opções de envio do e-mail para CC e CCO;
* Opção para envio de cópia para Transportadora;
* Opção para envio do respectivo Relatório DAMDFE em PDF - escolher relatório a ser gerado e valerá para todos registros selecionados.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações do patch específico **12.1.9**deste chamado.

## Procedimento para Utilização

1. Através do "TOTVS Gestão de Estoque, Compras e Faturamento" acesse a aba "Vendas > Faturamento > Manifesto Eletrônico de Documentos (MDF-e)";
2. Escolha o filtro desejado e na visão de registros disponíveis selecione um MDF-e com status "Autorizado";
3. Acesse o menu "Processos > Envio de MDF-e por e-mail";
4. Informe o comportamento do processo a ser executado:
   1. E-mail destinatário - selecione onde buscar o e-mail principal conforme documento(s) fiscal(ais) associados: NF-e: Remetente/Destinatário; CT-e: Remetente/Destinatário/Expedidor/Recebedor/Outros;
   2. Opção "Enviar cópia para Transportadora" - caso marque esta opção será enviado cópia para o e-mail informado no cadastro da Transportadora no movimento do CT-e/NF-e;
   3. Opção "Enviar Relatório DAMDFE em PDF" - caso marque esta opção selecione o relatório (aplicável a todos os registros selecionados na visão);  
      Observação: O sistema mostrará o relatório padrão parametrizado para o Tipo de Movimento - caso tenha, mas é possível selecionar outro relatório.
5. Confirme a execução do processo.
