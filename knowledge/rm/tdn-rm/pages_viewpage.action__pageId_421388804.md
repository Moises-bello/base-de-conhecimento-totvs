---
content_hash: 96ae4647168ba94dcd988c4a096811622f7beab6c7d559882c0c2c0bf6ab9335
fetched_at: '2026-06-29T00:09:18.868491+00:00'
page_id: '421388804'
product: rm
source: tdn-rm
title: Eventos Contábeis - Gestão Financeira 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388804
version: 3
---

Através do Evento Contábil você pode preencher automaticamente a contabilização dos Lançamentos Financeiros e dos Extratos de Caixa.

O Evento Contábil pode ser informado manualmente ou automaticamente.

Manualmente:

* Na Inclusão ou na Baixa de Lançamento Financeiro
* Na Emissão/Recebimento de Cheque
* No processo de Desconto de Duplicatas
* Na Aplicação Financeira
* No Extrato de Caixa

Automaticamente:

* Utilizando "Tabela Default para Evento" (Assistente de Parâmetros | etapa Contabilização do Financeiro | Tabela Default para Evento).

Ao alterar alguma tabela que esteja sendo utilizada no Evento Contábil o sistema pode "regerar a contabilização" automaticamente, para isso o parâmetro "Regerar Contabilização" (Assistente de Implantação de Processos | Contabilização dos Lançamentos Financeiros |  deve estar marcado.

Algumas Informações especificas ao utilizar o Evento Contábil no TOTVS Gestão Financeira:

Aplicar

* Se no campo "Calcular Valor a Partir de" for marcada a opção "Fórmula" e no campo "Buscar Default em" for selecionada a tabela de "Tributos", no campo "Aplicar" deve ser selecionada a opção "Lançamentos".
* Se no campo "Calcular Valor a Partir de" for marcada a opção "Percentual" e no campo "Buscar Default em" for selecionado a tabela de "Tributos", no campo "Aplicar" deve ser selecionada a opção "Tributos".

Aplicação da Classificação do Centro de Custo no Evento Contábil

Disponibilizada melhoria no Evento Contábil que possibilita ao usuário definir sobre qual contexto do evento contábil a classificação do centro de custo informada, deverá ser aplicada.

Veja mais detalhes das opções em Aplicar Classificação do C. Custo sobre.

Houve alteração no uso da fórmula, conforme descrito abaixo:

Fórmula:

VALORRATCCUPORCLASSIF (Financeiro)

Caso utilize a opção "Aplicar Classificação do C. Custo sobre" na informação "Itens gerenciais", a fórmula acima continua exercendo o mesmo comportamento, ou seja, funciona como sempre foi.

Porém quando utilizar a opção "Aplicar Classificação do C. Custo sobre" na informação "Item do evento (este item)" ou "Ambos" a utilização da fórmula acima não é recomendada, porque neste caso a fórmula vai somar os valores conforme a classificação, gerando assim o valor incorreto na partida do lançamento contábil.

Exemplo:

Imagine um cenário em que no rateio do centro de custo tenha dois ou mais centro de custo com a mesma classificação, neste caso a fórmula acima vai somar os valores conforme a classificação, gerando assim o valor errado na partida do lançamento contábil.

C. Custo 1.01 – Classificação = 01, valor = 1,000.  
 C. Custo 1.02 – Classificação = 01, valor = 1,500.  
 Valor da partida contábil = 2,500

**Sugestão:**

Utilizar a fórmula abaixo:

TABLANRATCCU (Financeiro)

Esta sugestão é aplicada quando o evento contábil está parametrizado com a opção "Aplicar" = "Rateio Centro de Custo".

Para as demais opções a ser parametrizado no campo "Aplicar" no item do evento, a fórmula a ser utilizada pode ser definida conforme a necessidade do cliente.

Lembrando que quando o evento contábil estiver parametrizado para buscar o centro de custo do rareio, o valor da partida contábil gerada pelo item do evento contábil será conforme o percentual do rateio do centro de custo preenchido na origem.

Para saber maiores informações sobre Eventos Contábeis acesse o link: [Eventos Contábeis](http://tdn.totvs.com/x/hcpEGQ).
