---
content_hash: 970d98019de3f246990cc4902b11ef7734b8d95d14aad83e80b744ccceca00fe
fetched_at: '2026-06-29T00:10:31.662521+00:00'
page_id: '521641736'
product: rm
source: tdn-rm
title: TAG vrSalFx - Parâmetro Considerar maior valor de salário-hora na tag vrSalFx
  para professores/horistas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521641736
version: 4
---

false

**A partir das Versões:**

* 12.1.24.246
* 12.1.25.185
* 12.1.26.129
* E Superiores.

# Objetivo:

---

Através deste documento será apresentado as mudanças realizadas na geração da tag vrSalFx quando o parâmetro **Considerar maior valor de salário-hora na tag vrSalFx para professores/horistas** estiver marcado.

---

Conforme descristo no eSocial MOS Página 153/154, tópico 35 :

Para atender a esse tópico foi criado o parâmetro **Considerar maior valor de salário-hora na tag vrSalFx para professores/horistas**em **RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 4/6.**

 Ao marcar este parâmetro o sistema passa a considerar o maior salário hora cadastrado conforme data do histórico salarial para a geração da tag vrSalFx dos eventos S-2200 e S-2206.

**Exemplo:**

Feito o aumento salarial por promoção para o funcionário (professor).

No cadastro do funcionário no campo **Descrição do Salário Variável**  foi descrito todos os salários hora.

Após a alteração salarial o sistema gerou um gatilho do evento S-2206. Ao gerar o evento na tag vrSalFx levou apenas o maior salário hora e as descrições dos salários hora do campo **Descrição do Salário Variável** na tag dsSalvar.
