---
content_hash: 18ea578c1084c646043c54d8b72ba893c885f217366139b3cce18dde5224cfad
fetched_at: '2026-06-29T00:05:51.765160+00:00'
page_id: '1055128037'
product: rm
source: tdn-rm
title: Percentual de redução para compras governamentais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1055128037
version: 7
---

## **Conteúdo**

**3Conteúdo**

# 1.**O que é**

Na Reforma Tributária (regulamentada pela Lei Complementar 214/2025) as compras governamentais possuem um regime específico que visa neutralizar o custo tributário para o próprio estado garantindo que o ente público não "pague imposto para si mesmo" de forma plena. O **percentual de redução de alíquota para compras governamentais** (Administração direta, autarquias e fundações), ao longo de um período, funcionará de forma escalonada e não se tratará de um percentual fixo único (tipo 20%, 40% etc.). Ele funciona por meio de um “redutor” variável, definido em lei.

Esse mecanismo foi criado para evitar o **desequilíbrio federativo**. Sem essa regra, se um município comprasse um veículo, ele estaria pagando CBS (para a União) e IBS Estadual (para o Estado), onerando o caixa municipal para financiar outros entes. Com a redução e a destinação exclusiva o custo tributário real da compra para o órgão público tende a ser próximo de zero.

Nota Técnica: O cálculo exato dos percentuais anuais de redução (o "redutor de alíquota") é calibrado anualmente pelo Comitê Gestor do IBS e pela Receita Federal para manter a neutralidade da carga, conforme previsto no Art. 472 da Lei Geral.

Como funciona esse percentual de redução

* + A lei determina que **as alíquotas de IBS e CBS serão reduzidas nas vendas para o governo**.
  + Essa redução ocorre por meio de um **fator (redutor)** aplicado sobre a alíquota cheia.
  + O objetivo é **manter a carga tributária semelhante à atual** nas compras públicas (neutralidade).

Percentual na prática

* + 📅 **De 2027 a 2033:** O redutor será **definido ano a ano** (não é fixo).
  + 📅 **A partir de 2034:** Fica **fixado no nível alcançado em 2033**.

Observação: Não existe um percentual único pré-definido (ex: “redução de 30%”), o percentual depende do redutor calculado pelo governo para garantir neutralidade fiscal.

Calculo da alíquota com a aplicação do percentual redutor

* + Alíquota padrão do IBS/CBS = “X”
  + Governo compra → aplica-se um **redutor (r)**
  + Alíquota efetiva = **X \* (1 – r)**

Esse “r” é ajustado ao longo do tempo.

# 2.**Cadastro de origem**

O percentual de redução de alíquota para compras governamentais é cadastrado junto à alíquota do tributo no cadastro de vigência e deve ser cadastrado apenas para o tributo CBS.

Maiores informações e regras do cadastro acesse .

# 3.**Seleção**

A busca do percentual de redução para compras governamentais ocorre de forma automática por meio do **Serviço de Seleção de Alíquota** (). Para que o sistema aplique o redutor corretamente, são observadas as seguintes regras:

**Regra de Recuperação**

O percentual de redução é recuperado exclusivamente a partir do cadastro do tributo **CBS**, mesmo que o cálculo esteja sendo avaliado para o **IBS**.

O sistema utiliza as mesmas regras de vigência e seleção configuradas para a alíquota da CBS.

 

Movimento, data de emissão/lançamento e vigência do tributo CBS

**Condição para aplicação do % de redução**

O redutor só será aplicado se o cliente da operação for identificado como um ente público. O sistema valida os seguintes pontos:

* + - **Perfil do Cliente:** Verifica se o campo **Órgão Público** (localizado no cadastro de *Cliente/Fornecedor* > aba *Outros* | *Tributos*) está preenchido.
    - **Esferas Abrangidas:** São considerados entes governamentais as esferas Municipal, Estadual, Federal e o Distrito Federal.

Movimento, cliente e órgão público

**Resultado do processamento**

* + - **Se for Órgão Público:** O serviço retorna o percentual redutor cadastrado, aplicando-o à alíquota dos tributos no **Item do Movimento**.

Ex. Alíquota padrão CBS \* (1 - % redutor da regra tributária) \* (1 - % redutor cliente governamental)

* + - **Se NÃO for Órgão Público:** O percentual redutor será **0 (zero)**, mantendo a alíquota cheia.

Itens do movimento

Tributos do item de movimento e retorno/aplicação do % de Redução para Compras Governamentais
