---
article_id: 1500005173222
category: Financeiro - Contas a Pagar
content_hash: 96d387871ed190182a45345933a79856ba20588a4d5c2edb56d7309cdd7bd7de
fetched_at: '2026-06-28T22:38:09.965446+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - Uso do parametro MV_NATSINT
type: support-article
updated_at: '2021-04-28T15:17:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005173222-MP-SIGAFIN-Uso-do-parametro-MV-NATSINT
---

**Dúvida**Qual a funcionalidade do parâmetro MV\_NATSINT?  
  
**Ambiente**Protheus – Financeiro – A partir de versão 12.1.17  
  
**Solução**

O parâmetro **MV\_NATSINT** permite configurar o uso da estrutura da modalidade Sintética / Analítica no registro das modalidades.

1.- Habilita a estrutura da modalidade sintética / analítica.

2.- Não usa (padrão).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007080701/mceclip0.png)

Quando o parâmetro estiver habilitado, no catálogo de modalidades (**Rotina FINA010**), será habilitado para edição o campo ED\_PAI, que deve ser configurado com uma modalidade Principal (Tipo de modalidade sintética).

No PROTHEUS existem 3 relatórios que para serem gerados, é necessário habilitar o parâmetro **MV\_NATSINT** e configurar as modalidades de naturezas analíticas com naturezas sintéticas.

**FINR158** - Títulos a receber por modalidade

**FINR138** - Títulos a pagar por modalidade

**FINR198** - Lista de afastamento por modalidade

**Saber mais**

[TDN - FIN0008\_CREL\_Configuracao\_para\_uso\_dos\_relatorios\_FINR158\_FINR138\_e\_FINR198](https://tdn.totvs.com/display/PROT/FIN0008_CREL_Configuracao_para_uso_dos_relatorios_FINR158_FINR138_e_FINR198)
