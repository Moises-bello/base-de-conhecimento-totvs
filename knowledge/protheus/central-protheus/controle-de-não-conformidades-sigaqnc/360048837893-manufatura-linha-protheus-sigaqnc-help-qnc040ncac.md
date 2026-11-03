---
article_id: 360048837893
category: Controle de Não Conformidades (SIGAQNC)
content_hash: e863248b69adcd11dd037db99db6949e9e04cf72c89c55c07a4fa31fecba3b6f
fetched_at: '2026-06-28T22:42:27.975303+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Help QNC040NCAC
type: support-article
updated_at: '2021-11-09T13:20:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048837893-Manufatura-Linha-Protheus-SIGAQNC-Help-QNC040NCAC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:20 min**  
**Ocorrência**No módulo **SIGAQNC - Controle de Não Conformidade**, ao tentar gerar o **Plano de Ação** para uma **FNC - Ficha de Não Conformidade** na rotina **QNCA040 - Cadastro de Ocorrências/Não Conformidades** é exibido o *help* **QNC040NCAC - Só poderá gerar Plano de Ação se o Usuário logado for o responsável e se a Ficha de Ocorrência/Não Conformidade proceder**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus)  - Controle de Não Conformidades (SIGAQNC) - Todas as versões  
  
**Causa**O *help* **QNC040NCAC** é exibido em duas situações:

1. Quando o usuário que está cadastrando a ficha não é o usuário responsável ou;
2. Quando o campo **Situação** é diferente da situação definida no parâmetro **MV\_QNCSFNC - Define os status que poderão incluir o Plano de Ação no cadastro da FNC (Ficha de Não-Conformidade) separados por virgulas Ex: 3,2**.

**Solução**Para que o **Plano de Ação** seja gerado para esta **FNC**, o campo **Situação** deve ser igual à situação indicada no parâmetro **MV\_QNCSFNC** e o campo **Cod Usr Resp** deve ser igual à matrícula do usuário que está incluindo a **FNC**.  
  
**Saiba mais**  
Quando utilizado o ponto de entrada [QN040AUT - Autoriza usuários a alterar a FNC](https://tdn.totvs.com/pages/releaseview.action?pageId=62390525) é possível definir quais usuários podem alterar a **FNC**, independente do conteúdo do campo **Cod Usr Resp**.
