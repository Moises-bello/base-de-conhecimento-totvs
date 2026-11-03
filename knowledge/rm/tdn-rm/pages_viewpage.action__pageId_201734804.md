---
content_hash: 7310a9e0a7328581cb63f84dcd7023c6c1e534d48d6836d28d110b2f6eaf7531
fetched_at: '2026-06-29T00:06:07.074197+00:00'
page_id: '201734804'
product: rm
source: tdn-rm
title: DT_Recurso_de_Glosa_como_Processo_de_Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201734804
version: 10
---

# Recurso de Glosa como Processo de Cobrança

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento / Recurso de Glosa |  |  | | --- | | **Rotina(s) envolvida(s)** | | Controle de Glosa, Controle de Recebimento | |
| **Cadastros Iniciais:** | Sincronismo dos cadastros de natureza financeira |
| **Parâmetro(s):** | Parâmetros de integração:   * Produto do tipo serviço utilizado para a geração do movimento de cobrança. * Tipo do documento que será gerado no Protheus. * Série do documento a ser gerado. |
| **Requisito (ISSUE):** | PCREQ-6801 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle e SQL Server |
| **Tabelas utilizadas:** | SZATENDIMENTOREC, SZPARCIALATEND |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

O processo ocorre na funcionalidade de **Recurso de Glosas**. Para que os os valores glosados não sejam mais tratados pelo TOTVS Gestão Hospitalar através de recurso, o usuário deve clicar no botão "**Gerar Processo de cobrança**" para que seja enviada uma mensagem de título a receber no BackOffice. Após esta geração do processo de cobrança, o usuário não poderá cancelar o processo de recurso de glosa, deve primeiro cancelar o processo de integração, para depois cancelar o recurso.

Uma vez gerado o processo de cobrança no BackOffice, o sistema não permitirá realizar o recebimento deste valor no controle de recebimento da tesouraria.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.7 da BibliotecaRM.

1. Aplique o patch do chamado e execute uma vez a rotina controle de glosa e depois o recurso de glosa.

## Procedimento para Utilização

1. Acesse o menu **Opções / Parâmetros / Parâmetros de Integração**, página **Parâmetros Protheus**.
   1. Preencha o produto que será utilizado para compor o movimento de cobrança (necessário apenas para gerar o movimento origem no RM).
   2. Informe o Tipo de documento que será gerado no **Protheus**.
   3. Informe a Série do titulo a receber.
2. De posse de uma fatura, faça o controle de recebimento conta à conta.
3. Acesse o **Controle de Glosa** e realize as glosas.
4. Acesse o menu **Faturamento / Recurso de Glosas**.  
                    
   1. Selecione uma conta, abra uma conta e deixe alguns itens que não serão apresentados para recursar.
   2. Processe o recurso.
   3. Se existir saldo que não foi recursado, será possível gerar um processo de cobrança no **Protheus** (título a receber).
5. Ao solicitar a geração do título a receber, é solicitado informar o tipo de movimento (que já vem por default) e o tipo de natureza financeira.
6. É gerado um titulo a pagar no **Protheus**.
   1. É exibido o código da referência gerado no **Protheus**.
7. Uma vez gerado o título a receber é habilitado o botão de Exclusão do título a receber.
