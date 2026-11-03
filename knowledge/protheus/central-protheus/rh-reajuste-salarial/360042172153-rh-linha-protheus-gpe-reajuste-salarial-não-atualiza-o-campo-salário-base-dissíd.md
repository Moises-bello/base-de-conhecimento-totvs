---
article_id: 360042172153
category: RH - Reajuste Salarial
content_hash: 5cb435077a85603c5f14db29f1308c763535104f85952376f9b444806b20c627
fetched_at: '2026-06-28T22:43:15.900684+00:00'
product: protheus
section_id: 360010855214
source: central-protheus
title: RH - Linha Protheus - GPE - Reajuste salarial não atualiza o campo Salário
  Base Dissídio (RA_ANTEAUM)
type: support-article
updated_at: '2025-09-12T20:01:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042172153-RH-Linha-Protheus-GPE-Reajuste-salarial-n%C3%A3o-atualiza-o-campo-Sal%C3%A1rio-Base-Diss%C3%ADdio-RA-ANTEAUM
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34903963277719) Tempo aproximado para leitura: 00:00:30 min**

**Dúvida**Ao realizar o reajuste salarial através da rotina **Reajuste > Salarial**  (GPER200), utilizando utilizando a pergunta, "**Aumento Sobre = Antecipação"** e **"Atualiza Base Dissídio = SIM"**, sistema atualiza o campo Salário (RA\_SALARIO), porém não atualiza o campo **Salário Base Dissídio (RA\_ANTEAUM)** no cadastro do funcionário.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Necessário verificar a pergunta, "Aumento Sobre"

Caso esteja como antecipação, sistema não atualizara o campo no cadastro do funcionário (SRA), somente será atualizado se a pergunta  "Aumento Sobre", seja igual a "AUMENTO REAL"

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056584973)

**OBS**: A opção "Antecipação" será utilizada somente quando a data base estiver em atraso e a empresa decidir conceder o reajuste enquanto aguarda a decisão do sindicato.

**Saiba Mais**  
[Pagina Centralizadora Reajuste Salarial](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855214-RH-Reajuste-Salarial)
