---
article_id: 4404416564503
category: eSocial
content_hash: 0d2c76ed68f4b785470c19d5945a29a8e3bfe615b13845fc84441639b46394b3
fetched_at: '2026-06-28T22:47:39.167389+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2220: Erro na validação do campo dtExm'
type: support-article
updated_at: '2024-02-12T14:24:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404416564503-RH-RM-SMT-S-2220-Erro-na-valida%C3%A7%C3%A3o-do-campo-dtExm
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035699577111) Tempo aproximado para leitura: 00:01:00 min****Dúvida**Ao gerar o XML do evento S-2220 aparece a mensagem: 'Erro na validação do campo 'dtExm': Deve ser uma data igual ou anterior a data do atestado de saúde ocupacional'. O que fazer ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM- Segurança e Saúde Ocupacional - 12.1.28 e superiores.

**Solução**Acesse o menu PCSMO > Prontuário medico e busque pelo funcionário desejado. Selecione o cadastro da consulta medica referente ao evento S-2220 e confira no campo **Data de emissão ASO**, qual é a data informada.

![](https://totvssuporte.zendesk.com/attachments/token/OWZJxk8ZxQZ4PLErDowlexvDY/?name=inline-1747979604.png)​

Edite o(s) exame(s) associado(s) a esta consulta, e valide se a data do exame medico **é uma data igual ou anterior** a data de emissão ASO, caso não seja faça a alteração e salve.

![](https://totvssuporte.zendesk.com/attachments/token/1l1fnjJWY5D8lEKpYKxfEQ5py/?name=inline-1538201015.png)
