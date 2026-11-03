---
content_hash: e43c27a3d67c9aa0089ad323483796b0ddaf13533cae020cdba8a308ad8efa90
fetched_at: '2026-06-29T00:09:53.536336+00:00'
page_id: '440841026'
product: rm
source: tdn-rm
title: Versão 2.5 - Qual a função do parâmetro "Não gerar gatilho S-2230 para afastamentos
  (P e O) com duração inferior ao definido no MOS"?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440841026
version: 19
---

# Objetivo:

---

O objetivo deste documento é informar o funcionamento do parâmetro: "Não gerar gatilho S-2230 para afastamentos (P e O) com duração inferior ao definido no MOS".

---

Com este parâmetro **Marcado** ao gerar um afastamento tipo( **P** ou **O)** inferior a 3 dias, NÃO será gerado um gatilho na fila de eventos.

 Foi criado no histórico de afastamento a coluna Gatilho Pendente Afast. Inferior ao MOS (Tipo P e O) que fará o controle dos gatilhos gerados na fila de eventos.

**Exemplo:**

1- ( Gatilho pendente de geração)

    0- ( Gatilho gerado )

    Branco- ( registros já existentes no histórico anterior a implementação deste controle)

 Os parâmetros abaixo ao serem selecionados influenciam na geração dos gatilhos inferiores a 3 dias.

 Para melhor entendimento do funcionamento destes parâmetros leiam o help abaixo:

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719376>

**Observação:**

* Quando houver 16 dias de afastamentos com “dias não corridos”, dentro do período de carência parametrizado o sistema  irá gerar  o gatilho dos atestados anteriores (com menos de 3 dias).

**Exemplo:**

              1º afastamento : 2 dias  (não gera gatilho);

              2º afastamento : 3 dias  (gera gatilho);

              3º afastamento : 2 dias  (não gera gatilho);

              4º afastamento:10 dias  (gera gatilho) .Neste momento gera-se também os gatilhos dos antecessores (Afastamento 1 e 3).

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |
|  |

falsefalse

**Status: Pendente**

false

**Data:**

false

**Autor:**
