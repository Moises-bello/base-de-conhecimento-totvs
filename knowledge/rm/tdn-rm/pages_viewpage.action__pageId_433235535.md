---
content_hash: d77a7a541f14071c04aa7d5d2643ab26d01e168f3fc541155b99c9bf0071abcd
fetched_at: '2026-06-29T00:09:44.407108+00:00'
page_id: '433235535'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-3170 DT CT-e Aquaviário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=433235535
version: 19
---

# CT-e Aquaviário

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | BackOffice. |
| **Módulo:** | Totvs Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Conhecimento de Transporte (CT-e). |
| **Situação/Requisito:** | Em atendimento ao CT-e 3.0, o Modal Aquaviário deve ser implementado, a fim de atender às normas do Manual do Conhecimento de Transporte Eletrônico. |
| **Solução/Implementação:** | Implementação referente ao CT-e Aquaviário, contemplando parâmetros, movimento e envio. |
| **Conversores e Parâmetros:** | Ambiente | Gestão de Estoque, Compras e Faturamento | Parâmetros Vendas | Faturamento | Tipo de Mov, | Aba Fis - Conhecimento de Transporte |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | Stories: MATFATCMPCRM01-5767, MATFATCMPCRM01-5769. |
| **Documento de Referência:** | Spike: MATFATCMPCRM01-5763. Épico: MATFATCMPCRM01-3170. |
| **Tabelas:** | TCTEAQUAVIARIO; TCTEBALSA; TCTRC; |

# Descrição

Para esta implementação, três pontos importantes sofreram alterações: Parâmetro, Movimento e Envio de Conhecimento de Transporte (CT-e).

Esse documento se refere às alterações especificas do modal Aquaviário: para outras informações sobre o CT-e, acessar o documento .

### Parâmetro

Acessar a visão de Parâmetros do Módulo, através do caminho: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento.

Após escolhido o Tipo de Movimento (1.2.XX ou 2.2.XX) e navegar até a Etapa Fis - Conhecimento de Transporte, a nova opção 'Aquaviário' estará disponível na Caixa de Seleção referente ao Modal.

### Movimento

#### Aquaviário e Balsa

Após parametrizado corretamente, o movimento deverá apresentar a opção 'CT-e' em seu menu.

Nele pode ser encontrada a aba 'Aquaviário', onde contemplará os novos campos que deverão ser utilizados de acordo com a Legislação.

Campos:

Aquaviário

* Valor da Prestação Base de Cáculo do AFRMM: Tipo decimal de tamanho (13, 2);
* AFRMM: Tipo decimal de tamanho (13, 2);
* Identificação do Navio: Tipo caractere de tamanho 60.
* Direção: Tipo 'caixa de seleção' com os valores:
  + Norte
  + Leste
  + Sul
  + Oeste
* IRIN do Navio: Tipo caractere de tamanho 10.
* Tipo de Navegação 'Caixa de Seleção' com os seguintes valores:
  + 0 - Interior
  + 1 - Cabotagem

Balsa

* Sequencial: Tipo inteiro e auto incremental;
* Identificador da Balsa: Tipo caractere de tamanho 60.

#### Contêiner

Para CT-e cujo Tipo do Serviço seja 'Redespacho Intermediário' ou 'Vinculado a Multimodal'.

#### 

Ao acessar a visão dos registros associados ao CT-e, através do caminho 'CTRC | CTRC Saída', seja incluindo manualmente ou através da busca de um movimento.

Para os registros cujo Tipo de Documento preenchido possuir 55 como seu Código de Modelo.

A aba 'Informações do Container' será habilitada, e nela estará disponível um campo para armazenar tal informação.

#### Consistências

A seguinte mensagem de consistência será acionada, caso algum dos campos obrigatórios da aba 'Aquaviário' não esteja preenchido, durante o processo de salvar o movimento.

A seguinte mensagem de consistência será acionada, caso o 'Identificador do Container' não esteja preenchido, durante o processo de salvar o movimento.

# Procedimento para Implantação

O sistema é atualizado logo após aplicação do pacote de atualizações 12.1.23.1 e posteriores à esta demanda.
