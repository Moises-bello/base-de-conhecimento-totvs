---
content_hash: 747e951071dce8fbdcf5fe00ae05bc98320ca3be55972b099b4685b78efd0c94
fetched_at: '2026-06-29T00:11:12.440587+00:00'
page_id: '652851832'
product: rm
source: tdn-rm
title: Versão S-1.0 - Qual a função do parâmetro "Não gerar gatilho S-2230 para afastamentos
  (P e O) com duração inferior ao definido no MOS"?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=652851832
version: 9
---

false

**A partir das Versões:**

* **12.1.31.273**
* **12.1.32.219**
* **12.1.33.146**
* **e Superiores**

# Objetivo:

---

O objetivo deste documento é informar o funcionamento do parâmetro: "Não gerar gatilho S-2230 para afastamentos (P e O) com duração inferior ao definido no MOS".

---

11ParametrizaçãoParametrização

1) Acesse o menu RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 3/7. Marque o parâmetro "Não gerar gatilho S-2230 para afastamentos (P e O) com duração inferior ao definido no MOS".

2) Acesse o menu RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Afastamento 1/2. Verifique a parametrização, os campos sinalizados abaixo influenciam na geração.

Mais informações em: <https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719376>

2Afastamento exemplosAfastamento exemplos

Parametro marcado conforme aba de parametrização (Item 1) sistema não irá gerar gatilho de um afastamentos (P e O) com duração inferior ao definido no MOS considerando a carência cadastrada (Item 2). Atualmente é superior a quinze dias.

No histórico de afastamento a coluna Gatilho Pendente Afast. Inferior ao MOS (Tipo P e O) que fará o controle dos gatilhos gerados na fila de eventos, com os status:

* 1- ( Gatilho pendente de geração);
* 0 - ( Gatilho gerado );
* Branco - ( registros já existentes no histórico anterior a implementação deste controle).Dois

33-1Exemplo 1Exemplo 1

**Afastamentos inferiores que somados durante o período de carência (Item 2 aba parametrização) totalizam um período superior a quinze dias.**

**Exemplo:**

              1º afastamento : 2 dias  (não gera gatilho);

              2º afastamento : 10 dias  (não gera gatilho);

              3º afastamento: 10 dias  (gera gatilho) .Neste momento gera-se também os gatilhos dos antecessores (Afastamento 1 e 2 ).

3-2Exemplo 2Exemplo 2

**Afastamentos superior a quinze dias.**

afastamento: 16 dias  (gera gatilho)
