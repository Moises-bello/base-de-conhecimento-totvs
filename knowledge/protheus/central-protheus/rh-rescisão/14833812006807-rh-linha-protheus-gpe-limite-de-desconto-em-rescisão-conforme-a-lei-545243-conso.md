---
article_id: 14833812006807
category: RH - Rescisão
content_hash: 5fe39ac95a6ed998b22ebb0121652ced1ca1d85ff309e04105156005c9b4008a
fetched_at: '2026-06-28T22:43:49.767114+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Limite de desconto em rescisão conforme a Lei 5.452/43
  Consolidação das Leis do Trabalho, em seu Art. 477
type: support-article
updated_at: '2025-05-21T11:20:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14833812006807-RH-Linha-Protheus-GPE-Limite-de-desconto-em-rescis%C3%A3o-conforme-a-Lei-5-452-43-Consolida%C3%A7%C3%A3o-das-Leis-do-Trabalho-em-seu-Art-477
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18260024102167) Tempo aproximado para leitura: **01:30 min** **Dúvida**Como limitar desconto em rescisão conforme a Lei 5.452/43 Consolidação das Leis do Trabalho, em seu Art. 477?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Conforme a Lei 5.452/43 Consolidação das Leis do Trabalho, em seu Art. 477 que dispõe sobre Rescisão do Contrato de Trabalho e especificamente em seu 5º Paragrafo: § 5º - Qualquer compensação no pagamento de que trata o parágrafo anterior não poderá exceder o equivalente a um mês de remuneração do empregado. 

Efetuado ajustes para possibilitar que a soma de descontos na rescisão seja limitada à remuneração mensal do funcionário.

Para tanto foi criado o mnemônico **P\_LIMRESPD**, cujo conteúdo padrão é "N", e que deverá ser alterado para que a limitação do desconto seja aplicada.

O mnemônico possui dois funcionamentos distintos de acordo com o preenchimento, que são:

|  |  |
| --- | --- |
| Preenchimento | Funcionamento |
| --- | --- |
| "S" | Se preenchido com "S", todas as verbas de desconto calculadas na rescisão serão somadas e, caso ultrapasse a remuneração mensal do funcionário (SALMES), o excedente será subtraído das verbas de desconto, por ordem de cálculo, da última para a primeira. |
| Código da verba.  Exemplo: "001/002/003" | Se preenchido desta forma, apenas as verbas contidas no mnemônico (verbas de descontos que deseja considerar) serão somadas e, caso ultrapasse a remuneração do funcionário (SALMES), o excedente será subtraído dessas mesmas verbas, também por ordem de cálculo, da última para a primeira. |

Além do mnemônico, para que o processo seja efetuado é necessário cadastrar uma verba de base para o novo identificador de cálculo:

| ID. Cálculo | Descrição |
| --- | --- |
| 1899 | Desconto acima do teto na rescisão |

Nessa verba será gravado o excedente entre o total original de descontos e a remuneração do funcionário. Exemplo:

Se a remuneração do funcionário é de R$ 1.000,00 por mês e a soma de descontos foi igual a R$ 1.100,00, o excedente (R$ 100,00) será abatido das verbas de desconto e o valor será gerado na verba com o novo identificador 1899.

Importante

Caso o mnemônico seja preenchido com "S", todas as todas as verbas de desconto, inclusive as de INSS e IR, por exemplo, serão utilizadas na somatória.

**Exemplo:**

**Salário 4.331,80**

**Desconto Insuficiência Saldo 16.341,80 Folha 04.2023**

**Folha 04.2023**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14833729253783)

**Rescisão 05.2023**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14833788413591)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14833766568599)

**Obs**: Verifique que o valor considerado na verba de ID 1899 é maior que a diferença entre o valor de 16.341,80 e 4.331,80 (12.010,00) pois neste ID é considerado também as verbas de descontos que não foram consideradas no cálculo em razão do valor alto do desconto, exemplo: INSS. IR, vale transporte, etc.

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo

<https://tdn.totvs.com/pages/releaseview.action?pageId=708095198>
