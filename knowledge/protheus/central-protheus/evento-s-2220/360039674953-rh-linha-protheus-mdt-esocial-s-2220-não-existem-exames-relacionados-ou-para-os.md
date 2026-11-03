---
article_id: 360039674953
category: Evento S-2220
content_hash: 4fdcb2a634e7dcee92d1a73d5fa3e63367152a3fd24424ec09cee94800a9fb18
fetched_at: '2026-06-28T22:45:25.528698+00:00'
product: protheus
section_id: 8260535758103
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2220 - Não existem exames relacionados
  ou para os exames relacionados não foi indicado o campo 'Proc.Realiz' ou ainda o
  (s) exame (s) relacionado (s) não é (são) do tipo 'Ocupacional'
type: support-article
updated_at: '2025-03-03T18:15:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039674953-RH-Linha-Protheus-MDT-eSocial-S-2220-N%C3%A3o-existem-exames-relacionados-ou-para-os-exames-relacionados-n%C3%A3o-foi-indicado-o-campo-Proc-Realiz-ou-ainda-o-s-exame-s-relacionado-s-n%C3%A3o-%C3%A9-s%C3%A3o-do-tipo-Ocupacional
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372801864343)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Após habilitar o parâmetro **MV\_NG2ESOC** e incluir um Atestado ASO no módulo SIGAMDT, o sistema passa a validar as informações para o eSocial e quando não identifica alguns campos obrigatórios no cadastro de Exames é apresentado mensagem:

**"Não existem exames relacionados ou para os exames relacionados não foi indicado o campo 'Proc.Realiz' ou ainda o (s) exame (s) relacionado (s) não é (são) do tipo 'Ocupacional'."**  
**Ambiente**TOTVS RH (Linha Protheus) > Medicina e Segurança do Trabalho > Todas as Versões  
  
**Solução**Deve ser relacionado ao menos um exame ao Atestado ASO, os exames relacionados devem possuir o campo "Procedimento Realizado" preenchido, que fica localizado no cadastro dos Exames (MDTA020) e os exames relacionados devem ser do tipo **Ocupacional**, que é definido no cadastro de Exames do Funcionário (MDTA120).

Deverá acessar a rotina Atualizações > PCMSO > Exames:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052408573)

Deverá acessar a rotina Atualizações > PCMSO > Exames do Funcionário:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052408693)

**Observação:** É necessário que as informações do cadastro Sesmt/Usuários (MDTA070) através do menu Atualizações > Sesmt > Sesmt/ usuar. aten. estejam preenchidos, pois são campos obrigatórios para o eSocial.

**Campos:** NIT, Ent Classe, Num Ent Classe, CPF, UF Ent e Resp  Amb.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8244652638999)  
 **Dica:** Neste link contém informação importante para auxilia-lo na geração do evento S-2220:  [Ao gerar o evento S-2220 gera o relatório de inconsistência Observação sobre o Procedimento Diagnóstico Em branco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411274053527)**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
