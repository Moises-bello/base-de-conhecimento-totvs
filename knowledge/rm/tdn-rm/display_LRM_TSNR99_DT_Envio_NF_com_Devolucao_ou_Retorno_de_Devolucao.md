---
content_hash: 010ba5559a70b4557e348fff796fdbc4f55bf07deca0860af760d4fc2e18642e
fetched_at: '2026-06-29T00:06:09.422396+00:00'
page_id: '203754363'
product: rm
source: tdn-rm
title: TSNR99_DT_Envio_NF_com_Devolucao_ou_Retorno_de_Devolucao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSNR99_DT_Envio_NF_com_Devolucao_ou_Retorno_de_Devolucao
version: 5
---

# ENVIO DE NF COM DEVOLUÇÃO OU RETORNO DE DEVOLUÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | ***Gestão de Estoque Compras Faturamento*** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *NF.01.0045* | *NF-E ENVIO* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **MOV.001** | *INCLUSAO DE MOVIMENTO* | | **MOV.013** | *COPIA A PARTIR DE OUTRO MOVIMENTO* | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *Não se aplica.* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Não se aplica.* |
| **Tabelas utilizadas:** | *TMov, TItmMov, TItmMovRelac, TMovRelac, TNFeEstadual* |
| **Sistema(s) operacional(is):** | *Não se aplica.* |
| **Versões/Release:** | *11.82.40 ou superior* |

## Descrição

Ao enviar nota que possua devolução ou retorno de devolução, o sistema irá referenciar a(s) Chave(s) de Acesso da(s) nota(s) original(ais) envolvida(s) no processo.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(11.82.40.115)* deste chamado.

## Procedimento para Utilização

No módulo "Gestão de Estoque, Compras e Faturamento", aba "Vendas > Faturamento > SPED NF-e (Estadual)", escolha o filtro desejado e acesse o Processo "Enviar", selecionando os dados (Filial, Tipo de Movimento, período e numeração).

1. Ao enviar nota que possua devolução ou retorno de devolução processada através de Cópia por Referência / Faturamento da nota de compra/venda o sistema registrou o devido relacionamento na tabela TMovRelac e TItmMovRelac;
2. Através do registro desse relacionamento e conforme o Motivo da Cópia de Referência parametrizado para o tipo de movimento o sistema irá localizar a(s) nota(s) original(ais) envolvida(s) no processo e disponibilizar o(s) respectivo(s) IdMov(s) para possibilitar o resgate dos dados necessários da(s) nota(s) a ser(em) referenciada(s).
