---
content_hash: 9ef299bed1f1b7af737ffebee99cd178fd09fd259a404606a27e67c8af619616
fetched_at: '2026-06-29T00:05:47.012110+00:00'
page_id: '1005897377'
product: rm
source: tdn-rm
title: Acelerador de Implantação PDC - Renegociação de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1005897377
version: 6
---

Esta tela **permite a configuração das regras e limites** para a funcionalidade de renegociação de contratos no portal do cliente.

**A Primeira verificação**que deve ser efetuada é a configuração do Parâmetro **Permite efetivação automática da renegociação de contrato**(Acelerador PDC>> Funcionalidades>> Renegociação de Contrato).

**A configuração deste Parâmetro**definese a renegociação elaborada pelo comprador será efetivada de forma automática pelo sistema ou se o novo plano será efetivado pelo setor responsável.

Os outros parâmetros apresentados definem:

* **Valor máximo para renegociação:** Valor máximo permitido a ser renegociado, ou seja, a soma das parcelas vencidas (depende do parâmetro de efetivação automática).
* **Número máximo de parcelas:**Quantidade máxima de parcelas permitidas para o novo plano que será gerado (depende do parâmetro de efetivação automática).
* **Dias corridos para o primeiro vencimento:** Informa a quantidade de dias corridos que o sistema utilizará para calcular o vencimento da primeira parcela do novo plano. Portanto a data do primeiro vencimento será igual a data que o aditivo foi criado mais o número de dias definido nos parâmetros.
* **Limite de parcelas:** Define o número máximo de parcelas que  que podem ser exibidas e/ou negociadas.
* **E-mail do(s) responsáveis pela aprovação:** Informa quais e-mails devem ser comunicados quando o comprador executa determinadas ações no Portal.

Os seguintes cenários que geram e-mail são:

1. 1. Comprador gera uma nova renegociação e a mesma foi efetivada de forma automática.
   2. Comprador gera uma nova renegociação e a mesma aguarda análise e aprovação.
   3. Comprador cancelou uma renegociação que estava na situação em preparação.

* **Utilizar SQL para filtrar as parcelas da tabela XVENDAPARCELA a serem exibidas no Renegociador:**  
  Define a **instrução SQL utilizada para filtrar as parcelas da tabela `XVENDAPARCELA`** que serão exibidas no **Negociador TCGI**.

**Finalidade:**  
Restringir as parcelas que aparecem para negociação, conforme critérios específicos definidos pela empresa (por exemplo, parcelas em aberto, dentro de determinado período ou com status específico).

**Detalhamento técnico:**

* + **Tabela base:** `XVENDAPARCELA`
  + **Tipo:** Texto (SQL)
  + **Uso:** O conteúdo do parâmetro é interpretado como um *filtro SQL WHERE* aplicado na consulta principal de carregamento das parcelas no Negociador.
  + **Exemplo de uso:**

    `NUMPARC = 1 AND NUMVENDA = 1`

**Comportamento esperado:**  
Somente as parcelas que atenderem às condições definidas na instrução SQL contida neste parâmetro serão apresentadas na tela de negociação.

**Observações:**

* + É importante garantir que o SQL seja válido e seguro (sem comandos de modificação de dados).
  + Caso o SQL retorne um conjunto vazio, nenhuma parcela será exibida no Negociador.
