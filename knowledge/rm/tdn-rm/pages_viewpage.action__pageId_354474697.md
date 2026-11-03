---
content_hash: a8cc442708cc8544952f57af36751d834d37e7c572670a3612ba9f77ef096a6d
fetched_at: '2026-06-29T00:08:57.758344+00:00'
page_id: '354474697'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-2021 - Tratamento do CT-e/CT-e OS de Anulação.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354474697
version: 2
---

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| **Segmento Executor:** | Construção e Projetos. | | |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento | | |
| **Rotina:** | Inclusão de movimento de CT-e/CT-e OS de Anulação - (Movimento e parametrização) | | |
| **Ticket:** | N/D | | |
| **Requisito (ISSUE):** | MATFATCMPCRM01-2021 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

## Objetivo

Com a mudança do leiaute do CT-e 2.0 para 3.0, foi criado um novo evento chamado de Prestação de Serviço em Desacordo. Este evento é emitido pelo tomador do CT-e e dessa forma, o emitente é quem deverá emitir um CT-e de Anulação (entrada) e posteriormente um CT-e de Substituição (saída).

Foram necessários alguns ajustes no sistema para permitir o envio de CT-e de entrada (Anulação) e algumas melhorias de usabilidade.

## Definição da Regra de Negócio

Foi implementado no parâmetro do tipo de movimento (1.x.xx) de Anulação as opções "Emitir CT-e" e "Emitir CT-e OS".

Para que estas opções sejam visíveis no tipo de movimento de entrada será necessário a seguinte parametrização:

Na etapa (Mov - Outros Dados) o parâmetro "Usar cópia de Movimentos por referência" deverá ser marcado e o motivo de referência utilizado deverá ser o 16 (Conhecimento Transporte Eletrônico (CT-e) - Anulação).

Após marcar o parâmetro acima, na etapa (Fis - Conhecimento de Transporte) no parâmetro "Tipo de Operação do Conhecimento de Transporte", além das opções já existentes para um movimento de entrada, será exibido também as opções "Emitir CT-e" e "Emitir CT-e OS".

Parametrizando o "Tipo de Operação do Conhecimento de Transporte" como "Emitir CT-e" ou "Emitir CT-e OS", o parâmetro "Modal" deverá ser apresentado com os seus respectivos valores.

"Emitir CT-e":

 "Emitir CT-e OS":

Quando estiver parametrizado para "Emitir CT-e OS", ficará visível o parâmetro "Tipo do Serviço CT-e OS" com seus respectivos valores. Este campo agora é um default do campo "Tipo do Serviço do CT-e OS" do movimento (Transporte | Identificação), portanto não é mais obrigatório o seu preenchimento nos parâmetros do tipo de movimento, mas caso seja preenchido, o valor definido no parâmetro deverá ser carregado para o movimento.

**Tela de Edição do Movimento:**

No tipo de movimento definido como "Emitir CT-e", na aba (Transporte | Identificação) será apresentado os campos "Tipo CT-e" e "Tipo do Serviço CT-e" com seus respectivos valores:

No tipo de movimento definido como "Emitir CT-e OS", na aba (Transporte | Identificação) será apresentado os campos "Tipo CT-e OS" e "Tipo do Serviço CT-e Os" com seus respectivos valores:

Quando for um movimento de "CT-e OS" e o campo ”Tipo do Serviço CT-e OS" for definido como "Excesso de bagagem", na aba (CTRC | CTRC Saída), ao incluir um novo registro os campos "Número Nota", 'Série", "Sub Série", "Valor Total" e "Data Emissão", ficarão visíveis para o preenchimento. Para os demais tipos de Serviços estes campos não serão apresentados.

Quando for um movimento de "CT-e OS" e o campo ”Tipo do Serviço CT-e OS" for definido como "Excesso de bagagem", na aba (CTRC | CT-e) não deverá ser apresentado "Informações de Percurso". Para os demais tipos de Serviços a aba será apresentada normalmente.

**Consistências:**

* O campo "Tipo do Serviço CT-e OS" é de preenchimento obrigatório.

Em tipos de movimento de Anulação parametrizados como "Emitir CT-e OS" será obrigatório o preenchimento do campo "Tipo do Serviço CT-e OS" no movimento e caso não seja preenchido, será apresentado a mensagem de consistência abaixo:

**Tabelas Utilizadas**

Para a implementação, foi criado o campo na base na tabela citada abaixo:

* TMOVTRANSP - Dados de Transporte.
* TITMTMV - Tipos de Movimento - Complemento
* TTMVEXT - Tipos de movimento

### Procedimento para Utilização

Não se aplica.

**CONFIGURAÇÃO DE PARÂMETROS**

Não se aplica.
