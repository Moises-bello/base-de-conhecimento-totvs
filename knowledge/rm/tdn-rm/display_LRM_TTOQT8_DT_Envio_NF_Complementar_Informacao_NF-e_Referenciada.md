---
content_hash: d561fbb4ef1062f61a89993873377e2c506151793aea3a8d0c2ec081b31750df
fetched_at: '2026-06-29T00:06:16.162314+00:00'
page_id: '211064107'
product: rm
source: tdn-rm
title: TTOQT8_DT_Envio_NF_Complementar_Informacao_NF-e_Referenciada
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOQT8_DT_Envio_NF_Complementar_Informacao_NF-e_Referenciada
version: 2
---

# ENVIO DE NF COMPLEMENTAR - INFORMAÇÃO DA NF-E REFERENCIADA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | ***Gestão de Estoque Compras Faturamento*** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *NF.01.0045* | *NF-E ENVIO* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **MOV.014** | *COPIA POR REFERENCIA* | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *Não se aplica.* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Não se aplica.* |
| **Tabelas utilizadas:** | *TMov, TMovRelac, TNFeEstadual* |
| **Sistema(s) operacional(is):** | *Não se aplica.* |
| **Versões/Release:** | *12.1.8 ou superior* |

## Descrição

Ao enviar nota complementar o sistema irá referenciar a Chave de Acesso da nota original envolvida no processo.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.8 ou superior* deste chamado.

## Procedimento para Utilização

No módulo "Gestão de Estoque, Compras e Faturamento", aba "Vendas > Faturamento > SPED NF-e (Estadual)", escolha o filtro desejado e acesse o Processo "Enviar", selecionando os dados (Filial, Tipo de Movimento, período e numeração).

1. Ao gerar nota complementar através de Cópia por Referência da nota de compra/venda o sistema registrou o devido relacionamento na tabela TMovRelac;
2. Através do registro desse relacionamento e conforme o Motivo da Cópia de Referência parametrizado para o tipo de movimento o sistema irá localizar a nota original envolvida no processo e disponibilizar o respectivo IdMov para possibilitar o resgate dos dados necessários da nota a ser referenciada (para preenchimento da respectiva tag refNFe).
