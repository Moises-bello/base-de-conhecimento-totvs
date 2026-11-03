---
article_id: 115009947187
category: RH - Diversos
content_hash: d5a133dbfb28746eccbe7b2833ccf59498dd76b3531a83b5e9bdb5570ba155ae
fetched_at: '2026-06-28T22:44:50.244032+00:00'
product: protheus
section_id: 32419184463255
source: central-protheus
title: RH - Linha Protheus - PON - Abonos  MV_ABOSEVE e MV_SUBABAP
type: support-article
updated_at: '2025-08-20T14:16:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115009947187-RH-Linha-Protheus-PON-Abonos-MV-ABOSEVE-e-MV-SUBABAP
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34316768355735) Tempo aproximado para leitura: 00:02:00 min****

****Dúvida****Consideramos a existência dos parâmetros **MV\_ABOSEVE** e **MV\_SUBABAP** para a composição dos abonos a serem demonstrados no Espelho de Ponto.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução****MV\_SUBABAP** - Esse novo parâmetro será utilizado para efetuar o tratamento abaixo:

**Release Desenvolvimento:**  
Se o Motivo de Abono estiver configurado como **Não Abona Horas** e o **Código do Evento Relacionado ao Abono** não estiver vazio, será considerado como uma alteração do Código de Evento. Ou seja, as Horas do Abono serão subtraídas das Horas Calculadas do evento original e direcionadas ao evento informado no abono.  
Podemos chamar essa operação de **“Informados via Abono”**.

### Exemplo:

**Apontamento 1**

* Evento: 101 – Horas Extras 50% 10.00
* Abono: 05.00, com Abona Horas = Não e Evento 105

**Cálculo Mensal:**

* Evento 101 – 05.00
* Evento 105 – 05.00

---

**Apontamento 2**

* Evento: 101 – Horas Extras 50% 10.00
* Abono: 10.00, com Abona Horas = Não e Evento 105

**Cálculo Mensal:**

* Evento 105 – 10.00

---

**Apontamento 3**

* Evento: 101 – Horas Extras 50% 10.00
* Abono:

  + 02.00, com Abona Horas = Não e Evento 105
  + 03.00, com Abona Horas = Não e Evento 106
  + 04.00, com Abona Horas = Não e Evento 107

**Cálculo Mensal:**

* Evento 101 – 01.00
* Evento 105 – 02.00
* Evento 106 – 03.00
* Evento 107 – 04.00

---

**Apontamento 4**

* Evento: 101 – Horas Extras 50% 10.00
* Abono:

  + 02.00, com Abona Horas = Não e Evento 105
  + 04.00, com Abona Horas = Não e Evento 106
  + 04.00, com Abona Horas = Não e Evento 107

**Cálculo Mensal:**

* Evento 105 – 02.00
* Evento 106 – 04.00
* Evento 107 – 04.00

---

⚠️ Essa rotina somente será aplicada quando o conteúdo do parâmetro for **MV\_SUBABAP = S**.

**Configuração no Configurador:**

* **Parâmetro:** MV\_SUBABAP
* **Tipo:** C
* **Descrição:** Gerar horas de Abono no Evento Relacionado subtraindo-as das Horas Calculadas quando Motivo “Não Abona Horas” e possui Evento. S = Sim ; N = Não
* **Conteúdo:** S ou N (DEFAULT = N)

---

## **MV\_ABOSEVE**

Deduz as Horas de Abono das Horas Apontadas.  
Somente válido quando solicitado que, no Cadastro do Motivo de Abonos (MV\_ABOSEVE = S), seja permitido abono de horas sem a especificação do código de evento associado.

Essa funcionalidade garante compatibilidade com a versão 6.09, onde era possível deduzir os abonos diretamente da verba.  
Dessa forma, as horas não serão apenas a soma das horas de faltas, atrasos e saídas.

**Configuração no Configurador:**

* **Nome Var.:** MV\_ABOSEVE
* **Tipo:** Caractere
* **Descrição:** Permitir o cadastramento de Motivo de Abono com a opção **Abona Horas = S**, sem a necessidade de informar o código de Evento. S = Sim ; N = Não

---

**Resumo dos Parâmetros:**

* **MV\_SUBABAP** → Subtrai Abono do Evento Apontado.
* **MV\_ABOSEVE** → Deduz Horas de Abono das Horas Apontadas.

****Saiba mais**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)**
