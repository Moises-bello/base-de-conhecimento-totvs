---
article_id: 21551073155351
category: Originação de Grãos (OG)
content_hash: 4dce6bf3153db1affa0e86ac5d7ece6820ae3208fd2d0dcbd81f79bb836804cc
fetched_at: '2026-06-28T22:45:38.991019+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Definição da Regra de Negócio em Ágio e Deságio
type: support-article
updated_at: '2025-06-24T11:52:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21551073155351-Agro-Linha-Protheus-AGR-Defini%C3%A7%C3%A3o-da-Regra-de-Neg%C3%B3cio-em-%C3%81gio-e-Des%C3%A1gio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21551073128471) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Em Característica do Requisito. Como realizar uma Definição da Regra de Negócio em Ágio e Deságio?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12.1.23  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Verifique a **Parametrização em Ágio e Deságio**;

* O processo de ágio e deságio necessita de parametrizações para utilização correta.
* As configurações que devem ser configuradas previamente são:
* MV\_AGRO005

**2.** Analise o **Parâmetro MV\_AGRO005**;

* Esse parâmetro permite a utilização do novo conceito de cálculo de Ágio e Deságio da Originação, sendo possível utilizar os contratos de venda.

**Tipo:**  Lógico.  
**Valor de utilização:**  .T.

**3.** Verifique o **Detalhamento do Ágio e Deságio**;

* No cadastro dos Contratos de Venda (OGA290), foi rompida a opção de registrar os Ágios e Deságios do Contrato de Venda.
* Caso o parâmetro MV\_AGRO005 esteja com conteúdo igual a .F., a aba Ágio e Deságio não estará disponível para utilização, conforme.

**Figura 1**

![ADE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21551073130775)

**4.** Veja com o parâmetro **MV\_AGRO005** com conteúdo igual a .T., na aba **Ágio/Deságio** estará disponível para utilização;

**Figura 2**

![ADE1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21552298554135)

**5.** Veja, existem 3 opções para registro de índices de Ágio/Deságio no Contrato de Venda, conforme;

* Por Tipo/Cor/Folha;
* Por HVI e
* Por Outros.

**6.** Observe, o **Ágio/Deságio por Tipo/Cor/Folha**. Através dessa opção é possível registrar Ágios (diferença para mais) e Deságios (diferença para menos) para os diversos **Tipos/Cores/Folha do algodão**. Essas diferenças podem ser registradas na forma de Valor, Porcentagem ou Pontuação;

* **Valor** : na forma de unidade monetária **$**
* **Porcentagem:** na forma de percentual, não pode ultrapassar o limite de 100%.
* **Pontuação:** na forma de pontos. Quando escolhida a forma de registro de ágio e deságio por pontuação torna-se obrigatório preencher o campo “Fator” que corresponde ao fator base para conversão de pontos no momento do cálculo.

**7.** Verifique, além disso, o usuário pode indicar se deseja que a aplicação dos índices de ágios e deságios seja feita de forma Individual ou por **Grupo**;

* Na forma **Individual**, no momento do cálculo o sistema irá analisar as características de cada fardo, individualmente, e aplicar os respectivos índices conforme sua classificação.
* Na forma **Grupo**, no momento do cálculo o sistema irá aplicar um índice único de ágio ou deságio, ignorando os índices informados nas notas.
* Deve ser informada também a Unidade de Medida do ágio e desejo, e, caso desejar, pode ser determinada uma % de Tolerância a ser considerada no momento do projeto.
* **Nota Descontos por Tipo:** informar o tipo e folha e o valor para aplicação do ágio/deságio; (ver Figura).

**Figura 3**

![ADE4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21552298581143)

* **Nota Descontos por Cor:** informar as cores e o valor para aplicação do ágio/deságio; (ver Figura).

**Figura 4**

![ADE5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21552298596119)

* **Grau Regra Aplicação de Descontos Conforme Dados HVI:** Nessa nota é possível informar regras condicionantes que irão determinar a aplicação dos ágios/deságios. Essas regras podem ser montadas com bases nos Dados HVI; (ver Figura).

**Figura 5**

![ADE6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21552355754775)
